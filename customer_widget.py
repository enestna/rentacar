from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt, QDate
from ui_customer_form import Ui_MusteriFormu
from database import get_db_connection, DB_NAME
import mysql.connector

class CustomerWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MusteriFormu()
        self.ui.setupUi(self)
        self.setWindowTitle("Müşteri İşlemleri (Kayıt, Güncelleme, Silme)")
        self.current_musteri_id = None

        self._setup_comboboxes()
        self._setup_table()

        self.ui.btn_kaydet.clicked.connect(self.save_customer)
        self.ui.btn_guncelle.clicked.connect(self.update_customer)
        self.ui.btn_sil.clicked.connect(self.delete_customer)
        self.ui.tbl_liste.itemSelectionChanged.connect(self.load_customer_to_form)
        self.ui.txt_arama.textChanged.connect(self.search_customer)

    def showEvent(self, event):

        self.load_customers()
        super().showEvent(event)

    def _setup_comboboxes(self):
        self.ui.cmb_ehliyet.addItems(["A", "B", "C", "D", "E", "F", "H"])
        self.ui.cmb_medeni.addItems(["Bekar", "Evli", "Boşanmış", "Dul"])
        self.ui.cmb_egitim.addItems(["İlkokul", "Ortaokul", "Lise", "Ön Lisans", "Lisans", "Yüksek Lisans", "Doktora"])
        self.ui.date_dogum.setDate(QDate(1990, 1, 1))

    def _setup_table(self):
        self.ui.tbl_liste.setColumnCount(12)
        headers = ["ID", "Ad", "Soyad", "TC Kimlik", "Doğum T.", "Adres", "Ev Tel", "Cep Tel", "Meslek", "Ehliyet", "Medeni", "Eğitim"]
        self.ui.tbl_liste.setHorizontalHeaderLabels(headers)
        self.ui.tbl_liste.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tbl_liste.horizontalHeader().setStretchLastSection(True)

    def load_customers(self, search_term=""):
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()
        query = "SELECT * FROM musteriler"
        params = ()
        if search_term:
            query += " WHERE tc_kimlik LIKE %s OR ad LIKE %s OR soyad LIKE %s"
            search_pattern = f"%{search_term}%"
            params = (search_pattern, search_pattern, search_pattern)

        cursor.execute(query, params)
        records = cursor.fetchall()
        self.ui.tbl_liste.setRowCount(0)

        for row_num, row_data in enumerate(records):
            self.ui.tbl_liste.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                item_text = str(data)
                self.ui.tbl_liste.setItem(row_num, col_num, QTableWidgetItem(item_text))

        cursor.close()
        conn.close()

    def search_customer(self):
        self.load_customers(self.ui.txt_arama.text())

    def clear_form(self):
        self.ui.txt_ad.clear()
        self.ui.txt_soyad.clear()
        self.ui.txt_tc.clear()
        self.ui.txt_adres.clear()
        self.ui.txt_telefon_ev.clear()
        self.ui.txt_telefon_cep.clear()
        self.ui.txt_meslek.clear()
        self.ui.date_dogum.setDate(QDate(1990, 1, 1))
        self.ui.cmb_ehliyet.setCurrentIndex(0)
        self.ui.cmb_medeni.setCurrentIndex(0)
        self.ui.cmb_egitim.setCurrentIndex(0)
        self.current_musteri_id = None

    def get_form_data(self):
        return (
            self.ui.txt_ad.text(), self.ui.txt_soyad.text(), self.ui.txt_tc.text(),
            self.ui.date_dogum.date().toString(Qt.ISODate), self.ui.txt_adres.toPlainText(),
            self.ui.txt_telefon_ev.text(), self.ui.txt_telefon_cep.text(),
            self.ui.txt_meslek.text(), self.ui.cmb_ehliyet.currentText(),
            self.ui.cmb_medeni.currentText(), self.ui.cmb_egitim.currentText()
        )

    def save_customer(self):
        ad, soyad, tc, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet, medeni, egitim = self.get_form_data()
        if not all([ad, soyad, tc]):
            QMessageBox.warning(self, "Hata", "Ad, Soyad ve TC alanları boş bırakılamaz.")
            return

        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        sql = """INSERT INTO musteriler
                 (ad, soyad, tc_kimlik, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet_sinifi, medeni_durum, egitim_durumu)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (ad, soyad, tc, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet, medeni, egitim)

        try:
            cursor.execute(sql, values)
            conn.commit()
            QMessageBox.information(self, "Başarılı", f"{ad} {soyad} başarıyla kaydedildi.")
            self.clear_form()
            self.load_customers()
        except mysql.connector.Error as err:
            if err.errno == 1062:
                QMessageBox.critical(self, "Hata", "Bu TC Kimlik numarası zaten kayıtlı!")
            else:
                QMessageBox.critical(self, "Hata", f"Kayıt sırasında hata oluştu: {err}")
        finally:
            cursor.close()
            conn.close()

    def update_customer(self):
        if self.current_musteri_id is None:
            QMessageBox.warning(self, "Hata", "Lütfen güncellemek için tablodan bir müşteri seçin.")
            return

        ad, soyad, tc, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet, medeni, egitim = self.get_form_data()

        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        sql = """UPDATE musteriler SET
                 ad=%s, soyad=%s, tc_kimlik=%s, dogum_tarihi=%s, adres=%s, telefon_ev=%s,
                 telefon_cep=%s, meslek=%s, ehliyet_sinifi=%s, medeni_durum=%s, egitim_durumu=%s
                 WHERE musteri_id=%s"""

        values = (ad, soyad, tc, dogum_tarihi, adres, telefon_ev, telefon_cep, meslek, ehliyet, medeni, egitim, self.current_musteri_id)

        try:
            cursor.execute(sql, values)
            conn.commit()
            QMessageBox.information(self, "Başarılı", f"{ad} {soyad} müşterisi başarıyla güncellendi.")
            self.clear_form()
            self.load_customers()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"Güncelleme sırasında hata oluştu: {err}")
        finally:
            cursor.close()
            conn.close()

    def delete_customer(self):
        if self.current_musteri_id is None:
            QMessageBox.warning(self, "Hata", "Lütfen silmek için tablodan bir müşteri seçin.")
            return

        reply = QMessageBox.question(self, 'Onay',
            "Seçili müşteriyi silmek istediğinizden emin misiniz? Bu işlem geri alınamaz.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            conn = get_db_connection(database=DB_NAME)
            if conn is None: return
            cursor = conn.cursor()

            sql = "DELETE FROM musteriler WHERE musteri_id = %s"

            try:
                cursor.execute(sql, (self.current_musteri_id,))
                conn.commit()
                QMessageBox.information(self, "Başarılı", "Müşteri kaydı başarıyla silindi.")
                self.clear_form()
                self.load_customers()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Hata", f"Silme sırasında hata oluştu: {err}")
            finally:
                cursor.close()
                conn.close()


    def load_customer_to_form(self):
        selected_row = self.ui.tbl_liste.currentRow()
        if selected_row >= 0:
            record = []
            for col in range(self.ui.tbl_liste.columnCount()):
                record.append(self.ui.tbl_liste.item(selected_row, col).text())

            self.current_musteri_id = record[0]

            self.ui.txt_ad.setText(record[1])
            self.ui.txt_soyad.setText(record[2])
            self.ui.txt_tc.setText(record[3])

            self.ui.date_dogum.setDate(QDate.fromString(record[4], Qt.ISODate))

            self.ui.txt_adres.setText(record[5])
            self.ui.txt_telefon_ev.setText(record[6])
            self.ui.txt_telefon_cep.setText(record[7])
            self.ui.txt_meslek.setText(record[8])

            self.ui.cmb_ehliyet.setCurrentText(record[9])
            self.ui.cmb_medeni.setCurrentText(record[10])
            self.ui.cmb_egitim.setCurrentText(record[11])

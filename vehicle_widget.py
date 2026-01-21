# vehicle_widget.py

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt
from ui_vehicle_form import Ui_AracFormu
from database import get_db_connection, DB_NAME
import mysql.connector

class VehicleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AracFormu()
        self.ui.setupUi(self)
        self.setWindowTitle("Araç İşlemleri")
        self.current_arac_id = None

        self._setup_comboboxes()
        self._setup_table()

        self.ui.btn_kaydet.clicked.connect(self.save_vehicle)
        self.ui.btn_guncelle.clicked.connect(self.update_vehicle)
        self.ui.btn_sil.clicked.connect(self.delete_vehicle)

        self.ui.tbl_liste.itemSelectionChanged.connect(self.load_vehicle_to_form)
        self.ui.txt_arama.textChanged.connect(self.search_vehicle)


        self.ui.cmb_yakit_turu.currentIndexChanged.connect(self.check_fuel_type)
        self.check_fuel_type()

    def showEvent(self, event):
        self.load_vehicles()
        super().showEvent(event)

    def check_fuel_type(self):
        """Elektrik seçilirse menzil kutusunu göster/aktif et."""

        try:
            is_electric = self.ui.cmb_yakit_turu.currentText() == "Elektrik"
            if hasattr(self.ui, 'txt_menzil'):
                self.ui.txt_menzil.setVisible(is_electric)
            if hasattr(self.ui, 'lbl_menzil'):
                self.ui.lbl_menzil.setVisible(is_electric)

            if not is_electric and hasattr(self.ui, 'txt_menzil'):
                self.ui.txt_menzil.clear()
        except:
            pass

    def _setup_comboboxes(self):
        self.ui.cmb_arac_turu.addItems(["Otomobil", "Arazi Aracı", "Kamyonet", "Minibüs"])
        self.ui.cmb_yakit_turu.addItems(["Benzin", "Dizel", "LPG", "Hibrit", "Elektrik"])
        self.ui.cmb_vites.addItems(["Manuel", "Otomatik", "Yarı Otomatik"])
        self.ui.cmb_kasa_tipi.addItems(["Sedan", "Hatchback", "SUV", "Coupe", "Station Wagon"])
        self.ui.cmb_cekis.addItems(["Önden Çekiş", "Arkadan İtiş", "4x4", "AWD"])

        self.ui.spin_uretim_yili.setRange(1900, 2100)
        self.ui.spin_uretim_yili.setValue(2023)
        self.ui.spin_motor_gucu.setMaximum(5000)
        self.ui.spin_motor_hacmi.setMaximum(10000)
        self.ui.spin_gunluk_bedel.setMaximum(99999.99)
        self.ui.spin_gunluk_bedel.setDecimals(2)

    def _setup_table(self):

        self.ui.tbl_liste.setColumnCount(18)
        headers = ["ID", "Tür", "Marka", "Model", "Yıl", "Yakıt", "Vites", "Güç", "Kasa", "Hacim", "Çekiş", "Kapı", "Renk", "Motor No", "Şasi No", "Bedel", "Kirada?", "Menzil"]
        self.ui.tbl_liste.setHorizontalHeaderLabels(headers)
        self.ui.tbl_liste.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tbl_liste.horizontalHeader().setStretchLastSection(True)

    def load_vehicles(self, search_term=""):
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        query = "SELECT arac_id, arac_turu, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_bedel, kirada, menzil, kullanim_disi FROM araclar"
        params = ()

        if search_term:
            query += " WHERE marka LIKE %s OR model LIKE %s OR sasi_no LIKE %s"
            search_pattern = f"%{search_term}%"
            params = (search_pattern, search_pattern, search_pattern)

        cursor.execute(query, params)
        records = cursor.fetchall()
        self.ui.tbl_liste.setRowCount(0)

        for row_num, row_data in enumerate(records):
            self.ui.tbl_liste.insertRow(row_num)

            for col_num in range(18):
                data = row_data[col_num]

                if col_num == 16:
                    item_text = "Evet" if data == 1 else "Hayır"
                elif col_num == 17:
                    item_text = str(data) if data is not None else "-"
                else:
                    item_text = str(data)

                self.ui.tbl_liste.setItem(row_num, col_num, QTableWidgetItem(item_text))

        cursor.close()
        conn.close()

    def search_vehicle(self):
        self.load_vehicles(self.ui.txt_arama.text())

    def clear_form(self):
        self.ui.cmb_arac_turu.setCurrentIndex(0)
        self.ui.txt_marka.clear()
        self.ui.txt_model.clear()
        self.ui.spin_uretim_yili.setValue(2023)
        self.ui.cmb_yakit_turu.setCurrentIndex(0)
        self.ui.cmb_vites.setCurrentIndex(0)
        self.ui.spin_motor_gucu.setValue(0)
        self.ui.cmb_kasa_tipi.setCurrentIndex(0)
        self.ui.spin_motor_hacmi.setValue(0)
        self.ui.cmb_cekis.setCurrentIndex(0)
        self.ui.spin_kapi.setValue(4)
        self.ui.txt_renk.clear()
        self.ui.txt_motor_no.clear()
        self.ui.txt_sasi_no.clear()
        self.ui.spin_gunluk_bedel.setValue(0.00)
        self.ui.chk_kullanim_disi.setChecked(False)
        if hasattr(self.ui, 'txt_menzil'):
            self.ui.txt_menzil.clear()
        self.current_arac_id = None

    def get_form_data(self):
        menzil = None
        if hasattr(self.ui, 'txt_menzil') and self.ui.cmb_yakit_turu.currentText() == "Elektrik":
            menzil = self.ui.txt_menzil.text()
            if menzil == "": menzil = None

        return (
            self.ui.cmb_arac_turu.currentText(), self.ui.txt_marka.text(), self.ui.txt_model.text(),
            self.ui.spin_uretim_yili.value(), self.ui.cmb_yakit_turu.currentText(), self.ui.cmb_vites.currentText(),
            self.ui.spin_motor_gucu.value(), self.ui.cmb_kasa_tipi.currentText(), self.ui.spin_motor_hacmi.value(),
            self.ui.cmb_cekis.currentText(), self.ui.spin_kapi.value(), self.ui.txt_renk.text(),
            self.ui.txt_motor_no.text(), self.ui.txt_sasi_no.text(),
            self.ui.spin_gunluk_bedel.value(),
            menzil,
            self.ui.chk_kullanim_disi.isChecked()
        )

    def save_vehicle(self):
        data = self.get_form_data()

        if not all([data[1], data[2], data[13], data[14]]): # Marka, Model, Şasi, Bedel
            QMessageBox.warning(self, "Hata", "Marka, Model, Şasi No ve Günlük Bedel zorunludur.")
            return

        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        sql = """INSERT INTO araclar (arac_turu, marka, model, uretim_yili, yakit_turu, vites, motor_gucu, kasa_tipi, motor_hacmi, cekis, kapi_sayisi, renk, motor_no, sasi_no, gunluk_bedel, menzil, kullanim_disi)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        try:
            cursor.execute(sql, data)
            conn.commit()
            QMessageBox.information(self, "Başarılı", f"{data[1]} {data[2]} başarıyla kaydedildi.")
            self.clear_form()
            self.load_vehicles()
        except mysql.connector.Error as err:
            if err.errno == 1062:
                QMessageBox.critical(self, "Hata", "Bu Motor No veya Şasi No zaten kayıtlı!")
            else:
                QMessageBox.critical(self, "Hata", f"Kayıt hatası: {err}")
        finally:
            cursor.close()
            conn.close()

    def update_vehicle(self):
        if self.current_arac_id is None:
            QMessageBox.warning(self, "Hata", "Lütfen güncellemek için araç seçin.")
            return

        data = self.get_form_data()

        if not all([data[1], data[2], data[13], data[14]]):
            QMessageBox.warning(self, "Hata", "Zorunlu alanları doldurun.")
            return

        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        sql = """UPDATE araclar SET
                 arac_turu=%s, marka=%s, model=%s, uretim_yili=%s, yakit_turu=%s, vites=%s, motor_gucu=%s,
                 kasa_tipi=%s, motor_hacmi=%s, cekis=%s, kapi_sayisi=%s, renk=%s, motor_no=%s, sasi_no=%s,
                 gunluk_bedel=%s, menzil=%s, kullanim_disi=%s
                 WHERE arac_id=%s"""

        values = data + (self.current_arac_id,)

        try:
            cursor.execute(sql, values)
            conn.commit()
            QMessageBox.information(self, "Başarılı", "Güncelleme tamamlandı.")
            self.clear_form()
            self.load_vehicles()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Hata", f"Güncelleme hatası: {err}")
        finally:
            cursor.close()
            conn.close()

    def delete_vehicle(self):
        if self.current_arac_id is None:
            QMessageBox.warning(self, "Hata", "Silmek için araç seçin.")
            return

        reply = QMessageBox.question(self, 'Onay',
            "Aracı silmek istediğinize emin misiniz?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            conn = get_db_connection(database=DB_NAME)
            if conn is None: return
            cursor = conn.cursor()

            check_sql = "SELECT kirada FROM araclar WHERE arac_id = %s"
            cursor.execute(check_sql, (self.current_arac_id,))
            is_rented = cursor.fetchone()[0]

            if is_rented:
                QMessageBox.critical(self, "Hata", "Bu araç kirada olduğu için silinemez.")
                cursor.close()
                conn.close()
                return

            sql = "DELETE FROM araclar WHERE arac_id = %s"
            try:
                cursor.execute(sql, (self.current_arac_id,))
                conn.commit()
                QMessageBox.information(self, "Başarılı", "Araç silindi.")
                self.clear_form()
                self.load_vehicles()
            except mysql.connector.Error as err:
                QMessageBox.critical(self, "Hata", f"Silme hatası: {err}")
            finally:
                cursor.close()
                conn.close()

    def load_vehicle_to_form(self):
        selected_row = self.ui.tbl_liste.currentRow()
        if selected_row >= 0:
            record = []
            for col in range(self.ui.tbl_liste.columnCount()):
                item = self.ui.tbl_liste.item(selected_row, col)
                record.append(item.text() if item is not None else "")

            self.current_arac_id = record[0]

            self.ui.cmb_arac_turu.setCurrentText(record[1])
            self.ui.txt_marka.setText(record[2])
            self.ui.txt_model.setText(record[3])
            self.ui.spin_uretim_yili.setValue(int(record[4]))


            self.ui.cmb_yakit_turu.setCurrentText(record[5])

            self.ui.cmb_vites.setCurrentText(record[6])
            self.ui.spin_motor_gucu.setValue(int(record[7]))
            self.ui.cmb_kasa_tipi.setCurrentText(record[8])
            self.ui.spin_motor_hacmi.setValue(int(record[9]))
            self.ui.cmb_cekis.setCurrentText(record[10])
            self.ui.spin_kapi.setValue(int(record[11]))
            self.ui.txt_renk.setText(record[12])
            self.ui.txt_motor_no.setText(record[13])
            self.ui.txt_sasi_no.setText(record[14])
            self.ui.spin_gunluk_bedel.setValue(float(record[15]))


            if hasattr(self.ui, 'txt_menzil'):
                try:
                    val = record[17]
                    if val != "-" and val != "None":
                        self.ui.txt_menzil.setText(val)
                    else:
                        self.ui.txt_menzil.clear()
                except: pass

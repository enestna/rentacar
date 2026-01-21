from PySide6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt, QDate
from ui_rental_list import Ui_KiradaOlanlarFormu
from database import get_db_connection, DB_NAME
import mysql.connector

class RentalListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_KiradaOlanlarFormu()
        self.ui.setupUi(self)
        self.setWindowTitle("Kirada Olan / Teslim Edilen Araçlar Listesi")
        self.current_kiralama_id = None
        self.current_arac_id = None

        self._setup_table()

        if hasattr(self.ui, 'btn_teslim_et'):
            self.ui.btn_teslim_et.clicked.connect(self.complete_rental)

        if hasattr(self.ui, 'btn_sil'):
            self.ui.btn_sil.clicked.connect(self.delete_rental)

        self.ui.tbl_liste.itemSelectionChanged.connect(self.select_rental)

    def showEvent(self, event):

        self.load_rentals()
        super().showEvent(event)

    def _setup_table(self):
        self.ui.tbl_liste.setColumnCount(8)
        headers = ["Kiralama ID", "Müşteri (TC)", "Araç Marka/Model", "Başlangıç Tarihi", "Kiralanan Gün", "Toplam Ücret", "Teslim Tarihi", "Araç ID (Gizli)"]
        self.ui.tbl_liste.setHorizontalHeaderLabels(headers)
        self.ui.tbl_liste.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tbl_liste.horizontalHeader().setStretchLastSection(True)
        self.ui.tbl_liste.setColumnHidden(7, True)


    def load_rentals(self):
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        query = """
        SELECT
            k.kiralama_id, m.ad, m.soyad, m.tc_kimlik, a.marka, a.model,
            k.kiralama_tarihi, k.kiralanan_gun, k.toplam_ucret, k.teslim_tarihi, k.arac_id
        FROM kiralamalar k
        JOIN musteriler m ON k.musteri_id = m.musteri_id
        JOIN araclar a ON k.arac_id = a.arac_id
        ORDER BY k.kiralama_tarihi DESC
        """

        cursor.execute(query)
        records = cursor.fetchall()

        self.ui.tbl_liste.setRowCount(0)

        for row_num, row_data in enumerate(records):
            self.ui.tbl_liste.insertRow(row_num)

            kiralama_id = str(row_data[0])
            musteri = f"{row_data[1]} {row_data[2]} ({row_data[3]})"
            arac = f"{row_data[4]} {row_data[5]}"
            kiralama_tarihi = str(row_data[6])
            kiralanan_gun = str(row_data[7])
            toplam_ucret = f"{row_data[8]:.2f} TL"
            teslim_tarihi = str(row_data[9]) if row_data[9] else "--- Kirada ---"
            arac_id = str(row_data[10])

            data_list = [kiralama_id, musteri, arac, kiralama_tarihi, kiralanan_gun, toplam_ucret, teslim_tarihi, arac_id]

            for col_num, data in enumerate(data_list):
                item = QTableWidgetItem(data)
                self.ui.tbl_liste.setItem(row_num, col_num, item)

        cursor.close()
        conn.close()

    def select_rental(self):
        selected_row = self.ui.tbl_liste.currentRow()
        if selected_row >= 0:
            self.current_kiralama_id = self.ui.tbl_liste.item(selected_row, 0).text()
            self.current_arac_id = self.ui.tbl_liste.item(selected_row, 7).text()

            teslim_durumu = self.ui.tbl_liste.item(selected_row, 6).text()

            if hasattr(self.ui, 'btn_teslim_et'):
                if teslim_durumu != "--- Kirada ---":
                    self.ui.btn_teslim_et.setEnabled(False)
                else:
                    self.ui.btn_teslim_et.setEnabled(True)
        else:
            self.current_kiralama_id = None
            self.current_arac_id = None
            if hasattr(self.ui, 'btn_teslim_et'):
                self.ui.btn_teslim_et.setEnabled(False)


    def complete_rental(self):
        if self.current_kiralama_id is None or self.current_arac_id is None:
            QMessageBox.warning(self, "Hata", "Lütfen teslim edilecek bir işlem seçin.")
            return

        reply = QMessageBox.question(self, 'Onay', "Aracı teslim almak istiyor musunuz?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self._update_rental_status(is_delete=False)


    def delete_rental(self):
        if self.current_kiralama_id is None:
            QMessageBox.warning(self, "Hata", "Lütfen silinecek bir işlem seçin.")
            return

        reply = QMessageBox.question(self, 'Onay',
            "Bu kiralama kaydını SİLMEK istediğinize emin misiniz?\nBu işlem geri alınamaz ve araç tekrar 'Müsait' duruma geçer.",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self._update_rental_status(is_delete=True)


    def _update_rental_status(self, is_delete=False):
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        try:
            if is_delete:
                sql_action = "DELETE FROM kiralamalar WHERE kiralama_id = %s"
                cursor.execute(sql_action, (self.current_kiralama_id,))
                msg = "Kiralama kaydı başarıyla silindi."
            else:
                teslim_tarihi = QDate.currentDate().toString(Qt.ISODate)
                sql_action = "UPDATE kiralamalar SET teslim_tarihi = %s WHERE kiralama_id = %s"
                cursor.execute(sql_action, (teslim_tarihi, self.current_kiralama_id))
                msg = "Araç başarıyla teslim alındı."

            sql_vehicle_update = "UPDATE araclar SET kirada = FALSE WHERE arac_id = %s"
            cursor.execute(sql_vehicle_update, (self.current_arac_id,))

            conn.commit()
            QMessageBox.information(self, "Başarılı", msg)

            self.load_rentals()

            if hasattr(self.ui, 'btn_teslim_et'):
                self.ui.btn_teslim_et.setEnabled(False)

        except mysql.connector.Error as err:
            conn.rollback()
            QMessageBox.critical(self, "Hata", f"İşlem sırasında hata oluştu: {err}")
        finally:
            cursor.close()
            conn.close()

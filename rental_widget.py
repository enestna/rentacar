# rental_widget.py

from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt, QDate
from ui_rental_form import Ui_KiralamaFormu
from database import get_db_connection, DB_NAME
import mysql.connector

class RentalWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_KiralamaFormu()
        self.ui.setupUi(self)
        self.setWindowTitle("Araç Kiralama İşlemi")

        self.customer_map = {}

        self._setup_ui()

        self.ui.btn_hesapla.clicked.connect(self.calculate_total_price)
        self.ui.btn_kirala.clicked.connect(self.save_rental)

        self.ui.cmb_arac.currentIndexChanged.connect(self.calculate_total_price)
        self.ui.spin_gun.valueChanged.connect(self.calculate_total_price)

    def showEvent(self, event):
        self.load_customers_to_combo()
        self.load_available_vehicles_to_combo()
        super().showEvent(event)

    def _setup_ui(self):
        self.ui.date_baslangic.setDate(QDate.currentDate())
        self.ui.spin_gun.setMinimum(1)
        self.ui.spin_gun.setMaximum(365)
        self.ui.lbl_toplam_ucret.setText("0.00 TL")

    def load_customers_to_combo(self):
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        query = "SELECT musteri_id, ad, soyad, tc_kimlik FROM musteriler ORDER BY soyad"
        cursor.execute(query)
        records = cursor.fetchall()

        self.ui.cmb_musteri.clear()
        self.ui.cmb_musteri.addItem("--- Müşteri Seçiniz ---", userData=None)

        for musteri_id, ad, soyad, tc in records:
            display_text = f"{ad} {soyad} ({tc})"
            self.ui.cmb_musteri.addItem(display_text, userData=musteri_id)
            self.customer_map[display_text] = musteri_id

        cursor.close()
        conn.close()

    def load_available_vehicles_to_combo(self):
        """Kirada olmayan araçları yükler."""
        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()


        query = "SELECT arac_id, marka, model, gunluk_bedel, yakit_turu FROM araclar WHERE kirada = 0 ORDER BY marka"
        cursor.execute(query)
        records = cursor.fetchall()

        self.ui.cmb_arac.clear()
        self.ui.cmb_arac.addItem("--- Araç Seçiniz ---", userData=None)

        for arac_id, marka, model, bedel, yakit in records:
            display_text = f"{marka} {model} ({yakit}) - {bedel:.2f} TL"

            self.ui.cmb_arac.addItem(display_text, userData={'id': arac_id, 'bedel': float(bedel), 'yakit': yakit})

        cursor.close()
        conn.close()


    def calculate_total_price(self):
        selected_vehicle_data = self.ui.cmb_arac.currentData()
        gun_sayisi = self.ui.spin_gun.value()

        if selected_vehicle_data is None or 'bedel' not in selected_vehicle_data:
            self.ui.lbl_toplam_ucret.setText("0.00 TL")
            return

        gunluk_bedel = selected_vehicle_data['bedel']
        yakit_turu = selected_vehicle_data['yakit']

        toplam_ucret = gunluk_bedel * gun_sayisi
        indirim_tutari = 0.0


        if yakit_turu == "Elektrik":
            indirim_tutari = toplam_ucret * 0.5
            toplam_ucret = toplam_ucret - indirim_tutari
            self.ui.lbl_toplam_ucret.setText(f"{toplam_ucret:.2f} TL (%50 İndirim!)")
            self.ui.lbl_toplam_ucret.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.ui.lbl_toplam_ucret.setText(f"{toplam_ucret:.2f} TL")
            self.ui.lbl_toplam_ucret.setStyleSheet("color: black;")


        return toplam_ucret


    def save_rental(self):
        musteri_id = self.ui.cmb_musteri.currentData()
        arac_data = self.ui.cmb_arac.currentData()

        if musteri_id is None or arac_data is None or arac_data.get('id') is None:
            QMessageBox.warning(self, "Hata", "Lütfen bir müşteri ve bir araç seçiniz.")
            return

        arac_id = arac_data['id']
        gunluk_bedel = arac_data['bedel']
        yakit_turu = arac_data['yakit']

        kiralama_tarihi = self.ui.date_baslangic.date().toString(Qt.ISODate)
        kiralanan_gun = self.ui.spin_gun.value()
        yolculuk_nereye = self.ui.txt_nereye.text()


        ham_fiyat = gunluk_bedel * kiralanan_gun
        indirim_miktari = 0.0
        toplam_ucret = ham_fiyat

        if yakit_turu == "Elektrik":
            indirim_miktari = ham_fiyat * 0.5
            toplam_ucret = ham_fiyat - indirim_miktari

        conn = get_db_connection(database=DB_NAME)
        if conn is None: return
        cursor = conn.cursor()

        try:

            sql_insert = """INSERT INTO kiralamalar
                            (musteri_id, arac_id, kiralama_tarihi, kiralanan_gun, yolculuk_nereye, toplam_ucret, indirim)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            values = (musteri_id, arac_id, kiralama_tarihi, kiralanan_gun, yolculuk_nereye, toplam_ucret, indirim_miktari)
            cursor.execute(sql_insert, values)

            sql_update = "UPDATE araclar SET kirada = TRUE WHERE arac_id = %s"
            cursor.execute(sql_update, (arac_id,))

            conn.commit()
            QMessageBox.information(self, "Başarılı",
                                    f"Kiralama başarılı.\nToplam: {toplam_ucret:.2f} TL\nUygulanan İndirim: {indirim_miktari:.2f} TL")

            self.ui.txt_nereye.clear()
            self.calculate_total_price()
            self.load_available_vehicles_to_combo()

        except mysql.connector.Error as err:
            conn.rollback()
            QMessageBox.critical(self, "Hata", f"Kiralama sırasında veritabanı hatası oluştu: {err}")
        finally:
            cursor.close()
            conn.close()

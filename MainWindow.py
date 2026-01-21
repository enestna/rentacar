import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from database import create_database_and_tables


from ui_form import Ui_MainWindow
from ui_customer_form import Ui_MusteriFormu
from ui_vehicle_form import Ui_AracFormu
from ui_rental_form import Ui_KiralamaFormu
from ui_rental_list import Ui_KiradaOlanlarFormu


from customer_widget import CustomerWidget
from vehicle_widget import VehicleWidget
from rental_widget import RentalWidget
from rental_list_widget import RentalListWidget



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.customer_window = CustomerWidget()
        self.vehicle_window = VehicleWidget()
        self.rental_window = RentalWidget()
        self.rental_list_window = RentalListWidget()


        self.btn_musteri.clicked.connect(self.customer_window.show)
        self.btn_arac.clicked.connect(self.vehicle_window.show)
        self.btn_kiralama.clicked.connect(self.rental_window.show)
        self.btn_listele.clicked.connect(self.rental_list_window.show)

        self.statusbar.showMessage("Uygulama hazır.")

if __name__ == "__main__":
    print("--- MySQL Veritabanı Kurulumu Başladı ---")
    create_database_and_tables()
    print("--- Kurulum Tamamlandı, Uygulama Başlatılıyor ---")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

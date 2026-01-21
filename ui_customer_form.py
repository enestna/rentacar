# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'customer_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MusteriFormu(object):
    def setupUi(self, MusteriFormu):
        if not MusteriFormu.objectName():
            MusteriFormu.setObjectName(u"MusteriFormu")
        MusteriFormu.resize(1431, 871)
        self.btn_kaydet = QPushButton(MusteriFormu)
        self.btn_kaydet.setObjectName(u"btn_kaydet")
        self.btn_kaydet.setGeometry(QRect(20, 680, 90, 29))
        self.btn_guncelle = QPushButton(MusteriFormu)
        self.btn_guncelle.setObjectName(u"btn_guncelle")
        self.btn_guncelle.setGeometry(QRect(150, 680, 90, 29))
        self.btn_sil = QPushButton(MusteriFormu)
        self.btn_sil.setObjectName(u"btn_sil")
        self.btn_sil.setGeometry(QRect(280, 680, 90, 29))
        self.layoutWidget = QWidget(MusteriFormu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 70, 365, 545))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.txt_ad = QLineEdit(self.layoutWidget)
        self.txt_ad.setObjectName(u"txt_ad")

        self.gridLayout.addWidget(self.txt_ad, 0, 1, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txt_soyad = QLineEdit(self.layoutWidget)
        self.txt_soyad.setObjectName(u"txt_soyad")

        self.gridLayout.addWidget(self.txt_soyad, 1, 1, 1, 2)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.txt_tc = QLineEdit(self.layoutWidget)
        self.txt_tc.setObjectName(u"txt_tc")

        self.gridLayout.addWidget(self.txt_tc, 2, 1, 1, 2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.date_dogum = QDateEdit(self.layoutWidget)
        self.date_dogum.setObjectName(u"date_dogum")
        self.date_dogum.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_dogum, 3, 1, 1, 2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.txt_adres = QTextEdit(self.layoutWidget)
        self.txt_adres.setObjectName(u"txt_adres")

        self.gridLayout.addWidget(self.txt_adres, 4, 1, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.txt_telefon_ev = QLineEdit(self.layoutWidget)
        self.txt_telefon_ev.setObjectName(u"txt_telefon_ev")

        self.gridLayout.addWidget(self.txt_telefon_ev, 5, 1, 1, 2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)

        self.txt_telefon_cep = QLineEdit(self.layoutWidget)
        self.txt_telefon_cep.setObjectName(u"txt_telefon_cep")

        self.gridLayout.addWidget(self.txt_telefon_cep, 6, 1, 1, 2)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)

        self.txt_meslek = QLineEdit(self.layoutWidget)
        self.txt_meslek.setObjectName(u"txt_meslek")

        self.gridLayout.addWidget(self.txt_meslek, 7, 1, 1, 2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.cmb_ehliyet = QComboBox(self.layoutWidget)
        self.cmb_ehliyet.setObjectName(u"cmb_ehliyet")

        self.gridLayout.addWidget(self.cmb_ehliyet, 8, 1, 1, 2)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 2)

        self.cmb_medeni = QComboBox(self.layoutWidget)
        self.cmb_medeni.setObjectName(u"cmb_medeni")

        self.gridLayout.addWidget(self.cmb_medeni, 9, 2, 1, 1)

        self.cmb_egitim = QComboBox(self.layoutWidget)
        self.cmb_egitim.setObjectName(u"cmb_egitim")

        self.gridLayout.addWidget(self.cmb_egitim, 10, 2, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 2)

        self.layoutWidget1 = QWidget(MusteriFormu)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(420, 92, 1011, 621))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.txt_arama = QLineEdit(self.layoutWidget1)
        self.txt_arama.setObjectName(u"txt_arama")

        self.verticalLayout.addWidget(self.txt_arama)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.tbl_liste = QTableWidget(self.layoutWidget1)
        self.tbl_liste.setObjectName(u"tbl_liste")

        self.verticalLayout.addWidget(self.tbl_liste)


        self.retranslateUi(MusteriFormu)

        QMetaObject.connectSlotsByName(MusteriFormu)
    # setupUi

    def retranslateUi(self, MusteriFormu):
        MusteriFormu.setWindowTitle(QCoreApplication.translate("MusteriFormu", u"musteri bilgileri", None))
        self.btn_kaydet.setText(QCoreApplication.translate("MusteriFormu", u"KAYDET", None))
        self.btn_guncelle.setText(QCoreApplication.translate("MusteriFormu", u"G\u00dcNCELLE", None))
        self.btn_sil.setText(QCoreApplication.translate("MusteriFormu", u"S\u0130L", None))
        self.label.setText(QCoreApplication.translate("MusteriFormu", u"AD", None))
        self.txt_ad.setText("")
        self.label_2.setText(QCoreApplication.translate("MusteriFormu", u"SOYAD", None))
        self.label_7.setText(QCoreApplication.translate("MusteriFormu", u"TC Kimlik", None))
        self.label_3.setText(QCoreApplication.translate("MusteriFormu", u"Do\u011fum Tarihi", None))
        self.label_5.setText(QCoreApplication.translate("MusteriFormu", u"Adres", None))
        self.label_6.setText(QCoreApplication.translate("MusteriFormu", u"Ev Telefonu", None))
        self.label_4.setText(QCoreApplication.translate("MusteriFormu", u"Cep Telefonu", None))
        self.label_9.setText(QCoreApplication.translate("MusteriFormu", u"Mesle\u011fi", None))
        self.label_8.setText(QCoreApplication.translate("MusteriFormu", u"Ehliyet S\u0131n\u0131f\u0131", None))
        self.label_11.setText(QCoreApplication.translate("MusteriFormu", u"Medeni Durumu", None))
        self.label_10.setText(QCoreApplication.translate("MusteriFormu", u"E\u011fitim Durumu", None))
        self.label_12.setText(QCoreApplication.translate("MusteriFormu", u" ARAMA :", None))
        self.label_13.setText(QCoreApplication.translate("MusteriFormu", u"M\u00dc\u015eTER\u0130 L\u0130STES\u0130 :", None))
    # retranslateUi


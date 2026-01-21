# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rental_form.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_KiralamaFormu(object):
    def setupUi(self, KiralamaFormu):
        if not KiralamaFormu.objectName():
            KiralamaFormu.setObjectName(u"KiralamaFormu")
        KiralamaFormu.resize(1091, 765)
        self.btn_hesapla = QPushButton(KiralamaFormu)
        self.btn_hesapla.setObjectName(u"btn_hesapla")
        self.btn_hesapla.setGeometry(QRect(50, 540, 90, 29))
        self.btn_kirala = QPushButton(KiralamaFormu)
        self.btn_kirala.setObjectName(u"btn_kirala")
        self.btn_kirala.setGeometry(QRect(200, 540, 231, 29))
        self.layoutWidget = QWidget(KiralamaFormu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 160, 321, 241))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cmb_musteri = QComboBox(self.layoutWidget)
        self.cmb_musteri.setObjectName(u"cmb_musteri")

        self.gridLayout.addWidget(self.cmb_musteri, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.cmb_arac = QComboBox(self.layoutWidget)
        self.cmb_arac.setObjectName(u"cmb_arac")

        self.gridLayout.addWidget(self.cmb_arac, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.date_baslangic = QDateEdit(self.layoutWidget)
        self.date_baslangic.setObjectName(u"date_baslangic")
        self.date_baslangic.setCalendarPopup(True)

        self.gridLayout.addWidget(self.date_baslangic, 2, 1, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.spin_gun = QSpinBox(self.layoutWidget)
        self.spin_gun.setObjectName(u"spin_gun")
        self.spin_gun.setMaximum(365)

        self.gridLayout.addWidget(self.spin_gun, 3, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.txt_nereye = QLineEdit(self.layoutWidget)
        self.txt_nereye.setObjectName(u"txt_nereye")

        self.gridLayout.addWidget(self.txt_nereye, 4, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.lbl_toplam_ucret = QLabel(self.layoutWidget)
        self.lbl_toplam_ucret.setObjectName(u"lbl_toplam_ucret")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.lbl_toplam_ucret.setFont(font)

        self.gridLayout.addWidget(self.lbl_toplam_ucret, 5, 1, 1, 1)


        self.retranslateUi(KiralamaFormu)

        QMetaObject.connectSlotsByName(KiralamaFormu)
    # setupUi

    def retranslateUi(self, KiralamaFormu):
        KiralamaFormu.setWindowTitle(QCoreApplication.translate("KiralamaFormu", u"Kiralama \u0130\u015flemi", None))
        self.btn_hesapla.setText(QCoreApplication.translate("KiralamaFormu", u"HESAPLA", None))
        self.btn_kirala.setText(QCoreApplication.translate("KiralamaFormu", u"K\u0130RALAMAYI TAMAMLA", None))
        self.label_2.setText(QCoreApplication.translate("KiralamaFormu", u"M\u00fc\u015fteri Se\u00e7in", None))
        self.label_3.setText(QCoreApplication.translate("KiralamaFormu", u"Ara\u00e7 Se\u00e7in", None))
        self.label_4.setText(QCoreApplication.translate("KiralamaFormu", u"Kiralama Tarihi ", None))
        self.label.setText(QCoreApplication.translate("KiralamaFormu", u"Kiralanacak G\u00fcn", None))
        self.label_5.setText(QCoreApplication.translate("KiralamaFormu", u"Gidilecek Yer", None))
        self.label_6.setText(QCoreApplication.translate("KiralamaFormu", u"Toplam \u00dccret (TL)", None))
        self.lbl_toplam_ucret.setText(QCoreApplication.translate("KiralamaFormu", u"0,00", None))
    # retranslateUi


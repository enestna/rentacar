# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vehicle_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_AracFormu(object):
    def setupUi(self, AracFormu):
        if not AracFormu.objectName():
            AracFormu.setObjectName(u"AracFormu")
        AracFormu.resize(1638, 803)
        self.layoutWidget = QWidget(AracFormu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 56, 391, 593))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.chk_kullanim_disi = QCheckBox(self.layoutWidget)
        self.chk_kullanim_disi.setObjectName(u"chk_kullanim_disi")

        self.gridLayout_2.addWidget(self.chk_kullanim_disi, 16, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)

        self.cmb_kasa_tipi = QComboBox(self.layoutWidget)
        self.cmb_kasa_tipi.setObjectName(u"cmb_kasa_tipi")

        self.gridLayout_2.addWidget(self.cmb_kasa_tipi, 8, 1, 1, 1)

        self.spin_gunluk_bedel = QDoubleSpinBox(self.layoutWidget)
        self.spin_gunluk_bedel.setObjectName(u"spin_gunluk_bedel")
        self.spin_gunluk_bedel.setMaximum(999999999999999.000000000000000)

        self.gridLayout_2.addWidget(self.spin_gunluk_bedel, 15, 1, 1, 1)

        self.cmb_vites = QComboBox(self.layoutWidget)
        self.cmb_vites.setObjectName(u"cmb_vites")

        self.gridLayout_2.addWidget(self.cmb_vites, 6, 1, 1, 1)

        self.txt_sasi_no = QLineEdit(self.layoutWidget)
        self.txt_sasi_no.setObjectName(u"txt_sasi_no")

        self.gridLayout_2.addWidget(self.txt_sasi_no, 14, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 11, 0, 1, 1)

        self.spin_kapi = QSpinBox(self.layoutWidget)
        self.spin_kapi.setObjectName(u"spin_kapi")
        self.spin_kapi.setMinimum(2)
        self.spin_kapi.setMaximum(5)

        self.gridLayout_2.addWidget(self.spin_kapi, 11, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 7, 0, 1, 1)

        self.txt_marka = QLineEdit(self.layoutWidget)
        self.txt_marka.setObjectName(u"txt_marka")

        self.gridLayout_2.addWidget(self.txt_marka, 1, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 12, 0, 1, 1)

        self.spin_motor_hacmi = QSpinBox(self.layoutWidget)
        self.spin_motor_hacmi.setObjectName(u"spin_motor_hacmi")
        self.spin_motor_hacmi.setMaximum(20000)

        self.gridLayout_2.addWidget(self.spin_motor_hacmi, 9, 1, 1, 1)

        self.spin_motor_gucu = QSpinBox(self.layoutWidget)
        self.spin_motor_gucu.setObjectName(u"spin_motor_gucu")
        self.spin_motor_gucu.setMaximum(20000)

        self.gridLayout_2.addWidget(self.spin_motor_gucu, 7, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 9, 0, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_2.addWidget(self.label_15, 15, 0, 1, 1)

        self.cmb_arac_turu = QComboBox(self.layoutWidget)
        self.cmb_arac_turu.setObjectName(u"cmb_arac_turu")

        self.gridLayout_2.addWidget(self.cmb_arac_turu, 0, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 14, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.txt_motor_no = QLineEdit(self.layoutWidget)
        self.txt_motor_no.setObjectName(u"txt_motor_no")

        self.gridLayout_2.addWidget(self.txt_motor_no, 13, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 10, 0, 1, 1)

        self.txt_renk = QLineEdit(self.layoutWidget)
        self.txt_renk.setObjectName(u"txt_renk")

        self.gridLayout_2.addWidget(self.txt_renk, 12, 1, 1, 1)

        self.cmb_cekis = QComboBox(self.layoutWidget)
        self.cmb_cekis.setObjectName(u"cmb_cekis")

        self.gridLayout_2.addWidget(self.cmb_cekis, 10, 1, 1, 1)

        self.cmb_yakit_turu = QComboBox(self.layoutWidget)
        self.cmb_yakit_turu.setObjectName(u"cmb_yakit_turu")

        self.gridLayout_2.addWidget(self.cmb_yakit_turu, 4, 1, 1, 1)

        self.spin_uretim_yili = QSpinBox(self.layoutWidget)
        self.spin_uretim_yili.setObjectName(u"spin_uretim_yili")
        self.spin_uretim_yili.setMinimum(1900)
        self.spin_uretim_yili.setMaximum(2100)

        self.gridLayout_2.addWidget(self.spin_uretim_yili, 3, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 13, 0, 1, 1)

        self.txt_model = QLineEdit(self.layoutWidget)
        self.txt_model.setObjectName(u"txt_model")

        self.gridLayout_2.addWidget(self.txt_model, 2, 1, 1, 1)

        self.lbl_menzil = QLabel(self.layoutWidget)
        self.lbl_menzil.setObjectName(u"lbl_menzil")

        self.gridLayout_2.addWidget(self.lbl_menzil, 5, 0, 1, 1)

        self.txt_menzil = QLineEdit(self.layoutWidget)
        self.txt_menzil.setObjectName(u"txt_menzil")

        self.gridLayout_2.addWidget(self.txt_menzil, 5, 1, 1, 1)

        self.btn_kaydet = QPushButton(AracFormu)
        self.btn_kaydet.setObjectName(u"btn_kaydet")
        self.btn_kaydet.setGeometry(QRect(60, 720, 90, 29))
        self.btn_guncelle = QPushButton(AracFormu)
        self.btn_guncelle.setObjectName(u"btn_guncelle")
        self.btn_guncelle.setGeometry(QRect(190, 720, 90, 29))
        self.btn_sil = QPushButton(AracFormu)
        self.btn_sil.setObjectName(u"btn_sil")
        self.btn_sil.setGeometry(QRect(320, 720, 90, 29))
        self.layoutWidget1 = QWidget(AracFormu)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(550, 140, 911, 541))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)

        self.txt_arama = QLineEdit(self.layoutWidget1)
        self.txt_arama.setObjectName(u"txt_arama")

        self.gridLayout.addWidget(self.txt_arama, 1, 0, 1, 1)

        self.tbl_liste = QTableWidget(self.layoutWidget1)
        self.tbl_liste.setObjectName(u"tbl_liste")

        self.gridLayout.addWidget(self.tbl_liste, 5, 0, 1, 1)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)


        self.retranslateUi(AracFormu)

        QMetaObject.connectSlotsByName(AracFormu)
    # setupUi

    def retranslateUi(self, AracFormu):
        AracFormu.setWindowTitle(QCoreApplication.translate("AracFormu", u"Ara\u00e7 Bilgileri", None))
        self.label.setText(QCoreApplication.translate("AracFormu", u"Ara\u00e7 T\u00fcr\u00fc", None))
        self.chk_kullanim_disi.setText(QCoreApplication.translate("AracFormu", u"KULLANIM DI\u015eI MI ?", None))
        self.label_5.setText(QCoreApplication.translate("AracFormu", u"Yak\u0131t T\u00fcr\u00fc", None))
        self.label_8.setText(QCoreApplication.translate("AracFormu", u"Kasa Tipi", None))
        self.label_3.setText(QCoreApplication.translate("AracFormu", u"Model", None))
        self.label_4.setText(QCoreApplication.translate("AracFormu", u"\u00dcretim Y\u0131l\u0131", None))
        self.label_11.setText(QCoreApplication.translate("AracFormu", u"Kap\u0131 Say\u0131s\u0131", None))
        self.label_6.setText(QCoreApplication.translate("AracFormu", u"Vites", None))
        self.label_7.setText(QCoreApplication.translate("AracFormu", u"Motor G\u00fcc\u00fc (HP)", None))
        self.label_12.setText(QCoreApplication.translate("AracFormu", u"Renk", None))
        self.label_9.setText(QCoreApplication.translate("AracFormu", u"Motor Hacmi (cc)", None))
        self.label_15.setText(QCoreApplication.translate("AracFormu", u"G\u00fcnl\u00fck Kiralama Bedeli (TL)", None))
        self.label_14.setText(QCoreApplication.translate("AracFormu", u"\u015easi No", None))
        self.label_2.setText(QCoreApplication.translate("AracFormu", u"Marka", None))
        self.label_10.setText(QCoreApplication.translate("AracFormu", u"\u00c7eki\u015f", None))
        self.label_13.setText(QCoreApplication.translate("AracFormu", u"Motor No", None))
        self.lbl_menzil.setText(QCoreApplication.translate("AracFormu", u"Menzil (km):", None))
        self.btn_kaydet.setText(QCoreApplication.translate("AracFormu", u"KAYDET", None))
        self.btn_guncelle.setText(QCoreApplication.translate("AracFormu", u"G\u00dcNCELLE", None))
        self.btn_sil.setText(QCoreApplication.translate("AracFormu", u"S\u0130L", None))
        self.label_17.setText(QCoreApplication.translate("AracFormu", u"ARA\u00c7 L\u0130STES\u0130", None))
        self.label_16.setText(QCoreApplication.translate("AracFormu", u"ARAMA", None))
    # retranslateUi


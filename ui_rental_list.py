# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rental_list.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_KiradaOlanlarFormu(object):
    def setupUi(self, KiradaOlanlarFormu):
        if not KiradaOlanlarFormu.objectName():
            KiradaOlanlarFormu.setObjectName(u"KiradaOlanlarFormu")
        KiradaOlanlarFormu.resize(1190, 790)
        self.layoutWidget = QWidget(KiradaOlanlarFormu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1021, 691))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_arama_kira = QLineEdit(self.layoutWidget)
        self.txt_arama_kira.setObjectName(u"txt_arama_kira")

        self.gridLayout.addWidget(self.txt_arama_kira, 1, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.tbl_liste = QTableWidget(self.layoutWidget)
        self.tbl_liste.setObjectName(u"tbl_liste")

        self.gridLayout.addWidget(self.tbl_liste, 3, 0, 1, 1)

        self.btn_sil = QPushButton(KiradaOlanlarFormu)
        self.btn_sil.setObjectName(u"btn_sil")
        self.btn_sil.setGeometry(QRect(29, 710, 551, 61))
        font = QFont()
        font.setPointSize(20)
        self.btn_sil.setFont(font)
        self.btn_teslim_et = QPushButton(KiradaOlanlarFormu)
        self.btn_teslim_et.setObjectName(u"btn_teslim_et")
        self.btn_teslim_et.setGeometry(QRect(700, 710, 321, 61))
        self.btn_teslim_et.setFont(font)

        self.retranslateUi(KiradaOlanlarFormu)

        QMetaObject.connectSlotsByName(KiradaOlanlarFormu)
    # setupUi

    def retranslateUi(self, KiradaOlanlarFormu):
        KiradaOlanlarFormu.setWindowTitle(QCoreApplication.translate("KiradaOlanlarFormu", u"Kirada Olan Ara\u00e7lar", None))
        self.label.setText(QCoreApplication.translate("KiradaOlanlarFormu", u"ARAMA YAP", None))
        self.label_2.setText(QCoreApplication.translate("KiradaOlanlarFormu", u"K\u0130RALAMA L\u0130STES\u0130", None))
        self.btn_sil.setText(QCoreApplication.translate("KiradaOlanlarFormu", u"S\u0130L", None))
        self.btn_teslim_et.setText(QCoreApplication.translate("KiradaOlanlarFormu", u"TESL\u0130M ET", None))
    # retranslateUi


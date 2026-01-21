# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1039, 765)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_musteri = QPushButton(self.widget)
        self.btn_musteri.setObjectName(u"btn_musteri")
        font1 = QFont()
        font1.setPointSize(15)
        self.btn_musteri.setFont(font1)
        self.btn_musteri.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.btn_musteri)

        self.btn_arac = QPushButton(self.widget)
        self.btn_arac.setObjectName(u"btn_arac")
        self.btn_arac.setFont(font1)

        self.verticalLayout.addWidget(self.btn_arac)

        self.btn_kiralama = QPushButton(self.widget)
        self.btn_kiralama.setObjectName(u"btn_kiralama")
        self.btn_kiralama.setFont(font1)

        self.verticalLayout.addWidget(self.btn_kiralama)

        self.btn_listele = QPushButton(self.widget)
        self.btn_listele.setObjectName(u"btn_listele")
        self.btn_listele.setFont(font1)

        self.verticalLayout.addWidget(self.btn_listele)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1039, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ara\u00e7 Kiralama Sistemi - Ana Men\u00fc", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RENT A CAR", None))
        self.btn_musteri.setText(QCoreApplication.translate("MainWindow", u"M\u00fc\u015fteri Bilgileri   (customer information)", None))
        self.btn_arac.setText(QCoreApplication.translate("MainWindow", u"Ara\u00e7 Bilgileri  (vehicle information)", None))
        self.btn_kiralama.setText(QCoreApplication.translate("MainWindow", u"Kiralama Bilgileri (rental information)", None))
        self.btn_listele.setText(QCoreApplication.translate("MainWindow", u"Kirada Olan Ara\u00e7lar  (vehicles on rent)", None))
    # retranslateUi


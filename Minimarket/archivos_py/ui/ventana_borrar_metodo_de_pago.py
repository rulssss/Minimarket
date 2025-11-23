# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_borrar_metodo_de_pago.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form_borrar_mp(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 190)
        Form.setMinimumSize(QSize(250, 190))
        Form.setMaximumSize(QSize(250, 190))
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #f8f9fa;      /* Gris muy claro */\n"
"    color: #222222;                 /* Texto oscuro */\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #e2e6ea;      /* Un poco m\u00e1s oscuro al pasar el mouse */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #d1d5d8;      /* Gris m\u00e1s oscuro al presionar */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))
        self.comboBox.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox.setFont(font1)

        self.verticalLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"M\u00e9todo de Pago", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Quitar", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Label advertencia", None))
    # retranslateUi


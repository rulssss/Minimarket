# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_agregar_metodo_de_pago.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form_agregar_mp(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 180)
        Form.setMinimumSize(QSize(250, 180))
        Form.setMaximumSize(QSize(250, 180))
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
"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(150, 0))
        self.lineEdit.setMaximumSize(QSize(150, 16777215))
        self.lineEdit.setFont(font)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 30))
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton.setFont(font2)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"M\u00e9todo de Pago", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Agregar", None))
    # retranslateUi


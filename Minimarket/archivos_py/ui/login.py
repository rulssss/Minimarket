# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_1.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form_login(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 480)
        Form.setMinimumSize(QSize(400, 480))
        Form.setMaximumSize(QSize(400, 480))
        Form.setStyleSheet(u"\n"
"QWidget {\n"
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
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 39))
        self.stackedWidget.setStyleSheet(u"QLineEdit {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"QComboBox {\n"
"    background-color: #f0f0f0;\n"
"}")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.page_1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(190, 0))
        self.comboBox.setMaximumSize(QSize(190, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        self.comboBox.setFont(font2)

        self.verticalLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.page_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(190, 0))
        self.lineEdit.setMaximumSize(QSize(190, 16777215))
        self.lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.page_1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(190, 0))
        self.lineEdit_2.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_10 = QLabel(self.page_1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))
        self.label_10.setFont(font1)

        self.verticalLayout.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_5 = QLineEdit(self.page_1)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(190, 0))
        self.lineEdit_5.setMaximumSize(QSize(180, 16777215))
        self.lineEdit_5.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_21 = QLabel(self.page_1)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 25))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton.setFont(font3)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_5 = QPushButton(self.page_1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_1)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_7 = QVBoxLayout(self.page_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_23 = QLabel(self.page_6)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.verticalLayout_7.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_24 = QLabel(self.page_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 35))
        self.label_24.setMaximumSize(QSize(16777215, 35))
        font4 = QFont()
        font4.setPointSize(11)
        self.label_24.setFont(font4)

        self.verticalLayout_7.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_25 = QLabel(self.page_6)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_11 = QLineEdit(self.page_6)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(190, 0))
        self.lineEdit_11.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_11.setFont(font2)

        self.verticalLayout_7.addWidget(self.lineEdit_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_26 = QLabel(self.page_6)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_12 = QLineEdit(self.page_6)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(190, 0))
        self.lineEdit_12.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_12.setFont(font2)

        self.verticalLayout_7.addWidget(self.lineEdit_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_27 = QLabel(self.page_6)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_7.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_15 = QPushButton(self.page_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 0))
        self.pushButton_15.setMaximumSize(QSize(150, 16777215))
        self.pushButton_15.setFont(font3)

        self.verticalLayout_7.addWidget(self.pushButton_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.pushButton_16 = QPushButton(self.page_6)
        self.pushButton_16.setObjectName(u"pushButton_16")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setUnderline(True)
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setFlat(True)

        self.verticalLayout_7.addWidget(self.pushButton_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_2 = QComboBox(self.page_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(190, 0))
        self.comboBox_2.setMaximumSize(QSize(190, 16777215))
        self.comboBox_2.setFont(font2)

        self.verticalLayout_2.addWidget(self.comboBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 20))
        self.label_7.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(190, 0))
        self.lineEdit_3.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_3.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 20))
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(190, 0))
        self.lineEdit_4.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_4.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineEdit_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 0))
        self.pushButton_2.setMaximumSize(QSize(150, 16777215))
        self.pushButton_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 35))
        self.label_11.setFont(font)

        self.verticalLayout_3.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.label_12 = QLabel(self.page_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_6 = QLineEdit(self.page_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(190, 0))
        self.lineEdit_6.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_6.setFont(font2)

        self.verticalLayout_3.addWidget(self.lineEdit_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_18 = QLabel(self.page_3)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_3.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(150, 0))
        self.pushButton_6.setMaximumSize(QSize(150, 16777215))
        self.pushButton_6.setFont(font3)

        self.verticalLayout_3.addWidget(self.pushButton_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_13 = QLabel(self.page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 35))
        self.label_13.setFont(font)

        self.verticalLayout_4.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_5)

        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_7 = QLineEdit(self.page)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(190, 0))
        self.lineEdit_7.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_7.setFont(font2)

        self.verticalLayout_4.addWidget(self.lineEdit_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_4.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(150, 0))
        self.pushButton_8.setMaximumSize(QSize(150, 16777215))
        self.pushButton_8.setFont(font3)

        self.verticalLayout_4.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(120, 0))
        self.pushButton_9.setMaximumSize(QSize(120, 16777215))
        self.pushButton_9.setFlat(True)

        self.verticalLayout_4.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_10 = QPushButton(self.page)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_4.addWidget(self.pushButton_10, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_7)

        self.label_15 = QLabel(self.page_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_8)

        self.lineEdit_8 = QLineEdit(self.page_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(190, 0))
        self.lineEdit_8.setMaximumSize(QSize(190, 16777215))

        self.verticalLayout_5.addWidget(self.lineEdit_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_5.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_11 = QPushButton(self.page_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(150, 0))
        self.pushButton_11.setMaximumSize(QSize(150, 16777215))
        self.pushButton_11.setFont(font3)

        self.verticalLayout_5.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.pushButton_12 = QPushButton(self.page_4)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_5.addWidget(self.pushButton_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_6 = QVBoxLayout(self.page_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_19 = QLabel(self.page_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 40))
        self.label_19.setFont(font)

        self.verticalLayout_6.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_20 = QLabel(self.page_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 25))
        self.label_20.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_9 = QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(190, 0))
        self.lineEdit_9.setMaximumSize(QSize(190, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.lineEdit_9.setFont(font6)

        self.verticalLayout_6.addWidget(self.lineEdit_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_22 = QLabel(self.page_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 25))
        self.label_22.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_10 = QLineEdit(self.page_5)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(190, 0))
        self.lineEdit_10.setMaximumSize(QSize(190, 16777215))
        self.lineEdit_10.setFont(font2)

        self.verticalLayout_6.addWidget(self.lineEdit_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_28 = QLabel(self.page_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_13 = QPushButton(self.page_5)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(150, 0))
        self.pushButton_13.setMaximumSize(QSize(150, 16777215))
        self.pushButton_13.setFont(font3)

        self.verticalLayout_6.addWidget(self.pushButton_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_6)

        self.pushButton_14 = QPushButton(self.page_5)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_6.addWidget(self.pushButton_14, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(2)
        self.pushButton_16.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Registrar Cuenta", None))
        self.label.setText(QCoreApplication.translate("Form", u"Tipo de cuenta :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Usuario :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"E-mail :", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"-- Ingrese su cuenta web --", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"E-mail :", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Ingresar", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Olvide mi contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Login rls", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Seleccione el Tipo de Cuenta :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Usuario :", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Registrar Cuenta", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Recuperar Cuenta", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Recuperar Cuenta", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"E-mail de recuperaci\u00f3n :", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"label de error", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Recuperar", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Verificaci\u00f3n", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Ingrese el c\u00f3digo de verificaci\u00f3n :", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"label de error", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Reenviar C\u00f3digo", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Introduzca el c\u00f3digo de verificacion enviado :", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"label de error", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Reestablecer Contrase\u00f1a", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Nueva Contrase\u00f1a :", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Repetir Contrase\u00f1a :", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"<< Atr\u00e1s", None))
    # retranslateUi


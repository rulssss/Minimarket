# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 39))
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_9 = QVBoxLayout(self.page_9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.page_9)
        self.label_24.setObjectName(u"label_24")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_24.setFont(font)

        self.verticalLayout_9.addWidget(self.label_24, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_25 = QLabel(self.page_9)
        self.label_25.setObjectName(u"label_25")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_25.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_25, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_26 = QLabel(self.page_9)
        self.label_26.setObjectName(u"label_26")
        font2 = QFont()
        font2.setBold(True)
        self.label_26.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_11 = QLineEdit(self.page_9)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 0))
        self.lineEdit_11.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEdit_11.setFont(font3)

        self.verticalLayout_9.addWidget(self.lineEdit_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_27 = QLabel(self.page_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_27, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_12 = QLineEdit(self.page_9)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setMinimumSize(QSize(200, 0))
        self.lineEdit_12.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_12.setSizeIncrement(QSize(0, 0))
        self.lineEdit_12.setFont(font3)

        self.verticalLayout_9.addWidget(self.lineEdit_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_32 = QLabel(self.page_9)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_9.addWidget(self.label_32, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_15)

        self.pushButton_15 = QPushButton(self.page_9)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(150, 0))
        self.pushButton_15.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.pushButton_15.setFont(font4)

        self.verticalLayout_9.addWidget(self.pushButton_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.pushButton_16 = QPushButton(self.page_9)
        self.pushButton_16.setObjectName(u"pushButton_16")
        font5 = QFont()
        font5.setUnderline(True)
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setAutoDefault(False)
        self.pushButton_16.setFlat(True)

        self.verticalLayout_9.addWidget(self.pushButton_16)

        self.stackedWidget.addWidget(self.page_9)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout = QVBoxLayout(self.page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label.setFont(font6)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.page)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 0))
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setFont(font3)

        self.verticalLayout.addWidget(self.comboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font6)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(200, 16777215))
        self.lineEdit.setFont(font3)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_2.setFont(font3)

        self.verticalLayout.addWidget(self.lineEdit_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout.addWidget(self.label_21, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))
        self.pushButton.setMaximumSize(QSize(150, 16777215))
        self.pushButton.setFont(font4)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_2 = QComboBox(self.page_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(200, 0))
        self.comboBox_2.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.comboBox_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.lineEdit_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(200, 0))
        self.lineEdit_4.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_2.addWidget(self.lineEdit_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_14 = QLabel(self.page_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)

        self.verticalLayout_2.addWidget(self.label_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_8 = QLineEdit(self.page_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(200, 0))
        self.lineEdit_8.setMaximumSize(QSize(200, 16777215))
        font7 = QFont()
        font7.setPointSize(9)
        self.lineEdit_8.setFont(font7)

        self.verticalLayout_2.addWidget(self.lineEdit_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 40))
        self.label_20.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.label_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 0))
        self.pushButton_4.setMaximumSize(QSize(150, 16777215))
        self.pushButton_4.setFont(font4)

        self.verticalLayout_2.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_3.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)

        self.verticalLayout_3.addWidget(self.label_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_5 = QLineEdit(self.page_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(200, 0))
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        self.lineEdit_5.setFont(font8)

        self.verticalLayout_3.addWidget(self.lineEdit_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_11 = QLabel(self.page_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)

        self.verticalLayout_3.addWidget(self.label_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_6 = QLineEdit(self.page_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(200, 0))
        self.lineEdit_6.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_6.setFont(font8)

        self.verticalLayout_3.addWidget(self.lineEdit_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_3.addWidget(self.label_19, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(150, 0))
        self.pushButton_6.setMaximumSize(QSize(150, 16777215))
        self.pushButton_6.setFont(font4)

        self.verticalLayout_3.addWidget(self.pushButton_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_16)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_8)

        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_3.addWidget(self.pushButton_7, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_4 = QVBoxLayout(self.page_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_12 = QLabel(self.page_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.verticalLayout_4.addWidget(self.label_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_9)

        self.label_13 = QLabel(self.page_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)

        self.verticalLayout_4.addWidget(self.label_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_10)

        self.lineEdit_7 = QLineEdit(self.page_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(200, 0))
        self.lineEdit_7.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_7.setFont(font3)

        self.verticalLayout_4.addWidget(self.lineEdit_7, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_17 = QLabel(self.page_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_4.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_8 = QPushButton(self.page_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(150, 0))
        self.pushButton_8.setMaximumSize(QSize(150, 16777215))
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setStrikeOut(False)
        self.pushButton_8.setFont(font9)

        self.verticalLayout_4.addWidget(self.pushButton_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.pushButton_9 = QPushButton(self.page_4)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_4.addWidget(self.pushButton_9, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_5 = QVBoxLayout(self.page_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_12)

        self.label_16 = QLabel(self.page_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.verticalLayout_5.addWidget(self.label_16, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_13)

        self.label_15 = QLabel(self.page_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_15, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_14)

        self.lineEdit_9 = QLineEdit(self.page_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(200, 0))
        self.lineEdit_9.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_9.setFont(font8)

        self.verticalLayout_5.addWidget(self.lineEdit_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_18 = QLabel(self.page_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_10 = QPushButton(self.page_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(150, 0))
        self.pushButton_10.setMaximumSize(QSize(150, 16777215))
        self.pushButton_10.setFont(font4)

        self.verticalLayout_5.addWidget(self.pushButton_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_11 = QPushButton(self.page_5)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMaximumSize(QSize(100, 16777215))
        self.pushButton_11.setFlat(True)

        self.verticalLayout_5.addWidget(self.pushButton_11, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.page_5)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_5.addWidget(self.pushButton_12, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_6 = QVBoxLayout(self.page_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_11)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_17)

        self.label_22 = QLabel(self.page_6)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_6.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_6.addItem(self.horizontalSpacer_7)

        self.lineEdit_10 = QLineEdit(self.page_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(200, 0))
        self.lineEdit_10.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_6.addWidget(self.lineEdit_10, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_23 = QLabel(self.page_6)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_6.addWidget(self.label_23, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_13 = QPushButton(self.page_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(150, 0))
        self.pushButton_13.setMaximumSize(QSize(150, 16777215))
        self.pushButton_13.setFont(font4)

        self.verticalLayout_6.addWidget(self.pushButton_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.pushButton_14 = QPushButton(self.page_6)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_6.addWidget(self.pushButton_14, 0, Qt.AlignmentFlag.AlignLeft)

        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_7 = QVBoxLayout(self.page_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_8 = QVBoxLayout(self.page_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_19)

        self.label_28 = QLabel(self.page_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.verticalLayout_8.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_18)

        self.label_29 = QLabel(self.page_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_29, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_13 = QLineEdit(self.page_8)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(200, 0))
        self.lineEdit_13.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_13.setFont(font3)

        self.verticalLayout_8.addWidget(self.lineEdit_13, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_30 = QLabel(self.page_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_30, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_14 = QLineEdit(self.page_8)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMinimumSize(QSize(200, 0))
        self.lineEdit_14.setSizeIncrement(QSize(0, 0))
        self.lineEdit_14.setFont(font3)

        self.verticalLayout_8.addWidget(self.lineEdit_14, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_31 = QLabel(self.page_8)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_8.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_18 = QPushButton(self.page_8)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(150, 0))
        self.pushButton_18.setSizeIncrement(QSize(150, 0))
        self.pushButton_18.setFont(font6)

        self.verticalLayout_8.addWidget(self.pushButton_18, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.page_8)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_16.setDefault(False)
        self.pushButton_3.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"-- Ingrese su cuenta web --", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"Email :", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Ingresar", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Olvide mi contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Login rls", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione el tipo de cuenta :", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Usuario :", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Registrar cuenta", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Recuperar cuenta", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Registrar Cuenta", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Tipo de cuenta :", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Usuario :", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Email :", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Reestablecer Contrase\u00f1a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a nueva :", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Repetir contrase\u00f1a :", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"<< Atr\u00e1s", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Recuperar Cuenta", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Email de recuperaci\u00f3n :", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Recuperar", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"< Atr\u00e1s", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Verificaci\u00f3n", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Ingrese el codigo de verificaci\u00f3n :", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Label de error", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Reenviar codigo", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"< Atras ", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"label de titulo donde avisa que inserte el codigo ", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"lABELD E ERRRO", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"< Atras", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"Verificaci\u00f3n", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"Codigo Email :", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"Codigo Tel\u00e9fono :", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"label error", None))
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"Verificar", None))
    # retranslateUi


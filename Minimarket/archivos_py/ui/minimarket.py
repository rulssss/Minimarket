# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disenio_front.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(2530, 1082)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 300))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(6)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setPointSize(6)
        font1.setBold(False)
        font1.setStrikeOut(False)
        self.centralwidget.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(315, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.tabWidget.setFont(font2)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setAutoFillBackground(True)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setStrikeOut(False)
        self.tab_1.setFont(font3)
        self.tab_1.setAutoFillBackground(True)
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_5)

        self.label = QLabel(self.tab_1)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 300))
        self.label.setFont(font2)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(self.tab_1)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMaximumSize(QSize(291, 16777215))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoRepeat(False)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.tab_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditFind))
        self.pushButton_2.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.tab_1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButton_4.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.tab_1)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_8 = QPushButton(self.tab_1)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.tab_1)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.tab_1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_5 = QPushButton(self.tab_1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_9 = QPushButton(self.tab_1)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.tab_1)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.tab_1)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_4)

        self.pushButton_14 = QPushButton(self.tab_1)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_14)

        self.pushButton_18 = QPushButton(self.tab_1)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_18)

        self.pushButton_22 = QPushButton(self.tab_1)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.pushButton_22)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.pushButton_12 = QPushButton(self.tab_1)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(150, 0))
        self.pushButton_12.setMaximumSize(QSize(150, 16777215))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning))
        self.pushButton_12.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_9 = QFrame(self.tab_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 0))
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font3)
        self.tab_3.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_7)

        self.pushButton_15 = QPushButton(self.tab_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FormatJustifyCenter))
        self.pushButton_15.setIcon(icon4)

        self.verticalLayout_3.addWidget(self.pushButton_15)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_9)

        self.pushButton_13 = QPushButton(self.tab_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AppointmentNew))
        self.pushButton_13.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.horizontalSpacer_164 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_164)

        self.pushButton_48 = QPushButton(self.tab_3)
        self.pushButton_48.setObjectName(u"pushButton_48")

        self.verticalLayout_3.addWidget(self.pushButton_48)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font3)
        self.tab.setAutoFillBackground(True)
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_13)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_4.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_10)

        self.pushButton_16 = QPushButton(self.tab)
        self.pushButton_16.setObjectName(u"pushButton_16")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailMessageNew))
        self.pushButton_16.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_16)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_11)

        self.pushButton_17 = QPushButton(self.tab)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.pushButton_17)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_8)

        self.label_63 = QLabel(self.tab)
        self.label_63.setObjectName(u"label_63")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setUnderline(True)
        font4.setStrikeOut(False)
        self.label_63.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_63)

        self.textEdit_3 = QTextEdit(self.tab)
        self.textEdit_3.setObjectName(u"textEdit_3")

        self.verticalLayout_4.addWidget(self.textEdit_3)

        self.horizontalSpacer_135 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_135)

        self.frame_39 = QFrame(self.tab)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(200, 0))
        self.frame_39.setMaximumSize(QSize(200, 16777215))
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_68 = QLabel(self.frame_39)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_10.addWidget(self.label_68, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_69 = QLabel(self.frame_39)
        self.label_69.setObjectName(u"label_69")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setStrikeOut(False)
        self.label_69.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_69, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_4.addWidget(self.frame_39, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_136 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_136)

        self.tabWidget.addTab(self.tab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.frame_37 = QFrame(self.centralwidget)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_37)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_66 = QLabel(self.frame_37)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font2)

        self.verticalLayout_33.addWidget(self.label_66)

        self.label_65 = QLabel(self.frame_37)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)
        self.label_65.setFrameShape(QFrame.Shape.StyledPanel)

        self.verticalLayout_33.addWidget(self.label_65, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame_37)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setAutoFillBackground(True)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.horizontalLayout_2 = QHBoxLayout(self.page_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.page_9)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setStrikeOut(False)
        self.comboBox.setFont(font6)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.frame_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(150, 0))
        self.comboBox_2.setFont(font6)

        self.gridLayout_2.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 0, 4, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_15, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setStrikeOut(False)
        self.label_8.setFont(font7)

        self.verticalLayout_6.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.lineEdit1 = QLineEdit(self.frame_4)
        self.lineEdit1.setObjectName(u"lineEdit1")
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(False)
        font8.setStrikeOut(False)
        self.lineEdit1.setFont(font8)

        self.verticalLayout_6.addWidget(self.lineEdit1, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font9 = QFont()
        font9.setPointSize(31)
        font9.setBold(True)
        font9.setStrikeOut(False)
        self.label_5.setFont(font9)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_tabla_productos = QFrame(self.frame)
        self.frame_tabla_productos.setObjectName(u"frame_tabla_productos")
        self.frame_tabla_productos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabla_productos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_tabla_productos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_59 = QFrame(self.frame_tabla_productos)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_134)

        self.label_120 = QLabel(self.frame_59)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setFont(font6)

        self.horizontalLayout_17.addWidget(self.label_120, 0, Qt.AlignmentFlag.AlignRight)

        self.label_121 = QLabel(self.frame_59)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font5)

        self.horizontalLayout_17.addWidget(self.label_121, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_7.addWidget(self.frame_59)

        self.tableWidget = QTableWidget(self.frame_tabla_productos)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        font10 = QFont()
        font10.setPointSize(16)
        font10.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font10);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(191)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.frame_tabla_productos)


        self.horizontalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_9)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_17 = QVBoxLayout(self.page_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_73)

        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_76)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_74)

        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_75)

        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_17.addItem(self.horizontalSpacer_77)

        self.frame_17 = QFrame(self.page_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(800, 250))
        self.frame_17.setAutoFillBackground(True)
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_17)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_72, 3, 2, 1, 1)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_71, 3, 0, 1, 1)

        self.label_34 = QLabel(self.frame_17)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)

        self.gridLayout_8.addWidget(self.label_34, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_69, 2, 1, 1, 1)

        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_67, 0, 1, 1, 1)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_68, 6, 1, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_17)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setMinimumSize(QSize(300, 0))
        self.lineEdit_16.setMaximumSize(QSize(300, 16777215))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(False)
        font11.setStrikeOut(False)
        self.lineEdit_16.setFont(font11)

        self.gridLayout_8.addWidget(self.lineEdit_16, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_27 = QPushButton(self.frame_19)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFont(font3)

        self.horizontalLayout_7.addWidget(self.pushButton_27)

        self.pushButton_28 = QPushButton(self.frame_19)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setFont(font3)

        self.horizontalLayout_7.addWidget(self.pushButton_28)


        self.gridLayout_8.addWidget(self.frame_19, 5, 1, 1, 1)

        self.label_80 = QLabel(self.frame_17)
        self.label_80.setObjectName(u"label_80")
        font12 = QFont()
        font12.setPointSize(8)
        font12.setBold(True)
        font12.setStrikeOut(False)
        self.label_80.setFont(font12)

        self.gridLayout_8.addWidget(self.label_80, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_17, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_24)

        self.stackedWidget.addWidget(self.page_7)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_10 = QVBoxLayout(self.page1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_8 = QFrame(self.page1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_30 = QLabel(self.frame_8)
        self.label_30.setObjectName(u"label_30")
        font13 = QFont()
        font13.setPointSize(59)
        font13.setBold(True)
        font13.setStrikeOut(False)
        self.label_30.setFont(font13)

        self.gridLayout_6.addWidget(self.label_30, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_10.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_8 = QVBoxLayout(self.page2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_18)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_32)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_33)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.horizontalSpacer_34)

        self.frame_6 = QFrame(self.page2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(800, 250))
        self.frame_6.setAutoFillBackground(True)
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_35, 6, 1, 1, 1)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_54, 0, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(300, 0))
        self.lineEdit_2.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_2.setFont(font11)

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_21 = QPushButton(self.frame_6)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(130, 0))
        self.pushButton_21.setMaximumSize(QSize(150, 16777215))
        self.pushButton_21.setFont(font7)

        self.gridLayout_3.addWidget(self.pushButton_21, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_72 = QLabel(self.frame_6)
        self.label_72.setObjectName(u"label_72")
        font14 = QFont()
        font14.setPointSize(8)
        font14.setBold(False)
        font14.setStrikeOut(False)
        self.label_72.setFont(font14)

        self.gridLayout_3.addWidget(self.label_72, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_48, 3, 2, 1, 1)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_38, 3, 0, 1, 1)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_37, 2, 1, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_11)

        self.stackedWidget.addWidget(self.page2)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_39)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_40)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_42)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_43)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_9.addItem(self.horizontalSpacer_41)

        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 250))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_10 = QLineEdit(self.frame_7)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setFont(font3)

        self.gridLayout_4.addWidget(self.lineEdit_10, 4, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_14, 7, 2, 1, 1)

        self.label_74 = QLabel(self.frame_7)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font14)

        self.gridLayout_4.addWidget(self.label_74, 5, 5, 1, 1)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_49, 0, 5, 1, 1)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)

        self.gridLayout_4.addWidget(self.label_12, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_13, 7, 3, 1, 1)

        self.comboBox_7 = QComboBox(self.frame_7)
        self.comboBox_7.setObjectName(u"comboBox_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy2)
        self.comboBox_7.setMinimumSize(QSize(100, 0))
        self.comboBox_7.setMaximumSize(QSize(200, 16777215))
        self.comboBox_7.setFont(font3)

        self.gridLayout_4.addWidget(self.comboBox_7, 4, 8, 1, 1)

        self.comboBox_3 = QComboBox(self.frame_7)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy2.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy2)
        self.comboBox_3.setMinimumSize(QSize(100, 0))
        self.comboBox_3.setMaximumSize(QSize(200, 16777215))
        self.comboBox_3.setFont(font3)

        self.gridLayout_4.addWidget(self.comboBox_3, 4, 1, 1, 1)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_51, 2, 5, 1, 1)

        self.label_26 = QLabel(self.frame_7)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font7)

        self.gridLayout_4.addWidget(self.label_26, 3, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font7)

        self.gridLayout_4.addWidget(self.label_24, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox_4 = QComboBox(self.frame_7)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy2.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy2)
        self.comboBox_4.setMinimumSize(QSize(100, 0))
        self.comboBox_4.setMaximumSize(QSize(200, 16777215))
        self.comboBox_4.setFont(font3)

        self.gridLayout_4.addWidget(self.comboBox_4, 4, 7, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_18, 7, 1, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_17, 7, 8, 1, 1)

        self.label_73 = QLabel(self.frame_7)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font14)

        self.gridLayout_4.addWidget(self.label_73, 5, 4, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_44, 7, 4, 1, 1)

        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)

        self.gridLayout_4.addWidget(self.label_27, 3, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_46, 0, 4, 1, 1)

        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font7)

        self.gridLayout_4.addWidget(self.label_23, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_28 = QLabel(self.frame_7)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)

        self.gridLayout_4.addWidget(self.label_28, 3, 8, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_13 = QLineEdit(self.frame_7)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setFont(font3)

        self.gridLayout_4.addWidget(self.lineEdit_13, 4, 6, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_15, 7, 6, 1, 1)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_50, 2, 4, 1, 1)

        self.label_29 = QLabel(self.frame_7)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)

        self.gridLayout_4.addWidget(self.label_29, 1, 5, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setFont(font3)

        self.gridLayout_4.addWidget(self.lineEdit_12, 4, 5, 1, 1)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.gridLayout_4.addWidget(self.label_11, 1, 4, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_45, 7, 5, 1, 1)

        self.pushButton_23 = QPushButton(self.frame_7)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton_23, 6, 4, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setFont(font3)

        self.gridLayout_4.addWidget(self.lineEdit_9, 4, 2, 1, 1)

        self.label_25 = QLabel(self.frame_7)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font7)

        self.gridLayout_4.addWidget(self.label_25, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_24 = QPushButton(self.frame_7)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setFont(font3)

        self.gridLayout_4.addWidget(self.pushButton_24, 6, 5, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setFont(font3)

        self.gridLayout_4.addWidget(self.lineEdit_11, 4, 4, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font7)

        self.gridLayout_4.addWidget(self.label_10, 3, 6, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 7, 7, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_55 = QFrame(self.page_2)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMaximumSize(QSize(800, 16777215))
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_55)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.label_115 = QLabel(self.frame_55)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font3)

        self.gridLayout_31.addWidget(self.label_115, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_56)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_116 = QLabel(self.frame_56)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font6)

        self.gridLayout_32.addWidget(self.label_116, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_117 = QLabel(self.frame_56)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font6)

        self.gridLayout_32.addWidget(self.label_117, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(100, 16777215))
        self.frame_57.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_118 = QLabel(self.frame_57)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font2)

        self.horizontalLayout_15.addWidget(self.label_118, 0, Qt.AlignmentFlag.AlignRight)

        self.doubleSpinBox = QDoubleSpinBox(self.frame_57)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font6)

        self.horizontalLayout_15.addWidget(self.doubleSpinBox)


        self.gridLayout_32.addWidget(self.frame_57, 1, 0, 1, 1)

        self.frame_58 = QFrame(self.frame_56)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMaximumSize(QSize(100, 16777215))
        self.frame_58.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_119 = QLabel(self.frame_58)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font2)

        self.horizontalLayout_16.addWidget(self.label_119, 0, Qt.AlignmentFlag.AlignRight)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.frame_58)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setFont(font6)

        self.horizontalLayout_16.addWidget(self.doubleSpinBox_2)


        self.gridLayout_32.addWidget(self.frame_58, 1, 1, 1, 1)


        self.gridLayout_31.addWidget(self.frame_56, 2, 0, 1, 1)

        self.comboBox_19 = QComboBox(self.frame_55)
        self.comboBox_19.setObjectName(u"comboBox_19")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_19.sizePolicy().hasHeightForWidth())
        self.comboBox_19.setSizePolicy(sizePolicy3)
        self.comboBox_19.setMinimumSize(QSize(150, 0))
        self.comboBox_19.setMaximumSize(QSize(200, 16777215))
        self.comboBox_19.setFont(font6)

        self.gridLayout_31.addWidget(self.comboBox_19, 0, 2, 1, 1)

        self.label_114 = QLabel(self.frame_55)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font5)

        self.gridLayout_31.addWidget(self.label_114, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_14, 1, 0, 1, 1)

        self.pushButton_49 = QPushButton(self.frame_55)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setMaximumSize(QSize(16777215, 50))
        self.pushButton_49.setFont(font7)

        self.gridLayout_31.addWidget(self.pushButton_49, 2, 2, 1, 1)

        self.comboBox_20 = QComboBox(self.frame_55)
        self.comboBox_20.setObjectName(u"comboBox_20")
        sizePolicy3.setHeightForWidth(self.comboBox_20.sizePolicy().hasHeightForWidth())
        self.comboBox_20.setSizePolicy(sizePolicy3)
        self.comboBox_20.setMinimumSize(QSize(150, 0))
        self.comboBox_20.setMaximumSize(QSize(200, 16777215))
        self.comboBox_20.setFont(font6)

        self.gridLayout_31.addWidget(self.comboBox_20, 1, 2, 1, 1)


        self.verticalLayout_9.addWidget(self.frame_55)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_12)

        self.stackedWidget.addWidget(self.page_2)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout = QVBoxLayout(self.page_10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_25)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_26)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_27)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_28)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_31)

        self.frame_5 = QFrame(self.page_10)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setAutoFillBackground(True)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)

        self.gridLayout_5.addWidget(self.label_22, 3, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 7, 6, 1, 1)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)

        self.gridLayout_5.addWidget(self.label_20, 1, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_23, 7, 3, 1, 1)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font7)

        self.gridLayout_5.addWidget(self.label_19, 3, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)

        self.gridLayout_5.addWidget(self.label_13, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_19 = QPushButton(self.frame_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font3)

        self.gridLayout_5.addWidget(self.pushButton_19, 6, 3, 1, 1)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font7)

        self.gridLayout_5.addWidget(self.label_18, 3, 6, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_22, 0, 4, 1, 1)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)

        self.gridLayout_5.addWidget(self.label_16, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_7 = QLineEdit(self.frame_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_7, 4, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_5)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_6, 4, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_4, 4, 3, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 7, 5, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 7, 2, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)

        self.gridLayout_5.addWidget(self.label_21, 1, 4, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_5)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_8, 4, 5, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_21, 0, 3, 1, 1)

        self.comboBox_5 = QComboBox(self.frame_5)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy2.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy2)
        self.comboBox_5.setMinimumSize(QSize(100, 0))
        self.comboBox_5.setMaximumSize(QSize(200, 16777215))
        self.comboBox_5.setFont(font3)

        self.gridLayout_5.addWidget(self.comboBox_5, 4, 6, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 7, 7, 1, 1)

        self.comboBox_6 = QComboBox(self.frame_5)
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy2.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy2)
        self.comboBox_6.setMinimumSize(QSize(100, 0))
        self.comboBox_6.setMaximumSize(QSize(200, 16777215))
        self.comboBox_6.setFont(font3)

        self.gridLayout_5.addWidget(self.comboBox_6, 4, 7, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font7)

        self.gridLayout_5.addWidget(self.label_17, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.gridLayout_5.addWidget(self.label_15, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 7, 1, 1, 1)

        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.gridLayout_5.addWidget(self.label_14, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_19, 2, 3, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_20, 2, 4, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_5, 4, 2, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_5)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font3)

        self.gridLayout_5.addWidget(self.pushButton_20, 6, 4, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_24, 7, 4, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font3)

        self.gridLayout_5.addWidget(self.lineEdit_3, 4, 4, 1, 1)

        self.label_70 = QLabel(self.frame_5)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font14)

        self.gridLayout_5.addWidget(self.label_70, 5, 3, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_71 = QLabel(self.frame_5)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font14)

        self.gridLayout_5.addWidget(self.label_71, 5, 4, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.stackedWidget.addWidget(self.page_10)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_62)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_63)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_64)

        self.horizontalSpacer_65 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_65)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_11.addItem(self.horizontalSpacer_66)

        self.frame_10 = QFrame(self.page_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(500, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 270))
        self.frame_10.setAutoFillBackground(True)
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)

        self.gridLayout_7.addWidget(self.label_37, 1, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_26 = QPushButton(self.frame_11)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(150, 0))
        self.pushButton_26.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButton_26)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_20)

        self.pushButton_25 = QPushButton(self.frame_11)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(150, 0))
        self.pushButton_25.setFont(font3)

        self.horizontalLayout_4.addWidget(self.pushButton_25)


        self.gridLayout_7.addWidget(self.frame_11, 6, 3, 1, 1)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_59, 2, 3, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_10)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setFont(font3)

        self.gridLayout_7.addWidget(self.lineEdit_17, 4, 5, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_10)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setFont(font3)

        self.gridLayout_7.addWidget(self.lineEdit_14, 4, 1, 1, 1)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_56, 4, 6, 1, 1)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_22, 4, 4, 1, 1)

        self.frame_40 = QFrame(self.frame_10)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMinimumSize(QSize(0, 35))
        self.frame_40.setMaximumSize(QSize(16777215, 35))
        self.frame_40.setSizeIncrement(QSize(0, 30))
        self.frame_40.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_76 = QLabel(self.frame_40)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font12)

        self.horizontalLayout_11.addWidget(self.label_76, 0, Qt.AlignmentFlag.AlignRight)

        self.label_75 = QLabel(self.frame_40)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font12)

        self.horizontalLayout_11.addWidget(self.label_75)


        self.gridLayout_7.addWidget(self.frame_40, 5, 3, 1, 1)

        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_57, 7, 3, 1, 1)

        self.horizontalSpacer_55 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_55, 4, 0, 1, 1)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_58, 0, 3, 1, 1)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_21, 4, 2, 1, 1)

        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font7)

        self.gridLayout_7.addWidget(self.label_32, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_41 = QLabel(self.frame_10)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font7)

        self.gridLayout_7.addWidget(self.label_41, 3, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)

        self.gridLayout_7.addWidget(self.label_33, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_15 = QLineEdit(self.frame_10)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setFont(font3)

        self.gridLayout_7.addWidget(self.lineEdit_15, 4, 3, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_19)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_12 = QVBoxLayout(self.page_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_91)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_92)

        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_93)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_94)

        self.horizontalSpacer_95 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_95)

        self.frame_12 = QFrame(self.page_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(800, 250))
        self.frame_12.setAutoFillBackground(True)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_12)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_87, 2, 1, 1, 1)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_90, 3, 2, 1, 1)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_89, 3, 0, 1, 1)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_86, 6, 1, 1, 1)

        self.pushButton_34 = QPushButton(self.frame_12)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(130, 0))
        self.pushButton_34.setMaximumSize(QSize(150, 16777215))
        self.pushButton_34.setFont(font7)

        self.gridLayout_11.addWidget(self.pushButton_34, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_20 = QLineEdit(self.frame_12)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setMinimumSize(QSize(300, 0))
        self.lineEdit_20.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_20.setFont(font11)

        self.gridLayout_11.addWidget(self.lineEdit_20, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_38 = QLabel(self.frame_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font5)

        self.gridLayout_11.addWidget(self.label_38, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_85, 0, 1, 1, 1)

        self.label_77 = QLabel(self.frame_12)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font12)

        self.gridLayout_11.addWidget(self.label_77, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_12, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_42 = QFrame(self.page_4)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_42)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_82 = QLabel(self.frame_42)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font11)

        self.verticalLayout_34.addWidget(self.label_82, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_42)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_23)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_13 = QVBoxLayout(self.page_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_112)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_115)

        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_113)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_117)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_116)

        self.horizontalSpacer_114 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_114)

        self.frame_13 = QFrame(self.page_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(500, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 270))
        self.frame_13.setAutoFillBackground(True)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_13)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.lineEdit_28 = QLineEdit(self.frame_13)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        sizePolicy1.setHeightForWidth(self.lineEdit_28.sizePolicy().hasHeightForWidth())
        self.lineEdit_28.setSizePolicy(sizePolicy1)
        self.lineEdit_28.setMinimumSize(QSize(100, 0))
        self.lineEdit_28.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_28.setFont(font3)

        self.gridLayout_13.addWidget(self.lineEdit_28, 4, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_107 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_107, 7, 3, 1, 1)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_111, 4, 6, 1, 1)

        self.label_52 = QLabel(self.frame_13)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font7)

        self.gridLayout_13.addWidget(self.label_52, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_37 = QPushButton(self.frame_14)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy3.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy3)
        self.pushButton_37.setMinimumSize(QSize(100, 0))
        self.pushButton_37.setMaximumSize(QSize(150, 16777215))
        self.pushButton_37.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_37)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_32)

        self.pushButton_38 = QPushButton(self.frame_14)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy3.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy3)
        self.pushButton_38.setMinimumSize(QSize(100, 0))
        self.pushButton_38.setMaximumSize(QSize(150, 16777215))
        self.pushButton_38.setFont(font3)

        self.horizontalLayout_5.addWidget(self.pushButton_38)


        self.gridLayout_13.addWidget(self.frame_14, 6, 3, 1, 1)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_108, 4, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.frame_13)
        self.comboBox_11.setObjectName(u"comboBox_11")
        sizePolicy1.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy1)
        self.comboBox_11.setMinimumSize(QSize(100, 0))
        self.comboBox_11.setMaximumSize(QSize(250, 16777215))
        self.comboBox_11.setFont(font3)

        self.gridLayout_13.addWidget(self.comboBox_11, 4, 1, 1, 1)

        self.label_50 = QLabel(self.frame_13)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font5)

        self.gridLayout_13.addWidget(self.label_50, 1, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_105 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_105, 0, 3, 1, 1)

        self.lineEdit_26 = QLineEdit(self.frame_13)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setMinimumSize(QSize(100, 0))
        self.lineEdit_26.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_26.setFont(font3)

        self.gridLayout_13.addWidget(self.lineEdit_26, 4, 5, 1, 1)

        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_31, 4, 2, 1, 1)

        self.label_53 = QLabel(self.frame_13)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font7)

        self.gridLayout_13.addWidget(self.label_53, 3, 5, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_106 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_106, 2, 3, 1, 1)

        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_30, 4, 4, 1, 1)

        self.label_51 = QLabel(self.frame_13)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font7)

        self.gridLayout_13.addWidget(self.label_51, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.frame_41 = QFrame(self.frame_13)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(16777215, 30))
        self.frame_41.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_78 = QLabel(self.frame_41)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font12)

        self.horizontalLayout_12.addWidget(self.label_78, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.label_79 = QLabel(self.frame_41)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font12)

        self.horizontalLayout_12.addWidget(self.label_79, 0, Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_13.addWidget(self.frame_41, 5, 3, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_33)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_6 = QHBoxLayout(self.page_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_15 = QFrame(self.page_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(16777215, 100))
        self.frame_16.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_16)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_18)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_57 = QLabel(self.frame_18)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font7)

        self.verticalLayout_15.addWidget(self.label_57, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.lineEdit_27 = QLineEdit(self.frame_18)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setFont(font8)

        self.verticalLayout_15.addWidget(self.lineEdit_27, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_14.addWidget(self.frame_18, 0, 0, 1, 1)

        self.horizontalSpacer_104 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_104, 0, 1, 1, 1)

        self.label_54 = QLabel(self.frame_16)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font9)

        self.gridLayout_14.addWidget(self.label_54, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_109 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_109, 0, 3, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_16)

        self.frame_tabla_productos_2 = QFrame(self.frame_15)
        self.frame_tabla_productos_2.setObjectName(u"frame_tabla_productos_2")
        self.frame_tabla_productos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabla_productos_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_tabla_productos_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_61 = QFrame(self.frame_tabla_productos_2)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_166 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_166)

        self.label_125 = QLabel(self.frame_61)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font6)

        self.horizontalLayout_19.addWidget(self.label_125, 0, Qt.AlignmentFlag.AlignRight)

        self.label_124 = QLabel(self.frame_61)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font5)

        self.horizontalLayout_19.addWidget(self.label_124, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_61)

        self.tableWidget_2 = QTableWidget(self.frame_tabla_productos_2)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font10);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font10);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font10);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font10);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setShowGrid(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.tableWidget_2)


        self.verticalLayout_14.addWidget(self.frame_tabla_productos_2)


        self.horizontalLayout_6.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page_6)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.verticalLayout_18 = QVBoxLayout(self.page_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_78)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_79)

        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_81)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_82)

        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontalSpacer_80)

        self.frame_20 = QFrame(self.page_8)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(800, 250))
        self.frame_20.setAutoFillBackground(True)
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_20)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineEdit_21 = QLineEdit(self.frame_20)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(300, 0))
        self.lineEdit_21.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_21.setFont(font11)

        self.gridLayout_12.addWidget(self.lineEdit_21, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_98, 2, 1, 1, 1)

        self.pushButton_36 = QPushButton(self.frame_20)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(130, 0))
        self.pushButton_36.setMaximumSize(QSize(150, 16777215))
        self.pushButton_36.setFont(font7)

        self.gridLayout_12.addWidget(self.pushButton_36, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_101 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_101, 3, 2, 1, 1)

        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_97, 6, 1, 1, 1)

        self.label_39 = QLabel(self.frame_20)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)

        self.gridLayout_12.addWidget(self.label_39, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_100 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_100, 3, 0, 1, 1)

        self.horizontalSpacer_96 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_96, 0, 1, 1, 1)

        self.label_81 = QLabel(self.frame_20)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font12)

        self.gridLayout_12.addWidget(self.label_81, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_20, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_25)

        self.stackedWidget.addWidget(self.page_8)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_23 = QVBoxLayout(self.page_11)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_21 = QFrame(self.page_11)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_21)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_24 = QFrame(self.frame_21)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(16777215, 100))
        self.frame_24.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_24)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_103 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_103, 0, 3, 1, 1)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_26)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_46 = QLabel(self.frame_26)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font7)

        self.verticalLayout_21.addWidget(self.label_46, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.lineEdit_19 = QLineEdit(self.frame_26)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setFont(font8)

        self.verticalLayout_21.addWidget(self.lineEdit_19, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_15.addWidget(self.frame_26, 0, 0, 1, 1)

        self.label_43 = QLabel(self.frame_24)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font9)

        self.gridLayout_15.addWidget(self.label_43, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalSpacer_102 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_102, 0, 1, 1, 1)


        self.verticalLayout_20.addWidget(self.frame_24)

        self.frame_tabla_productos_3 = QFrame(self.frame_21)
        self.frame_tabla_productos_3.setObjectName(u"frame_tabla_productos_3")
        self.frame_tabla_productos_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabla_productos_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_tabla_productos_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_62 = QFrame(self.frame_tabla_productos_3)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_167 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_167)

        self.label_126 = QLabel(self.frame_62)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font6)

        self.horizontalLayout_20.addWidget(self.label_126, 0, Qt.AlignmentFlag.AlignRight)

        self.label_127 = QLabel(self.frame_62)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font5)

        self.horizontalLayout_20.addWidget(self.label_127, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_22.addWidget(self.frame_62)

        self.tableWidget_3 = QTableWidget(self.frame_tabla_productos_3)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font10);
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font10);
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        if (self.tableWidget_3.rowCount() < 1):
            self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setShowGrid(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(680)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_22.addWidget(self.tableWidget_3)


        self.verticalLayout_20.addWidget(self.frame_tabla_productos_3)


        self.verticalLayout_23.addWidget(self.frame_21)

        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.verticalLayout_24 = QVBoxLayout(self.page_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalSpacer_124 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.horizontalSpacer_124)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.horizontalSpacer_125)

        self.horizontalSpacer_127 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.horizontalSpacer_127)

        self.horizontalSpacer_128 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.horizontalSpacer_128)

        self.horizontalSpacer_126 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_24.addItem(self.horizontalSpacer_126)

        self.frame_25 = QFrame(self.page_12)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(800, 386))
        self.frame_25.setAutoFillBackground(True)
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_25)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.checkBox_2 = QCheckBox(self.frame_25)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font3)

        self.gridLayout_16.addWidget(self.checkBox_2, 5, 1, 1, 1)

        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_121, 8, 1, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame_25)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font3)

        self.gridLayout_16.addWidget(self.checkBox_3, 3, 1, 1, 1)

        self.horizontalSpacer_123 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_123, 4, 2, 1, 1)

        self.horizontalSpacer_122 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_122, 4, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.frame_25)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setMinimumSize(QSize(130, 0))
        self.pushButton_30.setMaximumSize(QSize(150, 16777215))
        self.pushButton_30.setFont(font7)

        self.gridLayout_16.addWidget(self.pushButton_30, 10, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_83 = QLabel(self.frame_25)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font14)

        self.gridLayout_16.addWidget(self.label_83, 9, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_118 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_118, 0, 1, 1, 1)

        self.pushButton_29 = QPushButton(self.frame_25)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(100, 0))
        self.pushButton_29.setMaximumSize(QSize(90, 16777215))
        self.pushButton_29.setFont(font6)

        self.gridLayout_16.addWidget(self.pushButton_29, 11, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox_4 = QCheckBox(self.frame_25)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font3)

        self.gridLayout_16.addWidget(self.checkBox_4, 7, 1, 1, 1)

        self.horizontalSpacer_120 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_120, 2, 1, 1, 1)

        self.label_44 = QLabel(self.frame_25)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font5)

        self.gridLayout_16.addWidget(self.label_44, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.checkBox = QCheckBox(self.frame_25)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font3)

        self.gridLayout_16.addWidget(self.checkBox, 4, 1, 1, 1)

        self.horizontalSpacer_119 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_119, 12, 1, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_25)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font3)

        self.gridLayout_16.addWidget(self.checkBox_5, 6, 1, 1, 1)


        self.verticalLayout_24.addWidget(self.frame_25, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_26)

        self.stackedWidget.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_19 = QVBoxLayout(self.page_13)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_22 = QFrame(self.page_13)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_22)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 168))
        self.frame_23.setMaximumSize(QSize(16777215, 330))
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_23)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_30 = QFrame(self.frame_23)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_48 = QLabel(self.frame_30)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(170, 16777215))
        self.label_48.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_48, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_43 = QFrame(self.frame_30)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(40, 0))
        self.frame_43.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_8.addWidget(self.frame_43)

        self.label_47 = QLabel(self.frame_30)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_47, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_84)


        self.verticalLayout_27.addWidget(self.frame_30)

        self.tableWidget_7 = QTableWidget(self.frame_23)
        if (self.tableWidget_7.columnCount() < 7):
            self.tableWidget_7.setColumnCount(7)
        font15 = QFont()
        font15.setPointSize(12)
        font15.setBold(True)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font15);
        self.tableWidget_7.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        if (self.tableWidget_7.rowCount() < 1):
            self.tableWidget_7.setRowCount(1)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setShowGrid(False)
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(201)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tableWidget_7)


        self.gridLayout_9.addWidget(self.frame_23, 3, 0, 1, 1)

        self.frame_32 = QFrame(self.frame_22)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 100))
        self.frame_32.setMaximumSize(QSize(16777215, 100))
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_32)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_27, 1, 8, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_29, 1, 6, 1, 1)

        self.label_62 = QLabel(self.frame_32)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font5)

        self.gridLayout_17.addWidget(self.label_62, 1, 4, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.comboBox_10 = QComboBox(self.frame_32)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMaximumSize(QSize(100, 16777215))
        self.comboBox_10.setFont(font6)

        self.gridLayout_17.addWidget(self.comboBox_10, 1, 1, 1, 1)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_17.addItem(self.verticalSpacer_28, 1, 7, 1, 1)

        self.label_61 = QLabel(self.frame_32)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font5)

        self.gridLayout_17.addWidget(self.label_61, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.comboBox_9 = QComboBox(self.frame_32)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setMaximumSize(QSize(100, 16777215))
        self.comboBox_9.setFont(font6)

        self.gridLayout_17.addWidget(self.comboBox_9, 1, 3, 1, 1)

        self.label_60 = QLabel(self.frame_32)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font5)

        self.gridLayout_17.addWidget(self.label_60, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.comboBox_8 = QComboBox(self.frame_32)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setMaximumSize(QSize(100, 16777215))
        self.comboBox_8.setFont(font6)

        self.gridLayout_17.addWidget(self.comboBox_8, 1, 5, 1, 1)

        self.label_59 = QLabel(self.frame_32)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font5)

        self.gridLayout_17.addWidget(self.label_59, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_32, 1, 0, 1, 1)

        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 400))
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_27)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_31)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_58 = QLabel(self.frame_31)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font5)

        self.gridLayout_10.addWidget(self.label_58, 3, 1, 1, 1)

        self.comboBox_13 = QComboBox(self.frame_31)
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setMinimumSize(QSize(120, 0))
        self.comboBox_13.setFont(font14)

        self.gridLayout_10.addWidget(self.comboBox_13, 1, 1, 1, 1)

        self.horizontalSpacer_132 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_132, 3, 3, 1, 1)

        self.comboBox_12 = QComboBox(self.frame_31)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMinimumSize(QSize(120, 0))
        self.comboBox_12.setFont(font14)

        self.gridLayout_10.addWidget(self.comboBox_12, 0, 1, 1, 1)

        self.horizontalSpacer_131 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_131, 2, 3, 1, 1)

        self.pushButton_47 = QPushButton(self.frame_31)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setMinimumSize(QSize(100, 0))
        self.pushButton_47.setFont(font5)

        self.gridLayout_10.addWidget(self.pushButton_47, 0, 4, 1, 1)

        self.label_56 = QLabel(self.frame_31)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(100, 16777215))
        self.label_56.setFont(font5)

        self.gridLayout_10.addWidget(self.label_56, 3, 0, 1, 1)

        self.horizontalSpacer_129 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_129, 0, 3, 1, 1)

        self.label_40 = QLabel(self.frame_31)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font6)

        self.gridLayout_10.addWidget(self.label_40, 1, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_130 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_130, 1, 3, 1, 1)

        self.label_36 = QLabel(self.frame_31)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font6)

        self.gridLayout_10.addWidget(self.label_36, 0, 0, 1, 1)


        self.verticalLayout_26.addWidget(self.frame_31)

        self.tableWidget_6 = QTableWidget(self.frame_27)
        if (self.tableWidget_6.columnCount() < 7):
            self.tableWidget_6.setColumnCount(7)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font15);
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        if (self.tableWidget_6.rowCount() < 1):
            self.tableWidget_6.setRowCount(1)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setShowGrid(False)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(24)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(201)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_26.addWidget(self.tableWidget_6)


        self.gridLayout_9.addWidget(self.frame_27, 2, 0, 1, 1)

        self.frame_28 = QFrame(self.frame_22)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(16777215, 50))
        self.frame_28.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_35, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_9.addWidget(self.frame_28, 0, 0, 1, 1)


        self.verticalLayout_19.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.verticalLayout_28 = QVBoxLayout(self.page_14)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.frame_34 = QFrame(self.page_14)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 150))
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_34)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_44 = QFrame(self.frame_34)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_44)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_48 = QFrame(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_48)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_102 = QLabel(self.frame_48)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font7)

        self.gridLayout_26.addWidget(self.label_102, 0, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.dateEdit = QDateEdit(self.frame_48)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumSize(QSize(100, 16777215))
        self.dateEdit.setFont(font5)

        self.gridLayout_26.addWidget(self.dateEdit, 0, 3, 1, 1)

        self.label_101 = QLabel(self.frame_48)
        self.label_101.setObjectName(u"label_101")
        font16 = QFont()
        font16.setPointSize(14)
        font16.setBold(True)
        font16.setStrikeOut(False)
        self.label_101.setFont(font16)

        self.gridLayout_26.addWidget(self.label_101, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.dateEdit_2 = QDateEdit(self.frame_48)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMaximumSize(QSize(100, 16777215))
        self.dateEdit_2.setFont(font5)

        self.gridLayout_26.addWidget(self.dateEdit_2, 0, 6, 1, 1)

        self.label_103 = QLabel(self.frame_48)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font7)

        self.gridLayout_26.addWidget(self.label_103, 0, 5, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_147 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_147, 0, 1, 1, 1)


        self.verticalLayout_35.addWidget(self.frame_48)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_46)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.pushButton_42 = QPushButton(self.frame_46)
        self.pushButton_42.setObjectName(u"pushButton_42")
        font17 = QFont()
        font17.setPointSize(11)
        font17.setBold(False)
        font17.setUnderline(True)
        font17.setStrikeOut(False)
        self.pushButton_42.setFont(font17)
        self.pushButton_42.setFlat(True)

        self.gridLayout_23.addWidget(self.pushButton_42, 0, 4, 1, 1)

        self.pushButton_44 = QPushButton(self.frame_46)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setFont(font17)
        self.pushButton_44.setFlat(True)

        self.gridLayout_23.addWidget(self.pushButton_44, 0, 2, 1, 1)

        self.pushButton_45 = QPushButton(self.frame_46)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setFont(font17)
        self.pushButton_45.setFlat(True)

        self.gridLayout_23.addWidget(self.pushButton_45, 0, 1, 1, 1)

        self.pushButton_43 = QPushButton(self.frame_46)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setFont(font17)
        self.pushButton_43.setFlat(True)

        self.gridLayout_23.addWidget(self.pushButton_43, 0, 3, 1, 1)

        self.pushButton_46 = QPushButton(self.frame_46)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setFont(font17)
        self.pushButton_46.setFlat(True)

        self.gridLayout_23.addWidget(self.pushButton_46, 0, 0, 1, 1)


        self.verticalLayout_35.addWidget(self.frame_46)


        self.verticalLayout_25.addWidget(self.frame_44)


        self.verticalLayout_28.addWidget(self.frame_34)

        self.frame_33 = QFrame(self.page_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_33)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_50 = QFrame(self.frame_33)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_50)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.frame_51 = QFrame(self.frame_50)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(16777215, 150))
        self.frame_51.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_51)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.label_105 = QLabel(self.frame_51)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font2)

        self.gridLayout_28.addWidget(self.label_105, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_106 = QLabel(self.frame_51)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font2)

        self.gridLayout_28.addWidget(self.label_106, 2, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_104 = QLabel(self.frame_51)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font16)

        self.gridLayout_28.addWidget(self.label_104, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_108 = QLabel(self.frame_51)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setFont(font11)

        self.gridLayout_28.addWidget(self.label_108, 0, 1, 1, 1)

        self.label_110 = QLabel(self.frame_51)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font3)

        self.gridLayout_28.addWidget(self.label_110, 2, 1, 1, 1)

        self.horizontalSpacer_160 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_160, 2, 2, 1, 1)

        self.horizontalSpacer_161 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_161, 3, 2, 1, 1)

        self.horizontalSpacer_159 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_159, 1, 2, 1, 1)

        self.horizontalSpacer_158 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_158, 0, 2, 1, 1)

        self.label_107 = QLabel(self.frame_51)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font2)

        self.gridLayout_28.addWidget(self.label_107, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_109 = QLabel(self.frame_51)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font3)

        self.gridLayout_28.addWidget(self.label_109, 1, 1, 1, 1)

        self.label_111 = QLabel(self.frame_51)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font3)

        self.gridLayout_28.addWidget(self.label_111, 3, 1, 1, 1)


        self.gridLayout_27.addWidget(self.frame_51, 0, 0, 1, 1)

        self.widget = QWidget(self.frame_50)
        self.widget.setObjectName(u"widget")

        self.gridLayout_27.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.frame_50)
        self.widget_2.setObjectName(u"widget_2")

        self.gridLayout_27.addWidget(self.widget_2, 2, 0, 1, 1)


        self.verticalLayout_36.addWidget(self.frame_50)


        self.verticalLayout_28.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.verticalLayout_32 = QVBoxLayout(self.page_15)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_35 = QFrame(self.page_15)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_35)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMaximumSize(QSize(16777215, 100))
        self.frame_36.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_36)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer_133 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_133, 0, 3, 1, 1)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_83, 0, 1, 1, 1)

        self.label_64 = QLabel(self.frame_36)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font9)

        self.gridLayout_18.addWidget(self.label_64, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.frame_38 = QFrame(self.frame_36)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_38)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_67 = QLabel(self.frame_38)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font7)

        self.verticalLayout_30.addWidget(self.label_67, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.lineEdit_18 = QLineEdit(self.frame_38)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setFont(font8)

        self.verticalLayout_30.addWidget(self.lineEdit_18, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.gridLayout_18.addWidget(self.frame_38, 0, 0, 1, 1)


        self.verticalLayout_29.addWidget(self.frame_36)

        self.frame_60 = QFrame(self.frame_35)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_165 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_165)

        self.label_122 = QLabel(self.frame_60)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font6)

        self.horizontalLayout_18.addWidget(self.label_122, 0, Qt.AlignmentFlag.AlignRight)

        self.label_123 = QLabel(self.frame_60)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font5)

        self.horizontalLayout_18.addWidget(self.label_123, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_29.addWidget(self.frame_60)

        self.frame_tabla_productos_4 = QFrame(self.frame_35)
        self.frame_tabla_productos_4.setObjectName(u"frame_tabla_productos_4")
        self.frame_tabla_productos_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_tabla_productos_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_tabla_productos_4)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.tableWidget_4 = QTableWidget(self.frame_tabla_productos_4)
        if (self.tableWidget_4.columnCount() < 8):
            self.tableWidget_4.setColumnCount(8)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font10);
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem35)
        if (self.tableWidget_4.rowCount() < 1):
            self.tableWidget_4.setRowCount(1)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setShowGrid(False)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget_4.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_31.addWidget(self.tableWidget_4)


        self.verticalLayout_29.addWidget(self.frame_tabla_productos_4)


        self.verticalLayout_32.addWidget(self.frame_35)

        self.stackedWidget.addWidget(self.page_15)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_20 = QGridLayout(self.page)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_53, 1, 0, 1, 1)

        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_34, 6, 0, 1, 1)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_70, 4, 0, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_52, 0, 0, 1, 1)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_61, 3, 0, 1, 1)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_60, 2, 0, 1, 1)

        self.frame_29 = QFrame(self.page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMaximumSize(QSize(16777215, 250))
        self.frame_29.setAutoFillBackground(True)
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_29)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_30, 4, 7, 1, 1)

        self.pushButton_39 = QPushButton(self.frame_29)
        self.pushButton_39.setObjectName(u"pushButton_39")
        icon7 = QIcon()
        icon7.addFile(u"../resources/eye_visible_hide_hidden_show_icon_145988.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_39.setIcon(icon7)

        self.gridLayout_19.addWidget(self.pushButton_39, 4, 5, 1, 1)

        self.lineEdit_23 = QLineEdit(self.frame_29)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_23.sizePolicy().hasHeightForWidth())
        self.lineEdit_23.setSizePolicy(sizePolicy1)
        self.lineEdit_23.setMinimumSize(QSize(250, 0))
        self.lineEdit_23.setMaximumSize(QSize(100, 16777215))
        self.lineEdit_23.setFont(font3)
        self.lineEdit_23.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout_19.addWidget(self.lineEdit_23, 4, 2, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_29, 4, 0, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_36, 0, 2, 1, 1)

        self.label_87 = QLabel(self.frame_29)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font5)

        self.gridLayout_19.addWidget(self.label_87, 1, 4, 1, 1)

        self.label_89 = QLabel(self.frame_29)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font7)

        self.gridLayout_19.addWidget(self.label_89, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_24 = QLineEdit(self.frame_29)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        sizePolicy1.setHeightForWidth(self.lineEdit_24.sizePolicy().hasHeightForWidth())
        self.lineEdit_24.setSizePolicy(sizePolicy1)
        self.lineEdit_24.setMinimumSize(QSize(250, 0))
        self.lineEdit_24.setMaximumSize(QSize(100, 100))
        self.lineEdit_24.setFont(font3)

        self.gridLayout_19.addWidget(self.lineEdit_24, 4, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_85 = QLabel(self.frame_29)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font7)

        self.gridLayout_19.addWidget(self.label_85, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_88 = QLabel(self.frame_29)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font7)

        self.gridLayout_19.addWidget(self.label_88, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_31 = QPushButton(self.frame_29)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(150, 0))
        self.pushButton_31.setMaximumSize(QSize(100, 16777215))
        self.pushButton_31.setFont(font3)

        self.gridLayout_19.addWidget(self.pushButton_31, 6, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_45 = QLabel(self.frame_29)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font5)

        self.gridLayout_19.addWidget(self.label_45, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_42 = QLabel(self.frame_29)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font7)

        self.gridLayout_19.addWidget(self.label_42, 3, 6, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_32 = QPushButton(self.frame_29)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setMinimumSize(QSize(150, 0))
        self.pushButton_32.setMaximumSize(QSize(100, 16777215))
        self.pushButton_32.setFont(font3)

        self.gridLayout_19.addWidget(self.pushButton_32, 6, 4, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.label_55 = QLabel(self.frame_29)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font7)

        self.gridLayout_19.addWidget(self.label_55, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_90 = QLabel(self.frame_29)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font14)

        self.gridLayout_19.addWidget(self.label_90, 5, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.lineEdit = QLineEdit(self.frame_29)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 0))
        self.lineEdit.setMaximumSize(QSize(300, 16777215))
        self.lineEdit.setFont(font3)

        self.gridLayout_19.addWidget(self.lineEdit, 4, 6, 1, 1)

        self.comboBox_14 = QComboBox(self.frame_29)
        self.comboBox_14.setObjectName(u"comboBox_14")
        sizePolicy1.setHeightForWidth(self.comboBox_14.sizePolicy().hasHeightForWidth())
        self.comboBox_14.setSizePolicy(sizePolicy1)
        self.comboBox_14.setMinimumSize(QSize(100, 0))
        self.comboBox_14.setMaximumSize(QSize(300, 16777215))
        self.comboBox_14.setFont(font3)

        self.gridLayout_19.addWidget(self.comboBox_14, 4, 1, 1, 1)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_47, 2, 2, 1, 1)

        self.horizontalSpacer_143 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_143, 0, 4, 1, 1)

        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_144, 2, 4, 1, 1)

        self.label_96 = QLabel(self.frame_29)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font14)

        self.gridLayout_19.addWidget(self.label_96, 5, 4, 1, 1)


        self.gridLayout_20.addWidget(self.frame_29, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.gridLayout_22 = QGridLayout(self.page_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_141 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_141, 4, 0, 1, 1)

        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_140, 2, 0, 1, 1)

        self.frame_45 = QFrame(self.page_16)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMaximumSize(QSize(16777215, 250))
        self.frame_45.setAutoFillBackground(True)
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_45)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_86 = QLabel(self.frame_45)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font7)

        self.gridLayout_21.addWidget(self.label_86, 3, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_84 = QLabel(self.frame_45)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font7)

        self.gridLayout_21.addWidget(self.label_84, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_92 = QLabel(self.frame_45)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font7)

        self.gridLayout_21.addWidget(self.label_92, 3, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.label_91 = QLabel(self.frame_45)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font7)

        self.gridLayout_21.addWidget(self.label_91, 3, 3, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_145, 2, 4, 1, 1)

        self.label_98 = QLabel(self.frame_45)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_21.addWidget(self.label_98, 5, 4, 1, 1)

        self.label_49 = QLabel(self.frame_45)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font5)

        self.gridLayout_21.addWidget(self.label_49, 1, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_88, 4, 0, 1, 1)

        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_146, 0, 4, 1, 1)

        self.label_93 = QLabel(self.frame_45)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font14)

        self.gridLayout_21.addWidget(self.label_93, 5, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.pushButton_35 = QPushButton(self.frame_45)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(150, 0))
        self.pushButton_35.setFont(font3)

        self.gridLayout_21.addWidget(self.pushButton_35, 6, 4, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.lineEdit_22 = QLineEdit(self.frame_45)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(100, 0))
        self.lineEdit_22.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_22.setFont(font3)

        self.gridLayout_21.addWidget(self.lineEdit_22, 4, 6, 1, 1)

        self.comboBox_16 = QComboBox(self.frame_45)
        self.comboBox_16.setObjectName(u"comboBox_16")
        sizePolicy3.setHeightForWidth(self.comboBox_16.sizePolicy().hasHeightForWidth())
        self.comboBox_16.setSizePolicy(sizePolicy3)
        self.comboBox_16.setMinimumSize(QSize(250, 0))
        self.comboBox_16.setMaximumSize(QSize(300, 16777215))
        self.comboBox_16.setFont(font3)

        self.gridLayout_21.addWidget(self.comboBox_16, 4, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_137 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_137, 2, 2, 1, 1)

        self.label_99 = QLabel(self.frame_45)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font5)

        self.gridLayout_21.addWidget(self.label_99, 1, 4, 1, 1)

        self.lineEdit_25 = QLineEdit(self.frame_45)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(250, 0))
        self.lineEdit_25.setMaximumSize(QSize(250, 16777215))
        self.lineEdit_25.setFont(font3)

        self.gridLayout_21.addWidget(self.lineEdit_25, 4, 4, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_33 = QPushButton(self.frame_45)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setMinimumSize(QSize(150, 0))
        self.pushButton_33.setFont(font3)

        self.gridLayout_21.addWidget(self.pushButton_33, 6, 2, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.horizontalSpacer_99 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_99, 4, 7, 1, 1)

        self.comboBox_15 = QComboBox(self.frame_45)
        self.comboBox_15.setObjectName(u"comboBox_15")
        sizePolicy1.setHeightForWidth(self.comboBox_15.sizePolicy().hasHeightForWidth())
        self.comboBox_15.setSizePolicy(sizePolicy1)
        self.comboBox_15.setMinimumSize(QSize(100, 0))
        self.comboBox_15.setMaximumSize(QSize(300, 16777215))
        self.comboBox_15.setFont(font3)

        self.gridLayout_21.addWidget(self.comboBox_15, 4, 1, 1, 1)

        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_110, 0, 2, 1, 1)

        self.label_97 = QLabel(self.frame_45)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font7)

        self.gridLayout_21.addWidget(self.label_97, 3, 6, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_41 = QPushButton(self.frame_45)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setIcon(icon7)

        self.gridLayout_21.addWidget(self.pushButton_41, 4, 5, 1, 1)


        self.gridLayout_22.addWidget(self.frame_45, 5, 0, 1, 1)

        self.horizontalSpacer_138 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_138, 0, 0, 1, 1)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_142, 3, 0, 1, 1)

        self.horizontalSpacer_139 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_139, 1, 0, 1, 1)

        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_35, 6, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_16)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.gridLayout_25 = QGridLayout(self.page_17)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.horizontalSpacer_157 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_157, 4, 0, 1, 1)

        self.horizontalSpacer_154 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_154, 1, 0, 1, 1)

        self.frame_47 = QFrame(self.page_17)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(773, 250))
        self.frame_47.setAutoFillBackground(True)
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_47)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.lineEdit_29 = QLineEdit(self.frame_47)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(300, 0))
        self.lineEdit_29.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_29.setFont(font11)

        self.gridLayout_24.addWidget(self.lineEdit_29, 3, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_148 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_148, 2, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.frame_47)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setMinimumSize(QSize(130, 0))
        self.pushButton_40.setMaximumSize(QSize(150, 16777215))
        self.pushButton_40.setFont(font7)

        self.gridLayout_24.addWidget(self.pushButton_40, 5, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_149, 3, 2, 1, 1)

        self.horizontalSpacer_150 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_150, 6, 1, 1, 1)

        self.label_94 = QLabel(self.frame_47)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font5)

        self.gridLayout_24.addWidget(self.label_94, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_151 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_151, 3, 0, 1, 1)

        self.horizontalSpacer_152 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_152, 0, 1, 1, 1)

        self.label_95 = QLabel(self.frame_47)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font12)

        self.gridLayout_24.addWidget(self.label_95, 4, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_25.addWidget(self.frame_47, 5, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_153 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_153, 0, 0, 1, 1)

        self.horizontalSpacer_155 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_155, 2, 0, 1, 1)

        self.horizontalSpacer_156 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_156, 3, 0, 1, 1)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_25.addItem(self.verticalSpacer_36, 7, 0, 1, 1)

        self.label_100 = QLabel(self.page_17)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font11)

        self.gridLayout_25.addWidget(self.label_100, 6, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.gridLayout_29 = QGridLayout(self.page_18)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.frame_49 = QFrame(self.page_18)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(16777215, 112))
        self.frame_49.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_163 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_163)

        self.label_112 = QLabel(self.frame_49)
        self.label_112.setObjectName(u"label_112")
        font18 = QFont()
        font18.setPointSize(30)
        font18.setBold(True)
        font18.setStrikeOut(False)
        self.label_112.setFont(font18)

        self.horizontalLayout_13.addWidget(self.label_112, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_162 = QSpacerItem(330, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_162)

        self.frame_53 = QFrame(self.frame_49)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(400, 16777215))
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_53)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.label_113 = QLabel(self.frame_53)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font3)

        self.gridLayout_30.addWidget(self.label_113, 0, 0, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(200, 0))
        self.frame_54.setMaximumSize(QSize(200, 16777215))
        self.frame_54.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox_18 = QComboBox(self.frame_54)
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setFont(font6)

        self.horizontalLayout_14.addWidget(self.comboBox_18)

        self.dateEdit_3 = QDateEdit(self.frame_54)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(100, 0))
        self.dateEdit_3.setFont(font6)

        self.horizontalLayout_14.addWidget(self.dateEdit_3)


        self.gridLayout_30.addWidget(self.frame_54, 1, 1, 1, 1)

        self.comboBox_17 = QComboBox(self.frame_53)
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMinimumSize(QSize(150, 0))
        self.comboBox_17.setMaximumSize(QSize(200, 16777215))
        self.comboBox_17.setFont(font6)

        self.gridLayout_30.addWidget(self.comboBox_17, 0, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.frame_53)


        self.gridLayout_29.addWidget(self.frame_49, 0, 0, 1, 1)

        self.frame_52 = QFrame(self.page_18)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_52)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tableWidget_5 = QTableWidget(self.frame_52)
        if (self.tableWidget_5.columnCount() < 6):
            self.tableWidget_5.setColumnCount(6)
        font19 = QFont()
        font19.setPointSize(14)
        font19.setBold(True)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font19);
        self.tableWidget_5.setHorizontalHeaderItem(5, __qtablewidgetitem41)
        if (self.tableWidget_5.rowCount() < 1):
            self.tableWidget_5.setRowCount(1)
        font20 = QFont()
        font20.setPointSize(11)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem42.setFont(font20);
        self.tableWidget_5.setItem(0, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 4, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_5.setItem(0, 5, __qtablewidgetitem46)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget_5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tableWidget_5.setAlternatingRowColors(False)
        self.tableWidget_5.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tableWidget_5.setGridStyle(Qt.PenStyle.NoPen)
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(260)
        self.tableWidget_5.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_38.addWidget(self.tableWidget_5)


        self.gridLayout_29.addWidget(self.frame_52, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_18)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.comboBox_15, self.comboBox_16)
        QWidget.setTabOrder(self.comboBox_16, self.lineEdit_25)
        QWidget.setTabOrder(self.lineEdit_25, self.pushButton_41)
        QWidget.setTabOrder(self.pushButton_41, self.lineEdit_22)
        QWidget.setTabOrder(self.lineEdit_22, self.pushButton_33)
        QWidget.setTabOrder(self.pushButton_33, self.pushButton_35)
        QWidget.setTabOrder(self.pushButton_35, self.comboBox_14)
        QWidget.setTabOrder(self.comboBox_14, self.lineEdit_23)
        QWidget.setTabOrder(self.lineEdit_23, self.lineEdit_24)
        QWidget.setTabOrder(self.lineEdit_24, self.pushButton_39)
        QWidget.setTabOrder(self.pushButton_39, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton_31)
        QWidget.setTabOrder(self.pushButton_31, self.pushButton_32)
        QWidget.setTabOrder(self.pushButton_32, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.lineEdit_9)
        QWidget.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        QWidget.setTabOrder(self.lineEdit_13, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.comboBox_7)
        QWidget.setTabOrder(self.comboBox_7, self.pushButton_23)
        QWidget.setTabOrder(self.pushButton_23, self.pushButton_24)
        QWidget.setTabOrder(self.pushButton_24, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.lineEdit_6)
        QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_5)
        QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.pushButton_19)
        QWidget.setTabOrder(self.pushButton_19, self.pushButton_20)
        QWidget.setTabOrder(self.pushButton_20, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.lineEdit_15)
        QWidget.setTabOrder(self.lineEdit_15, self.lineEdit_17)
        QWidget.setTabOrder(self.lineEdit_17, self.pushButton_26)
        QWidget.setTabOrder(self.pushButton_26, self.pushButton_25)
        QWidget.setTabOrder(self.pushButton_25, self.lineEdit_20)
        QWidget.setTabOrder(self.lineEdit_20, self.pushButton_34)
        QWidget.setTabOrder(self.pushButton_34, self.comboBox_11)
        QWidget.setTabOrder(self.comboBox_11, self.lineEdit_28)
        QWidget.setTabOrder(self.lineEdit_28, self.lineEdit_26)
        QWidget.setTabOrder(self.lineEdit_26, self.pushButton_37)
        QWidget.setTabOrder(self.pushButton_37, self.pushButton_38)
        QWidget.setTabOrder(self.pushButton_38, self.lineEdit_27)
        QWidget.setTabOrder(self.lineEdit_27, self.tableWidget_2)
        QWidget.setTabOrder(self.tableWidget_2, self.lineEdit_21)
        QWidget.setTabOrder(self.lineEdit_21, self.pushButton_36)
        QWidget.setTabOrder(self.pushButton_36, self.lineEdit_19)
        QWidget.setTabOrder(self.lineEdit_19, self.tableWidget_3)
        QWidget.setTabOrder(self.tableWidget_3, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton_30)
        QWidget.setTabOrder(self.pushButton_30, self.pushButton_29)
        QWidget.setTabOrder(self.pushButton_29, self.comboBox_10)
        QWidget.setTabOrder(self.comboBox_10, self.comboBox_9)
        QWidget.setTabOrder(self.comboBox_9, self.comboBox_8)
        QWidget.setTabOrder(self.comboBox_8, self.pushButton_12)
        QWidget.setTabOrder(self.pushButton_12, self.lineEdit_18)
        QWidget.setTabOrder(self.lineEdit_18, self.tableWidget_4)
        QWidget.setTabOrder(self.tableWidget_4, self.lineEdit1)
        QWidget.setTabOrder(self.lineEdit1, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit_16)
        QWidget.setTabOrder(self.lineEdit_16, self.pushButton_27)
        QWidget.setTabOrder(self.pushButton_27, self.pushButton_28)
        QWidget.setTabOrder(self.pushButton_28, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_21)
        QWidget.setTabOrder(self.pushButton_21, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.pushButton_18)
        QWidget.setTabOrder(self.pushButton_18, self.pushButton_22)
        QWidget.setTabOrder(self.pushButton_22, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.comboBox_13)
        QWidget.setTabOrder(self.comboBox_13, self.comboBox_12)
        QWidget.setTabOrder(self.comboBox_12, self.pushButton_15)
        QWidget.setTabOrder(self.pushButton_15, self.pushButton_10)
        QWidget.setTabOrder(self.pushButton_10, self.pushButton_11)
        QWidget.setTabOrder(self.pushButton_11, self.pushButton_16)
        QWidget.setTabOrder(self.pushButton_16, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.pushButton_13)
        QWidget.setTabOrder(self.pushButton_13, self.pushButton_9)
        QWidget.setTabOrder(self.pushButton_9, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_8)
        QWidget.setTabOrder(self.pushButton_8, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.lineEdit_29)
        QWidget.setTabOrder(self.lineEdit_29, self.pushButton_40)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_3.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contenido de Datos", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Agregar Producto", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Editar Producto", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u" Borrar Producto", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Visualizar Productos", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u" Agregar Proveedor", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" Editar Proveedor", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u" Borrar Proveedor", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Visualizar Proveedores", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u" Agregar Categor\u00eda", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u" Borrar Categor\u00eda", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Visualizar Categor\u00edas", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Agregar Usuario", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Editar Usuario", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Borrar Usuario", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u" Borrar Datos", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Usuario :", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"rls", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contenido Buscar Datos", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u" Arqueo", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Estadisticas", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Movimientos", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contenido de Administracion", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u" Facturero", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u" Compras", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Anotador", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Usuario :", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"rls", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"04/07/25", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"22:22PM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nombre :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Seleccione categor\u00eda o proveedor :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Buscador:", None))
        self.lineEdit1.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Precio de Compra", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio de Venta", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Stock Ideal", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Ingrese Nombre de la Categor\u00eda :", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"rls", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID o Nombre del Prducto :", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Borrar Producto", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Precio de Compra", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"ID del Producto", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre del Producto", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Producto :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Precio de Venta", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stock IDEAL", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Aumentar por", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Precio Compra", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Precio Venta", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Aumentar Precios por Categor\u00eda o Proveedor", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"Aumentar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Stock IDEAL", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ingrese los Datos", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ID del Producto", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Precio de Venta", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"del Producto :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Precio de Compra", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Nombre del Producto", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Ingrese los Datos del Proveedor :", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Telefono", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Mail(opcional)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Nombre del Proveedor", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"Borrar Proveedor", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Nombre del Proveedor :", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"laberl de advertencia", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Telefono", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Editar Proveedor :", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Mail(opcional)", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Nombre del Proveedor", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Buscador:", None))
        self.lineEdit_27.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Mail", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Productos", None));
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Borrar Categor\u00eda", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Nombre de la Categor\u00eda :", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Buscador:", None))
        self.lineEdit_19.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Categor\u00edas", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Productos", None));
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Categor\u00edas (excepto \"sin categor\u00eda\")", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Proveedores (ligado a sus productos)", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Borrar Datos", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Usuarios (ligado a sus ventas y compras)", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u00bfQu\u00e9 datos desea borrar?", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Ventas, compras y sus detalles", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Movimientos", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Compras Total :", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        ___qtablewidgetitem14 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem15 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem16 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem17 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo de Pago", None));
        ___qtablewidgetitem18 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem19 = self.tableWidget_7.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem20 = self.tableWidget_7.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Precio Unitario", None));
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Mes", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"D\u00eda", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Seleccione una fecha :", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Corte", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Ventas Total :", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Ventas y compras solo por :", None))
        ___qtablewidgetitem21 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem22 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem23 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem24 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"M\u00e9todo de Pago", None));
        ___qtablewidgetitem25 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem26 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem27 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Precio Unitario", None));
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Arqueo/Mes/A\u00f1o", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Desde ", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Ventas del A\u00f1o 2025", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Hasta ", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Periodo", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"Mes Actual", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Mes Anterior", None))
        self.pushButton_43.setText(QCoreApplication.translate("MainWindow", u"A\u00f1o Actual", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Semana Actual ", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Ventas  ", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Venta Promedio  ", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Ventas Totales  ", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Ganancia  ", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"$0.00", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Productos", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Buscador:", None))
        self.lineEdit_18.setText("")
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"0", None))
        ___qtablewidgetitem28 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem29 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem30 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Precio de Compra", None));
        ___qtablewidgetitem31 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Precio de Venta", None));
        ___qtablewidgetitem32 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem33 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Stock Ideal", None));
        ___qtablewidgetitem34 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda", None));
        ___qtablewidgetitem35 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        self.pushButton_39.setText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Datos del Usuario :", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Nombre del Usuario", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_88.setText("")
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Ingrese los", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Tipo de Usuario", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Label", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Tipo de Usuario", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Nombre del Usuario", None))
        self.label_91.setText("")
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"label error", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Usuario :", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.pushButton_41.setText("")
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"Borrar Usuario", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Nombre del Usuario :", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Movimientos", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Ver por ", None))
        ___qtablewidgetitem36 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtablewidgetitem37 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem38 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem39 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Accion", None));
        ___qtablewidgetitem40 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Entidad Afectada", None));
        ___qtablewidgetitem41 = self.tableWidget_5.horizontalHeaderItem(5)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));

        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)

    # retranslateUi


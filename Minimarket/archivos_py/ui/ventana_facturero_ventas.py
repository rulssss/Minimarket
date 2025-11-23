# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_facturero_ventas.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form_ventas(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 700)
        Form.setMinimumSize(QSize(600, 700))
        Form.setMaximumSize(QSize(600, 700))
        Form.setStyleSheet(u"QWidget {\n"
"    background-color: #ffffff; /* Fondo blanco */\n"
"}\n"
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
"QTableWidget {\n"
"    background-color: #f3f3f3;    /* Gris claro */\n"
"}\n"
"QLineEdit {\n"
"    background-color: #f3f3f3;    /* Gris claro */\n"
"}\n"
"QComboBox {\n"
"    background-color: #f3f3f3;    /* Gris claro */\n"
"}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)

        self.verticalLayout_3.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_2 = QComboBox(self.frame_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(200, 0))
        self.comboBox_2.setMaximumSize(QSize(200, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.comboBox_2.setFont(font1)

        self.gridLayout_3.addWidget(self.comboBox_2, 6, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(120, 30))
        self.pushButton_2.setMaximumSize(QSize(120, 30))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton_2.setFont(font2)

        self.gridLayout_3.addWidget(self.pushButton_2, 8, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 6, 5, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_3.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_3.addWidget(self.label_9, 7, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(200, 0))
        self.lineEdit_4.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_4.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_4, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 0))
        self.lineEdit_2.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_2.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 25))
        self.pushButton.setMaximumSize(QSize(16777215, 25))
        self.pushButton.setFont(font1)

        self.gridLayout_3.addWidget(self.pushButton, 8, 0, 1, 1, Qt.AlignmentFlag.AlignBottom)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMaximumSize(QSize(20, 16777215))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.pushButton_5.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(20, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_6)


        self.gridLayout_3.addWidget(self.frame_5, 6, 4, 1, 1)

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 0))
        self.comboBox.setMaximumSize(QSize(200, 16777215))
        self.comboBox.setFont(font1)

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(200, 16777215))
        self.lineEdit.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        self.lineEdit_3.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_3.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_3, 5, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(200, 0))
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_5.setFont(font1)

        self.gridLayout_3.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.tableWidget.setFont(font6)
        self.tableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(74)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font2)

        self.horizontalLayout.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_10)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 50))
        self.pushButton_3.setMaximumSize(QSize(150, 16777215))
        self.pushButton_3.setFont(font5)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.horizontalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.horizontalLayout.addWidget(self.label_12)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Facturero Ventas", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Agregar", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Proveedor", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre del Producto", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"M\u00e9todo de Pago", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"label error", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Categor\u00eda", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Borrar \u00daltimo Agregado", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"-", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Precio de Venta", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Cantidad", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Productos seleccionados ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Producto", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Precio V.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Categor\u00eda", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Proveedor", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"M.P.", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Total ", None));
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Cerrar", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Procesar", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Total :", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"$0.00", None))
    # retranslateUi


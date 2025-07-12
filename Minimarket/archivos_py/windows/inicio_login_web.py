from PySide6.QtWidgets import QWidget, QLineEdit
from archivos_py.ui.login import Ui_Form_login  # Importa la clase generada por qt Designer
from PySide6.QtGui import QIcon
from archivos_py.threads.db_threads_login_web import Login_web_Thread  # Ajusta la ruta según tu estructura


class InicioWeb(QWidget):
    def __init__(self):
        super(InicioWeb, self).__init__()
        self.ui = Ui_Form_login()
        self.ui.setupUi(self)

        # Inicializa los atributos necesarios para almacenar threads
        self.threads = []

        # Atributo para rastrear si el botón ya está conectado
        self.pushButton_connected = False

        # Establece el icono y el título de la ventana principal
        self.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
        self.setWindowTitle("rls")

        self.open_login_web_window()
        

    def open_login_web_window(self):

        self.ui.stackedWidget.setCurrentIndex(0)


        line_edit_11 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_11")
        line_edit_12 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_12")
        push_button_15 = self.ui.stackedWidget.findChild(QWidget, "pushButton_15")
        push_button_16 = self.ui.stackedWidget.findChild(QWidget, "pushButton_16")

        if push_button_15:
            push_button_15.clicked.connect(self.open_verificar_contrasenia)


        if push_button_16:
            push_button_16.clicked.connect(self.open_link_a_recuperar_contrasenia)

    
    def open_verificar_contrasenia(self):

        line_edit_11 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_11")
        line_edit_12 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_12")
        label_32 = self.ui.stackedWidget.findChild(QWidget, "label_32")
        push_button_15 = self.ui.stackedWidget.findChild(QWidget, "pushButton_15")

        if push_button_15:
            push_button_15.setEnabled(False)

        value_line_edit_11 = line_edit_11.text()
        value_line_edit_12 = line_edit_12.text()

        if value_line_edit_11 and value_line_edit_12:
            # Aquí deberías iniciar el thread de verificación de contraseña
            self.login_thread = Login_web_Thread(value_line_edit_11, value_line_edit_12)
            self.login_thread.finished.connect(self.handle_login_finished)
            self.login_thread.start()
        

    def open_link_a_recuperar_contrasenia(self):
        pass

    def handle_login_finished(self, exito):
    
        push_button_15 = self.ui.stackedWidget.findChild(QWidget, "pushButton_15")
        label_32 = self.ui.stackedWidget.findChild(QWidget, "label_32")

        # Reactivar el botón
        if push_button_15:
            push_button_15.setEnabled(True)

        if exito:
            # Login exitoso - abrir ventana del minimarket
            print("exito")
        else:
            if label_32:
                label_32.setText("Usuario o contraseña incorrectos")
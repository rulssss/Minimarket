from PySide6.QtWidgets import QWidget, QLineEdit, QApplication
from archivos_py.ui.login import Ui_Form_login  # Importa la clase generada por qt Designer
from PySide6.QtGui import QIcon
from archivos_py.threads.db_thread_loginWeb_api import Login_web_Thread, Login_web_Thread_verificar_existencia_mail
from archivos_py.windows.inicio_login import Inicio
import sys
import webbrowser  # Agregué este import
from PySide6.QtCore import Qt
from archivos_py.db.sesiones import SessionManager
 


class InicioWeb(QWidget):
    def __init__(self):
        super(InicioWeb, self).__init__()
        self.ui = Ui_Form_login()
        self.ui.setupUi(self)
        self.session_manager = SessionManager()

        # Inicializa los atributos necesarios para almacenar threads
        self.threads = []

        # Atributo para rastrear si el botón ya está conectado
        self.pushButton_connected = False

        # Establece el icono y el título de la ventana principal
        self.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
        self.setWindowTitle("rls")

        self.open_login_web_window()

    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()
        

    def open_login_web_window(self):

        self.ui.stackedWidget.setCurrentIndex(0)


        line_edit_11 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_11")
        line_edit_12 = self.ui.stackedWidget.findChild(QLineEdit, "lineEdit_12")
        push_button_15 = self.ui.stackedWidget.findChild(QWidget, "pushButton_15")
        push_button_16 = self.ui.stackedWidget.findChild(QWidget, "pushButton_16")
        label_32 = self.ui.stackedWidget.findChild(QWidget, "label_32")
        if label_32:
            label_32.setStyleSheet("color: transparent")

        if push_button_15:
            push_button_15.setShortcut(Qt.Key_Return)
            push_button_15.clicked.connect(self.open_verificar_contrasenia)

        if line_edit_11:
            line_edit_11.setPlaceholderText("Email")
            line_edit_11.setClearButtonEnabled(True)

        if line_edit_12:
            line_edit_12.setEchoMode(QLineEdit.Password)
            line_edit_12.setPlaceholderText("Contraseña")

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
            self.login_thread.resultado.connect(self.handle_login_finished)
            self.start_thread(self.login_thread)
        else:
            if label_32:
                label_32.setStyleSheet("color: red; font-weight: bold")
                label_32.setText("Por favor, completa todos los campos")

            push_button_15.setEnabled(True)

    def open_link_a_recuperar_contrasenia(self):
        """Abre el link de recuperación de contraseña en el navegador web"""
        try:
            webbrowser.open("https://rlsweb.vercel.app/dashboard")
            print("Abriendo link de recuperación de contraseña...")
        except Exception as e:
            print(f"Error al abrir el navegador: {e}")

    def handle_login_finished(self, exito, datos_usuario):

        print("Respuesta de la API Flask:", datos_usuario)
        
        push_button_15 = self.ui.stackedWidget.findChild(QWidget, "pushButton_15")
        label_32 = self.ui.stackedWidget.findChild(QWidget, "label_32")

        # Reactivar el botón
        if push_button_15:
            push_button_15.setEnabled(True)

        if exito:
            # Aquí puedes manejar el caso de éxito
            if label_32:
                label_32.setStyleSheet("color: green; font-weight: bold")
                label_32.setText("Login exitoso Ingresando...")

             # Extraer solo uid y subscription de los datos del usuario
            uid = datos_usuario.get('uid', '')
            email = datos_usuario.get('email', '')

            # Guardar la sesión
            self.session_manager.save_session(email, uid)

            #se cierra la aplicacion de login web
            self.close()

            # verificar existencia de mail , si existe pasa y sino guarda el mail y uid
            self.login_thread_verificar = Login_web_Thread_verificar_existencia_mail(email, uid)
            self.start_thread(self.login_thread_verificar)

             # Crear y mostrar la ventana Inicio
            try:

                self.inicio_window = Inicio()
                self.inicio_window.show()
            except Exception as e:
                print(f"Error al abrir ventana Inicio: {e}")

        else:
            

            if datos_usuario == "Usuario sin suscripción Pro":
            
                if label_32:
                    label_32.setStyleSheet("color: red; font-weight: bold")
                    label_32.setText("Usuario sin suscripción 'Pro'\n no puede iniciar sesión")
                
                push_button_15.setEnabled(True)
            else:
                if label_32:
                    label_32.setStyleSheet("color: red; font-weight: bold")
                    label_32.setText("Usuario o contraseña incorrectos")

                push_button_15.setEnabled(True)


    def verificar_estado_subscripcion(self):
        session_manager = SessionManager()
        email = session_manager.get_email()
        uid = session_manager.get_uid()
        # Ahora puedes usar email y uid como necesites
        print("Email:", email)
        print("UID:", uid)



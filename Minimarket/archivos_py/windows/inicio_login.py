from PySide6.QtWidgets import QWidget, QLineEdit
from PySide6.QtGui import QIcon, Qt
from PySide6.QtCore import QTimer, QThread
from archivos_py.ui.login import Ui_Form_login  # Importa la clase generada por qt Designer
from archivos_py.threads.db_threads_login import LoginThread, RegistroCheckThread, EnviarCodigoThread, CodigoOtroAdminThread, RegistrarUsuarioThread, VerificarYEnviarCodigoThread, ActualizarContrasenaThread
from PySide6 import QtGui
from archivos_py.windows.inicio_minimarket import MainWindow
from archivos_py.threads.db_thread_minimarket import MovimientoLoginThread
import os
import sys
import warnings
warnings.filterwarnings("ignore", message=".*Failed to disconnect.*")
from archivos_py.db.sesiones import SessionManager
from archivos_py.threads.db_thread_loginWeb_api import Cambiar_False_open

#se establece el directorio base para los recursos
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(BASE_DIR, "archivos_py", "resources", "r.ico")


class Inicio(QWidget):
    def __init__(self, id_usuario_perfil):
        super(Inicio, self).__init__()
        self.ui = Ui_Form_login()
        self.ui.setupUi(self)  # Configura la interfaz en el widget base (self)
        self.id_usuario_perfil = id_usuario_perfil

        # Inicializa los atributos necesarios para almacenar threads
        self.threads = []

        # Atributo para rastrear si el botón ya está conectado
        self.pushButton_connected = False

        # Establece el icono y el título de la ventana principal
        self.setWindowIcon(QIcon(icon_path))
        self.setWindowTitle("rls")

        self.open_login_window()

    # funcion para abrir la ventana de login
    def open_login_window(self):
        
        self.ui.stackedWidget.setCurrentIndex(2)

        label_9 = self.ui.stackedWidget.findChild(QWidget, "label_9")
        combobox_2 = self.ui.stackedWidget.findChild(QWidget, "comboBox_2")
        line_edit_4 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_4")
        pushButton = self.ui.stackedWidget.findChild(QWidget, "pushButton_2")
        pushButton_3 = self.ui.stackedWidget.findChild(QWidget, "pushButton_3")
        pushButton_4 = self.ui.stackedWidget.findChild(QWidget, "pushButton_4")
        line_edit = self.ui.stackedWidget.findChild(QWidget, "lineEdit_3")

        if combobox_2:
            combobox_2.clear()
            combobox_2.addItem("Administrador")
            combobox_2.addItem("Usuario")

        if line_edit:
            line_edit.setPlaceholderText("Usuario")
            line_edit.setAlignment(Qt.AlignCenter)
            line_edit.setFocus()
    

        if line_edit_4:
            line_edit_4.setEchoMode(QLineEdit.Password)
            line_edit_4.setAlignment(Qt.AlignCenter)
            line_edit_4.setPlaceholderText("Contraseña")


        if pushButton:
            pushButton.setEnabled(True)
            # Conecta el botón solo si no está conectado
            if not self.pushButton_connected:
                pushButton.clicked.connect(self.verificar_login)
                pushButton.setShortcut(Qt.Key_Return)
                self.pushButton_connected = True

        if pushButton_3:
            pushButton_3.setEnabled(True)
            pushButton_3.clicked.connect(self.open_register_window)
            
        if pushButton_4:
            pushButton_4.setEnabled(True)
            pushButton_4.clicked.connect(self.open_recover_window)

        if label_9:
            label_9.setStyleSheet("color: transparent;")

    def verificar_login(self):
        combobox_2 = self.ui.stackedWidget.findChild(QWidget, "comboBox_2")
        line_edit_3 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_3")
        line_edit_4 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_4")
        value_line_edit = line_edit_3.text()
        value_line_edit_2 = line_edit_4.text()
        value_combobox = combobox_2.currentText()  
        label_9 = self.ui.stackedWidget.findChild(QWidget, "label_9")
        pushButton_2 = self.ui.stackedWidget.findChild(QWidget, "pushButton_2")
        push_button_3 = self.ui.stackedWidget.findChild(QWidget, "pushButton_3")
        push_button_4 = self.ui.stackedWidget.findChild(QWidget, "pushButton_4")

        if value_combobox and value_line_edit and value_line_edit_2:

            pushButton_2.setEnabled(False)
            push_button_3.setEnabled(False)
            push_button_4.setEnabled(False)

            # Aquí lanzas el thread en vez de llamar directo a la función lenta
            self.login_thread = LoginThread(self.id_usuario_perfil, value_combobox, value_line_edit, value_line_edit_2)
            self.login_thread.finished.connect(
                lambda exito, mensaje: self.on_login_finished(
                    exito, mensaje, pushButton_2, push_button_3, push_button_4, label_9, value_line_edit, value_combobox
                )
            )
            self.start_thread(self.login_thread)

        else:
            label_9.setText("Complete todos los campos correctamente")
            label_9.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent;"))

    def on_login_finished(self, exito, mensaje, pushButton_2, pushButton_3, pushButton_4, label_9, usuario, account):

        if not exito:
            pushButton_2.setEnabled(True)
            pushButton_3.setEnabled(True)
            pushButton_4.setEnabled(True)

            label_9.setText("Tipo de usuario, usuario o contraseña incorrecto")
            label_9.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent;"))
        else:

            label_9.setText("Ingresando...")
            label_9.setStyleSheet("color: green;")
            QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent;"))
            QTimer.singleShot(6000, lambda: (
                setattr(self, "_cerrando_para_main", True),
                self.open_main_window(self.id_usuario_perfil, usuario, account)
            ))


    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()

    def closeEvent(self, event):
        # Solo poner open en False si NO es para abrir MainWindow
        if not hasattr(self, "_cerrando_para_main") or not self._cerrando_para_main:
            session_manager = SessionManager()
            uid = session_manager.get_uid()

            if uid:
                self.thread_cambiar_false_open = Cambiar_False_open(uid)
                self.start_thread(self.thread_cambiar_false_open)

        # Detener y limpiar otros threads
        for thread in list(self.threads):
            thread.wait()


    def open_main_window(self, id_usuario_perfil, usuario, account):
        print("se inicia el minimarket")
        self._cerrando_para_main = True  # <--- Marca que el cierre es para abrir MainWindow
        self.main_window = MainWindow(id_usuario_perfil, usuario, account)
        self.main_window.resize(1690, 900)
        self.main_window.show()

        # Crear y ejecutar hilo para cargar movimiento del usuario
        self.movimiento_login_thread = MovimientoLoginThread(self.id_usuario_perfil, usuario)
        self.start_thread(self.movimiento_login_thread)
    
        self.close()  # Cierra la ventana de login


    def open_register_window(self):
        
        self.ui.stackedWidget.setCurrentIndex(0)

        label_21 = self.ui.stackedWidget.findChild(QWidget, "label_21")
        combobox = self.ui.stackedWidget.findChild(QWidget, "comboBox")
        line_edit = self.ui.stackedWidget.findChild(QWidget, "lineEdit")
        line_edit_5 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_5")
        line_edit_2 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_2")
        pushButton = self.ui.stackedWidget.findChild(QWidget, "pushButton")
        pushButton_5 = self.ui.stackedWidget.findChild(QWidget, "pushButton_5")


        if combobox:    
            combobox.clear()
            combobox.addItem("Administrador")
            combobox.addItem("Usuario")

        if line_edit:
            line_edit.setAlignment(Qt.AlignCenter)
            line_edit.setPlaceholderText("Usuario")
            line_edit.setFocus()

        if line_edit_2:
            line_edit_2.setAlignment(Qt.AlignCenter)
            line_edit_2.setEchoMode(QLineEdit.Password)
            line_edit_2.setPlaceholderText("Contraseña")

        if line_edit_5:
            line_edit_5.setAlignment(Qt.AlignCenter)
            line_edit_5.setPlaceholderText("Email")


        if pushButton:
            pushButton.setEnabled(True)
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                try:
                    pushButton.clicked.disconnect(self.verificar_registro)
                except (TypeError, RuntimeError):
                    pass
            pushButton.clicked.connect(self.verificar_registro)
            pushButton.setShortcut(Qt.Key_Return)

        if pushButton_5:
            pushButton_5.setEnabled(True)
            pushButton_5.clicked.connect(self.volver_al_login_y_limpiar_campos)

        if label_21:
            label_21.setStyleSheet("color: transparent;")

    def volver_al_login_y_limpiar_campos(self):

        line_edit = self.ui.stackedWidget.findChild(QWidget, "lineEdit")
        line_edit_2 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_2")
        line_edit_5 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_5")

        if line_edit:
            line_edit.clear()

        if line_edit_2:
            line_edit_2.clear()

        if line_edit_5:
            line_edit_5.clear()

        self.open_login_window()

    def verificar_registro(self): 
        push_button_5 = self.ui.stackedWidget.findChild(QWidget, "pushButton_5")
        pushButton = self.ui.stackedWidget.findChild(QWidget, "pushButton")
        combobox = self.ui.stackedWidget.findChild(QWidget, "comboBox")
        line_edit = self.ui.stackedWidget.findChild(QWidget, "lineEdit")
        line_edit_2 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_2")
        line_edit_5 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_5")
        value_combobox = combobox.currentText()
        value_line_edit_3 = line_edit.text().strip()
        value_line_edit_4 = line_edit_2.text().strip()
        value_line_edit_5 = line_edit_5.text().strip()


        label_21 = self.ui.stackedWidget.findChild(QWidget, "label_21")

        if value_line_edit_3 and value_line_edit_4 and value_line_edit_5 and ("@gmail" in value_line_edit_5 or "@hotmail" in value_line_edit_5 or "@outlook" in value_line_edit_5) and value_combobox:
            pushButton.setEnabled(False)
            push_button_5.setEnabled(False)

            self.registro_thread = RegistroCheckThread(self.id_usuario_perfil, value_line_edit_3, value_line_edit_4, value_line_edit_5, value_combobox)
            self.registro_thread.finished.connect(
            lambda result: (

                self.on_registro_check_finished(result, value_combobox, pushButton, push_button_5)
            )
            )
            self.start_thread(self.registro_thread)

        else:
            label_21.setText("Complete todos los campos correctamente")
            label_21.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_21.setStyleSheet("color: transparent;"))

    def on_registro_check_finished(self, result, value_combobox, pushButton, pushButton_5):
        label_21 = self.ui.stackedWidget.findChild(QWidget, "label_21")

        if value_combobox == "Administrador" and result["hay_admin"]:
            if result["usuario_existe"]:
                label_21.setText("Usuario existente")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            elif not result["password_ok"]:
                label_21.setText("La contraseña debe tener al menos 8 caracteres")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            elif result["mail_existe"]:
                label_21.setText("Email existente")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            else:
                
                self.verificar_cuenta_usuario()
                return
        else:
            if result["usuario_existe"]:
                label_21.setText("Usuario existente")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            elif not result["password_ok"]:
                label_21.setText("La contraseña debe tener al menos 8 caracteres")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            elif result["mail_existe"]:
                label_21.setText("Email existente")
                label_21.setStyleSheet("color: red;")
                if pushButton:
                    pushButton.setEnabled(True)
                    pushButton_5.setEnabled(True)
            else:
    
                self.verificar_codigo_para_agregar_otra_cuenta()
                return

        QTimer.singleShot(6000, lambda: label_21.setStyleSheet("color: transparent;"))

    def verificar_cuenta_usuario(self):
        line_edit_5 = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit_5")
        mail = line_edit_5.text()
        pushButton = self.ui.stackedWidget.findChild(QWidget, "pushButton")
        if pushButton:
                pushButton.setEnabled(False)


        self.enviar_codigo_thread = EnviarCodigoThread(mail)
        self.enviar_codigo_thread.finished.connect(self.on_codigo_enviado_admin)
        self.start_thread(self.enviar_codigo_thread)

   
    
    def on_codigo_enviado_admin(self, codigo):
        self.enviar_codigo_thread = None
        global codigo_usuario
        codigo_usuario = codigo
        

        label_21 = self.ui.stackedWidget.findChild(QWidget, "label_21")
        if codigo_usuario is not None:
            self.open_verificar_codigo_cuent_admin()
        else:
            pushButton = self.ui.stackedWidget.findChild(QWidget, "pushButton")
            if pushButton:
                pushButton.setEnabled(True)

            pushButton_5 = self.ui.stackedWidget.findChild(QWidget, "pushButton_5")
            if pushButton_5:
                pushButton_5.setEnabled(True)

            label_21.setAlignment(Qt.AlignCenter)
            label_21.setText("El email no es válido porfavor editelo")
            label_21.setStyleSheet("color: red;")
            QTimer.singleShot(15000, lambda: label_21.setStyleSheet("color: transparent;"))

    def open_verificar_codigo_cuent_admin(self):

        self.ui.stackedWidget.setCurrentIndex(5)

        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        label_15 = self.ui.stackedWidget.findChild(QWidget, "label_15")
        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")

        if label_15:
            label_15.setAlignment(Qt.AlignCenter)
            label_15.setText("Introduzca el código de verificación enviado :")

            label_15.setStyleSheet("color: black; font-size: 16px; font-weight: bold;")

        if label_17:
            label_17.setStyleSheet("color: transparent;")

        if line_edit_8:
            line_edit_8.clear()
            line_edit_8.setValidator(QtGui.QIntValidator())
            line_edit_8.setAlignment(Qt.AlignCenter)
            line_edit_8.setPlaceholderText("Código de verificacion")
            line_edit_8.setStyleSheet("font-weight: bold;")

        if pushButton_11:
            pushButton_11.setEnabled(True)
            pushButton_11.clicked.connect(self.verificar_codigo_para_luego_enviarle_al_admin)
            pushButton_11.setShortcut(Qt.Key_Return)

        if pushButton_12:
            pushButton_12.setEnabled(True)
            pushButton_12.clicked.connect(self.open_register_window)


    def verificar_codigo_para_luego_enviarle_al_admin(self):
        global codigo_usuario

        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")

        if line_edit_8:
            line_edit_8.setFocus()
            value_line_edit_8 = line_edit_8.text().strip()

        if value_line_edit_8:

            if int(codigo_usuario) == int(value_line_edit_8):

                if label_17:
                    if pushButton_11 and pushButton_12:
                        pushButton_11.setEnabled(False)
                        pushButton_12.setEnabled(False)
                        try:
                            pushButton_11.clicked.disconnect()
                        except (TypeError, RuntimeError):
                            pass

                    QTimer.singleShot(0, lambda: QTimer().stop())
                    label_17.setText("Código correcto, ahora se le enviara al admin aguarde...")
                    label_17.setStyleSheet("color: green;")
                    QTimer.singleShot(8000, lambda: (label_17.setStyleSheet("color: transparent;"), self.verificar_codigo_para_agregar_otro_admin()))
                
            else:
                QTimer.singleShot(0, lambda: QTimer().stop())
                label_17 = self.ui.stackedWidget.findChild(QWidget, "label_23")
                label_17.setText("Codigo incorrecto")
                label_17.setStyleSheet("color: red;")
                QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))

                if pushButton_11 and pushButton_12:
                    pushButton_11.setEnabled(True)
                    pushButton_12.setEnabled(True)

                line_edit_8.clear()
        else:
            if pushButton_11 and pushButton_12:
                pushButton_11.setEnabled(True)
                pushButton_12.setEnabled(True)
            QTimer.singleShot(0, lambda: QTimer().stop())
            label_17 = self.ui.stackedWidget.findChild(QWidget, "label_23")
            label_17.setText("Complete el código correctamente")
            label_17.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))

    def verificar_codigo_para_agregar_otro_admin(self):

        self.codigo_otro_admin_thread = CodigoOtroAdminThread(self.id_usuario_perfil)
        self.codigo_otro_admin_thread.finished.connect(self.on_codigo_otro_admin_finished)
        self.start_thread(self.codigo_otro_admin_thread)

    def on_codigo_otro_admin_finished(self, codigo):
        global codigo_admin
        codigo_admin = codigo

        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")
        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")

        if codigo_admin is not None:
            self.open_verificar_codigo_admin()
        else:
            if pushButton_11 and pushButton_12:
                pushButton_11.setEnabled(True)
                pushButton_12.setEnabled(True)

            label_17.setAlignment(Qt.AlignCenter)
            label_17.setText("El email del admin principal no se encuentra\n disponible, edítelo o cámbielo en la sección de Datos")
            label_17.setStyleSheet("color: red;")
            QTimer.singleShot(15000, lambda: label_17.setStyleSheet("color: transparent;"))


    def open_verificar_codigo_admin(self):


        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        label_15 = self.ui.stackedWidget.findChild(QWidget, "label_15")
        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")

        if label_15:
            label_15.setAlignment(Qt.AlignCenter)
            label_15.setText("Introduzca el codigo de verificacion\n enviado al correo del administrador\n principal")
            label_15.setStyleSheet("color: black; font-size: 16px; font-weight: bold;")

        if line_edit_8:
            line_edit_8.clear()
            line_edit_8.setAlignment(Qt.AlignCenter)
            line_edit_8.setPlaceholderText("Código de verificación")
            line_edit_8.setStyleSheet("font-weight: bold;")

        if label_17:
            label_17.setStyleSheet("color: transparent;")

        if pushButton_11:
            pushButton_11.setEnabled(True)
            pushButton_11.clicked.connect(self.verificar_codigo_admin)
            pushButton_11.setShortcut(Qt.Key_Return)


        if pushButton_12:
            pushButton_12.setEnabled(True)
            pushButton_12.clicked.connect(self.open_register_window)

    def verificar_codigo_admin(self):
        global codigo_admin

        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")

        if line_edit_8:
            value_line_edit_8 = line_edit_8.text()
        else:
            value_line_edit_8 = ""

        if value_line_edit_8:
            if int(codigo_admin) == int(value_line_edit_8):
                pushButton_11.setEnabled(False)
                pushButton_12.setEnabled(False)
                combobox = "Administrador"
                line_edit = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit")
                line_edit_2 = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit_2")
                line_edit_5 = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit_5")
                value_line_edit = line_edit.text()
                value_line_edit_2 = line_edit_2.text()
                value_line_edit_5 = line_edit_5.text()

                # Lanzar el thread para registrar usuario
                self.registrar_usuario_thread = RegistrarUsuarioThread(self.id_usuario_perfil,
                    value_line_edit, value_line_edit_2, combobox, value_line_edit_5
                )
                self.registrar_usuario_thread.finished.connect(
                    lambda exito: self.on_registro_admin_finished(
                        exito, line_edit_8, line_edit, line_edit_2, line_edit_5, label_17
                    )
                )
                self.start_thread(self.registrar_usuario_thread)

            else:
                QTimer.singleShot(0, lambda: QTimer().stop())
                label_17.setText("Código incorrecto")
                label_17.setStyleSheet("color: red;")
                QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))
                pushButton_11.setEnabled(True)
                pushButton_12.setEnabled(True)
        else:
            pushButton_11.setEnabled(True)
            pushButton_12.setEnabled(True)
            QTimer.singleShot(0, lambda: QTimer().stop())
            label_17.setText("Complete el código correctamente")
            label_17.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))
            line_edit_8.clear()

    def on_registro_admin_finished(self, exito, line_edit_8, line_edit, line_edit_2, line_edit_5, label_17):
        global codigo_admin

        if exito:
            label_17.setText("Administrador registrado correctamente, aguarde...")
            label_17.setStyleSheet("color: green;")
            QTimer.singleShot(6000, lambda: (label_17.setStyleSheet("color: transparent;"), self.open_login_window()))
        else:
            label_17.setText("Error al registrar administrador")
            label_17.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))

        line_edit_8.clear()
        line_edit.clear()
        line_edit_2.clear()
        line_edit_5.clear()
        codigo_admin = None

    
    def verificar_codigo_para_agregar_otra_cuenta(self):
        line_edit_5 = self.ui.stackedWidget.widget(2).findChild(QWidget, "lineEdit_5")
        mail = line_edit_5.text()

        self.enviar_codigo_cuenta_thread = EnviarCodigoThread(mail)
        self.enviar_codigo_cuenta_thread.finished.connect(self.on_codigo_enviado_cuenta)
        self.start_thread(self.enviar_codigo_cuenta_thread)

    def on_codigo_enviado_cuenta(self, codigo):
        global codigo_usuario
        codigo_usuario = codigo

        label_21 = self.ui.stackedWidget.findChild(QWidget, "label_21")
        if codigo is not None:
            self.open_verificar_codigo_cuenta()
        else:
            QTimer.singleShot(0, lambda: QTimer().stop())
            label_21.setAlignment(Qt.AlignCenter)
            label_21.setText("El email no es válido porfavor edítelo")
            label_21.setStyleSheet("color: red;")
            QTimer.singleShot(15000, lambda: label_21.setStyleSheet("color: transparent;"))


    def open_verificar_codigo_cuenta(self):
        self.ui.stackedWidget.setCurrentIndex(5)

        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        label_15 = self.ui.stackedWidget.findChild(QWidget, "label_15")
        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")

        if label_15:
            label_15.setAlignment(Qt.AlignCenter)
            label_15.setText("Introduzca el código de verificación enviado :")
            label_15.setStyleSheet("color: black; font-size: 16px;")

        if label_17:
            label_17.setStyleSheet("color: transparent;")

        if line_edit_8:
            line_edit_8.setValidator(QtGui.QIntValidator())
            line_edit_8.setAlignment(Qt.AlignCenter)
            line_edit_8.setPlaceholderText("Código de verificacion")
            line_edit_8.setStyleSheet("font-weight: bold;")

        if pushButton_11:
            pushButton_11.setEnabled(True)
            pushButton_11.clicked.connect(self.verificar_codigo_cuenta)
            pushButton_11.setShortcut(Qt.Key_Return)

        if pushButton_12:
            pushButton_12.setEnabled(True)
            pushButton_12.clicked.connect(self.open_register_window)


    def verificar_codigo_cuenta(self):
        global codigo_usuario


        line_edit_8 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_8")
        label_17 = self.ui.stackedWidget.findChild(QWidget, "label_17")
        pushButton_11 = self.ui.stackedWidget.findChild(QWidget, "pushButton_11")
        pushButton_12 = self.ui.stackedWidget.findChild(QWidget, "pushButton_12")


        if pushButton_11:
            pushButton_11.setEnabled(False)

        if pushButton_12:
            pushButton_12.setEnabled(False)

        if line_edit_8:
            value_line_edit_8 = line_edit_8.text()
        else:
            value_line_edit_8 = ""

        if value_line_edit_8:
            if int(codigo_usuario) == int(value_line_edit_8):
                combobox = self.ui.stackedWidget.widget(0).findChild(QWidget, "comboBox")
                line_edit = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit")
                line_edit_2 = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit_2")
                line_edit_5 = self.ui.stackedWidget.widget(0).findChild(QWidget, "lineEdit_5")
                value_line_edit = line_edit.text()
                value_line_edit_2 = line_edit_2.text()
                value_line_edit_5 = line_edit_5.text()
                value_combobox = combobox.currentText()

                # Lanzar el thread para registrar usuario
                
                self.registrar_usuario_cuenta_thread = RegistrarUsuarioThread(self.id_usuario_perfil,
                    value_line_edit, value_line_edit_2, value_combobox, value_line_edit_5
                )
                self.registrar_usuario_cuenta_thread.finished.connect(
                    lambda exito: self.on_registro_cuenta_finished(
                        exito, line_edit_8, line_edit, line_edit_2, line_edit_5, combobox, label_17
                    )
                )
                self.start_thread(self.registrar_usuario_cuenta_thread)
            else:
                QTimer.singleShot(0, lambda: QTimer().stop())
                label_17.setText("Codigo incorrecto")
                label_17.setStyleSheet("color: red;")
                pushButton_11.setEnabled(True)
                pushButton_12.setEnabled(True)
                QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))
        else:
            QTimer.singleShot(0, lambda: QTimer().stop())
            label_17.setText("Complete el código correctamente")
            label_17.setStyleSheet("color: red;")
            pushButton_11.setEnabled(True)
            pushButton_12.setEnabled(True)
            QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))

    def on_registro_cuenta_finished(self, exito, line_edit_8, line_edit, line_edit_2, line_edit_5, combobox, label_17):
        global codigo

        if exito:
            label_17.setText("Usuario registrado correctamente aguarde...")
            label_17.setStyleSheet("color: green;")
            QTimer.singleShot(6000, lambda: (label_17.setStyleSheet("color: transparent;"), self.open_login_window()))
        else:
            label_17.setText("Error al registrar usuario")
            label_17.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_17.setStyleSheet("color: transparent;"))

        line_edit_8.clear()
        line_edit.clear()
        line_edit_2.clear()
        line_edit_5.clear()
        combobox.setCurrentIndex(0)
        


    def open_recover_window(self):
        self.ui.stackedWidget.setCurrentIndex(3)

        label_18 = self.ui.stackedWidget.findChild(QWidget, "label_18")
        pushButton_6 = self.ui.stackedWidget.findChild(QWidget, "pushButton_6")
        push_Button_7 = self.ui.stackedWidget.findChild(QWidget, "pushButton_7")

        if pushButton_6:
            pushButton_6.setEnabled(True)
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=RuntimeWarning)
                try:
                    pushButton_6.clicked.disconnect(self.verificar_existencia_mail)
                except (TypeError, RuntimeError):
                    pass
            pushButton_6.clicked.connect(self.verificar_existencia_mail)
            pushButton_6.setShortcut(Qt.Key_Return)

        if push_Button_7:
            push_Button_7.setEnabled(True)
            push_Button_7.clicked.connect(self.open_login_window)

        if label_18:
            label_18.setStyleSheet("color: transparent;")

    def verificar_existencia_mail(self):
        line_edit_6 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_6")
        value_line_edit_6 = line_edit_6.text()
        label_18 = self.ui.stackedWidget.findChild(QWidget, "label_18")
        pushButton_6 = self.ui.stackedWidget.findChild(QWidget, "pushButton_6")
        push_Button_7 = self.ui.stackedWidget.findChild(QWidget, "pushButton_7")

        if value_line_edit_6 and ("@gmail" in value_line_edit_6 or "@hotmail" in value_line_edit_6 or "@outlook" in value_line_edit_6):
            global email_guardado
            email_guardado = value_line_edit_6

            pushButton_6.setEnabled(False)
            push_Button_7.setEnabled(False)

            # Deshabilita el botón y muestra mensaje de espera si quieres
            label_18.setText("Verificando email y enviando código...")
            label_18.setStyleSheet("color: blue;")
            self.verificar_thread = VerificarYEnviarCodigoThread(self.id_usuario_perfil, value_line_edit_6)
            self.verificar_thread.finished.connect(self.on_verificar_existencia_mail_finished)
            self.start_thread(self.verificar_thread)
        else:
            label_18.setText("Complete todos los campos correctamente")
            label_18.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_18.setStyleSheet("color: transparent;"))

    def on_verificar_existencia_mail_finished(self, existe, codigo):
        pushButton_6 = self.ui.stackedWidget.findChild(QWidget, "pushButton_6")
        push_Button_7 = self.ui.stackedWidget.findChild(QWidget, "pushButton_7")
        line_edit_6 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_6")
        label_18 = self.ui.stackedWidget.findChild(QWidget, "label_18")

        if existe:
            pushButton_6.setEnabled(True)
            push_Button_7.setEnabled(True)
            global codigo_recuperar
            codigo_recuperar = codigo
            if codigo:
                self.open_verificar_recuperar_contra()
            else:
                QTimer.singleShot(0, lambda: QTimer().stop())
                label_18.setAlignment(Qt.AlignCenter)
                label_18.setText("El email no se encuentra disponible")
                label_18.setStyleSheet("color: red;")
                QTimer.singleShot(15000, lambda: label_18.setStyleSheet("color: transparent;"))
            line_edit_6.clear()
        else:
            pushButton_6.setEnabled(True)
            push_Button_7.setEnabled(True)
            label_18.setText("Mail no existente")
            label_18.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_18.setStyleSheet("color: transparent;"))

    def open_verificar_recuperar_contra(self):
        self.ui.stackedWidget.setCurrentIndex(4)

        label_16 = self.ui.stackedWidget.findChild(QWidget, "label_16")
        pushButton_8 = self.ui.stackedWidget.findChild(QWidget, "pushButton_8")
        pushButton_9 = self.ui.stackedWidget.findChild(QWidget, "pushButton_9")
        pushButton_10 = self.ui.stackedWidget.findChild(QWidget, "pushButton_10")
        line_edit_7 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_7")

        if line_edit_7:
            line_edit_7.clear()
            line_edit_7.setAlignment(Qt.AlignCenter)
            line_edit_7.setPlaceholderText("Código de verificación")
            line_edit_7.setFocus()

        if pushButton_8:
            pushButton_8.setEnabled(True)
            try:
                pushButton_8.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
            pushButton_8.clicked.connect(self.verificar_codigo)
            pushButton_8.setShortcut(Qt.Key_Return)

        if pushButton_9:
            pushButton_9.setEnabled(False)
            QTimer.singleShot(40000, lambda: pushButton_9.setEnabled(True))
            try:
                pushButton_9.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
            pushButton_9.clicked.connect(lambda: (self.reenviar_mail(), pushButton_9.setEnabled(False), QTimer.singleShot(60000, lambda: pushButton_9.setEnabled(True))))

        if pushButton_10:
            pushButton_10.setEnabled(True)
            try:
                pushButton_10.clicked.disconnect()
            except (TypeError, RuntimeError):
                pass
            pushButton_10.clicked.connect(self.open_recover_window)

        if label_16:
            label_16.setStyleSheet("color: transparent;")

    def reenviar_mail(self):
        label_16 = self.ui.stackedWidget.findChild(QWidget, "label_16")
        global email_guardado

        label_16.setText("Reenviando código...")
        label_16.setStyleSheet("color: blue;")
        self.reenviar_thread = EnviarCodigoThread(email_guardado)
        self.reenviar_thread.finished.connect(self.on_codigo_reenviado)
        self.start_thread(self.reenviar_thread)

    def on_codigo_reenviado(self, codigo):
        global codigo_recuperar
        label_16 = self.ui.stackedWidget.findChild(QWidget, "label_16")
        if codigo:
            codigo_recuperar = codigo
            label_16.setText("Código reenviado correctamente")
            label_16.setStyleSheet("color: green;")
        else:
            label_16.setText("Error al reenviar el código")
            label_16.setStyleSheet("color: red;")
        QTimer.singleShot(6000, lambda: label_16.setStyleSheet("color: transparent;"))

    def verificar_codigo(self):
        global codigo_usuario

        line_edit_7 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_7")
        label_16 = self.ui.stackedWidget.findChild(QWidget, "label_16")
        value_line_edit_7 = line_edit_7.text()
        pushButton_8 = self.ui.stackedWidget.findChild(QWidget, "pushButton_8")
        pushButton_9 = self.ui.stackedWidget.findChild(QWidget, "pushButton_9")
        pushButton_10 = self.ui.stackedWidget.findChild(QWidget, "pushButton_10")

        if value_line_edit_7.isdigit():

            if int(codigo_recuperar) == int(value_line_edit_7):
                pushButton_8.setEnabled(False)
                pushButton_9.setEnabled(False)
                pushButton_10.setEnabled(False)
                self.open_recuperar_contra()

            else:
                pushButton_8.setEnabled(True)
                pushButton_9.setEnabled(True)
                pushButton_10.setEnabled(True)
                label_16.setText("Codigo incorrecto")
                label_16.setStyleSheet("color: red;")
                QTimer.singleShot(6000, lambda: label_16.setStyleSheet("color: transparent;"))
        else:
            label_16.setText("Complete todos los campos correctamente")
            label_16.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_16.setStyleSheet("color: transparent;"))

    # ventana de recuperar contrasenia
    def open_recuperar_contra(self):
        self.ui.stackedWidget.setCurrentIndex(6)

        label_28 = self.ui.stackedWidget.findChild(QWidget, "label_28")
        pushButton_13 = self.ui.stackedWidget.findChild(QWidget, "pushButton_13")
        pushButton_14 = self.ui.stackedWidget.findChild(QWidget, "pushButton_14")
        line_edit_9 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_9")
        line_edit_10 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_10")

        if line_edit_9:
            line_edit_9.clear()
            line_edit_9.setAlignment(Qt.AlignCenter)
            line_edit_9.setEchoMode(QLineEdit.Password)
            line_edit_9.setPlaceholderText("Nueva contraseña")
            line_edit_9.setFocus()
        
        if line_edit_10:
            line_edit_10.clear()
            line_edit_10.setAlignment(Qt.AlignCenter)
            line_edit_10.setEchoMode(QLineEdit.Password)
            line_edit_10.setPlaceholderText("Repetir nueva contraseña")

        if pushButton_13:
            pushButton_13.setEnabled(True)
            pushButton_13.clicked.connect(self.verificar_repeticion_o_igualdad_de_contrasenias)
            pushButton_13.setShortcut(Qt.Key_Return)

        if pushButton_14:
            pushButton_14.setEnabled(True)
            pushButton_14.clicked.connect(self.open_recover_window)

        if label_28:
            label_28.setStyleSheet("color: transparent;")


    def verificar_repeticion_o_igualdad_de_contrasenias(self):
        line_edit_9 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_9")
        line_edit_10 = self.ui.stackedWidget.findChild(QWidget, "lineEdit_10")
        label_28 = self.ui.stackedWidget.findChild(QWidget, "label_28")
        value_line_edit_9 = line_edit_9.text()
        value_line_edit_10 = line_edit_10.text()
        pushButton_13 = self.ui.stackedWidget.findChild(QWidget, "pushButton_13")
        pushButton_14 = self.ui.stackedWidget.findChild(QWidget, "pushButton_14")

        global email_guardado

        if value_line_edit_9 and value_line_edit_10:
            if pushButton_13:
                pushButton_13.setEnabled(False)
            if pushButton_14:
                pushButton_14.setEnabled(False)
            if len(value_line_edit_9) >= 8 and len(value_line_edit_10) >= 8:
                if value_line_edit_9 == value_line_edit_10:
                    # Lanza el thread para actualizar la contraseña
                    self.actualizar_contrasena_thread = ActualizarContrasenaThread(self.id_usuario_perfil, value_line_edit_9, email_guardado)
                    self.actualizar_contrasena_thread.finished.connect(
                        lambda exito: self.on_actualizar_contrasena_finished(
                            exito, label_28
                        )
                    )
                    self.start_thread(self.actualizar_contrasena_thread)
                else:
                    if pushButton_13:
                        pushButton_13.setEnabled(True)
                    if pushButton_14:
                        pushButton_14.setEnabled(True)
                    label_28.setText("Las contraseñas no coinciden")
                    label_28.setStyleSheet("color: red;")
                    QTimer.singleShot(6000, lambda: label_28.setStyleSheet("color: transparent;"))
            else:
                if pushButton_13:
                    pushButton_13.setEnabled(True)
                if pushButton_14:
                    pushButton_14.setEnabled(True)
                label_28.setText("Las contraseñas deben tener al menos 8 caracteres")
                label_28.setStyleSheet("color: red;")
                QTimer.singleShot(6000, lambda: label_28.setStyleSheet("color: transparent;"))
        else:
            label_28.setText("Complete todos los campos correctamente")
            label_28.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_28.setStyleSheet("color: transparent;"))

    def on_actualizar_contrasena_finished(self, exito, label_28):
        if exito:
            label_28.setText("Contraseña cambiada correctamente aguarde...")
            label_28.setStyleSheet("color: green;")
            QTimer.singleShot(6000, lambda: (label_28.setStyleSheet("color: transparent;"), self.open_login_window()))
        else:
            pushButton_13 = self.ui.stackedWidget.findChild(QWidget, "pushButton_13")
            pushButton_14 = self.ui.stackedWidget.findChild(QWidget, "pushButton_14")

            pushButton_13.setEnabled(True)
            pushButton_14.setEnabled(True)

            label_28.setText("Error al cambiar la contraseña")
            label_28.setStyleSheet("color: red;")
            QTimer.singleShot(6000, lambda: label_28.setStyleSheet("color: transparent;"))
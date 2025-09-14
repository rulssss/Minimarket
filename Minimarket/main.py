from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QProgressBar
from archivos_py.windows.inicio_login import Inicio
import sys
from archivos_py.windows.inicio_login_web import InicioWeb
from archivos_py.db.sesiones import SessionManager
from archivos_py.threads.db_thread_loginWeb_api import Login_web_Thread_verificar_existencia_mail, Cambiar_a_True_open
import socket
import requests
from PySide6.QtWidgets import QMessageBox
from archivos_py.threads.db_thread_minimarket import ObtenerVersionThread
import subprocess
from PySide6.QtCore import QThread
import os
from PySide6.QtGui import QIcon
from archivos_py.ui.theme_utils import is_windows_dark_mode, apply_dark_palette
import hashlib

def verificar_estado_subscripcion(uid):
    """
    Consulta a la API Flask si el usuario sigue teniendo suscripción Pro.
    Retorna True si tiene Pro, False si no.
    """
    API_URL = "https://web-production-aa989.up.railway.app" # Pon aquí tu URL pública
    try:
        response = requests.post(f"{API_URL}/api/verificar_suscripcion", json={"uid": uid})
        data = response.json()
        pro = data.get("pro", False)
        open = data.get("open", False)

        return pro, open
    except Exception as e:
        print(f"Error al consultar API: {e}")
        return False, False  # Devuelve SIEMPRE dos valores


single_instance_socket = None  # <-- variable global

# Verificar si ya hay una instancia del programa corriendo
def check_single_instance(port=65432):
    global single_instance_socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        single_instance_socket = s
        return True
    except OSError:
        return False

if not check_single_instance():
    print("El programa ya está abierto.")
    sys.exit(0)


# Obtener la ruta base del directorio del script
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Definir la versión actual
VERSION_ACTUAL = "1.0.1"  

threads = []  # Lista para almacenar los hilos

def mostrar_y_actualizar(url_instalador):
    class ActualizandoDialog(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Actualizando aplicación")
            self.setModal(True)
            # Establecer el ícono personalizado
            icon_path = os.path.join(BASE_DIR, "archivos_py", "resources", "r.ico")
            self.setWindowIcon(QIcon(icon_path))
            
            layout = QVBoxLayout()
            self.label = QLabel("Por favor espere el programa se iniciara en cuanto\ntermine su actualización.")
            self.progress = QProgressBar()
            self.progress.setRange(0, 0)  # Barra indeterminada
            layout.addWidget(self.label)
            layout.addWidget(self.progress)
            self.setLayout(layout)
            self.setFixedSize(300, 100)

    url = url_instalador
    destino = "rls_nuevo.exe"

    dialog = ActualizandoDialog()
    dialog.show()
    QApplication.processEvents()  # Para mostrar la ventana antes de descargar

    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(destino, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        dialog.close()
        QThread.sleep(3)  # <-- Espera 3 segundos extra antes de continuar
        
        # Usa la ruta absoluta de updater.exe
        updater_path = os.path.join(os.path.dirname(sys.argv[0]), "updater.exe")

        subprocess.Popen([updater_path, "rls_nuevo.exe", "rls.exe"], shell=False)
        sys.exit(0)
    except Exception as e:
        dialog.close()
        QMessageBox.critical(None, "Error", f"No se pudo descargar la actualización.\n{e}")
        sys.exit(0)

def on_version_obtenida(version, url_instalador):
    print("verificando version")
    print("version obtenida:", version)
    if version and version.strip() != VERSION_ACTUAL:
        print("actualizando version")
        mostrar_y_actualizar(url_instalador)
    else:
        iniciar_aplicacion()

def iniciar_aplicacion():
    global window
    # Verificar si hay una sesión activa
    session_manager = SessionManager()

    ######### linea para borrar el usuario web para pruebas
    #session_manager.clear_session()
    ####################################


    if session_manager.is_logged_in():
        # Si hay sesión activa, ir directamente al inicio
        print("Sesión activa encontrada, iniciando aplicación...")
        # Obtener datos guardados
        email = session_manager.get_email()
        uid = session_manager.get_uid()
        #open = session_manager.get_open()

        id_usuario_perfil = firebase_uid_to_uuid(uid)
        
        # Ejecutar el hilo para llevar el UID a functions para poder enviar querys
        login_thread_verificar = Login_web_Thread_verificar_existencia_mail(email, id_usuario_perfil)
        login_thread_verificar.resultado.connect(lambda exito, id_usuario_perfil: on_login_web_verificado(exito, id_usuario_perfil, uid, session_manager))
        start_thread(login_thread_verificar)

    else:
        # Si no hay sesión, mostrar login
        print("No hay sesión activa, mostrando login...")
        window = InicioWeb()
        window.show()

def firebase_uid_to_uuid(uid):
        import hashlib
        uid_limpio = uid.strip().strip('"').strip("'")
        firebase_bytes = uid_limpio.encode('utf-8')
        hash_object = hashlib.md5(firebase_bytes)
        uuid_string = hash_object.hexdigest()
        formatted_uuid = f"{uuid_string[:8]}-{uuid_string[8:12]}-{uuid_string[12:16]}-{uuid_string[16:20]}-{uuid_string[20:32]}"
        return formatted_uuid

def on_login_web_verificado(exito, id_usuario_perfil, uid, session_manager):
    global window
    # verificar estado de suscripción en Firebase
    pro, open = verificar_estado_subscripcion(uid)

    session_manager = SessionManager()
    open_  = session_manager.get_open()

    if pro and not open:
        #$pasar variable open a true para indicar que la sesion esta activa
        
        # obtener el uid original de firebase
        uid = session_manager.get_uid()

        thread_change_false_open = Cambiar_a_True_open(uid)
        start_thread(thread_change_false_open)

        window = Inicio(id_usuario_perfil)

    elif not pro and not open:
        icon_path = os.path.join(BASE_DIR, "archivos_py", "resources", "r.ico")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Sin conexión")
        msg.setText("No hay conexión a internet")
        msg.setWindowIcon(QIcon(icon_path))
        msg.exec()
        window = InicioWeb()

    elif open and open_:
        print("la cuenta se cerro en estado de Reconectando")
        window = InicioWeb()

    elif not pro:
        print("El usuario no tiene suscripción Pro.")
        session_manager.clear_session()
        window = InicioWeb()

    else:
        print("La cuenta se encuentra abierta en otra sesión.")
        window = InicioWeb()

    window.show()

def start_thread(thread):
        threads.append(thread)
        thread.finished.connect(lambda: threads.remove(thread) if thread in threads else None)
        thread.start()
        
#inicio del login web y luego al programa si no inicio sesion web y si inicio directo al programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    if is_windows_dark_mode():
        apply_dark_palette(app)

    # Ejecutar el hilo para obtener la versión antes de mostrar la ventana principal
    obtener_version_thread = ObtenerVersionThread()
    obtener_version_thread.version_obtenida.connect(on_version_obtenida)
    start_thread(obtener_version_thread)

    sys.exit(app.exec())
    


# inicio del login pruebas del login rls
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Fusion")
#    window = Inicio()
#    window.show()
#    sys.exit(app.exec())


# inicio del minimarket SOLO para pruebas ya que se abre el minimarket sin loguin
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    app.setStyle("Fusion")
#    print("se inicia el minimarket")
#    main_window = MainWindow(usuario="mariano", account="Administrador")
#    main_window.resize(1690, 900)
#    main_window.show()
#    sys.exit(app.exec())    




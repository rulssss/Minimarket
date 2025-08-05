from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QProgressBar
from archivos_py.windows.inicio_login import Inicio
import sys
from archivos_py.windows.inicio_login_web import InicioWeb
from archivos_py.db.sesiones import SessionManager
from archivos_py.threads.db_thread_loginWeb_api import Login_web_Thread_verificar_existencia_mail
import socket
import requests
from PySide6.QtWidgets import QMessageBox
from archivos_py.threads.db_thread_minimarket import ObtenerVersionThread
import subprocess
from PySide6.QtCore import QThread
import os
from PySide6.QtGui import QIcon

def verificar_estado_subscripcion(uid):
    """
    Consulta a la API Flask si el usuario sigue teniendo suscripción Pro.
    Retorna True si tiene Pro, False si no.
    """
    API_URL = "https://web-production-aa989.up.railway.app" # Pon aquí tu URL pública
    try:
        response = requests.post(f"{API_URL}/api/verificar_suscripcion", json={"uid": uid})
        resultado = response.json().get("pro", False)
        return resultado
    except Exception as e:
        print(f"Error al consultar API: {e}")
        return False


# Verificar si ya hay una instancia del programa corriendo
def check_single_instance(port=65432):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", port))
        return True
    except OSError:
        return False

if not check_single_instance():
    print("El programa ya está abierto.")
    sys.exit(0)

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


VERSION_ACTUAL = "1.0.1"  


obtener_version_thread = None  # referencia global

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
            self.label = QLabel("Actualizando aplicación...\nPor favor espere.")
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
        print("Buscando updater.exe en:", updater_path)
        print("Archivos en la carpeta:", os.listdir(os.path.dirname(sys.argv[0])))

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
 
        
        # Ejecutar el hilo para llevar el UID a functions para poder enviar querys
        login_thread_verificar = Login_web_Thread_verificar_existencia_mail(email, uid)
        login_thread_verificar.start()

        # Verificar estado de suscripción en Firebase
        if verificar_estado_subscripcion(uid):
            window = Inicio()
        else:
            print("La suscripción Pro ha cambiado. Mostrando login web.")
            session_manager.clear_session()
            window = InicioWeb()

    else:
        
        # Si no hay sesión, mostrar login
        print("No hay sesión activa, mostrando login...")
        window = InicioWeb()
    
    window.show()


#inicio del login web y luego al programa si no inicio sesion web y si inicio directo al programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    
    # Ejecutar el hilo para obtener la versión antes de mostrar la ventana principal
    obtener_version_thread = ObtenerVersionThread()
    obtener_version_thread.version_obtenida.connect(on_version_obtenida)
    obtener_version_thread.start()
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




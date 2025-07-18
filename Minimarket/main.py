from PySide6.QtWidgets import QApplication
from archivos_py.windows.inicio_login import Inicio
import sys
from archivos_py.windows.inicio_minimarket import MainWindow
from archivos_py.windows.inicio_login_web import InicioWeb
from archivos_py.db.sesiones import SessionManager
from archivos_py.threads.db_thread_loginWeb_api import Login_web_Thread_verificar_existencia_mail
import socket
import requests

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

   

#inicio del login web y luego al programa si no inicio sesion web y si inicio directo al programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
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




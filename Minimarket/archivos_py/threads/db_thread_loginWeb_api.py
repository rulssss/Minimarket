from urllib import response
import requests
from PySide6.QtCore import QThread, Signal

API_URL = "https://web-production-aa989.up.railway.app"  # Cambia el host/puerto si tu API está en otro lugar

class Login_web_Thread(QThread):
    resultado = Signal(bool, object)  # bool para éxito, object para datos del usuario o mensaje de error

    def __init__(self, mail, contrasena):
        super().__init__()
        self.mail = mail
        self.contrasena = contrasena

    def run(self):
        try:
            url = f"{API_URL}/api/login"
            payload = {"email": self.mail, "password": self.contrasena}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.resultado.emit(data.get("exito", False), data.get("resultado"))
            else:
                self.resultado.emit(False, "Error de conexión con el backend")
        except Exception as e:
            print(f"Error en el thread de login: {e}")
            self.resultado.emit(False, f"Error interno: {str(e)}")

class Cambiar_a_True_open(QThread):
    finished = Signal()  # Señal que emite cuando termina

    def __init__(self, id_usuario_perfil):
        super().__init__()
        self.id_usuario_perfil = id_usuario_perfil

    def run(self):
        
        try:
            url = f"{API_URL}/api/cambiar_a_true_open"
            response = requests.post(url, json={"uid": self.id_usuario_perfil})
            # Puedes manejar la respuesta si lo necesitas
            self.finished.emit()
        except Exception as e:
            print(f"Error al cambiar open a True: {e}")
            self.finished.emit()

class Cambiar_False_open(QThread):
    finished = Signal()  # Señal que emite cuando termina

    def __init__(self, id_usuario_perfil):
        super().__init__()
        self.id_usuario_perfil = id_usuario_perfil

    def run(self):
        try:
            url = f"{API_URL}/api/cambiar_a_false_open"
            response = requests.post(url, json={"uid": self.id_usuario_perfil})
            # Puedes manejar la respuesta si lo necesitas
            self.finished.emit()
        except Exception as e:
            print(f"Error al cambiar open a False: {e}")
            self.finished.emit()

class Login_web_Thread_verificar_existencia_mail(QThread):
    resultado = Signal(bool, str)  # bool para éxito, str para id_usuario_perfil

    def __init__(self, email, uid):
        super().__init__()
        self.email = email
        self.uid = uid

    def run(self):
        try:
            url = f"{API_URL}/api/verificar_existencia_mail"
            payload = {"email": self.email, "uid": self.uid}
            print(f"  Email: {self.email}")
            response = requests.post(url, json=payload)
           
            if response.status_code == 200:
                data = response.json()
                verificado = data.get("verificado", [False, None])
                exito = verificado[0]
                id_usuario_perfil = verificado[1]

                self.resultado.emit(exito, id_usuario_perfil)
            else:
                self.resultado.emit(False, None)
        except Exception as e:
            print(f"Error en el thread de verificación de mail: {e}")
            self.resultado.emit(False, None)


class Login_web_Thread_actualizar_pago_por_uid(QThread):
    finished_update = Signal()  # Señal que emite (éxito, mensaje)

    def __init__(self, uid):
        super().__init__()
        self.uid = uid

    def run(self):
        try:
            url = f"{API_URL}/api/actualizar_pago_por_uid"
            payload = {"uid": self.uid}
            response = requests.post(url, json=payload)
            # Puedes manejar la respuesta si lo necesitas
            self.finished_update.emit()
        except Exception as e:
            print(f"Error al actualizar pago: {e}")
            self.finished_update.emit()
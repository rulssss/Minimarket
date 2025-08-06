from PySide6.QtCore import QThread, Signal
import requests

API_URL = "https://web-production-aa989.up.railway.app"

class LoginThread(QThread):
    finished = Signal(bool, str)
    def __init__(self, tipo, usuario, contrasenia):
        super().__init__()
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.tipo = tipo

    def run(self):
        try:
            url = f"{API_URL}/api/verificar_contrasenia"
            payload = {
                "tipo_usuario": self.tipo,
                "usuario": self.usuario,
                "contrasenia": self.contrasenia
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                
                valido = data.get("valido", False)
                mensaje = "Login correcto" if valido else "Usuario o contraseña incorrectos"
                self.finished.emit(valido, mensaje)
            else:
                self.finished.emit(False, "Error de conexión con el backend")
        except Exception as e:
            print(f"Error en el thread de login: {e}")
            self.finished.emit(False, f"Error interno: {str(e)}")

class RegistroCheckThread(QThread):
    finished = Signal(dict)

    def __init__(self, username, password, email, tipo_usuario):
        super().__init__()
        self.username = username
        self.password = password
        self.email = email
        self.tipo_usuario = tipo_usuario

    def run(self):
        try:
            url = f"{API_URL}/api/registro_check"
            payload = {
                "username": self.username,
                "password": self.password,
                "email": self.email,
                "tipo_usuario": self.tipo_usuario
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.finished.emit(data)
            else:
                self.finished.emit({
                    "hay_admin": False,
                    "usuario_existe": False,
                    "mail_existe": False,
                    "password_ok": False,
                    "error": "Error de conexión con el backend"
                })
        except Exception as e:
            print(f"Error en el thread de registro: {e}")
            self.finished.emit({
                "hay_admin": False,
                "usuario_existe": False,
                "mail_existe": False,
                "password_ok": False,
                "error": f"Error interno: {str(e)}"
            })


class EnviarCodigoThread(QThread):
    finished = Signal(object)  # Puede ser el código o None

    def __init__(self, mail):
        super().__init__()
        self.mail = mail

    def run(self):
        try:
            url = f"{API_URL}/api/enviar_codigo_verificacion"
            payload = {"mail": self.mail}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                codigo = data.get("codigo")
                if codigo:
                    print(f"Codigo enviado al usuario: {codigo}")
                    self.finished.emit(codigo)
                else:
                    print("No se pudo enviar el código.")
                    self.finished.emit(None)
            else:
                print(f"Error al enviar código: {response.text}")
                self.finished.emit(None)
        except Exception as e:
            print(f"Error en el thread de enviar código: {e}")
            self.finished.emit(None)

class CodigoOtroAdminThread(QThread):
    finished = Signal(object)  # El código o None

    def run(self):
        
        try:
            url = f"{API_URL}/api/codigo_otro_admin"
            response = requests.post(url)
            if response.status_code == 200:
                data = response.json()
                codigo = data.get("codigo")
                
                self.finished.emit(codigo)
            else:
                print(f"Error al obtener código de otro admin: {response.text}")
                self.finished.emit(None)
        except Exception as e:
            print(f"Error en el thread de enviar código a admin: {e}")
            self.finished.emit(None)

class RegistrarUsuarioThread(QThread):
    finished = Signal(bool)

    def __init__(self, usuario, contrasena, tipo, email):
        super().__init__()
        self.usuario = usuario
        self.contrasena = contrasena
        self.tipo = tipo
        self.email = email

    def run(self):
    
        try:
            url = f"{API_URL}/api/registrar_usuario"
            payload = {
                "usuario": self.usuario,
                "contrasena": self.contrasena,
                "tipo": self.tipo,
                "email": self.email
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit(True)
            else:
                self.finished.emit(False)
        except Exception as e:
            print(f"Error en el thread de registrar usuario: {e}")
            self.finished.emit(False)


class VerificarYEnviarCodigoThread(QThread):
    finished = Signal(bool, object)  # (existe, codigo o None)

    def __init__(self, mail):
        super().__init__()
        self.mail = mail

    def run(self):
        try:
            url = f"{API_URL}/api/verificar_y_enviar_codigo"
            payload = {"mail": self.mail}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                existe = data.get("existe", False)
                codigo = data.get("codigo")
                if existe and codigo:
                    
                    self.finished.emit(True, codigo)
                else:
                    print("No se pudo enviar el código.")
                    self.finished.emit(False, None)
            else:
                print(f"Error al verificar y enviar código: {response.text}")
                self.finished.emit(False, None)
        except Exception as e:
            print(f"Error en el thread de verificar y enviar código: {e}")
            self.finished.emit(False, None)


class ActualizarContrasenaThread(QThread):
    finished = Signal(bool)

    def __init__(self, nueva_contrasena, email):
        super().__init__()
        self.nueva_contrasena = nueva_contrasena
        self.email = email

    def run(self):
        try:
            url = f"{API_URL}/api/actualizar_contrasena"
            payload = {
                "nueva_contrasena": self.nueva_contrasena,
                "email": self.email
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit(True)
            else:
                self.finished.emit(False)
        except Exception as e:
            print(f"Error en el thread de actualizar contraseña: {e}")
            self.finished.emit(False)


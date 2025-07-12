from PySide6.QtCore import QThread, Signal
from archivos_py.db.usuarios import *

class LoginThread(QThread):
    finished = Signal(bool, str)
    def __init__(self, usuario, contrasenia, tipo):
        super().__init__()
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.tipo = tipo
    def run(self):
        exito = verificar_contrasenia(self.contrasenia, self.tipo, self.usuario)
        self.finished.emit(not exito, "Login correcto" if not exito else "Error")

class RegistroCheckThread(QThread):
    finished = Signal(dict)

    def __init__(self, username, password, email, tipo_usuario):
        super().__init__()
        self.username = username
        self.password = password
        self.email = email
        self.tipo_usuario = tipo_usuario

    def run(self):
        result = {
            "hay_admin": hay_admin() if self.tipo_usuario == "Administrador" else False,
            "usuario_existe": verificar_usuario_existente(self.username),
            "mail_existe": verificar_mail_existente(self.email),
            "password_ok": len(self.password) >= 8
        }
        self.finished.emit(result)


class EnviarCodigoThread(QThread):
    finished = Signal(object)  # Puede ser el código o None

    def __init__(self, mail):
        super().__init__()
        self.mail = mail

    def run(self):
        codigo = enviar_codigo_verificacion(self.mail)
        if codigo:
            print(f"Codigo enviado al usuario: {codigo}")
        self.finished.emit(codigo)


class CodigoOtroAdminThread(QThread):
    finished = Signal(object)  # El código o None

    def run(self):
        administrador = traer_administradores()
        mail = traer_mail_admin(administrador)
        codigo = enviar_codigo_verificacion(mail)
        print("codigo enviado a admin", codigo)
        self.finished.emit(codigo)

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
            registrar_usuario(self.usuario, self.contrasena, self.tipo, self.email)
            self.finished.emit(True)
        except Exception:
            self.finished.emit(False)

class VerificarYEnviarCodigoThread(QThread):
    finished = Signal(bool, object)  # (existe, codigo o None)

    def __init__(self, mail):
        super().__init__()
        self.mail = mail

    def run(self):
        existe = existencia_mail(self.mail)
        if existe:
            codigo = enviar_codigo_verificacion(self.mail)
            print(f"Codigo enviado al usuario: {codigo}")
            self.finished.emit(True, codigo)
        else:
            self.finished.emit(False, None)


class ActualizarContrasenaThread(QThread):
    finished = Signal(bool)

    def __init__(self, nueva_contrasena, email):
        super().__init__()
        self.nueva_contrasena = nueva_contrasena
        self.email = email

    def run(self):
        exito = actualizar_contrasena(self.nueva_contrasena, self.email)
        self.finished.emit(exito)
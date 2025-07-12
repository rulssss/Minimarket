from PySide6.QtCore import QThread, Signal

class Login_web_Thread(QThread):
    resultado = Signal(bool)  # bool para éxito, str para mensaje
    
    def __init__(self, mail, contrasena):
        super().__init__()
        self.mail = mail
        self.contrasena = contrasena
    
    def run(self):
        try:
            # Aquí haces la verificación de login
            # Puedes usar una función de base de datos o API
            exito = self.verificar_credenciales(self.mail, self.contrasena)
            
            if exito:
                self.resultado.emit(True)
            else:
                self.resultado.emit(False)

        except Exception as e:
            print("Error en el thread de login:", e)
            self.resultado.emit(False)

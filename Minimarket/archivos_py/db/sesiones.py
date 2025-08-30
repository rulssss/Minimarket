import json
import os
import base64
import secrets
from datetime import datetime, timedelta
from cryptography.fernet import Fernet

class SessionManager:
    def __init__(self):
        # Ruta oculta en la carpeta de usuario
        user_dir = os.path.expanduser("~")
        hidden_dir = os.path.join(user_dir, ".mnmkt_session")
        os.makedirs(hidden_dir, exist_ok=True)

        # Nombre aleatorio para el archivo de sesión
        self.session_file = os.path.join(hidden_dir, "session.dat")

        # Clave de cifrado (guárdala en un lugar seguro, aquí solo para ejemplo)
        self.key_file = os.path.join(hidden_dir, "key.key")
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as kf:
                kf.write(key)
        else:
            with open(self.key_file, "rb") as kf:
                key = kf.read()
        self.fernet = Fernet(key)

    def get_email(self):
        session = self.load_session()
        return session.get('email', '') if session else ''

    def get_open(self):
        session = self.load_session()
        return session.get('open', False) if session else False

    def get_uid(self):
        session = self.load_session()
        return session.get('uid', '') if session else ''
    
    #def set_open(self, value: bool):
    #    session = self.load_session()
    #    if session:
    #        session['open'] = value
    #        self.save_session(session.get('email', ''), session.get('uid', ''), value)

    def save_session(self, email, uid, open_):
        """Guarda la sesión del usuario cifrada"""
        try:
            session_data = {
                'email': email,
                'uid': uid,
                'open': open_,
                'login_time': datetime.now().isoformat(),
            }
            json_data = json.dumps(session_data).encode("utf-8")
            encrypted_data = self.fernet.encrypt(json_data)
            with open(self.session_file, "wb") as f:
                f.write(encrypted_data)
            return True
        except Exception as e:
            print(f"Error al guardar sesión: {e}")
            return False

    def load_session(self):
        """Carga la sesión cifrada si existe y no ha expirado"""
        try:
            if not os.path.exists(self.session_file):
                return None
            with open(self.session_file, "rb") as f:
                encrypted_data = f.read()
            json_data = self.fernet.decrypt(encrypted_data)
            session_data = json.loads(json_data.decode("utf-8"))
            return session_data
        except Exception as e:
            print(f"Error al cargar sesión: {e}")
            return None

    def clear_session(self):
        """Elimina la sesión guardada"""
        try:
            if os.path.exists(self.session_file):
                os.remove(self.session_file)
        except Exception as e:
            print(f"Error al eliminar sesión: {e}")

    def is_logged_in(self):
        """Verifica si hay una sesión activa"""
        session = self.load_session()
        return session is not None
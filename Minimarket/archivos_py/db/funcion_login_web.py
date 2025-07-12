from firebase_admin import auth
import firebase_admin
from firebase_admin import credentials
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar Firebase (solo una vez)
def inicializar_firebase():
    if not firebase_admin._apps:
        # Obtener ruta del archivo de credenciales desde variable de entorno
        cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
        if cred_path and os.path.exists(cred_path):
            cred = credentials.Certificate(cred_path)
            firebase_admin.initialize_app(cred)
        else:
            raise Exception("No se encontraron las credenciales de Firebase")

def verificar_credenciales(mail, contrasena):
    """
    Verifica credenciales usando Firebase Auth
    Retorna (exito: bool, mensaje: str, user_data: dict)
    """
    try:
        inicializar_firebase()
        
        # Verificar si el usuario existe
        user = auth.get_user_by_email(mail)
        
        if not user.email_verified:
            return False, "Email no verificado. Por favor verifica tu email antes de continuar.", None
        
        # Para verificar la contraseña, necesitas usar Firebase Auth REST API
        # Ya que Firebase Admin SDK no puede verificar contraseñas directamente
        login_exitoso = verificar_contrasena_firebase(mail, contrasena)
        
        if login_exitoso:
            user_data = {
                'uid': user.uid,
                'email': user.email,
                'display_name': user.display_name,
                'email_verified': user.email_verified
            }
            return True, "Usuario autenticado exitosamente", user_data
        else:
            return False, "Contraseña incorrecta", None
            
    except auth.UserNotFoundError:
        return False, "Usuario no encontrado", None
    except Exception as e:
        return False, f"Error al iniciar sesión: {e}", None

def verificar_contrasena_firebase(email, password):
    """
    Verifica la contraseña usando Firebase Auth REST API
    """
    try:
        # URL de la API de Firebase Auth
        url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        
        # Obtener API Key desde variable de entorno
        API_KEY = os.getenv('FIREBASE_API_KEY')
        if not API_KEY:
            raise Exception("No se encontró la API Key de Firebase en las variables de entorno")
        
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        
        response = requests.post(f"{url}?key={API_KEY}", json=payload)
        
        if response.status_code == 200:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error al verificar contraseña: {e}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    email = "marianopicco83@gmail.com"
    contrasena = "Mariano302"
    
    exito, mensaje, datos_usuario = verificar_credenciales(email, contrasena)
    
    if exito:
        print(f"✅ {mensaje}")
        print(f"Datos del usuario: {datos_usuario}")
    else:
        print(f"❌ {mensaje}")
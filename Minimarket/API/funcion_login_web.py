from firebase_admin import auth, firestore
import firebase_admin
from firebase_admin import credentials
import requests
import os



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

# Función para verificar si un usuario es Pro
def is_user_pro(user_uid):
    """Verificar si un usuario tiene suscripción Pro"""
    try:
        db = firestore.client()
        user_doc = db.collection('users').document(user_uid).get()
        
        if user_doc.exists:
            user_data = user_doc.to_dict()
            return user_data.get('subscription') == 'pro'
        return False
    except Exception as e:
        print(f"Error al verificar suscripción Pro: {e}")
        return False

def verificar_credenciales(mail, contrasena):
    """
    Verifica credenciales usando Firebase Auth y que el usuario sea Pro
    Retorna (exito: bool, user_data: dict o str con mensaje de error)
    """
    try:
        inicializar_firebase()
        
        # Verificar si el usuario existe
        user = auth.get_user_by_email(mail)
        
        if not user.email_verified:
            return False, "Email no verificado"
        
        # Para verificar la contraseña, necesitas usar Firebase Auth REST API
        login_exitoso = verificar_contrasena_firebase(mail, contrasena)
        
        if login_exitoso:
            # Verificar si el usuario tiene suscripción Pro
            if is_user_pro(user.uid):
                user_data = {
                    'uid': user.uid,
                    'email': user.email,
                    'display_name': user.display_name,
                    'email_verified': user.email_verified,
                    'subscription': 'pro'
                }
                return True, user_data
            else:
                return False, "Usuario sin suscripción Pro"
        else:
            return False, "Credenciales incorrectas"
            
    except auth.UserNotFoundError:
        return False, "Usuario no encontrado"
    except Exception as e:
        return False, f"Error interno: {str(e)}"

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


def verificar_estado_suscripcion(uid):
    """
    Consulta Firestore/Firebase si el usuario con ese UID sigue teniendo suscripción Pro.
    Retorna True si tiene Pro, False si no.
    """
    print(f"Verificando estado de suscripción para UID: {uid}")
    try:
        # Inicializa Firebase si no está inicializado
        inicializar_firebase()  # Usa tu función que maneja la variable de entorno

        db = firestore.client()
        user_doc = db.collection('users').document(uid).get()
        if user_doc.exists:
            user_data = user_doc.to_dict()
            return user_data.get('subscription', '').lower() == 'pro'
        return False
    except Exception as e:
        print(f"Error al verificar estado de suscripción: {e}")
        return False
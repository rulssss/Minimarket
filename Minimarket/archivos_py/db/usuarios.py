from archivos_py.db.connection import get_connection
import random
import smtplib
from email.mime.text import MIMEText
from psycopg2 import errors

# LOGIN

def check_activation():
    return True, "1234567890"  # Simulación de la función de verificación de activación. Devuelve True y un código de validación ficticio.

def verificar_contrasenia(tipo_usuario, usuario, contrasenia):
    conn = get_connection()
    cursor = conn.cursor()
    query_data2 = f"SELECT usuarios.id_usuario, contrasenas.contrasena, usuarios.admin FROM usuarios JOIN contrasenas ON usuarios.id_usuario = contrasenas.id_usuario WHERE usuarios.nombre = '{usuario}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if tipo_usuario == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o false para verificar que tipo de cuenta es

    if data != []:
        if data[0][1] != contrasenia or data[0][2] != account:
            ## verifica password igual y si el tipo es igual al seleccionado
            return True # devuelve true si alguno es distinto para tirar el mensaje de error
        else:
            return False
    else:
        return True #no vienen datos de la base de datos, por lo que no existe el usuario o la contraseña
    
#REGISTRO

def hay_admin():
    conn = get_connection()
    cursor= conn.cursor()
    query_data = f"SELECT id_usuario FROM usuarios WHERE admin = True"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if data == []: # verifica si hay algun administrador, si no hay devuelve false y abre la ventana de registro
        return False
    else:
        return True
    

def verificar_mail_existente(value_line_edit_8):
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT mail FROM usuarios WHERE mail = '{value_line_edit_8}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if data != []: # verifica existencia de mail, si no hay no procede a la siguiente ventana de registro
        return True
    else:
        return False
    

def verificar_usuario_existente(value_line_edit_3):
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT nombre FROM usuarios WHERE nombre = '{value_line_edit_3}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if data != []: # verifica existencia de nombre, si no hay no procede a la siguiente ventana de registro
        return True
    else:
        return False
    
    
def enviar_codigo_verificacion(mail):
    # Generar un código de verificación de 6 dígitos
    codigo = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    # Configuración del correo
    remitente = "relssbot@gmail.com"
    contrasena = "hnxd xita zgze goyz"
    asunto = "Código de Verificación rls"
    mensaje = f"Tu código de verificación es: {codigo}"
    
    # Crear el mensaje
    msg = MIMEText(mensaje)
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = mail
    
    try:
        # Conectar al servidor SMTP y enviar el correo
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contrasena)
        servidor.sendmail(remitente, mail, msg.as_string())
        servidor.quit()
        return codigo  # Retornar el código generado
    except Exception as e:
        return None
    

def traer_administradores():
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT nombre FROM usuarios WHERE admin = True ORDER BY id_usuario"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data[0][0] # devuelve una lista con los administradores de la base de datos

def traer_mail_admin(administrador):
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT mail FROM usuarios WHERE nombre = '{administrador}' ORDER BY id_usuario"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] # devuelve el mail del administrador


def registrar_usuario(username, password, account, mail):
    mail = mail.lower()

    if account == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o fals epara verificar que tipo de cuenta es
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query_data1 = f"INSERT INTO usuarios(nombre, admin, mail) VALUES('{username}', {account}, '{mail}')"
        cursor.execute(query_data1)

        cursor = conn.cursor()
        query_data = f"SELECT id_usuario FROM usuarios WHERE nombre = '{username}'"
        cursor.execute(query_data)
        data_id = cursor.fetchall()


        query_data2 = f"INSERT INTO contrasenas(id_usuario, contrasena) VALUES({data_id[0][0]}, '{password}')"
        cursor.execute(query_data2)
        cursor.close()
        conn.commit()
        conn.close()
        return True # devuelve true si se registro correctamente
    
    except errors.UniqueViolation:
        cursor.close()
        return False

# recuperar cuenta


def existencia_mail(value_line_edit_7):
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT mail FROM usuarios WHERE mail = '{value_line_edit_7}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if data != []: # verifica existencia de mail, si no hay no procede a la siguiente ventana de registro
        return True
    else:
        return False


def actualizar_contrasena(value_line_edit_5, email_guardado):
    conn = get_connection()
    cursor= conn.cursor()
    query_data = f"UPDATE contrasenas SET contrasena = '{value_line_edit_5}' WHERE id_usuario = (SELECT id_usuario FROM usuarios WHERE mail = '{email_guardado}')"
    cursor.execute(query_data)
    cursor.close()
    conn.commit()
    conn.close()
    return True # devuelve true si se registro correctamente

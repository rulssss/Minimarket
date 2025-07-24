import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../API')))
from datetime import datetime
import uuid
import hashlib
from supabase import create_client, Client


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

API_URL = "https://web-production-aa989.up.railway.app"

# variable global de usuario perfil

global id_usuario_perfil
id_usuario_perfil = None

# variable global de mapeo
global month_mapping
month_mapping = {
    "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
    "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
    "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
}
global day_mapping
# definir la variable day_mapping fuera de la función para que sea global y usarla en otras funciones
day_mapping = {
    "Domingo": 0, "Lunes": 1, "Martes": 2, "Miércoles": 3,
    "Jueves": 4, "Viernes": 5, "Sábado": 6
    
}


###########################################################################
###################### FUNCIONES DE INICIO DE SESION ######################
############################################################################

import random
import smtplib
from email.mime.text import MIMEText


# LOGIN

#funcion para verificar perfiles

def verificar_existencia_usuario_mail(email, uid):
    global id_usuario_perfil
    print("agregando usuario a supabase")

    # Convertir Firebase UID a UUID válido
    uid_limpio = uid.strip().strip('"').strip("'")
    firebase_bytes = uid_limpio.encode('utf-8')
    import hashlib
    hash_object = hashlib.md5(firebase_bytes)
    uuid_string = hash_object.hexdigest()
    formatted_uuid = f"{uuid_string[:8]}-{uuid_string[8:12]}-{uuid_string[12:16]}-{uuid_string[16:20]}-{uuid_string[20:32]}"

    try:
        # Verifica si existe el usuario en Supabase
        response = supabase.table("profiles").select("id").eq("email", email).execute()
        data = response.data
        if data:
            # Usuario ya existe
            id_usuario_perfil = str(data[0]["id"])
        else:
            # Insertar nuevo usuario con fecha/hora real
            from datetime import datetime
            insert_response = supabase.table("profiles").insert({
                "id": formatted_uuid,
                "email": email,
                "primer_inicio": datetime.now().isoformat()
            }).execute()
            # Buscar el UUID generado para asignarlo a la variable global
            response = supabase.table("profiles").select("id").eq("email", email).execute()
            data = response.data
            if data:
                id_usuario_perfil = str(data[0]["id"])
        return True
    except Exception as e:
        print(f"Error al verificar/agregar usuario en Supabase: {e}")
        return False



def verificar_contrasenia(tipo_usuario, usuario, contrasenia):
    global id_usuario_perfil

    # Buscar usuario y contraseña en Supabase
    response = supabase.table("usuarios") \
        .select("id_usuario, admin") \
        .eq("nombre", usuario) \
        .eq("u_id", id_usuario_perfil) \
        .execute()
    usuarios = response.data

    if not usuarios:
        return True  # No existe el usuario

    id_usuario = usuarios[0]["id_usuario"]
    admin = usuarios[0]["admin"]

    # Buscar contraseña en Supabase
    response_pw = supabase.table("contrasenas") \
        .select("contrasena") \
        .eq("id_usuario", id_usuario) \
        .eq("u_id", id_usuario_perfil) \
        .execute()
    pw_data = response_pw.data

    if tipo_usuario == "Administrador":
        account = True
    else:
        account = False

    if pw_data:
        if pw_data[0]["contrasena"] != contrasenia or admin != account:
            return True  # Contraseña incorrecta o tipo de cuenta incorrecto
        else:
            return False  # Todo OK
    else:
        return True  # No existe la contraseña
    

#REGISTRO

def hay_admin():
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("admin", True) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if not data:  # No hay administradores
            return False
        else:
            return True
    except Exception as e:
        print(f"Error al verificar administradores en Supabase: {e}")
        return False
    
def verificar_mail_existente(mail):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("mail") \
            .eq("mail", mail) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:  # Si hay resultados, el mail existe
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar mail en Supabase: {e}")
        return False



def verificar_usuario_existente(nombre_usuario):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("nombre") \
            .eq("nombre", nombre_usuario) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:  # Si hay resultados, el usuario existe
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar usuario en Supabase: {e}")
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
        print(f"Error al enviar correo de verificación: {e}")
        return None
    

def traer_administradores():
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("nombre") \
            .eq("admin", True) \
            .eq("u_id", id_usuario_perfil) \
            .order("id_usuario") \
            .execute()
        data = response.data
        if data:
            # Devuelve una lista con los nombres de los administradores
            return [admin["nombre"] for admin in data]
        else:
            return []
    except Exception as e:
        print(f"Error al traer administradores en Supabase: {e}")
        return []
    
def traer_mail_admin(administrador):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("mail") \
            .eq("nombre", administrador) \
            .eq("u_id", id_usuario_perfil) \
            .order("id_usuario") \
            .execute()
        data = response.data
        if data:
            return data[0]["mail"]  # Devuelve el mail del administrador
        else:
            return None
    except Exception as e:
        print(f"Error al traer mail del administrador en Supabase: {e}")
        return None
    

def registrar_usuario(username, password, account, mail):
    global id_usuario_perfil
    mail = mail.lower()

    if account == "Administrador":
        account = True
    else:
        account = False  # Acomoda la variable account a un true o false para verificar que tipo de cuenta es

    try:
        # Insertar el usuario en la tabla "usuarios"
        response = supabase.table("usuarios").insert({
            "nombre": username,
            "admin": account,
            "mail": mail,
            "u_id": id_usuario_perfil
        }).execute()

        # Obtener el id_usuario recién creado
        response_id = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("nombre", username) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data_id = response_id.data

        if not data_id:
            return False

        id_usuario = data_id[0]["id_usuario"]

        # Insertar la contraseña en la tabla "contrasenas"
        supabase.table("contrasenas").insert({
            "id_usuario": id_usuario,
            "contrasena": password,
            "u_id": id_usuario_perfil
        }).execute()

        return True  # Devuelve true si se registró correctamente

    except Exception as e:
        print(f"Error al registrar usuario en Supabase: {e}")
        return False

# recuperar cuenta



def existencia_mail(mail):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("mail") \
            .eq("mail", mail) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:  # Si hay resultados, el mail existe
            return True
        else:
            return False
    except Exception as e:
        print(f"Error al verificar existencia de mail en Supabase: {e}")
        return False

def actualizar_contrasena(nueva_contrasena, email_guardado):
    global id_usuario_perfil
    try:
        # Buscar el id_usuario por el mail y u_id
        response = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("mail", email_guardado) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if not data:
            return False  # No se encontró el usuario

        id_usuario = data[0]["id_usuario"]

        # Actualizar la contraseña en la tabla "contrasenas"
        supabase.table("contrasenas") \
            .update({"contrasena": nueva_contrasena}) \
            .eq("id_usuario", id_usuario) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        return True
    except Exception as e:
        print(f"Error al actualizar contraseña en Supabase: {e}")
        return False


###########################################################
############ funciones de minimarket ######################
###########################################################


def traer_categorias():
    global id_usuario_perfil
    try:
        response = supabase.table("categorias") \
            .select("id_categoria, nombre_descrip") \
            .eq("u_id", id_usuario_perfil) \
            .order("id_categoria") \
            .execute()
        data = response.data
        return [(cat["id_categoria"], cat["nombre_descrip"]) for cat in data] if data else []
    except Exception as e:
        print(f"Error al traer categorías en Supabase: {e}")
        return []

def crear_categuno():
    global id_usuario_perfil
    try:
        supabase.table("categorias").insert({
            "id_categoria": 1,
            "nombre_descrip": "Sin categoría",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al crear categoría en Supabase: {e}")
        return False
    

    
def crear_provuno():
    global id_usuario_perfil
    try:
        supabase.table("proveedores").insert({
            "id_proveedor": 1,
            "nombre_proveedor": "Proveedor1",
            "telefono": "123456789",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al crear proveedor en Supabase: {e}")
        return False


def cargar_producto(id_producto, nombre_producto, precio_compra_producto, precio_venta_producto, cantidad_producto, stock_ideal, categoria_producto, proveedor_producto):
    global id_usuario_perfil
    categoria_id = traer_id_categoria(categoria_producto)
    proveedor_id = traer_id_proveedor(proveedor_producto)
    try:
        supabase.table("productos").insert({
            "id_producto": id_producto,
            "nombre": nombre_producto,
            "precio_de_compra": precio_compra_producto,
            "precio_de_venta": precio_venta_producto,
            "stock": cantidad_producto,
            "stock_ideal": stock_ideal,
            "id_categoria": categoria_id,
            "id_proveedor": proveedor_id,
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al cargar producto en Supabase: {e}")
        return False

    
def traer_id_categoria(categoria_producto):
    global id_usuario_perfil
    try:
        response = supabase.table("categorias") \
            .select("id_categoria") \
            .eq("nombre_descrip", categoria_producto) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_categoria"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de categoría en Supabase: {e}")
        return None
    
def traer_id_proveedor(proveedor_producto):
    global id_usuario_perfil
    try:
        response = supabase.table("proveedores") \
            .select("id_proveedor") \
            .eq("nombre_proveedor", proveedor_producto) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_proveedor"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de proveedor en Supabase: {e}")
        return None
    

def traer_id_usuario(usuario):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("nombre", usuario) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_usuario"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de usuario en Supabase: {e}")
        return None
    
def traer_nom_producto(dato):
    global id_usuario_perfil
    try:
        response = supabase.table("productos") \
            .select("nombre") \
            .eq("id_producto", dato) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["nombre"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer nombre de producto en Supabase: {e}")
        return None
    
def buscar_producto(nombre_prod_o_id):
    global id_usuario_perfil
    try:
        # Buscar por ID de producto (si es dígito)
        if str(nombre_prod_o_id).isdigit():
            response = supabase.table("productos") \
                .select("id_producto") \
                .eq("id_producto", int(nombre_prod_o_id)) \
                .eq("u_id", id_usuario_perfil) \
                .execute()
            data = response.data
            if data:
                supabase.table("productos") \
                    .delete() \
                    .eq("id_producto", int(nombre_prod_o_id)) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                return True
            else:
                return False
        else:
            # Buscar por nombre de producto
            response = supabase.table("productos") \
                .select("nombre") \
                .eq("nombre", nombre_prod_o_id) \
                .eq("u_id", id_usuario_perfil) \
                .execute()
            data = response.data
            if data:
                supabase.table("productos") \
                    .delete() \
                    .eq("nombre", nombre_prod_o_id) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                return True
            else:
                return False
    except Exception as e:
        print(f"Error al buscar/borrar producto en Supabase: {e}")
        return False

        
def traer_id_producto(nombre):
    global id_usuario_perfil
    try:
        response = supabase.table("productos") \
            .select("id_producto") \
            .eq("nombre", nombre) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_producto"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de producto en Supabase: {e}")
        return None

def aumentar_precios_categoria(precio_compra, precio_venta, nombre):
    global id_usuario_perfil
    id_categoria = traer_id_categoria(nombre)
    try:
        # Obtener todos los productos de la categoría
        response = supabase.table("productos") \
            .select("id_producto, precio_de_compra, precio_de_venta") \
            .eq("id_categoria", id_categoria) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        productos = response.data

        for prod in productos:
            nuevo_precio_compra = prod["precio_de_compra"] * (1 + precio_compra / 100.0)
            nuevo_precio_venta = prod["precio_de_venta"] * (1 + precio_venta / 100.0)
            supabase.table("productos").update({
                "precio_de_compra": nuevo_precio_compra,
                "precio_de_venta": nuevo_precio_venta
            }).eq("id_producto", prod["id_producto"]).eq("u_id", id_usuario_perfil).execute()
        return True
    except Exception as e:
        print(f"Error al aumentar precios por categoría en Supabase: {e}")
        return False

def aumentar_precios_proveedor(precio_compra, precio_venta, nombre):
    """
    Aumenta los precios de compra y venta de todos los productos de un proveedor en un porcentaje dado.
    precio_compra y precio_venta pueden ser decimales (ej: 5.5 para 5,5%).
    nombre es el nombre del proveedor.
    """
    global id_usuario_perfil

    id_proveedor = traer_id_proveedor(nombre)
    try:
        # Obtener todos los productos del proveedor
        response = supabase.table("productos") \
            .select("id_producto, precio_de_compra, precio_de_venta") \
            .eq("id_proveedor", id_proveedor) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        productos = response.data

        for prod in productos:
            nuevo_precio_compra = prod["precio_de_compra"] * (1 + precio_compra / 100.0)
            nuevo_precio_venta = prod["precio_de_venta"] * (1 + precio_venta / 100.0)
            supabase.table("productos").update({
                "precio_de_compra": nuevo_precio_compra,
                "precio_de_venta": nuevo_precio_venta
            }).eq("id_producto", prod["id_producto"]).eq("u_id", id_usuario_perfil).execute()
        return True
    except Exception as e:
        print(f"Error al aumentar precios por proveedor en Supabase: {e}")
        return False

def traer_datosproducto_por_id(barcode):
    global id_usuario_perfil

    if not barcode:
        return False

    try:
        # Obtener el producto por id y u_id
        response = supabase.table("productos") \
            .select("id_producto, nombre, precio_de_compra, precio_de_venta, stock, stock_ideal, id_categoria, id_proveedor") \
            .eq("id_producto", barcode) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data

        if not data:
            return False

        producto = data[0]

        # Obtener nombre de la categoría
        categoria_nombre = None
        proveedor_nombre = None

        if producto.get("id_categoria"):
            cat_resp = supabase.table("categorias") \
                .select("nombre_descrip") \
                .eq("id_categoria", producto["id_categoria"]) \
                .eq("u_id", id_usuario_perfil) \
                .execute()
            cat_data = cat_resp.data
            if cat_data:
                categoria_nombre = cat_data[0]["nombre_descrip"]

        # Obtener nombre del proveedor
        if producto.get("id_proveedor"):
            prov_resp = supabase.table("proveedores") \
                .select("nombre_proveedor") \
                .eq("id_proveedor", producto["id_proveedor"]) \
                .eq("u_id", id_usuario_perfil) \
                .execute()
            prov_data = prov_resp.data
            if prov_data:
                proveedor_nombre = prov_data[0]["nombre_proveedor"]

        # Devuelve una tupla similar a la consulta SQL original
        return (
            producto["id_producto"],
            producto["nombre"],
            producto["precio_de_compra"],
            producto["precio_de_venta"],
            producto["stock"],
            producto["stock_ideal"],
            categoria_nombre,
            proveedor_nombre
        )
    except Exception as e:
        print(f"Error al traer datos de producto por id en Supabase: {e}")
        return False
    
def actualizar_producto(id, nombre_producto, precio_compra_producto, precio_venta_producto, stock, stock_ideal, categoria_producto, proveedor_producto):
    global id_usuario_perfil

    categoria_id = traer_id_categoria(categoria_producto)
    proveedor_id = traer_id_proveedor(proveedor_producto)
    try:
        supabase.table("productos").update({
            "nombre": nombre_producto,
            "precio_de_compra": precio_compra_producto,
            "precio_de_venta": precio_venta_producto,
            "stock": stock,
            "stock_ideal": stock_ideal,
            "id_categoria": categoria_id,
            "id_proveedor": proveedor_id
        }).eq("id_producto", id).eq("u_id", id_usuario_perfil).execute()
        return True
    except Exception as e:
        print(f"Error al actualizar producto en Supabase: {e}")
        return False

def cargar_proveedor(nombre_producto, num_telefono, mail):
    global id_usuario_perfil

    try:
        supabase.table("proveedores").insert({
            "nombre_proveedor": nombre_producto,
            "telefono": num_telefono,
            "mail": mail,
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al cargar proveedor en Supabase: {e}")
        return False

    
def buscar_proveedor(nombre_prov):
    global id_usuario_perfil
    if nombre_prov != "Proveedor1":
        try:
            supabase.table("proveedores") \
                .delete() \
                .eq("nombre_proveedor", nombre_prov) \
                .eq("u_id", id_usuario_perfil) \
                .execute()
            return True
        except Exception as e:
            print(f"Error al borrar proveedor en Supabase: {e}")
            return False
    return False

def actualizar_proveedor(nombre_proveedor, num_proveedor, mail_producto):
    global id_usuario_perfil
    try:
        supabase.table("proveedores").update({
            "telefono": num_proveedor,
            "mail": mail_producto
        }).eq("nombre_proveedor", nombre_proveedor).eq("u_id", id_usuario_perfil).execute()
        return True
    except Exception as e:
        print(f"Error al actualizar proveedor en Supabase: {e}")
        return False
    

# distinto de traeer proveedores ya que la enterior solo extrae sus nombres
def traer_proveedor():
    global id_usuario_perfil
    try:
        response = supabase.table("proveedores") \
            .select("nombre_proveedor, telefono, mail") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        # Devuelve una lista de tuplas como hacía fetchall()
        return [(prov["nombre_proveedor"], prov["telefono"], prov["mail"]) for prov in data] if data else []
    except Exception as e:
        print(f"Error al traer proveedores en Supabase: {e}")
        return []
    
def cargar_categoria(nombre_categoria):
    global id_usuario_perfil
    try:
        supabase.table("categorias").insert({
            "nombre_descrip": nombre_categoria,
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al cargar categoría en Supabase: {e}")
        return False

def buscar_categoria(nombre_cat):
    global id_usuario_perfil
    try:
        # Verificar si existe la categoría
        response = supabase.table("categorias") \
            .select("id_categoria") \
            .eq("nombre_descrip", nombre_cat) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data

        if data:
            id_categoria = data[0]["id_categoria"]
            try:
                # Intentar borrar la categoría
                supabase.table("categorias") \
                    .delete() \
                    .eq("id_categoria", id_categoria) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                return True
            except Exception as e:
                # Si hay error de ForeignKey, reasignar productos a "Sin categoría" (id_categoria=1) y volver a intentar
                supabase.table("productos") \
                    .update({"id_categoria": 1}) \
                    .eq("id_categoria", id_categoria) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                supabase.table("categorias") \
                    .delete() \
                    .eq("id_categoria", id_categoria) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                return True
        else:
            return False
    except Exception as e:
        print(f"Error al borrar categoría en Supabase: {e}")
        return False
    
def clear_data(borrar_categorias, borrar_ventas_compras, borrar_proveedores, borrar_usuarios, borrar_movimientos):
    global id_usuario_perfil

    v = True  # ventana_confirmacion()
    if v:
        # Borrar categorías (excepto la de id 1)
        if borrar_categorias:
            try:
                # Intentar borrar categorías distintas de 1
                supabase.table("categorias") \
                    .delete() \
                    .neq("id_categoria", 1) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
            except Exception as e:
                # Si hay error de ForeignKey, reasignar productos a "Sin categoría" y volver a intentar
                supabase.table("productos") \
                    .update({"id_categoria": 1}) \
                    .neq("id_categoria", 1) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
                supabase.table("categorias") \
                    .delete() \
                    .neq("id_categoria", 1) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()

        # Borrar ventas, compras y sus detalles
        if borrar_ventas_compras:
            supabase.table("ventas").delete().eq("u_id", id_usuario_perfil).execute()
            supabase.table("detalle_ventas").delete().eq("u_id", id_usuario_perfil).execute()
            supabase.table("compras").delete().eq("u_id", id_usuario_perfil).execute()
            supabase.table("detalle_compras").delete().eq("u_id", id_usuario_perfil).execute()

        # Borrar proveedores
        if borrar_proveedores:
            supabase.table("proveedores").delete().eq("u_id", id_usuario_perfil).execute()

        # Borrar usuarios y contraseñas y métodos de pago
        if borrar_usuarios:
            supabase.table("contrasenas").delete().eq("u_id", id_usuario_perfil).execute()
            supabase.table("usuarios").delete().eq("u_id", id_usuario_perfil).execute()
            supabase.table("metodos_pago").delete().eq("u_id", id_usuario_perfil).execute()

        # Borrar movimientos
        if borrar_movimientos:
            supabase.table("movimientos").delete().eq("u_id", id_usuario_perfil).execute()


def traer_todos_los_usuarios():
    global id_usuario_perfil
    try:
        # Obtener todos los usuarios del perfil
        response_usuarios = supabase.table("usuarios") \
            .select("id_usuario, nombre, mail, admin") \
            .eq("u_id", id_usuario_perfil) \
            .order("id_usuario") \
            .execute()
        usuarios = response_usuarios.data

        if not usuarios:
            return False

        # Obtener todas las contraseñas del perfil
        response_contrasenas = supabase.table("contrasenas") \
            .select("id_usuario, contrasena") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        contrasenas = response_contrasenas.data
        contrasenas_dict = {c["id_usuario"]: c["contrasena"] for c in contrasenas}

        # Unir usuarios y contraseñas por id_usuario
        resultado = []
        for u in usuarios:
            contrasena = contrasenas_dict.get(u["id_usuario"], None)
            resultado.append((
                u["id_usuario"],
                u["nombre"],
                u["mail"],
                u["admin"],
                contrasena
            ))

        return resultado if resultado else False
    except Exception as e:
        print(f"Error al traer todos los usuarios en Supabase: {e}")
        return False
    

def agregar_a_registro_usuario(tipo_usuario, nombre, contrasenia, mail):
    global id_usuario_perfil

    if tipo_usuario == "Administrador":
        tipo_usuario = True
    else:
        tipo_usuario = False  # Acomoda la variable account a un true o false

    try:
        # Insertar el usuario en la tabla "usuarios"
        supabase.table("usuarios").insert({
            "nombre": nombre,
            "admin": tipo_usuario,
            "mail": mail,
            "u_id": id_usuario_perfil
        }).execute()

        # Obtener el id_usuario recién creado
        response_id = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("nombre", nombre) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data_id = response_id.data

        if not data_id:
            return False

        id_usuario = data_id[0]["id_usuario"]

        # Insertar la contraseña en la tabla "contrasenas"
        supabase.table("contrasenas").insert({
            "id_usuario": id_usuario,
            "contrasena": contrasenia,
            "u_id": id_usuario_perfil
        }).execute()

        return True  # Devuelve true si se registró correctamente

    except Exception as e:
        print(f"Error al agregar usuario en Supabase: {e}")
        return False
    

def cargar_movimiento_agregar_usuario(nombre_usuario, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Agregar",
            "entidad_afectada": "Usuarios",
            "id_entidad": id_usuario,
            "descripcion": f"Usuario agregado: {nombre_usuario}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de usuario agregado en Supabase: {e}")
        return False
    

def actualizar_usuario(id, tipo_usuario, contrasenia, mail):
    global id_usuario_perfil

    if tipo_usuario == "Administrador":
        tipo_usuario = True
    else:
        tipo_usuario = False  # Acomoda la variable account a un true o false

    try:
        # Actualizar usuario en Supabase
        supabase.table("usuarios").update({
            "admin": tipo_usuario,
            "mail": mail
        }).eq("id_usuario", id).eq("u_id", id_usuario_perfil).execute()

        # Actualizar contraseña en Supabase
        supabase.table("contrasenas").update({
            "contrasena": contrasenia
        }).eq("id_usuario", id).eq("u_id", id_usuario_perfil).execute()

        return True  # Devuelve true si se actualizó correctamente
    except Exception as e:
        print(f"Error al actualizar usuario en Supabase: {e}")
        return False
    


def borrar_usuario(usuario):
    global id_usuario_perfil
    try:
        # Buscar el id del usuario por su nombre y perfil
        response = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("nombre", usuario) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data

        if data:
            id_usuario = data[0]["id_usuario"]

            # Borrar la contraseña asociada al id del usuario
            supabase.table("contrasenas") \
                .delete() \
                .eq("id_usuario", id_usuario) \
                .eq("u_id", id_usuario_perfil) \
                .execute()

            # Borrar el usuario por su id
            supabase.table("usuarios") \
                .delete() \
                .eq("id_usuario", id_usuario) \
                .eq("u_id", id_usuario_perfil) \
                .execute()

            return True  # Retorna True si se borró correctamente
        else:
            return False  # Retorna False si no se encontró el usuario
    except Exception as e:
        print(f"Error al borrar usuario en Supabase: {e}")
        return False
    
def traer_movimientos_por_usuario(usuario_seleccionado):
    global id_usuario_perfil
    try:
        # Obtener el id_usuario a partir del nombre
        response = supabase.table("usuarios") \
            .select("id_usuario") \
            .eq("nombre", usuario_seleccionado) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        usuarios = response.data
        if not usuarios:
            return []

        id_usuario = usuarios[0]["id_usuario"]

        # Obtener los movimientos de ese usuario
        response_mov = supabase.table("movimientos") \
            .select("id_usuario, fecha_hora, tipo_accion, entidad_afectada, descripcion") \
            .eq("id_usuario", id_usuario) \
            .eq("u_id", id_usuario_perfil) \
            .order("fecha_hora", desc=True) \
            .execute()
        movimientos = response_mov.data

        # Devuelve una lista de tuplas como hacía fetchall()
        return [
            (
                mov["id_usuario"],
                mov["fecha_hora"],
                mov["tipo_accion"],
                mov["entidad_afectada"],
                mov["descripcion"]
            ) for mov in movimientos
        ] if movimientos else []
    except Exception as e:
        print(f"Error al traer movimientos por usuario en Supabase: {e}")
        return []
    
def traer_movimientos_por_fecha(fecha_seleccionada):
    global id_usuario_perfil
    try:
        # Obtener todos los movimientos de la fecha seleccionada y perfil
        response = supabase.table("movimientos") \
            .select("id_usuario, fecha_hora, tipo_accion, entidad_afectada, descripcion") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        movimientos = response.data

        # Filtrar por fecha (YYYY-MM-DD) en Python, ya que Supabase no soporta DATE() directamente
        movimientos_filtrados = [
            (
                mov["id_usuario"],
                mov["fecha_hora"],
                mov["tipo_accion"],
                mov["entidad_afectada"],
                mov["descripcion"]
            )
            for mov in movimientos
            if mov["fecha_hora"].startswith(str(fecha_seleccionada))
        ]

        # Ordenar por fecha_hora descendente
        movimientos_filtrados.sort(key=lambda x: x[1], reverse=True)

        return movimientos_filtrados
    except Exception as e:
        print(f"Error al traer movimientos por fecha en Supabase: {e}")
        return []
    
def traer_movimientos_por_accion(accion_seleccionada):
    global id_usuario_perfil
    try:
        # Obtener todos los movimientos con la acción seleccionada y perfil
        response = supabase.table("movimientos") \
            .select("id_usuario, fecha_hora, tipo_accion, entidad_afectada, descripcion") \
            .eq("tipo_accion", accion_seleccionada) \
            .eq("u_id", id_usuario_perfil) \
            .order("fecha_hora", desc=True) \
            .execute()
        movimientos = response.data

        # Devuelve una lista de tuplas como hacía fetchall()
        return [
            (
                mov["id_usuario"],
                mov["fecha_hora"],
                mov["tipo_accion"],
                mov["entidad_afectada"],
                mov["descripcion"]
            ) for mov in movimientos
        ] if movimientos else []
    except Exception as e:
        print(f"Error al traer movimientos por acción en Supabase: {e}")
        return []
    
def traer_metodo_pago_id(valor):
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("id_mp") \
            .eq("nombre_mp", valor) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_mp"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de método de pago en Supabase: {e}")
        return None
    

def traer_todos_metodos_pago():
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("id_mp, nombre_mp") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        metodos = response.data
        # Devuelve una lista de tuplas como hacía fetchall()
        return [(m["id_mp"], m["nombre_mp"]) for m in metodos] if metodos else []
    except Exception as e:
        print(f"Error al obtener métodos de pago en Supabase: {e}")
        return []
    
    


def traer_datos_ventas_metodo_o_usuario(id, fecha):
    global id_usuario_perfil

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, id_usuario, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha si corresponde
        ventas_filtradas = []
        if fecha and "-" in fecha:
            partes = fecha.split("-")
            anio = partes[0]
            mes = partes[1] if len(partes) > 1 else None
            dia = partes[2] if len(partes) > 2 else None

            for v in ventas:
                fecha_v = v["fecha_hora"]
                if (
                    fecha_v.startswith(anio)
                    and (not mes or fecha_v[5:7] == mes.zfill(2))
                    and (not dia or fecha_v[8:10] == dia.zfill(2))
                ):
                    ventas_filtradas.append(v)
        elif fecha:
            # Solo año
            for v in ventas:
                if v["fecha_hora"].startswith(str(fecha)):
                    ventas_filtradas.append(v)
        else:
            ventas_filtradas = ventas

        # Filtrar por usuario o método de pago
        ventas_filtradas = [
            v for v in ventas_filtradas
            if v["id_usuario"] == id or v["id_metodo_pago"] == id
        ]

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, id_producto, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Unir ventas y detalles
        resultados = []
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    resultados.append((
                        v["id_usuario"],
                        v["fecha_hora"],
                        v["id_metodo_pago"],
                        d["id_producto"],
                        d["cantidad"],
                        d["precio_unitario_venta"]
                    ))

        return resultados
    except Exception as e:
        print(f"Error al traer datos de ventas por método o usuario en Supabase: {e}")
        return []
    

def traer_datos_compras_metodo_o_usuario(id, fecha):
    global id_usuario_perfil

    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, id_usuario, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por fecha si corresponde
        compras_filtradas = []
        if fecha and "-" in fecha:
            partes = fecha.split("-")
            anio = partes[0]
            mes = partes[1] if len(partes) > 1 else None
            dia = partes[2] if len(partes) > 2 else None

            for c in compras:
                fecha_c = c["fecha_hora"]
                if (
                    fecha_c.startswith(anio)
                    and (not mes or fecha_c[5:7] == mes.zfill(2))
                    and (not dia or fecha_c[8:10] == dia.zfill(2))
                ):
                    compras_filtradas.append(c)
        elif fecha:
            # Solo año
            for c in compras:
                if c["fecha_hora"].startswith(str(fecha)):
                    compras_filtradas.append(c)
        else:
            compras_filtradas = compras

        # Filtrar por usuario o método de pago
        compras_filtradas = [
            c for c in compras_filtradas
            if c["id_usuario"] == id or c["id_metodo_pago"] == id
        ]

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, id_producto, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Unir compras y detalles
        resultados = []
        for c in compras_filtradas:
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    resultados.append((
                        c["id_usuario"],
                        c["fecha_hora"],
                        c["id_metodo_pago"],
                        d["id_producto"],
                        d["cantidad"],
                        d["precio_unitario"]
                    ))

        return resultados
    except Exception as e:
        print(f"Error al traer datos de compras por método o usuario en Supabase: {e}")
        return []
    


def traer_metodo_pago(metodo):  # traer el nombre del método de pago a través del id
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("nombre_mp") \
            .eq("id_mp", metodo) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["nombre_mp"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer nombre de método de pago en Supabase: {e}")
        return None
    

def traer_datos_arqueo_ventas_fecha(fecha):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, id_usuario, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha si corresponde
        ventas_filtradas = []
        if fecha and "-" in fecha:
            partes = fecha.split("-")
            anio = partes[0]
            mes = partes[1] if len(partes) > 1 else None
            dia = partes[2] if len(partes) > 2 else None

            for v in ventas:
                fecha_v = v["fecha_hora"]
                if (
                    fecha_v.startswith(anio)
                    and (not mes or fecha_v[5:7] == mes.zfill(2))
                    and (not dia or fecha_v[8:10] == dia.zfill(2))
                ):
                    ventas_filtradas.append(v)
        elif fecha:
            # Solo año
            for v in ventas:
                if v["fecha_hora"].startswith(str(fecha)):
                    ventas_filtradas.append(v)
        else:
            ventas_filtradas = ventas

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, id_producto, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Unir ventas y detalles
        resultados = []
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    resultados.append((
                        v["id_usuario"],
                        v["fecha_hora"],
                        v["id_metodo_pago"],
                        d["id_producto"],
                        d["cantidad"],
                        d["precio_unitario_venta"]
                    ))

        return resultados
    except Exception as e:
        print(f"Error al traer datos de arqueo de ventas por fecha en Supabase: {e}")
        return []
    

def traer_datos_arqueo_compras_fecha(fecha):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, id_usuario, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por fecha si corresponde
        compras_filtradas = []
        if fecha and "-" in fecha:
            partes = fecha.split("-")
            anio = partes[0]
            mes = partes[1] if len(partes) > 1 else None
            dia = partes[2] if len(partes) > 2 else None

            for c in compras:
                fecha_c = c["fecha_hora"]
                if (
                    fecha_c.startswith(anio)
                    and (not mes or fecha_c[5:7] == mes.zfill(2))
                    and (not dia or fecha_c[8:10] == dia.zfill(2))
                ):
                    compras_filtradas.append(c)
        elif fecha:
            # Solo año
            for c in compras:
                if c["fecha_hora"].startswith(str(fecha)):
                    compras_filtradas.append(c)
        else:
            compras_filtradas = compras

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, id_producto, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Unir compras y detalles
        resultados = []
        for c in compras_filtradas:
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    resultados.append((
                        c["id_usuario"],
                        c["fecha_hora"],
                        c["id_metodo_pago"],
                        d["id_producto"],
                        d["cantidad"],
                        d["precio_unitario"]
                    ))

        return resultados
    except Exception as e:
        print(f"Error al traer datos de arqueo de compras por fecha en Supabase: {e}")
        return []
    


def traer_metodos_de_pago():  # trae todos los métodos de pago de la base de datos
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("nombre_mp") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        # Devuelve una lista de tuplas como hacía fetchall()
        return [(row["nombre_mp"],) for row in data] if data else []
    except Exception as e:
        print(f"Error al traer métodos de pago en Supabase: {e}")
        return []
    
def traer_ventas_totales_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha (YYYY-MM-DD)
        ventas_filtradas = [
            v for v in ventas if v["fecha_hora"].startswith(str(fecha_selecc))
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas del día
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ventas totales del día en Supabase: {e}")
        return 0
    

def traer_ganancias_totales_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha (YYYY-MM-DD)
        ventas_filtradas = [
            v for v in ventas if v["fecha_hora"].startswith(str(fecha_selecc))
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias del día
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias totales del día en Supabase: {e}")
        return 0
    
def traer_compras_totales_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por fecha (YYYY-MM-DD)
        compras_filtradas = [
            c for c in compras if c["fecha_hora"].startswith(str(fecha_selecc))
        ]

        if not compras_filtradas:
            return 0

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de compras del día
        total = 0
        for c in compras_filtradas:
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    total += d["precio_unitario"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer compras totales del día en Supabase: {e}")
        return 0
    
def traer_numero_de_compras_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por fecha (YYYY-MM-DD)
        compras_filtradas = [
            c for c in compras if c["fecha_hora"].startswith(str(fecha_selecc))
        ]

        return len(compras_filtradas)
    except Exception as e:
        print(f"Error al traer número de compras del día en Supabase: {e}")
        return 0
    
def traer_compras_totales_mes(anio, mes):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por año y mes en Python
        compras_filtradas = [
            c for c in compras
            if c["fecha_hora"].startswith(f"{anio}-{str(mes).zfill(2)}")
        ]

        if not compras_filtradas:
            return 0

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de compras del mes
        total = 0
        for c in compras_filtradas:
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    total += d["precio_unitario"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer compras totales del mes en Supabase: {e}")
        return 0
    
def traer_numero_de_compras_mes(anio, mes):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por año y mes en Python
        compras_filtradas = [
            c for c in compras
            if c["fecha_hora"].startswith(f"{anio}-{str(mes).zfill(2)}")
        ]

        return len(compras_filtradas)
    except Exception as e:
        print(f"Error al traer número de compras del mes en Supabase: {e}")
        return 0
    
def traer_compras_totales_ano_actual(anio):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por año en Python
        compras_filtradas = [
            c for c in compras
            if c["fecha_hora"].startswith(f"{anio}-")
        ]

        if not compras_filtradas:
            return 0

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de compras del año
        total = 0
        for c in compras_filtradas:
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    total += d["precio_unitario"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer compras totales del año en Supabase: {e}")
        return 0
    
def traer_numero_de_compras_ano_actual(anio):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por año en Python
        compras_filtradas = [
            c for c in compras
            if c["fecha_hora"].startswith(f"{anio}-")
        ]

        return len(compras_filtradas)
    except Exception as e:
        print(f"Error al traer número de compras del año en Supabase: {e}")
        return 0
    
def traer_ventas_por_metodo_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, id_metodo_pago, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha (YYYY-MM-DD)
        ventas_filtradas = [
            v for v in ventas if v["fecha_hora"].startswith(str(fecha_selecc))
        ]

        if not ventas_filtradas:
            return {}

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar por método de pago
        resultados = {}
        for v in ventas_filtradas:
            id_metodo = v["id_metodo_pago"]
            total = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]
            if id_metodo in resultados:
                resultados[id_metodo] += total
            else:
                resultados[id_metodo] = total

        return resultados
    except Exception as e:
        print(f"Error al traer ventas por método del día en Supabase: {e}")
        return {}
    

def traer_compras_por_metodo_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, id_metodo_pago, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por fecha (YYYY-MM-DD)
        compras_filtradas = [
            c for c in compras if c["fecha_hora"].startswith(str(fecha_selecc))
        ]

        if not compras_filtradas:
            return {}

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar por método de pago
        resultados = {}
        for c in compras_filtradas:
            id_metodo = c["id_metodo_pago"]
            total = 0
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    total += d["precio_unitario"] * d["cantidad"]
            if id_metodo in resultados:
                resultados[id_metodo] += total
            else:
                resultados[id_metodo] = total

        return resultados
    except Exception as e:
        print(f"Error al traer compras por método del día en Supabase: {e}")
        return {}
    

def traer_ventas_por_metodo_mes(anio, mes):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, id_metodo_pago, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y mes en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{anio}-{str(mes).zfill(2)}")
        ]

        if not ventas_filtradas:
            return {}

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar por método de pago
        resultados = {}
        for v in ventas_filtradas:
            id_metodo = v["id_metodo_pago"]
            total = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]
            if id_metodo in resultados:
                resultados[id_metodo] += total
            else:
                resultados[id_metodo] = total

        return resultados
    except Exception as e:
        print(f"Error al traer ventas por método del mes en Supabase: {e}")
        return {}
    
def traer_compras_por_metodo_mes(anio, mes):
    global id_usuario_perfil
    try:
        # Obtener todas las compras del perfil
        response_compras = supabase.table("compras") \
            .select("id_compra, id_metodo_pago, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        compras = response_compras.data

        # Filtrar compras por año y mes en Python
        compras_filtradas = [
            c for c in compras
            if c["fecha_hora"].startswith(f"{anio}-{str(mes).zfill(2)}")
        ]

        if not compras_filtradas:
            return {}

        # Obtener todos los detalles de compras del perfil
        response_detalles = supabase.table("detalle_compras") \
            .select("id_compra, cantidad, precio_unitario") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar por método de pago
        resultados = {}
        for c in compras_filtradas:
            id_metodo = c["id_metodo_pago"]
            total = 0
            for d in detalles:
                if d["id_compra"] == c["id_compra"]:
                    total += d["precio_unitario"] * d["cantidad"]
            if id_metodo in resultados:
                resultados[id_metodo] += total
            else:
                resultados[id_metodo] = total

        return resultados
    except Exception as e:
        print(f"Error al traer compras por método del mes en Supabase: {e}")
        return {}
    


def traer_ventas_por_metodo_ano(anio):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, id_metodo_pago, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{anio}-")
        ]

        if not ventas_filtradas:
            return {}

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar por método de pago
        resultados = {}
        for v in ventas_filtradas:
            id_metodo = v["id_metodo_pago"]
            total = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]
            if id_metodo in resultados:
                resultados[id_metodo] += total
            else:
                resultados[id_metodo] = total

        return resultados
    except Exception as e:
        print(f"Error al traer ventas por método del año en Supabase: {e}")
        return {}
    


def traer_numero_de_ventas_ano(anio):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{anio}-")
        ]

        return len(ventas_filtradas)
    except Exception as e:
        print(f"Error al traer número de ventas del año en Supabase: {e}")
        return 0
    
def traer_numero_de_ventas_mes(anio, mes):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y mes en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{anio}-{str(mes).zfill(2)}")
        ]

        return len(ventas_filtradas)
    except Exception as e:
        print(f"Error al traer número de ventas del mes en Supabase: {e}")
        return 0
    
def traer_numero_de_ventas_dia(fecha_selecc):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por fecha (YYYY-MM-DD)
        ventas_filtradas = [
            v for v in ventas if v["fecha_hora"].startswith(str(fecha_selecc))
        ]

        return len(ventas_filtradas)
    except Exception as e:
        print(f"Error al traer número de ventas del día en Supabase: {e}")
        return 0
    
def traer_ventas_totales_ano_actual(ano_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas del año
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ventas totales del año en Supabase: {e}")
        return 0
    
def traer_ganancias_totales_ano_actual(ano_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias del año
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias totales del año en Supabase: {e}")
        return 0
    
def traer_ganancias_totales_mes(ano_actual, mes_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y mes en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_actual).zfill(2)}")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias del mes
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias totales del mes en Supabase: {e}")
        return 0
    
def traer_ventas_totales_mes(ano_actual, mes_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y mes en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_actual).zfill(2)}")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas del mes
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ventas totales del mes en Supabase: {e}")
        return 0
    
    
def traer_venta_promedio_ano_actual(ano_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Calcular el promedio de ventas del año actual
        totales = []
        for v in ventas_filtradas:
            total_venta = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total_venta += d["precio_unitario_venta"] * d["cantidad"]
            if total_venta > 0:
                totales.append(total_venta)

        if not totales:
            return 0

        return sum(totales) / len(totales)
    except Exception as e:
        print(f"Error al traer el promedio de ventas del año en Supabase: {e}")
        return 0
    
def traer_ventas_ano_actual(ano_actual, meses):
    global id_usuario_perfil
    global month_mapping

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        ventas_por_mes = []
        for mes in meses:
            mes_numero = month_mapping.get(mes, mes)
            # Filtrar ventas por año y mes
            ventas_filtradas = [
                v for v in ventas
                if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_numero).zfill(2)}")
            ]
            # Sumar el total de ventas del mes
            total = 0
            for v in ventas_filtradas:
                for d in detalles:
                    if d["id_venta"] == v["id_venta"]:
                        total += d["precio_unitario_venta"] * d["cantidad"]
            ventas_por_mes.append(total)
        return ventas_por_mes
    except Exception as e:
        print(f"Error al traer ventas del año actual en Supabase: {e}")
        return [0 for _ in meses]
    
def traer_ganancias_ano_actual(ano_actual, meses):
    global id_usuario_perfil
    global month_mapping

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        ganancias_por_mes = []
        for mes in meses:
            mes_numero = month_mapping.get(mes, mes)
            # Filtrar ventas por año y mes
            ventas_filtradas = [
                v for v in ventas
                if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_numero).zfill(2)}")
            ]
            # Sumar el total de ganancias del mes
            total = 0
            for v in ventas_filtradas:
                for d in detalles:
                    if d["id_venta"] == v["id_venta"]:
                        total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]
            ganancias_por_mes.append(total)
        return ganancias_por_mes
    except Exception as e:
        print(f"Error al traer ganancias del año actual en Supabase: {e}")
        return [0 for _ in meses]
    
def traer_metodos_pago_y_su_id():  # trae todos los métodos de pago de la base de datos
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("*") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        # Devuelve una lista de tuplas como hacía fetchall()
        if data:
            # Ordenar las claves para mantener el orden de columnas similar a fetchall()
            keys = list(data[0].keys())
            return [tuple(row[k] for k in keys) for row in data]
        else:
            return []
    except Exception as e:
        print(f"Error al traer métodos de pago y su id en Supabase: {e}")
        return []
    

def traer_datos_por_metodo_y_mes(ano_actual, metodo, meses):
    global id_usuario_perfil
    global month_mapping

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .eq("id_metodo_pago", metodo) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        datos_por_mes = []
        for mes in meses:
            mes_numero = month_mapping.get(mes, mes)
            # Filtrar ventas por año y mes y método de pago
            ventas_filtradas = [
                v for v in ventas
                if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_numero).zfill(2)}")
            ]
            # Sumar el total de ventas del mes para ese método
            total = 0
            for v in ventas_filtradas:
                for d in detalles:
                    if d["id_venta"] == v["id_venta"]:
                        total += d["precio_unitario_venta"] * d["cantidad"]
            datos_por_mes.append(total)
        return datos_por_mes
    except Exception as e:
        print(f"Error al traer datos por método y mes en Supabase: {e}")
        return [0 for _ in meses]
    
def traer_venta_promedio_mes(ano_actual, mes_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y mes en Python
        ventas_filtradas = [
            v for v in ventas
            if v["fecha_hora"].startswith(f"{ano_actual}-{str(mes_actual).zfill(2)}")
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Calcular el promedio de ventas del mes actual
        totales = []
        for v in ventas_filtradas:
            total_venta = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total_venta += d["precio_unitario_venta"] * d["cantidad"]
            if total_venta > 0:
                totales.append(total_venta)

        if not totales:
            return 0

        return sum(totales) / len(totales)
    except Exception as e:
        print(f"Error al traer el promedio de ventas del mes en Supabase: {e}")
        return 0
    
def traer_numero_de_ventas_semana(ano_actual, semana_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y semana en Python
        from datetime import datetime
        ventas_filtradas = []
        for v in ventas:
            try:
                fecha = datetime.fromisoformat(v["fecha_hora"])
                if fecha.isocalendar()[0] == int(ano_actual) and fecha.isocalendar()[1] == int(semana_actual):
                    ventas_filtradas.append(v)
            except Exception:
                continue

        return len(ventas_filtradas)
    except Exception as e:
        print(f"Error al traer número de ventas de la semana en Supabase: {e}")
        return 0
    
def traer_venta_promedio_semana(ano_actual, semana_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y semana en Python
        from datetime import datetime
        ventas_filtradas = []
        for v in ventas:
            try:
                fecha = datetime.fromisoformat(v["fecha_hora"])
                if fecha.isocalendar()[0] == int(ano_actual) and fecha.isocalendar()[1] == int(semana_actual):
                    ventas_filtradas.append(v)
            except Exception:
                continue

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Calcular el promedio de ventas de la semana actual
        totales = []
        for v in ventas_filtradas:
            total_venta = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total_venta += d["precio_unitario_venta"] * d["cantidad"]
            if total_venta > 0:
                totales.append(total_venta)

        if not totales:
            return 0

        return sum(totales) / len(totales)
    except Exception as e:
        print(f"Error al traer el promedio de ventas de la semana en Supabase: {e}")
        return 0
    
def traer_ganancias_totales_semana(ano_actual, semana_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y semana en Python
        from datetime import datetime
        ventas_filtradas = []
        for v in ventas:
            try:
                fecha = datetime.fromisoformat(v["fecha_hora"])
                if fecha.isocalendar()[0] == int(ano_actual) and fecha.isocalendar()[1] == int(semana_actual):
                    ventas_filtradas.append(v)
            except Exception:
                continue

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias de la semana
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias totales de la semana en Supabase: {e}")
        return 0
    
def traer_ventas_semana_actual(ano_actual, semana_actual, dias_semana):
    global id_usuario_perfil
    global day_mapping

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        from datetime import datetime
        ventas_por_dia = []
        for dia in dias_semana:
            dia_numero = day_mapping.get(dia, dia)  # Map day name to number (0=domingo,...,6=sábado)
            total = 0
            for v in ventas:
                try:
                    fecha = datetime.fromisoformat(v["fecha_hora"])
                    if (
                        fecha.isocalendar()[0] == int(ano_actual)
                        and fecha.isocalendar()[1] == int(semana_actual)
                        and fecha.weekday() == (dia_numero - 1 if dia_numero > 0 else 6)
                    ):
                        for d in detalles:
                            if d["id_venta"] == v["id_venta"]:
                                total += d["precio_unitario_venta"] * d["cantidad"]
                except Exception:
                    continue
            ventas_por_dia.append(total)
        return ventas_por_dia
    except Exception as e:
        print(f"Error al traer ventas de la semana actual en Supabase: {e}")
        return [0 for _ in dias_semana]
    
def traer_ganancias_semana_actual(ano_actual, semana_actual, dias_semana):
    global id_usuario_perfil
    global day_mapping

    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        from datetime import datetime
        ganancias_por_dia = []
        for dia in dias_semana:
            dia_numero = day_mapping.get(dia, dia)  # 0=domingo,...,6=sábado
            total = 0
            for v in ventas:
                try:
                    fecha = datetime.fromisoformat(v["fecha_hora"])
                    if (
                        fecha.isocalendar()[0] == int(ano_actual)
                        and fecha.isocalendar()[1] == int(semana_actual)
                        and fecha.weekday() == (dia_numero - 1 if dia_numero > 0 else 6)
                    ):
                        for d in detalles:
                            if d["id_venta"] == v["id_venta"]:
                                total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]
                except Exception:
                    continue
            ganancias_por_dia.append(total)
        return ganancias_por_dia
    except Exception as e:
        print(f"Error al traer ganancias de la semana actual en Supabase: {e}")
        return [0 for _ in dias_semana]
    
def traer_datos_por_metodo_y_dia_semana(ano_actual, semana_actual, id_metodo, dias_semana):
    global id_usuario_perfil
    global day_mapping

    try:
        # Obtener todas las ventas del perfil con el método de pago seleccionado
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .eq("id_metodo_pago", id_metodo) \
            .execute()
        ventas = response_ventas.data

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        from datetime import datetime
        datos_por_dia = []
        for dia in dias_semana:
            dia_numero = day_mapping.get(dia, dia)  # 0=domingo,...,6=sábado
            total = 0
            for v in ventas:
                try:
                    fecha = datetime.fromisoformat(v["fecha_hora"])
                    # Python: weekday() 0=lunes,...,6=domingo; PostgreSQL DOW: 0=domingo,...,6=sábado
                    if (
                        fecha.isocalendar()[0] == int(ano_actual)
                        and fecha.isocalendar()[1] == int(semana_actual)
                        and fecha.weekday() == (dia_numero - 1 if dia_numero > 0 else 6)
                    ):
                        for d in detalles:
                            if d["id_venta"] == v["id_venta"]:
                                total += d["precio_unitario_venta"] * d["cantidad"]
                except Exception:
                    continue
            datos_por_dia.append(total)
        return datos_por_dia
    except Exception as e:
        print(f"Error al traer datos por método y día de semana en Supabase: {e}")
        return [0 for _ in dias_semana]
    
def traer_ventas_totales_semana(ano_actual, semana_actual):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por año y semana en Python
        from datetime import datetime
        ventas_filtradas = []
        for v in ventas:
            try:
                fecha = datetime.fromisoformat(v["fecha_hora"])
                if fecha.isocalendar()[0] == int(ano_actual) and fecha.isocalendar()[1] == int(semana_actual):
                    ventas_filtradas.append(v)
            except Exception:
                continue

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas de la semana
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ventas totales de la semana en Supabase: {e}")
        return 0
    
def traer_ventas_totales_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas del periodo
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ventas totales del periodo en Supabase: {e}")
        return 0
    
def traer_numero_de_ventas_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        return len(ventas_filtradas)
    except Exception as e:
        print(f"Error al traer número de ventas del periodo en Supabase: {e}")
        return 0
    
def traer_venta_promedio_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Calcular el promedio de ventas del periodo seleccionado
        totales = []
        for v in ventas_filtradas:
            total_venta = 0
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total_venta += d["precio_unitario_venta"] * d["cantidad"]
            if total_venta > 0:
                totales.append(total_venta)

        if not totales:
            return 0

        return sum(totales) / len(totales)
    except Exception as e:
        print(f"Error al traer el promedio de ventas del periodo en Supabase: {e}")
        return 0
    

def traer_ganancias_totales_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias del periodo
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias totales del periodo en Supabase: {e}")
        return 0
    
def traer_ventas_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return []

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Agrupar y sumar ventas por día
        from collections import defaultdict
        ventas_por_dia = defaultdict(float)
        for v in ventas_filtradas:
            dia = v["fecha_hora"][:10]  # YYYY-MM-DD
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    ventas_por_dia[dia] += d["precio_unitario_venta"] * d["cantidad"]

        # Ordenar por fecha y devolver solo los totales
        return [ventas_por_dia[dia] for dia in sorted(ventas_por_dia.keys())]
    except Exception as e:
        print(f"Error al traer ventas por periodo en Supabase: {e}")
        return []
    
def traer_ganancias_periodo(periodo1, periodo2):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil en el rango de fechas
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta, precio_unitario_compra") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ganancias del periodo
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += (d["precio_unitario_venta"] - d["precio_unitario_compra"]) * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer ganancias del periodo en Supabase: {e}")
        return 0
    
def traer_datos_por_metodo_y_dia_periodo(periodo1, periodo2, id_metodo):
    global id_usuario_perfil
    try:
        # Obtener todas las ventas del perfil con el método de pago seleccionado
        response_ventas = supabase.table("ventas") \
            .select("id_venta, fecha_hora, id_metodo_pago") \
            .eq("u_id", id_usuario_perfil) \
            .eq("id_metodo_pago", id_metodo) \
            .execute()
        ventas = response_ventas.data

        # Filtrar ventas por rango de fechas
        ventas_filtradas = [
            v for v in ventas
            if periodo1 <= v["fecha_hora"] <= periodo2
        ]

        if not ventas_filtradas:
            return 0

        # Obtener todos los detalles de ventas del perfil
        response_detalles = supabase.table("detalle_ventas") \
            .select("id_venta, cantidad, precio_unitario_venta") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        detalles = response_detalles.data

        # Sumar el total de ventas del periodo para ese método
        total = 0
        for v in ventas_filtradas:
            for d in detalles:
                if d["id_venta"] == v["id_venta"]:
                    total += d["precio_unitario_venta"] * d["cantidad"]

        return total
    except Exception as e:
        print(f"Error al traer datos por método y día del periodo en Supabase: {e}")
        return 0
    

def verificar_existencia_de_mp():
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("id_mp") \
            .eq("u_id", id_usuario_perfil) \
            .limit(1) \
            .execute()
        data = response.data
        return bool(data)
    except Exception as e:
        print(f"Error al verificar existencia de métodos de pago en Supabase: {e}")
        return False
    
def agregar_mp_default():
    global id_usuario_perfil
    try:
        # Insertar métodos de pago por defecto en Supabase
        metodos = ['Efectivo', 'Transferencia', 'Tarjeta de Crédito', 'Tarjeta de Débito']
        for metodo in metodos:
            supabase.table("metodos_pago").insert({
                "nombre_mp": metodo,
                "u_id": id_usuario_perfil
            }).execute()
        return True
    except Exception as e:
        print(f"Error al agregar métodos de pago por defecto en Supabase: {e}")
        return False
    

def agregar_mp_db(lineEdit_value):
    global id_usuario_perfil
    try:
        # Insertar método de pago en Supabase
        supabase.table("metodos_pago").insert({
            "nombre_mp": lineEdit_value,
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        # Si el error es por duplicado, retorna False
        if "duplicate" in str(e).lower() or "unique" in str(e).lower():
            return False
        print(f"Error al agregar método de pago en Supabase: {e}")
        return False
    
    
def borrar_mp_db(combobox_value):
    global id_usuario_perfil
    try:
        # Borrar método de pago en Supabase
        supabase.table("metodos_pago") \
            .delete() \
            .eq("nombre_mp", combobox_value) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        return True
    except Exception as e:
        print(f"Error al borrar método de pago en Supabase: {e}")
        return False
    

def actualizar_cantidad_productos(producto_modificado, m, s):
    global id_usuario_perfil

    # s controla si es una venta o una compra (True=venta, False=compra)
    # m controla si son varios productos (True) o solo uno (False)
    try:
        if m:
            for producto in producto_modificado:
                nombre = producto[0]
                cantidad = float(producto[2])
                nuevo_stock = {"stock": supabase.rpc(
                    "stock_update",
                    {
                        "nombre_producto": nombre,
                        "cantidad": -cantidad if s else cantidad,
                        "u_id": id_usuario_perfil
                    }
                )}
                # Si no tienes una función RPC, usa update:
                supabase.table("productos").update({
                    "stock": supabase.table("productos")
                        .select("stock")
                        .eq("nombre", nombre)
                        .eq("u_id", id_usuario_perfil)
                        .execute().data[0]["stock"] + (-cantidad if s else cantidad)
                }).eq("nombre", nombre).eq("u_id", id_usuario_perfil).execute()
        else:
            nombre = producto_modificado[0][0]
            cantidad = float(producto_modificado[0][2])
            supabase.table("productos").update({
                "stock": supabase.table("productos")
                    .select("stock")
                    .eq("nombre", nombre)
                    .eq("u_id", id_usuario_perfil)
                    .execute().data[0]["stock"] + (-cantidad if s else cantidad)
            }).eq("nombre", nombre).eq("u_id", id_usuario_perfil).execute()
        return True
    except Exception as e:
        print(f"Error al actualizar cantidad de productos en Supabase: {e}")
        return False
    

def agregar_a_registro(productos_seleccionados, s, usuario):
    global id_usuario_perfil

    # s define si es una venta o una compra, si es true es una venta y si es false es una compra

    try:
        id_usuario = traer_id_usuario(usuario)

        for producto in productos_seleccionados:
            nombre = producto[0]  # Nombre del producto
            precio_compra = traer_precio_compra(nombre)
            precio = float(producto[1])  # precio del producto
            cantidad = float(producto[2])  # Cantidad del producto
            fecha_hora = datetime.now().isoformat()
            metodo_pago_nombre = producto[5]
            metodo_pago = traer_mp(metodo_pago_nombre)

            if s:
                # Venta
                # Insertar venta
                response_venta = supabase.table("ventas").insert({
                    "fecha_hora": fecha_hora,
                    "id_metodo_pago": metodo_pago,
                    "id_usuario": id_usuario,
                    "u_id": id_usuario_perfil
                }).execute()
                # Obtener id_venta recién creada
                id_venta = response_venta.data[0]["id_venta"] if response_venta.data else None

                # Obtener id_producto
                id_prod = traer_id_producto(nombre)

                # Actualizar stock
                stock_actual = supabase.table("productos") \
                    .select("stock") \
                    .eq("id_producto", id_prod) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute().data[0]["stock"]
                supabase.table("productos").update({
                    "stock": stock_actual - cantidad
                }).eq("id_producto", id_prod).eq("u_id", id_usuario_perfil).execute()

                # Insertar detalle de venta
                supabase.table("detalle_ventas").insert({
                    "id_venta": id_venta,
                    "id_producto": id_prod,
                    "cantidad": cantidad,
                    "precio_unitario_venta": precio,
                    "precio_unitario_compra": precio_compra,
                    "u_id": id_usuario_perfil
                }).execute()

                cargar_movimiento_venta(usuario)

            else:
                # Compra
                # Insertar compra
                response_compra = supabase.table("compras").insert({
                    "fecha_hora": fecha_hora,
                    "id_usuario": id_usuario,
                    "id_metodo_pago": metodo_pago,
                    "u_id": id_usuario_perfil
                }).execute()
                # Obtener id_compra recién creada
                id_compra = response_compra.data[0]["id_compra"] if response_compra.data else None

                # Obtener id_producto
                id_prod = traer_id_producto(nombre)

                # Actualizar stock
                stock_actual = supabase.table("productos") \
                    .select("stock") \
                    .eq("id_producto", id_prod) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute().data[0]["stock"]
                supabase.table("productos").update({
                    "stock": stock_actual + cantidad
                }).eq("id_producto", id_prod).eq("u_id", id_usuario_perfil).execute()

                # Insertar detalle de compra
                supabase.table("detalle_compras").insert({
                    "id_compra": id_compra,
                    "id_producto": id_prod,
                    "cantidad": cantidad,
                    "precio_unitario": precio,
                    "u_id": id_usuario_perfil
                }).execute()

                cargar_movimiento_compra(usuario)

        return True
    except Exception as e:
        print(f"Error al agregar a registro en Supabase: {e}")
        return False
    

def traer_precio_compra(nombre):
    global id_usuario_perfil
    try:
        response = supabase.table("productos") \
            .select("precio_de_compra") \
            .eq("nombre", nombre) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["precio_de_compra"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer precio de compra en Supabase: {e}")
        return None
    

def traer_mp(metodo_pago):
    global id_usuario_perfil
    try:
        response = supabase.table("metodos_pago") \
            .select("id_mp") \
            .eq("nombre_mp", metodo_pago) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_mp"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id de método de pago en Supabase: {e}")
        return None
    

def agregar_mp_db(lineEdit_value):
    global id_usuario_perfil
    try:
        # Insertar método de pago en Supabase
        supabase.table("metodos_pago").insert({
            "nombre_mp": lineEdit_value,
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        # Si el error es por duplicado, retorna False
        if "duplicate" in str(e).lower() or "unique" in str(e).lower():
            return False
        print(f"Error al agregar método de pago en Supabase: {e}")
        return False
    
def traer_ultimo_agregado_anotador():
    global id_usuario_perfil
    try:
        response = supabase.table("anotador") \
            .select("contenido") \
            .eq("u_id", id_usuario_perfil) \
            .order("id_anotador", desc=True) \
            .limit(1) \
            .execute()
        data = response.data
        if data:
            return data[0]["contenido"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer el último agregado del anotador en Supabase: {e}")
        return None
    

def set_text_principal(usuario):
    global id_usuario_perfil

    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        # Insertar anotación inicial en Supabase
        supabase.table("anotador").insert({
            "id_nota": 1,
            "contenido": 'GENERAL:\n',
            "fecha_modificacion": fecha_hora_actual,
            "tipo_cambio": 'inicial',
            "usuario_id": traer_id_usuario(usuario),
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al setear texto principal en Supabase: {e}")
        return False
    
def guardar_texto_anotador_sincrono(texto, usuario):
    global id_usuario_perfil

    """
    Actualiza la nota del anotador que contiene el u_id de id_usuario_perfil.
    Si existe, la edita; si no existe, la crea.
    Retorna True si se guardó exitosamente, False en caso contrario.
    """
    try:
        id_usuario = traer_id_usuario(usuario)
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Intentar actualizar la nota existente
        response = supabase.table("anotador") \
            .update({
                "contenido": texto,
                "tipo_cambio": "editado",
                "usuario_id": id_usuario,
                "fecha_modificacion": fecha_hora_actual
            }) \
            .eq("u_id", id_usuario_perfil) \
            .eq("id_nota", 1) \
            .execute()
        
        return True
    except Exception as e:
        print(f"Error al guardar texto del anotador en Supabase: {e}")
        return False
    
    
def limpiar_anotaciones_automatico():
    global id_usuario_perfil

    """
    Limpia automáticamente la tabla anotador si hay más de 5 registros.
    Retorna True si se limpió exitosamente, False en caso contrario.
    """
    try:
        # Contar cuántos registros hay en Supabase
        response = supabase.table("anotador") \
            .select("id_anotador") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if not data:
            return True

        if len(data) > 5:
            # Ordenar por fecha_modificacion descendente y conservar el más reciente
            data_sorted = sorted(data, key=lambda x: x.get("fecha_modificacion", ""), reverse=True)
            ids_a_conservar = {data_sorted[0]["id_anotador"]}
            ids_a_borrar = [row["id_anotador"] for row in data if row["id_anotador"] not in ids_a_conservar]

            # Borrar todos menos el más reciente
            for id_anotador in ids_a_borrar:
                supabase.table("anotador") \
                    .delete() \
                    .eq("id_anotador", id_anotador) \
                    .eq("u_id", id_usuario_perfil) \
                    .execute()
        return True
    except Exception as e:
        print(f"Error al limpiar anotaciones automáticamente en Supabase: {e}")
        return False
    

def traer_todos_los_productos():
    global id_usuario_perfil
    try:
        # Obtener todos los productos del perfil, junto con su categoría y proveedor
        response = supabase.table("productos") \
            .select("id_producto, nombre, precio_de_compra, precio_de_venta, stock, stock_ideal, id_categoria, id_proveedor") \
            .eq("u_id", id_usuario_perfil) \
            .order("nombre") \
            .execute()
        productos = response.data

        if not productos:
            return []

        # Obtener todas las categorías y proveedores del perfil
        response_categorias = supabase.table("categorias") \
            .select("id_categoria, nombre_descrip") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        categorias = {c["id_categoria"]: c["nombre_descrip"] for c in response_categorias.data} if response_categorias.data else {}

        response_proveedores = supabase.table("proveedores") \
            .select("id_proveedor, nombre_proveedor") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        proveedores = {p["id_proveedor"]: p["nombre_proveedor"] for p in response_proveedores.data} if response_proveedores.data else {}

        # Armar la lista de tuplas como el fetchall()
        resultado = []
        for p in productos:
            resultado.append((
                p["id_producto"],
                p["nombre"],
                p["precio_de_compra"],
                p["precio_de_venta"],
                p["stock"],
                p["stock_ideal"],
                categorias.get(p["id_categoria"], None),
                proveedores.get(p["id_proveedor"], None)
            ))
        return resultado
    except Exception as e:
        print(f"Error al traer todos los productos en Supabase: {e}")
        return []
    



####################################################################
####################################################################
# MOVIMIENTOS:

def cargar_movimiento_producto_agregado(input_id_value, usuario):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario)
    nombre_producto = traer_nom_producto(input_id_value)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Agregar",
            "entidad_afectada": "Productos",
            "id_entidad": input_id_value,
            "descripcion": f"Producto agregado: {nombre_producto}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de producto agregado en Supabase: {e}")
        return False
    

def cargar_movimiento_producto_borrado(id, nombre, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Productos",
            "id_entidad": id,
            "descripcion": f"Producto borrado: {nombre}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de producto borrado en Supabase: {e}")
        return False
    

def cargar_movimiento_aumento_precios(combobox_20_value, usuario_activo, s):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    if s:
        combobox_20_ID = traer_id_categoria(combobox_20_value)
    else:
        combobox_20_ID = traer_id_proveedor(combobox_20_value)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Aumento",
            "entidad_afectada": "Productos",
            "id_entidad": combobox_20_ID,
            "descripcion": f"Aumento precios de: {combobox_20_value}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de aumento de precios en Supabase: {e}")
        return False
    
    

def cargar_movimiento_producto_editado(producto_id, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    nombre_producto = traer_nom_producto(producto_id)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Editar",
            "entidad_afectada": "Productos",
            "id_entidad": producto_id,
            "descripcion": f"Producto editado: {nombre_producto}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de producto editado en Supabase: {e}")
        return False
    
def cargar_movimiento_agregar_proveedor(nombre_proveedor, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_proveedor = traer_id_proveedor(nombre_proveedor)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Agregar",
            "entidad_afectada": "Proveedores",
            "id_entidad": id_proveedor,
            "descripcion": f"Proveedor agregado: {nombre_proveedor}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de proveedor agregado en Supabase: {e}")
        return False
    
def cargar_movimiento_proveedor_borrado(nombre_proveedor, id_proveedor, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Proveedores",
            "id_entidad": id_proveedor,
            "descripcion": f"Proveedor borrado: {nombre_proveedor}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de proveedor borrado en Supabase: {e}")
        return False
    

def cargar_movimiento_proveedor_editado(nombre_proveedor, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    id_proveedor = traer_id_proveedor(nombre_proveedor)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Editar",
            "entidad_afectada": "Proveedores",
            "id_entidad": id_proveedor,
            "descripcion": f"Proveedor editado: {nombre_proveedor}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de proveedor editado en Supabase: {e}")
        return False
    

def cargar_movimiento_agregar_categoria(lineEdit_16_value, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_categoria = traer_id_categoria(lineEdit_16_value)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Agregar",
            "entidad_afectada": "Categorias",
            "id_entidad": id_categoria,
            "descripcion": f"Categoria agregada: {lineEdit_16_value}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de categoría agregada en Supabase: {e}")
        return False
    

def cargar_movimiento_categoria_borrada(lineEdit_21_value, id_categoria, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Categorias",
            "id_entidad": id_categoria,
            "descripcion": f"Categoria borrada: {lineEdit_21_value}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de categoría borrada en Supabase: {e}")
        return False
    

def cargar_movimientos_datos_borrados(usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Datos",
            "id_entidad": None,
            "descripcion": "Datos borrados",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de datos borrados en Supabase: {e}")
        return False
    

def cargar_movimiento_editar_usuario(id_usuario, nombre_usuario, usuario_activo):
    global id_usuario_perfil
                    
    id_usuario_activo = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario_activo,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Editar",
            "entidad_afectada": "Usuarios",
            "id_entidad": id_usuario,
            "descripcion": f"Usuario editado: {nombre_usuario}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de usuario editado en Supabase: {e}")
        return False

def cargar_movimiento_usuario_borrado(nombre_usuario, id_usuario, usuario_activo):
    global id_usuario_perfil

    id_usuario_activo = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario_activo,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Usuarios",
            "id_entidad": id_usuario,
            "descripcion": f"Usuario borrado: {nombre_usuario}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de usuario borrado en Supabase: {e}")
        return False
    
def traer_id_venta():
    global id_usuario_perfil
    try:
        response = supabase.table("ventas") \
            .select("id_venta") \
            .eq("u_id", id_usuario_perfil) \
            .order("id_venta", desc=True) \
            .limit(1) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_venta"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id_venta en Supabase: {e}")
        return None
    

def traer_id_compra():
    global id_usuario_perfil
    try:
        response = supabase.table("compras") \
            .select("id_compra") \
            .eq("u_id", id_usuario_perfil) \
            .order("id_compra", desc=True) \
            .limit(1) \
            .execute()
        data = response.data
        if data:
            return data[0]["id_compra"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer id_compra en Supabase: {e}")
        return None
    

def traer_prod_vendido(id_venta):
    global id_usuario_perfil
    try:
        response = supabase.table("detalle_ventas") \
            .select("id_producto") \
            .eq("id_venta", id_venta) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        # Devuelve el id del producto vendido, ya que solo se espera un producto por ID de venta
        if data:
            return data[0]["id_producto"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer producto vendido en Supabase: {e}")
        return None
    
def traer_prod_compra(id_compra):
    global id_usuario_perfil
    try:
        response = supabase.table("detalle_compras") \
            .select("id_producto") \
            .eq("id_compra", id_compra) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        # Devuelve el id del producto comprado, ya que solo se espera un producto por ID de compra
        if data:
            return data[0]["id_producto"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer producto comprado en Supabase: {e}")
        return None

def cargar_movimiento_venta(usuario_activo):
    global id_usuario_perfil
    
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_venta = traer_id_venta()
    id_prod = traer_prod_vendido(id_venta)
    prod_vendido = traer_nom_producto(id_prod)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Venta",
            "entidad_afectada": "Ventas",
            "id_entidad": id_venta,
            "descripcion": f"se vendió: {prod_vendido}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de venta en Supabase: {e}")
        return False

def cargar_movimiento_agregar_metodo_pago(metodo_pago, usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_entidad = traer_mp(metodo_pago)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Agregar",
            "entidad_afectada": "Metodos de Pago",
            "id_entidad": id_entidad,
            "descripcion": f"Método de pago agregado: {metodo_pago}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de método de pago agregado en Supabase: {e}")
        return False
    

def cargar_movimiento_borrar_metodo_pago(metodo_pago, usuario_activo, id):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Borrar",
            "entidad_afectada": "Metodos de Pago",
            "id_entidad": id,
            "descripcion": f"Método de pago borrado: {metodo_pago}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de método de pago borrado en Supabase: {e}")
        return False

def cargar_movimiento_compra(usuario_activo):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_compra = traer_id_compra()
    id_prod = traer_prod_compra(id_compra)
    prod_comprado = traer_nom_producto(id_prod)

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Compra",
            "entidad_afectada": "Compras",
            "id_entidad": None,
            "descripcion": f"se compro: {prod_comprado}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de compra en Supabase: {e}")
        return False
    

def traer_rol_usuario(usuario):
    global id_usuario_perfil
    try:
        response = supabase.table("usuarios") \
            .select("admin") \
            .eq("nombre", usuario) \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if data:
            return data[0]["admin"]
        else:
            return None
    except Exception as e:
        print(f"Error al traer rol de usuario en Supabase: {e}")
        return None
    

def cargar_movimiento_inicio(usuario):
    global id_usuario_perfil

    id_usuario = traer_id_usuario(usuario)
    fecha_hora = datetime.now().astimezone().isoformat()
    rol = traer_rol_usuario(usuario)

    if rol:
        usuario_rol = 'administrador'
    else:
        usuario_rol = 'usuario'

    try:
        supabase.table("movimientos").insert({
            "id_usuario": id_usuario,
            "fecha_hora": fecha_hora,
            "tipo_accion": "Login",
            "entidad_afectada": "Sistema",
            "id_entidad": None,
            "descripcion": f"{usuario_rol} : {usuario}",
            "u_id": id_usuario_perfil
        }).execute()
        return True
    except Exception as e:
        print(f"Error al registrar movimiento de inicio en Supabase: {e}")
        return False
    

def traer_anios():
    global id_usuario_perfil
    try:
        # Selecciona solo la columna fecha_hora de la tabla ventas
        response = supabase.table("ventas") \
            .select("fecha_hora") \
            .eq("u_id", id_usuario_perfil) \
            .execute()
        data = response.data
        if not data:
            return []
        # Extrae el año de cada fecha_hora y elimina duplicados
        anios = set()
        for row in data:
            fecha = row["fecha_hora"]
            # Asume formato ISO: 'YYYY-MM-DD...'
            anio = fecha[:4]
            if anio.isdigit():
                anios.add(int(anio))
        return sorted(anios)
    except Exception as e:
        print(f"Error al traer años desde ventas en Supabase: {e}")
        return []

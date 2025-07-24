import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Flask, request, jsonify
from API.funcion_login_web import verificar_credenciales, verificar_estado_suscripcion
# Supabase integration
from supabase import create_client, Client
from API.functions import *
import os
import json
import firebase_admin
from firebase_admin import credentials

# Inicialización de Firebase (al inicio del archivo, después de los imports)
if not firebase_admin._apps:
    cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
    if cred_path and os.path.exists(cred_path):
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    else:
        raise Exception("No se encontraron las credenciales de Firebase")


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



app = Flask(__name__)

###### firebase endpoints ######

@app.route('/api/verificar_existencia_mail', methods=['POST'])
def api_verificar_existencia_mail():
    data = request.json
    email = data.get('email')
    uid = data.get('uid')
    if not email or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    resultado = verificar_existencia_usuario_mail(email, uid)  # Aquí está la lógica
    return jsonify({"verificado": resultado})

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    if not email or not password:
        return jsonify({"exito": False, "resultado": "Faltan datos"}), 400
    exito, resultado = verificar_credenciales(email, password)
    return jsonify({"exito": exito, "resultado": resultado})

@app.route('/api/verificar_suscripcion', methods=['POST'])
def api_verificar_suscripcion():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"pro": False, "error": "Falta UID"}), 400
    es_pro = verificar_estado_suscripcion(uid)
    return jsonify({"pro": es_pro})

###### supabase endpoints ######

@app.route('/api/verificar_contrasenia', methods=['POST'])
def api_verificar_contrasenia():
    data = request.json
    tipo_usuario = data.get('tipo_usuario')
    usuario = data.get('usuario')
    contrasenia = data.get('contrasenia')
    if not all([tipo_usuario, usuario, contrasenia]):
        return jsonify({"error": "Faltan datos"}), 400
    resultado = verificar_contrasenia(tipo_usuario, usuario, contrasenia)
    # True = error, False = válido
    return jsonify({"valido": not resultado})

@app.route('/api/hay_admin', methods=['POST'])
def api_hay_admin():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    # Asigna el UID global antes de llamar a la función
    from functions import id_usuario_perfil
    id_usuario_perfil = uid
    existe = hay_admin()
    return jsonify({"existe": existe})

@app.route('/api/registro_check', methods=['POST'])
def api_registro_check():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    tipo_usuario = data.get('tipo_usuario')

    if not all([username, password, email, tipo_usuario]):
        return jsonify({"error": "Faltan datos"}), 400

    hay_admin_result = hay_admin() if tipo_usuario == "Administrador" else False
    usuario_existe_result = verificar_usuario_existente(username)
    mail_existe_result = verificar_mail_existente(email)
    password_ok_result = len(password) >= 8

    return jsonify({
        "hay_admin": hay_admin_result,
        "usuario_existe": usuario_existe_result,
        "mail_existe": mail_existe_result,
        "password_ok": password_ok_result
    })


@app.route('/api/verificar_mail_existente', methods=['POST'])
def api_verificar_mail_existente():
    data = request.json
    mail = data.get('mail')
    if not mail:
        return jsonify({"error": "Falta mail"}), 400
    existe = verificar_mail_existente(mail)
    return jsonify({"existe": existe})

@app.route('/api/verificar_usuario_existente', methods=['POST'])
def api_verificar_usuario_existente():
    data = request.json
    nombre = data.get('nombre')
    uid = data.get('uid')
    if not nombre or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    existe = verificar_usuario_existente(nombre)
    return jsonify({"existe": existe})

@app.route('/api/codigo_otro_admin', methods=['POST'])
def api_codigo_otro_admin():
    try:
        administrador = traer_administradores()
        mail = traer_mail_admin(administrador[0])
        codigo = enviar_codigo_verificacion(mail)
        if codigo:
            return jsonify({"codigo": codigo})
        else:
            return jsonify({"error": "No se pudo enviar el código"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/enviar_codigo_verificacion', methods=['POST'])
def api_enviar_codigo_verificacion():
    data = request.json
    mail = data.get('mail')
    if not mail:
        return jsonify({"error": "Falta mail"}), 400
    codigo = enviar_codigo_verificacion(mail)
    if codigo:
        return jsonify({"codigo": codigo})
    else:
        return jsonify({"error": "No se pudo enviar el código"}), 500


@app.route('/api/traer_administradores', methods=['POST'])
def api_traer_administradores():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    try:    
        administradores = traer_administradores()
        return jsonify({"administrador": administradores})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_mail_admin', methods=['POST'])
def api_traer_mail_admin():
    data = request.json
    administrador = data.get('administrador')
    uid = data.get('uid')
    if not administrador or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    global id_usuario_perfil
    
    try:
        mail = traer_mail_admin(administrador)
        return jsonify({"mail": mail})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/registrar_usuario', methods=['POST'])
def api_registrar_usuario():
    data = request.json
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')
    tipo = data.get('tipo')
    email = data.get('email')

    if not all([usuario, contrasena, tipo, email]):
        return jsonify({"error": "Faltan datos"}), 400

    try:
        registrar_usuario(usuario, contrasena, tipo, email)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500
    

@app.route('/api/verificar_y_enviar_codigo', methods=['POST'])
def api_verificar_y_enviar_codigo():
    data = request.json
    mail = data.get('mail')
    if not mail:
        return jsonify({"error": "Falta mail"}), 400
    existe = existencia_mail(mail)
    if existe:
        codigo = enviar_codigo_verificacion(mail)
        if codigo:
            return jsonify({"existe": True, "codigo": codigo})
        else:
            return jsonify({"existe": True, "codigo": None, "error": "No se pudo enviar el código"}), 500
    else:
        return jsonify({"existe": False, "codigo": None})
    
    
@app.route('/api/existencia_mail', methods=['POST'])
def api_existencia_mail():
    data = request.json
    mail = data.get('mail')
    uid = data.get('uid')
    if not mail or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    existe = existencia_mail(mail)
    return jsonify({"existe": existe})

@app.route('/api/actualizar_contrasena', methods=['POST'])
def api_actualizar_contrasena():
    data = request.json
    nueva_contrasena = data.get('nueva_contrasena')
    mail = data.get('mail')
    uid = data.get('uid')
    if not nueva_contrasena or not mail or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        resultado = actualizar_contrasena(nueva_contrasena, mail)
        return jsonify({"actualizado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/traer_categorias', methods=['POST'])
def api_traer_categorias():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    try:
        categorias = traer_categorias()
        return jsonify({"categorias": categorias})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/crear_categuno', methods=['POST'])
def api_crear_categuno():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    try:
        crear_categuno()
        return jsonify({"creado": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/crear_provuno', methods=['POST'])
def api_crear_provuno():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    try:
        crear_provuno()
        return jsonify({"creado": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cargar_producto', methods=['POST'])
def api_cargar_producto():
    data = request.json
    uid = data.get('uid')
    id_producto = data.get('id_producto')
    nombre_producto = data.get('nombre_producto')
    precio_compra = data.get('precio_compra_producto')
    precio_venta = data.get('precio_venta_producto')
    cantidad = data.get('cantidad_producto')
    stock_ideal = data.get('stock_ideal')
    categoria = data.get('categoria_producto')
    proveedor = data.get('proveedor_producto')
    if not all([uid, id_producto, nombre_producto, precio_compra, precio_venta, cantidad, stock_ideal, categoria, proveedor]):
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        resultado = cargar_producto(id_producto, nombre_producto, precio_compra, precio_venta, cantidad, stock_ideal, categoria, proveedor)
        return jsonify({"cargado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_id_categoria', methods=['POST'])
def api_traer_id_categoria():
    data = request.json
    categoria = data.get('categoria')
    uid = data.get('uid')
    if not categoria or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        id_categoria = traer_id_categoria(categoria)
        return jsonify({"id_categoria": id_categoria})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_id_proveedor', methods=['POST'])
def api_traer_id_proveedor():
    data = request.json
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "Falta el nombre"}), 400
    try:
        id_prov = traer_id_proveedor(nombre)
        return jsonify({"id_proveedor": id_prov})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/traer_id_usuario', methods=['POST'])
def api_traer_id_usuario():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    if not nombre_usuario:
        return jsonify({"error": "Falta el nombre de usuario"}), 400
    try:
        id_usuario = traer_id_usuario(nombre_usuario)
        return jsonify({"id_usuario": id_usuario})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_nom_producto', methods=['POST'])
def api_traer_nom_producto():
    data = request.json
    id_producto = data.get('id_producto')
    if not id_producto:
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        nombre = traer_nom_producto(id_producto)
        return jsonify({"nombre": nombre})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_id_producto', methods=['POST'])
def api_traer_id_producto():
    data = request.json
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        id_producto = traer_id_producto(nombre)
        return jsonify({"id_producto": id_producto})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/aumentar_precios_categoria', methods=['POST'])
def api_aumentar_precios_categoria():
    data = request.json
    valor1 = data.get('valor1')
    valor2 = data.get('valor2')
    categoria = data.get('categoria')
    if valor1 is None or valor2 is None or not categoria:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        aumentar_precios_categoria(valor1, valor2, categoria)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/aumentar_precios_proveedor', methods=['POST'])
def api_aumentar_precios_proveedor():
    data = request.json
    valor1 = data.get('valor1')
    valor2 = data.get('valor2')
    proveedor = data.get('proveedor')
    if valor1 is None or valor2 is None or not proveedor:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        aumentar_precios_proveedor(valor1, valor2, proveedor)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/actualizar_producto', methods=['POST'])
def api_actualizar_producto():
    data = request.json
    try:
        exito = actualizar_producto(
            data.get("id"),
            data.get("nombre_prod"),
            data.get("precio_compra"),
            data.get("precio_venta"),
            data.get("stock"),
            data.get("stock_ideal"),
            data.get("categoria"),
            data.get("proveedor")
        )
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/cargar_proveedor', methods=['POST'])
def api_cargar_proveedor():
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    mail = data.get('mail')
    uid = data.get('uid')
    if not all([nombre, telefono, mail, uid]):
        return jsonify({"error": "Faltan datos"}), 400
    
    try:
        resultado = cargar_proveedor(nombre, telefono, mail)
        return jsonify({"creado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/buscar_proveedor', methods=['POST'])
def api_buscar_proveedor():
    data = request.json
    nombre = data.get('nombre')
    if not nombre:
        return jsonify({"error": "Falta el nombre"}), 400
    try:
        bandera = buscar_proveedor(nombre)
        return jsonify({"existe": bandera})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/actualizar_proveedor', methods=['POST'])
def api_actualizar_proveedor():
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    if not nombre or not telefono:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        exito = actualizar_proveedor(nombre, telefono, direccion)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_proveedor', methods=['POST'])
def api_traer_proveedor():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    try:
        proveedores = traer_proveedor()
        return jsonify({"proveedores": proveedores})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/buscar_categoria', methods=['POST'])
def api_buscar_categoria():
    data = request.json
    nombre_categoria = data.get('nombre_categoria')
    if not nombre_categoria:
        return jsonify({"error": "Falta el nombre de la categoría"}), 400
    try:
        existe = buscar_categoria(nombre_categoria)
        return jsonify({"existe": existe})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/agregar_registro_usuario', methods=['POST'])
def api_agregar_registro_usuario():
    data = request.json
    rol = data.get('rol')
    usuario = data.get('usuario')
    password = data.get('password')
    email = data.get('email')
    if not rol or not usuario or not password:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        exito = agregar_a_registro_usuario(rol, usuario, password, email)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/clear_data', methods=['POST'])
def api_clear_data():
    data = request.json
    borrar_categorias = data.get('borrar_categorias')
    borrar_ventas_compras = data.get('borrar_ventas_compras')
    borrar_proveedores = data.get('borrar_proveedores')
    borrar_usuarios = data.get('borrar_usuarios')
    borrar_movimientos = data.get('borrar_movimientos')
    try:
        clear_data(
            borrar_categorias,
            borrar_ventas_compras,
            borrar_proveedores,
            borrar_usuarios,
            borrar_movimientos
        )
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_todos_los_usuarios', methods=['GET'])
def api_traer_todos_los_usuarios():
    try:
        usuarios = traer_todos_los_usuarios()
        return jsonify({"usuarios": usuarios})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/api/movimiento_agregar_usuario', methods=['POST'])
def api_movimiento_agregar_usuario():
    data = request.json
    usuario = data.get('usuario')
    usuario_activo = data.get('usuario_activo')
    if not usuario or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_agregar_usuario(usuario, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/api/actualizar_usuario', methods=['POST'])
def api_actualizar_usuario():
    data = request.json
    id_usuario = data.get('id_usuario')
    rol = data.get('rol')
    mail = data.get('mail')
    password = data.get('password')
    if not id_usuario or not rol or not mail or not password:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        exito = actualizar_usuario(id_usuario, rol, mail, password)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/borrar_usuario', methods=['POST'])
def api_borrar_usuario():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    if not nombre_usuario:
        return jsonify({"error": "Falta el nombre de usuario"}), 400
    try:
        exito = borrar_usuario(nombre_usuario)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimientos_por_usuario', methods=['POST'])
def api_movimientos_por_usuario():
    data = request.json
    usuario = data.get('usuario')
    if not usuario:
        return jsonify({"error": "Falta el usuario"}), 400
    try:
        movimientos = traer_movimientos_por_usuario(usuario)
        return jsonify({"movimientos": movimientos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/movimientos_por_fecha', methods=['POST'])
def api_movimientos_por_fecha():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        movimientos = traer_movimientos_por_fecha(fecha)
        return jsonify({"movimientos": movimientos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
@app.route('/api/movimientos_por_accion', methods=['POST'])
def api_movimientos_por_accion():
    data = request.json
    accion = data.get('accion')
    if not accion:
        return jsonify({"error": "Falta la acción"}), 400
    try:
        movimientos = traer_movimientos_por_accion(accion)
        return jsonify({"movimientos": movimientos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_metodo_pago_id', methods=['POST'])
def api_traer_metodo_pago_id():
    data = request.json
    nombre_metodo = data.get('nombre_metodo')
    if not nombre_metodo:
        return jsonify({"error": "Falta el nombre del método"}), 400
    try:
        id_metodo = traer_metodo_pago_id(nombre_metodo)
        return jsonify({"id_metodo": id_metodo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_todos_metodos_pago', methods=['GET'])
def api_traer_todos_metodos_pago():
    try:
        metodos = traer_todos_metodos_pago()
        return jsonify({"metodos_pago": metodos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/traer_datos_ventas_metodo_o_usuario', methods=['POST'])
def api_traer_datos_ventas_metodo_o_usuario():
    data = request.json
    id_metodo_o_usuario = data.get('id_metodo_o_usuario')
    fecha = data.get('fecha')
    if not id_metodo_o_usuario or not fecha:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        datos = traer_datos_ventas_metodo_o_usuario(id_metodo_o_usuario, fecha)
        return jsonify({"datos": datos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/traer_datos_compras_metodo_o_usuario', methods=['POST'])
def api_traer_datos_compras_metodo_o_usuario():
    data = request.json
    id_metodo_o_usuario = data.get('id_metodo_o_usuario')
    fecha = data.get('fecha')
    if not id_metodo_o_usuario or not fecha:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        datos = traer_datos_compras_metodo_o_usuario(id_metodo_o_usuario, fecha)
        return jsonify({"datos": datos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/traer_metodo_pago', methods=['POST'])
def api_traer_metodo_pago():
    data = request.json
    id_metodo = data.get('id_metodo')
    if not id_metodo:
        return jsonify({"error": "Falta el id del método"}), 400
    try:
        metodo = traer_metodo_pago(id_metodo)
        return jsonify({"metodo": metodo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_datos_arqueo_ventas_fecha', methods=['POST'])
def api_traer_datos_arqueo_ventas_fecha():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        datos = traer_datos_arqueo_ventas_fecha(fecha)
        return jsonify({"datos": datos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_datos_arqueo_compras_fecha', methods=['POST'])
def api_traer_datos_arqueo_compras_fecha():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        datos = traer_datos_arqueo_compras_fecha(fecha)
        return jsonify({"datos": datos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_metodos_de_pago', methods=['GET'])
def api_traer_metodos_de_pago():
    try:
        metodos = traer_metodos_de_pago()
        return jsonify({"metodos_pago": metodos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_ventas_totales_dia', methods=['POST'])
def api_traer_ventas_totales_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        total = traer_ventas_totales_dia(fecha)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_ganancias_totales_dia', methods=['POST'])
def api_traer_ganancias_totales_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        total = traer_ganancias_totales_dia(fecha)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_compras_totales_dia', methods=['POST'])
def api_traer_compras_totales_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        total = traer_compras_totales_dia(fecha)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_numero_de_compras_dia', methods=['POST'])
def api_traer_numero_de_compras_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        total = traer_numero_de_compras_dia(fecha)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/traer_compras_totales_mes', methods=['POST'])
def api_traer_compras_totales_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        total = traer_compras_totales_mes(anio, mes)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_numero_de_compras_mes', methods=['POST'])
def api_traer_numero_de_compras_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        total = traer_numero_de_compras_mes(anio, mes)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_compras_totales_ano', methods=['POST'])
def api_traer_compras_totales_ano():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Falta el año"}), 400
    try:
        total = traer_compras_totales_ano_actual(anio)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_numero_de_compras_ano_actual', methods=['POST'])
def api_traer_numero_de_compras_ano_actual():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_numero_de_compras_ano_actual(anio)
    return jsonify({"numero_compras_ano": total})

@app.route('/api/traer_ventas_por_metodo_dia', methods=['POST'])
def api_traer_ventas_por_metodo_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        ventas_por_metodo = traer_ventas_por_metodo_dia(fecha)
        return jsonify({"ventas_por_metodo": ventas_por_metodo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_compras_por_metodo_dia', methods=['POST'])
def api_traer_compras_por_metodo_dia():
    data = request.json
    fecha = data.get('fecha')
    uid = data.get('uid')
    if not fecha or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultados = traer_compras_por_metodo_dia(fecha)
    return jsonify({"compras_por_metodo": resultados})


@app.route('/api/traer_ventas_por_metodo_mes', methods=['POST'])
def api_traer_ventas_por_metodo_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        ventas_por_metodo = traer_ventas_por_metodo_mes(anio, mes)
        return jsonify({"ventas_por_metodo": ventas_por_metodo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_compras_por_metodo_mes', methods=['POST'])
def api_traer_compras_por_metodo_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    uid = data.get('uid')
    if not anio or not mes or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultados = traer_compras_por_metodo_mes(anio, mes)
    return jsonify({"compras_por_metodo_mes": resultados})

@app.route('/api/traer_ventas_por_metodo_ano', methods=['POST'])
def api_traer_ventas_por_metodo_ano():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Falta el año"}), 400
    try:
        ventas_por_metodo = traer_ventas_por_metodo_ano(anio)
        return jsonify({"ventas_por_metodo": ventas_por_metodo})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_numero_de_ventas_ano', methods=['POST'])
def api_traer_numero_de_ventas_ano():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_numero_de_ventas_ano(anio)
    return jsonify({"numero_ventas_ano": total})

@app.route('/api/traer_numero_de_ventas_mes', methods=['POST'])
def api_traer_numero_de_ventas_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_numero_de_ventas_mes(anio, mes)
    return jsonify({"numero_ventas_mes": total})


@app.route('/api/traer_numero_de_ventas_dia', methods=['POST'])
def api_traer_numero_de_ventas_dia():
    data = request.json
    fecha = data.get('fecha')
    if not fecha:
        return jsonify({"error": "Falta la fecha"}), 400
    try:
        total = traer_numero_de_ventas_dia(fecha)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_ventas_totales_ano', methods=['POST'])
def api_traer_ventas_totales_ano():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Falta el año"}), 400
    try:
        total = traer_ventas_totales_ano_actual(anio)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/traer_ganancias_totales_ano', methods=['POST'])
def api_traer_ganancias_totales_ano():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Falta el año"}), 400
    try:
        total = traer_ganancias_totales_ano_actual(anio)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_ganancias_totales_mes', methods=['POST'])
def api_traer_ganancias_totales_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        total = traer_ganancias_totales_mes(anio, mes)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_ventas_totales_mes', methods=['POST'])
def api_traer_ventas_totales_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        total = traer_ventas_totales_mes(anio, mes)
        return jsonify({"total": total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/traer_venta_promedio_ano_actual', methods=['POST'])
def api_traer_venta_promedio_ano_actual():
    data = request.json
    anio = data.get('anio')
    if not anio:
        return jsonify({"error": "Faltan datos"}), 400
    
    promedio = traer_venta_promedio_ano_actual(anio)
    return jsonify({"venta_promedio_ano": promedio})

@app.route('/api/traer_ventas_ano_actual', methods=['POST'])
def api_traer_ventas_ano_actual():
    data = request.json
    anio = data.get('anio')
    meses = data.get('meses')  # Debe ser una lista de nombres o números de mes
    if not anio or not meses or not isinstance(meses, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    ventas = traer_ventas_ano_actual(anio, meses)
    return jsonify({"ventas_por_mes": ventas})

@app.route('/api/traer_ganancias_ano_actual', methods=['POST'])
def api_traer_ganancias_ano_actual():
    data = request.json
    anio = data.get('anio')
    meses = data.get('meses')  # Debe ser una lista de nombres o números de mes

    if not anio or not meses or not isinstance(meses, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    ganancias = traer_ganancias_ano_actual(anio, meses)
    return jsonify({"ganancias_por_mes": ganancias})


@app.route('/api/traer_metodos_pago_y_su_id', methods=['GET'])
def api_traer_metodos_pago_y_su_id():
    metodos = traer_metodos_pago_y_su_id()
    return jsonify({"metodos_pago": metodos})

@app.route('/api/traer_datos_por_metodo_y_mes', methods=['POST'])
def api_traer_datos_por_metodo_y_mes():
    data = request.json
    anio = data.get('anio')
    metodo = data.get('metodo')
    meses = data.get('meses')  # Debe ser una lista de nombres o números de mes
 
    if not anio or not metodo or not meses or not isinstance(meses, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    datos = traer_datos_por_metodo_y_mes(anio, metodo, meses)
    return jsonify({"ventas_por_mes_metodo": datos})

@app.route('/api/traer_venta_promedio_mes', methods=['POST'])
def api_traer_venta_promedio_mes():
    data = request.json
    anio = data.get('anio')
    mes = data.get('mes')
    if not anio or not mes:
        return jsonify({"error": "Faltan datos"}), 400
    
    promedio = traer_venta_promedio_mes(anio, mes)
    return jsonify({"venta_promedio_mes": promedio})

@app.route('/api/traer_numero_de_ventas_semana', methods=['POST'])
def api_traer_numero_de_ventas_semana():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')
    if not anio or not semana:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_numero_de_ventas_semana(anio, semana)
    return jsonify({"numero_ventas_semana": total})

@app.route('/api/traer_venta_promedio_semana', methods=['POST'])
def api_traer_venta_promedio_semana():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')

    if not anio or not semana:
        return jsonify({"error": "Faltan datos"}), 400
    
    promedio = traer_venta_promedio_semana(anio, semana)
    return jsonify({"venta_promedio_semana": promedio})

@app.route('/api/traer_ganancias_totales_semana', methods=['POST'])
def api_traer_ganancias_totales_semana():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')

    if not anio or not semana:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_ganancias_totales_semana(anio, semana)
    return jsonify({"total_ganancias_semana": total})

@app.route('/api/traer_ventas_semana_actual', methods=['POST'])
def api_traer_ventas_semana_actual():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')
    dias = data.get('dias')  # Debe ser una lista de nombres o números de día
    if not anio or not semana or not dias or not isinstance(dias, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    ventas = traer_ventas_semana_actual(anio, semana, dias)
    return jsonify({"ventas_por_dia": ventas})

@app.route('/api/traer_ganancias_semana_actual', methods=['POST'])
def api_traer_ganancias_semana_actual():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')
    dias = data.get('dias')  # Debe ser una lista de nombres o números de día

    if not anio or not semana or not dias or not isinstance(dias, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    ganancias = traer_ganancias_semana_actual(anio, semana, dias)
    return jsonify({"ganancias_por_dia": ganancias})

@app.route('/api/traer_datos_por_metodo_y_dia_semana', methods=['POST'])
def api_traer_datos_por_metodo_y_dia_semana():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')
    metodo = data.get('metodo')
    dias = data.get('dias')  # Debe ser una lista de nombres o números de día

    if not anio or not semana or not metodo or not dias or not isinstance(dias, list):
        return jsonify({"error": "Faltan datos o formato incorrecto"}), 400
    
    datos = traer_datos_por_metodo_y_dia_semana(anio, semana, metodo, dias)
    return jsonify({"ventas_por_dia_metodo": datos})

@app.route('/api/traer_ventas_totales_semana', methods=['POST'])
def api_traer_ventas_totales_semana():
    data = request.json
    anio = data.get('anio')
    semana = data.get('semana')
    if not anio or not semana:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_ventas_totales_semana(anio, semana)
    return jsonify({"total_ventas_semana": total})

@app.route('/api/traer_ventas_totales_periodo', methods=['POST'])
def api_traer_ventas_totales_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
  
    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_ventas_totales_periodo(periodo1, periodo2)
    return jsonify({"total_ventas_periodo": total})

@app.route('/api/traer_numero_de_ventas_periodo', methods=['POST'])
def api_traer_numero_de_ventas_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
    
    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_numero_de_ventas_periodo(periodo1, periodo2)
    return jsonify({"numero_ventas_periodo": total})

@app.route('/api/traer_venta_promedio_periodo', methods=['POST'])
def api_traer_venta_promedio_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')

    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    promedio = traer_venta_promedio_periodo(periodo1, periodo2)
    return jsonify({"venta_promedio_periodo": promedio})


@app.route('/api/traer_ganancias_totales_periodo', methods=['POST'])
def api_traer_ganancias_totales_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
    
    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_ganancias_totales_periodo(periodo1, periodo2)
    return jsonify({"total_ganancias_periodo": total})


@app.route('/api/traer_ventas_periodo', methods=['POST'])
def api_traer_ventas_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    ventas = traer_ventas_periodo(periodo1, periodo2)
    return jsonify({"ventas_por_dia": ventas})


@app.route('/api/traer_ganancias_periodo', methods=['POST'])
def api_traer_ganancias_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
   
    if not periodo1 or not periodo2:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_ganancias_periodo(periodo1, periodo2)
    return jsonify({"total_ganancias_periodo": total})

@app.route('/api/traer_datos_por_metodo_y_dia_periodo', methods=['POST'])
def api_traer_datos_por_metodo_y_dia_periodo():
    data = request.json
    periodo1 = data.get('periodo1')
    periodo2 = data.get('periodo2')
    metodo = data.get('metodo')
    
    if not periodo1 or not periodo2 or not metodo:
        return jsonify({"error": "Faltan datos"}), 400
    
    total = traer_datos_por_metodo_y_dia_periodo(periodo1, periodo2, metodo)
    return jsonify({"total_ventas_metodo_periodo": total})

@app.route('/api/verificar_existencia_de_mp', methods=['GET'])
def api_verificar_existencia_de_mp():
    existe = verificar_existencia_de_mp()
    return jsonify({"existe": existe})

@app.route('/api/agregar_mp_default', methods=['POST'])
def api_agregar_mp_default():

    agregar_mp_default()
    return jsonify({"resultado": "Métodos de pago por defecto agregados"})


@app.route('/api/borrar_mp_db', methods=['POST'])
def api_borrar_mp_db():
    data = request.json
    nombre_mp = data.get('nombre_mp')
    uid = data.get('uid')
    if not nombre_mp or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = borrar_mp_db(nombre_mp)
    return jsonify({"borrado": resultado})

@app.route('/api/actualizar_cantidad_productos', methods=['POST'])
def api_actualizar_cantidad_productos():
    data = request.json
    productos_seleccionados = data.get('productos_seleccionados')
    m = data.get('m')
    s = data.get('s', False)
    if productos_seleccionados is None or m is None:
        return jsonify({"exito": False, "error": "Faltan datos"}), 400

    try:
        exito = actualizar_cantidad_productos(productos_seleccionados, m, s)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500

@app.route('/api/agregar_a_registro', methods=['POST'])
def api_agregar_a_registro():
    data = request.json
    productos_seleccionados = data.get('productos_seleccionados')
    s = data.get('s')
    usuario_activo = data.get('usuario_activo')
    if productos_seleccionados is None or s is None or usuario_activo is None:
        return jsonify({"exito": False, "error": "Faltan datos"}), 400

    try:
        exito = agregar_a_registro(productos_seleccionados, s, usuario_activo)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500

@app.route('/api/traer_precio_compra', methods=['POST'])
def api_traer_precio_compra():
    data = request.json
    nombre = data.get('nombre')
    uid = data.get('uid')
    if not nombre or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    precio = traer_precio_compra(nombre)
    return jsonify({"precio_compra": precio})

@app.route('/api/traer_mp', methods=['POST'])
def api_traer_mp():
    data = request.json
    nombre_mp = data.get('nombre_mp')
    uid = data.get('uid')
    if not nombre_mp or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    id_mp = traer_mp(nombre_mp)
    return jsonify({"id_mp": id_mp})

@app.route('/api/agregar_mp_db', methods=['POST'])
def api_agregar_mp_db():
    data = request.json
    nombre_mp = data.get('nombre_mp')
    uid = data.get('uid')
    if not nombre_mp or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = agregar_mp_db(nombre_mp)
    return jsonify({"agregado": resultado})

@app.route('/api/movimiento_agregar_categoria', methods=['POST'])
def api_movimiento_agregar_categoria():
    data = request.json
    nombre_categoria = data.get('nombre_categoria')
    usuario_activo = data.get('usuario_activo')
    if not nombre_categoria or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_agregar_categoria(nombre_categoria, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_ultimo_agregado_anotador', methods=['POST'])
def api_traer_ultimo_agregado_anotador():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    contenido = traer_ultimo_agregado_anotador()
    return jsonify({"contenido": contenido})

@app.route('/api/set_text_principal', methods=['POST'])
def api_set_text_principal():
    data = request.json
    usuario = data.get('usuario')
    uid = data.get('uid')
    if not usuario or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    set_text_principal(usuario)
    return jsonify({"resultado": "Texto principal inicializado"})

@app.route('/api/guardar_texto_anotador', methods=['POST'])
def api_guardar_texto_anotador():
    data = request.json
    texto = data.get('texto')
    usuario = data.get('usuario')
    if texto is None or usuario is None:
        return jsonify({"exito": False, "error": "Faltan datos"}), 400

    try:
        exito = guardar_texto_anotador_sincrono(texto, usuario)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500


@app.route('/api/limpiar_anotaciones', methods=['POST'])
def api_limpiar_anotaciones():
    try:
        exito = limpiar_anotaciones_automatico()
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500


@app.route('/api/traer_todos_los_productos', methods=['GET'])
def api_traer_todos_los_productos():
    try:
        productos = traer_todos_los_productos()
        return jsonify({"productos": productos})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/cargar_movimiento_producto_agregado', methods=['POST'])
def api_cargar_movimiento_producto_agregado():
    data = request.json
    input_id_value = data.get('input_id_value')
    usuario = data.get('usuario')
    if not input_id_value or not usuario:
        return jsonify({"error": "Faltan datos"}), 400
    cargar_movimiento_producto_agregado(input_id_value, usuario)
    return jsonify({"resultado": "Movimiento de producto agregado registrado"})


@app.route('/api/movimiento_producto_borrado', methods=['POST'])
def api_movimiento_producto_borrado():
    data = request.json
    borrar_id = data.get('_borrar_id')
    input_nombre_o_id_value = data.get('input_nombre_o_id_value')
    usuario_activo = data.get('usuario_activo')
    if not borrar_id or not input_nombre_o_id_value or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_producto_borrado(borrar_id, input_nombre_o_id_value, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_aumento_precios', methods=['POST'])
def api_movimiento_aumento_precios():
    data = request.json
    categoria_o_proveedor = data.get('categoria_o_proveedor')
    usuario = data.get('usuario')
    es_categoria = data.get('es_categoria')
    if not categoria_o_proveedor or not usuario or es_categoria is None:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_aumento_precios(categoria_o_proveedor, usuario, es_categoria)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_producto_editado', methods=['POST'])
def api_movimiento_producto_editado():
    data = request.json
    id_producto = data.get('id_producto')
    usuario_activo = data.get('usuario_activo')
    if not id_producto or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_producto_editado(id_producto, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/agregar_proveedor', methods=['POST'])
def api_agregar_proveedor():
    data = request.json
    nombre = data.get('nombre')
    telefono = data.get('telefono')
    direccion = data.get('direccion')
    if not nombre or not telefono:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        exito = cargar_proveedor(nombre, telefono, direccion)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/movimiento_agregar_proveedor', methods=['POST'])
def api_movimiento_agregar_proveedor():
    data = request.json
    nombre = data.get('nombre')
    usuario_activo = data.get('usuario_activo')
    if not nombre or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_agregar_proveedor(nombre, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/movimiento_proveedor_borrado', methods=['POST'])
def api_movimiento_proveedor_borrado():
    data = request.json
    nombre = data.get('nombre')
    id_proveedor = data.get('id_proveedor')
    usuario_activo = data.get('usuario_activo')
    if not nombre or not id_proveedor or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_proveedor_borrado(nombre, id_proveedor, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_proveedor_editado', methods=['POST'])
def api_movimiento_proveedor_editado():
    data = request.json
    nombre = data.get('nombre')
    usuario_activo = data.get('usuario_activo')
    if not nombre or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_proveedor_editado(nombre, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/agregar_categoria', methods=['POST'])
def api_agregar_categoria():
    data = request.json
    nombre_categoria = data.get('nombre_categoria')
    if not nombre_categoria:
        return jsonify({"error": "Falta el nombre de la categoría"}), 400
    try:
        exito = cargar_categoria(nombre_categoria)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_categoria_borrada', methods=['POST'])
def api_movimiento_categoria_borrada():
    data = request.json
    nombre_categoria = data.get('nombre_categoria')
    id_categoria = data.get('id_categoria')
    usuario_activo = data.get('usuario_activo')
    if not nombre_categoria or not id_categoria or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_categoria_borrada(nombre_categoria, id_categoria, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/cargar_movimientos_datos_borrados', methods=['POST'])
def api_cargar_movimientos_datos_borrados():
    data = request.json
    usuario_activo = data.get('usuario_activo')
    if not usuario_activo:
        return jsonify({"error": "Falta el usuario activo"}), 400
    try:
        cargar_movimientos_datos_borrados(usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_editar_usuario', methods=['POST'])
def api_movimiento_editar_usuario():
    data = request.json
    id_usuario = data.get('id_usuario')
    nombre_usuario = data.get('nombre_usuario')
    usuario_activo = data.get('usuario_activo')
    if not id_usuario or not nombre_usuario or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_editar_usuario(id_usuario, nombre_usuario, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/movimiento_usuario_borrado', methods=['POST'])
def api_movimiento_usuario_borrado():
    data = request.json
    nombre_usuario = data.get('nombre_usuario')
    id_usuario = data.get('id_usuario')
    usuario_activo = data.get('usuario_activo')
    if not nombre_usuario or not id_usuario or not usuario_activo:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        cargar_movimiento_usuario_borrado(nombre_usuario, id_usuario, usuario_activo)
        return jsonify({"exito": True})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_id_venta', methods=['POST'])
def api_traer_id_venta():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    id_venta = traer_id_venta()
    return jsonify({"id_venta": id_venta})

@app.route('/api/traer_id_compra', methods=['POST'])
def api_traer_id_compra():
    data = request.json
    uid = data.get('uid')
    if not uid:
        return jsonify({"error": "Falta UID"}), 400
    
    id_compra = traer_id_compra()
    return jsonify({"id_compra": id_compra})

@app.route('/api/traer_prod_vendido', methods=['POST'])
def api_traer_prod_vendido():
    data = request.json
    id_venta = data.get('id_venta')
    uid = data.get('uid')
    if not id_venta or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    id_producto = traer_prod_vendido(id_venta)
    return jsonify({"id_producto": id_producto})


@app.route('/api/traer_prod_compra', methods=['POST'])
def api_traer_prod_compra():
    data = request.json
    id_compra = data.get('id_compra')
    uid = data.get('uid')
    if not id_compra or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    id_producto = traer_prod_compra(id_compra)
    return jsonify({"id_producto": id_producto})

@app.route('/api/cargar_movimiento_venta', methods=['POST'])
def api_cargar_movimiento_venta():
    data = request.json
    usuario = data.get('usuario')

    if not usuario:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = cargar_movimiento_venta(usuario)
    return jsonify({"resultado": resultado})

@app.route('/api/cargar_movimiento_agregar_metodo_pago', methods=['POST'])
def api_cargar_movimiento_agregar_metodo_pago():
    data = request.json
    metodo_pago = data.get('metodo_pago')
    usuario = data.get('usuario')
    if not metodo_pago or not usuario:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = cargar_movimiento_agregar_metodo_pago(metodo_pago, usuario)
    return jsonify({"resultado": resultado})

@app.route('/api/agregar_metodo_pago', methods=['POST'])
def api_agregar_metodo_pago():
    data = request.json
    nombre_metodo = data.get('nombre_metodo')
    if not nombre_metodo:
        return jsonify({"exito": False, "error": "Falta el nombre del método"}), 400

    exito = agregar_mp_db(nombre_metodo)
    return jsonify({"exito": exito})

@app.route('/api/borrar_metodo_pago', methods=['POST'])
def api_borrar_metodo_pago():
    data = request.json
    nombre_metodo = data.get('nombre_metodo')
    if not nombre_metodo:
        return jsonify({"exito": False, "error": "Falta el nombre del método"}), 400
    try:
        exito = borrar_mp_db(nombre_metodo)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500
    
@app.route('/api/traer_ultimo_texto_anotador', methods=['GET'])
def api_traer_ultimo_texto_anotador():
    try:
        ultimo_texto = traer_ultimo_agregado_anotador()
        return jsonify({"ultimo_texto": ultimo_texto})
    except Exception as e:
        return jsonify({"ultimo_texto": ""}), 500
    
@app.route('/api/set_texto_principal_anotador', methods=['POST'])
def api_set_texto_principal_anotador():
    data = request.json
    usuario = data.get('usuario')
    if not usuario:
        return jsonify({"exito": False, "error": "Falta el usuario"}), 400

    try:
        exito = set_text_principal(usuario)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500

@app.route('/api/cargar_movimiento_borrar_metodo_pago', methods=['POST'])
def api_cargar_movimiento_borrar_metodo_pago():
    data = request.json
    metodo_pago = data.get('metodo_pago')
    usuario = data.get('usuario')
    id_metodo = data.get('id')
    
    if not metodo_pago or not usuario or id_metodo is None:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = cargar_movimiento_borrar_metodo_pago(metodo_pago, usuario, id_metodo)
    return jsonify({"resultado": resultado})


@app.route('/api/cargar_movimiento_compra', methods=['POST'])
def api_cargar_movimiento_compra():
    data = request.json
    usuario = data.get('usuario')

    if not usuario:
        return jsonify({"error": "Faltan datos"}), 400
    
    resultado = cargar_movimiento_compra(usuario)
    return jsonify({"resultado": resultado})

@app.route('/api/traer_rol_usuario', methods=['POST'])
def api_traer_rol_usuario():
    data = request.json
    usuario = data.get('usuario')
    uid = data.get('uid')
    if not usuario or not uid:
        return jsonify({"error": "Faltan datos"}), 400
    
    rol = traer_rol_usuario(usuario)
    return jsonify({"rol_admin": rol})

@app.route('/api/cargar_movimiento_inicio', methods=['POST'])
def api_cargar_movimiento_inicio():
    data = request.json
    usuario = data.get('usuario')
    if not usuario:
        return jsonify({"exito": False, "error": "Falta el usuario"}), 400

    try:
        exito = cargar_movimiento_inicio(usuario)
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"exito": False, "error": str(e)}), 500
    


@app.route('/api/categorias', methods=['GET'])
def api_categorias():
    categorias = traer_categorias()
    if not categorias:
        crear_categuno()
        categorias = traer_categorias()
    return jsonify({"categorias": categorias})

@app.route('/api/proveedores', methods=['GET'])
def api_proveedores():
    proveedores = traer_proveedor()
    if not proveedores:
        crear_provuno()
        proveedores = traer_proveedor()
    return jsonify({"proveedores": proveedores})

@app.route('/api/agregar_producto', methods=['POST'])
def api_agregar_producto():
    data = request.json
    # data es un diccionario con los campos del producto
    exito = cargar_producto(
        data.get("id_producto"),
        data.get("nombre_producto"),
        data.get("precio_compra_producto"),
        data.get("precio_venta_producto"),
        data.get("cantidad_producto"),
        data.get("stock_ideal"),
        data.get("categoria_producto"),
        data.get("proveedor_producto")
    )
    return jsonify({"exito": exito})

@app.route('/api/borrar_producto', methods=['POST'])
def api_borrar_producto():
    data = request.json
    valor = data.get('valor')
    if not valor:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        exito = buscar_producto(valor)  # O tu función real de borrado
        return jsonify({"exito": exito})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/traer_producto_por_id', methods=['POST'])
def api_traer_producto_por_id():
    data = request.json
    id_producto = data.get('id_producto')
    if not id_producto:
        return jsonify({"error": "Faltan datos"}), 400
    try:
        producto = traer_datosproducto_por_id(id_producto)
        return jsonify({"producto": producto})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/traer_anios_con_datos', methods=['GET'])
def api_traer_anios_con_datos():
    anios = traer_anios()  # Debe devolver una lista de años con datos
    return jsonify({"anios": anios})

    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
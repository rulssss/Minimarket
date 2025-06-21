from archivos_py.db.connection import get_connection
from psycopg2 import errors
from datetime import datetime



def traer_categorias():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT id_categoria, nombre_descrip FROM categorias ORDER BY id_categoria"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    conn.commit() 
    cursor.close()
    conn.close()

    return data

def crear_categuno():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"INSERT INTO categorias(id_categoria, nombre_descrip) VALUES(1, 'Sin categoría')"
    cursor.execute(query_data2)
    cursor.close()
    conn.commit()
    conn.close()

    

def crear_provuno():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"INSERT INTO proveedores(id_proveedor, nombre_proveedor, telefono) VALUES(1, 'Proveedor1', '123456789')"
    cursor.execute(query_data2)
    cursor.close()
    conn.commit()
    conn.close()


def cargar_producto(id_producto, nombre_producto, precio_compra_producto, precio_venta_producto, cantidad_producto, stock_ideal, categoria_producto, proveedor_producto):
    
    categoria_producto = traer_id_categoria(categoria_producto)
    proveedor_producto = traer_id_proveedor(proveedor_producto)
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"INSERT INTO productos(id_producto, nombre, precio_de_compra, precio_de_venta, stock, id_categoria, id_proveedor, stock_ideal) VALUES({id_producto}, '{nombre_producto}', {precio_compra_producto}, {precio_venta_producto}, {cantidad_producto}, {categoria_producto}, {proveedor_producto}, {stock_ideal})"
    #verifcacion de que el producto existe
    try:
        cursor.execute(query_data2)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except errors.UniqueViolation:
        cursor.close()
        conn.close()
        return False
    
def traer_id_categoria(categoria_producto):
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT id_categoria FROM categorias WHERE nombre_descrip = '{categoria_producto}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0]

def traer_id_proveedor(proveedor_producto):
    try:

        conn = get_connection()
        cursor= conn.cursor()
        query_data2 = f"SELECT id_proveedor FROM proveedores WHERE nombre_proveedor = '{proveedor_producto}'"
        cursor.execute(query_data2)
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return data[0][0]
    
    except IndexError:
        cursor.close()
        conn.close()
        return None

def traer_id_usuario(usuario):

    try:
        conn = get_connection()
        cursor = conn.cursor()
        query_id_usuario = f"SELECT id_usuario FROM usuarios WHERE nombre = '{usuario}'"
        cursor.execute(query_id_usuario)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data[0][0]
    except IndexError:
        return None

def traer_nom_producto(dato):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query_nombre = f"SELECT nombre FROM productos WHERE id_producto = {dato}"
        cursor.execute(query_nombre)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data[0][0]
    except IndexError:
        cursor.close()
        conn.close()
        return None


def buscar_producto(nombre_prod_o_id):
    conn = get_connection()
    cursor= conn.cursor()

    if nombre_prod_o_id.isdigit():
        query_data2 = f"SELECT EXISTS (SELECT 1 FROM productos WHERE id_producto = {nombre_prod_o_id}) AS existe"
        cursor.execute(query_data2)
        data = cursor.fetchone()[0]
        if data:
            query_data3 = f"DELETE FROM productos WHERE id_producto = '{nombre_prod_o_id}'"
            cursor.execute(query_data3)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()
            return False

    else:

        query_data2 = f"SELECT EXISTS (SELECT 1 FROM productos WHERE nombre = '{nombre_prod_o_id}') AS existe" # ve si existe y devuelve true o false, ver el fetchone
        cursor.execute(query_data2)
        data = cursor.fetchone()[0]
    
        if data:
            query_data3 = f"DELETE FROM productos WHERE nombre = '{nombre_prod_o_id}'"
            cursor.execute(query_data3)
            conn.commit()
            cursor.close()
            conn.close()
            return True

        else:
            cursor.close()
            conn.close()
            return False
        
def traer_id_producto(nombre):
    conn = get_connection()
    cursor= conn.cursor()

    try:
        query_data2 = f"SELECT id_producto FROM productos WHERE nombre = '{nombre}'"
        cursor.execute(query_data2)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data[0][0]
    except IndexError:
        cursor.close()
        conn.close()
        return None


def aumentar_precios_categoria(precio_compra, precio_venta, nombre):
    id_categoria = traer_id_categoria(nombre)
    conn = get_connection()
    cursor = conn.cursor()
    query_compra = """
        UPDATE productos
        SET precio_de_compra = precio_de_compra * (1 + %s / 100.0)
        WHERE id_categoria = %s
    """
    cursor.execute(query_compra, (precio_compra, id_categoria))
    query_venta = """
        UPDATE productos
        SET precio_de_venta = precio_de_venta * (1 + %s / 100.0)
        WHERE id_categoria = %s
    """
    cursor.execute(query_venta, (precio_venta, id_categoria))
    conn.commit()
    cursor.close()
    conn.close()

def aumentar_precios_proveedor(precio_compra, precio_venta, nombre):
    """
    Aumenta los precios de compra y venta de todos los productos de un proveedor en un porcentaje dado.
    precio_compra y precio_venta pueden ser decimales (ej: 5.5 para 5,5%).
    nombre es el nombre del proveedor.
    """
    id_proveedor = traer_id_proveedor(nombre)
    conn = get_connection()
    cursor = conn.cursor()
    query_compra = """
        UPDATE productos
        SET precio_de_compra = precio_de_compra * (1 + %s / 100.0)
        WHERE id_proveedor = %s
    """
    cursor.execute(query_compra, (precio_compra, id_proveedor))
    query_venta = """
        UPDATE productos
        SET precio_de_venta = precio_de_venta * (1 + %s / 100.0)
        WHERE id_proveedor = %s
    """
    cursor.execute(query_venta, (precio_venta, id_proveedor))
    conn.commit()
    conn.close()
    cursor.close()

def traer_datosproducto_por_id(barcode):
    conn = get_connection()
    cursor= conn.cursor()

    if barcode != "":
        query_data2 = f"SELECT p.id_producto, p.nombre, p.precio_de_compra, p.precio_de_venta, p.stock, p.stock_ideal, c.nombre_descrip, pr.nombre_proveedor FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor WHERE p.id_producto = {barcode}"
        cursor.execute(query_data2)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        if data != []:
            return data[0]
        else: 
            return False
    else:
        return False
    
def actualizar_producto(id, nombre_prdoucto, precio_compra_producto, precio_venta_producto, stock, stock_ideal, categoria_producto, proveedor_producto):
    
    categoria_producto = traer_id_categoria(categoria_producto)
    proveedor_producto = traer_id_proveedor(proveedor_producto)
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"UPDATE productos SET nombre = '{nombre_prdoucto}', precio_de_compra = {precio_compra_producto}, precio_de_venta = {precio_venta_producto}, stock = {stock}, stock_ideal = {stock_ideal}, id_categoria = {categoria_producto}, id_proveedor = {proveedor_producto} WHERE id_producto = {id}"
    cursor.execute(query_data2)
    conn.commit()
    cursor.close()
    conn.close()
    


def cargar_proveedor(nombre_producto, num_telefono, mail):
    try: 
        conn = get_connection()
        cursor= conn.cursor()
        query_data2 = f"INSERT INTO proveedores(nombre_proveedor, telefono, mail) VALUES('{nombre_producto}', {num_telefono}, '{mail}')"

        cursor.execute(query_data2)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    except TypeError:
        cursor.close()
        conn.close()
        return False
    
def buscar_proveedor(nombre_prov):
    conn = get_connection()
    if nombre_prov != "Proveedor1":
        cursor= conn.cursor()
    
        query_data3 = f"DELETE FROM proveedores WHERE nombre_proveedor = '{nombre_prov}'"
        cursor.execute(query_data3)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    return False

def actualizar_proveedor(nombre_proveedor, num_proveedor, mail_producto):
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"UPDATE proveedores SET telefono = {num_proveedor}, mail = '{mail_producto}' WHERE nombre_proveedor = '{nombre_proveedor}'"
    cursor.execute(query_data2)
    conn.commit()
    cursor.close()
    conn.close()
    return True



# distinto de traeer proveedores ya que la enterior solo extrae sus nombres
def traer_proveedor():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT nombre_proveedor, telefono, mail FROM proveedores"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def cargar_categoria(nombre_categoria):
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"INSERT INTO categorias(nombre_descrip) VALUES('{nombre_categoria}')"

    try:
        cursor.execute(query_data2)
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except errors.UniqueViolation:
        return False
    

def buscar_categoria(nombre_cat):
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT EXISTS (SELECT 1 FROM categorias WHERE nombre_descrip = '{nombre_cat}') AS existe" # ve si existe y devuelve true o false, ver el fetchone
    cursor.execute(query_data2)
    data = cursor.fetchone()[0]
    
    
    if data:
        try:
            
            query_update_data= f"DELETE FROM categorias WHERE nombre_descrip = '{nombre_cat}'"
            cursor.execute(query_update_data)
            cursor.close()
            conn.commit()
            conn.close()
            return True
        
        except errors.ForeignKeyViolation:
            
            # Actualizar todos los productos a "sin categoría"
            query_update_products = f"UPDATE productos SET id_categoria = 1 WHERE id_categoria = {traer_id_categoria(nombre_cat)}"
            cursor.execute(query_update_products)
            # Intentar nuevamente el DELETE
            query_update_data2= f"DELETE FROM categorias WHERE nombre_descrip = '{nombre_cat}'"
            cursor.execute(query_update_data2)
            cursor.close()
            conn.commit()
            conn.close()
            return True
        
    else: 
        cursor.close()
        return False


def clear_data(borrar_categorias, borrar_ventas_compras, borrar_proveedores, borrar_usuarios, borrar_movimientos):
    
    v = True #ventana_confirmacion()
    conn = get_connection()
    cursor = conn.cursor()
    if v:
        

        if borrar_categorias:
            try:
                query_update_data = "DELETE FROM categorias WHERE id_categoria != 1"
                cursor.execute(query_update_data)
                
            except errors.ForeignKeyViolation:
                # Actualizar todos los productos a "sin categoría"
                query_update_products = "UPDATE productos SET id_categoria = 1 WHERE id_categoria != 1"
                cursor.execute(query_update_products)
                # Intentar nuevamente el DELETE
                query_update_data2 = "DELETE FROM categorias WHERE id_categoria != 1"
                cursor.execute(query_update_data2)      

        if borrar_ventas_compras:
            # Lógica para borrar ventas, compras y sus detalles
            query_update_data5 = f"DELETE FROM ventas"
            cursor.execute(query_update_data5)
            query_update_data2 = f"DELETE FROM detalle_ventas"
            cursor.execute(query_update_data2)
            query_update_data6 = f"DELETE FROM compras"
            cursor.execute(query_update_data6)
            query_update_data4 = f"DELETE FROM detalle_compras"
            cursor.execute(query_update_data4)

        if borrar_proveedores:

            # Lógica para borrar proveedores y sus productos
            query_update_data3 = f"DELETE FROM proveedores CASCADE"
            cursor.execute(query_update_data3)

        if borrar_usuarios:
            # Lógica para borrar usuarios y sus contraseñas
            query_update_data3 = f"DELETE FROM contrasenas"
            cursor.execute(query_update_data3)
            query_update_data3 = f"DELETE FROM usuarios"
            cursor.execute(query_update_data3)

            query_update_data4 = "DELETE FROM metodos_pago CASCADE"
            cursor.execute(query_update_data4)

        if borrar_movimientos:
            query_delete_movimientos = "DELETE FROM movimientos"
            cursor.execute(query_delete_movimientos)
        
    
    conn.commit()        
    cursor.close()
    conn.close()


def traer_todos_los_usuarios():
    conn = get_connection()
    cursor = conn.cursor()
    query_data = f"SELECT usuarios.id_usuario, usuarios.nombre, usuarios.mail, usuarios.admin, contrasenas.contrasena FROM usuarios JOIN contrasenas ON usuarios.id_usuario = contrasenas.id_usuario"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    if data != []:
        return data
    else: 
        return False


def agregar_a_registro_usuario(tipo_usuario, nombre, contrasenia, mail):
    if tipo_usuario == "Administrador":
        tipo_usuario = True
    else:
        tipo_usuario = False     #Aacomoda la variable account a un true o false para verificar que tipo de cuenta es
    
    
    try:
        # Conexión a la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        query_data1 = f"INSERT INTO usuarios(nombre, admin, mail) VALUES('{nombre}', {tipo_usuario}, '{mail}')"
        cursor.execute(query_data1)

        cursor = conn.cursor()
        query_data = f"SELECT id_usuario FROM usuarios WHERE nombre = '{nombre}'"
        cursor.execute(query_data)
        data_id = cursor.fetchall()


        query_data2 = f"INSERT INTO contrasenas(id_usuario, contrasena) VALUES({data_id[0][0]}, '{contrasenia}')"
        cursor.execute(query_data2)
        cursor.close()
        conn.commit()
        conn.close()
        return True # devuelve true si se registro correctamente
    
    except errors.UniqueViolation:
        cursor.close()
        conn.close()
        return False
    
def cargar_movimiento_agregar_usuario(nombre_usuario, usuario_activo):
                
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Agregar', 'Usuarios', {id_usuario}, 'Usuario agregado: {nombre_usuario}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()


def actualizar_usuario(id, tipo_usuario, contrasenia, mail):

    if tipo_usuario == "Administrador":
        tipo_usuario = True
    else:
        tipo_usuario = False     #Aacomoda la variable account a un true o false para verificar que tipo de cuenta es
    try:
        conn = get_connection()
        cursor= conn.cursor()
        query_data = f"UPDATE usuarios SET admin = {tipo_usuario}, mail = '{mail}' WHERE id_usuario = {id}"
        cursor.execute(query_data)

        query_data2 = f"UPDATE contrasenas SET contrasena = '{contrasenia}' WHERE id_usuario = {id}"
        cursor.execute(query_data2)
        cursor.close()
        conn.commit()
        conn.close()
        return True # devuelve true si se registro correctamente
    except errors.UniqueViolation:
        cursor.close()
        return False

def borrar_usuario(usuario):

    conn = get_connection()
    cursor = conn.cursor()
    # Buscar el id del usuario por su nombre
    query_id_usuario = f"SELECT id_usuario FROM usuarios WHERE nombre = '{usuario}'"
    cursor.execute(query_id_usuario)
    data = cursor.fetchall()

    if data:
        id_usuario = data[0][0]

        # Borrar la contraseña asociada al id del usuario
        query_delete_password = f"DELETE FROM contrasenas WHERE id_usuario = {id_usuario}"
        cursor.execute(query_delete_password)

        # Borrar el usuario por su id
        query_delete_user = f"DELETE FROM usuarios WHERE id_usuario = {id_usuario}"
        cursor.execute(query_delete_user)
        conn.commit()
        conn.close()
        cursor.close()
        return True  # Retorna True si se borró correctamente
    else:
        conn.close()
        cursor.close()
        return False  # Retorna False si no se encontró el usuario
    

# MOVIMIENTOS:

def cargar_movimiento_producto_agregado(input_id_value, usuario):

    id_usuario = traer_id_usuario(usuario)
    nombre_producto = traer_nom_producto(input_id_value)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Agregar', 'Productos', {input_id_value}, 'Producto agregado: {nombre_producto}')"
    cursor.execute(query)
    cursor.close()
    conn.close()

def cargar_movimiento_producto_borrado(id, nombre, usuario_activo):

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Productos', {id}, 'Producto borrado: {nombre}')"
    cursor.execute(query)
    cursor.close()
    conn.close()

def cargar_movimiento_aumento_precios(combobox_20_value, usuario_activo, s):
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    if s:
        combobox_20_ID = traer_id_categoria(combobox_20_value)
    else:
        combobox_20_ID = traer_id_proveedor(combobox_20_value)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Aumento', 'Productos', {combobox_20_ID}, 'Aumento de precios de {combobox_20_value}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    

def cargar_movimiento_producto_editado(producto_id, usuario_activo):
        
    id_usuario = traer_id_usuario(usuario_activo)
    nombre_producto = traer_nom_producto(producto_id)
    fecha_hora = datetime.now().astimezone().isoformat()
    
    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Editar', 'Productos', {producto_id}, 'Producto editado: {nombre_producto}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()

def traer_todos_los_productos():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT id_producto, nombre, precio_de_compra, precio_de_venta, stock, stock_ideal, nombre_descrip, nombre_proveedor FROM productos JOIN categorias ON productos.id_categoria = categorias.id_categoria JOIN proveedores ON productos.id_proveedor = proveedores.id_proveedor ORDER BY productos.nombre"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def cargar_movimiento_agregar_proveedor(nombre_proveedor, usuario_activo):
        
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_proveedor = traer_id_proveedor(nombre_proveedor)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Agregar', 'Proveedores', {id_proveedor}, 'Proveedor agregado: {nombre_proveedor}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


def cargar_movimiento_proveedor_borrado(nombre_proveedor, id_proveedor, usuario_activo):
            
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Proveedores', {id_proveedor}, 'Proveedor borrado: {nombre_proveedor}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

def cargar_movimiento_proveedor_editado(nombre_proveedor, usuario_activo):
            
    id_usuario = traer_id_usuario(usuario_activo)
    id_proveedor = traer_id_proveedor(nombre_proveedor)
    fecha_hora = datetime.now().astimezone().isoformat()
    
    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Editar', 'Proveedores', {id_proveedor}, 'Proveedor editado: {nombre_proveedor}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()


def cargar_movimiento_agregar_categoria(lineEdit_16_value, usuario_activo):
            
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_categoria = traer_id_categoria(lineEdit_16_value)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Agregar', 'Categorias', {id_categoria}, 'Categoria agregada: {lineEdit_16_value}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

def cargar_movimiento_categoria_borrada(lineEdit_21_value, id_categoria, usuario_activo):
                
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Categorias', {id_categoria}, 'Categoria borrada: {lineEdit_21_value}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

def cargar_movimientos_datos_borrados(usuario_activo):
        
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Datos', NULL, 'Datos borrados')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()  


def cargar_movimiento_editar_usuario(id_usuario, nombre_usuario,usuario_activo):
                    
    id_usuario_activo = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario_activo}, '{fecha_hora}', 'Editar', 'Usuarios', {id_usuario}, 'Usuario editado: {nombre_usuario}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()

def cargar_movimiento_usuario_borrado(nombre_usuario, id_usuario, usuario_activo):
                    
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Usuarios', {id_usuario}, 'Usuario borrado: {nombre_usuario}')"
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close()
    
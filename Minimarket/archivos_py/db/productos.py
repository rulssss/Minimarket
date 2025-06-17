from archivos_py.db.connection import get_connection
from psycopg2 import errors
from datetime import datetime



def traer_categorias():
    conn = get_connection()
    cursor= conn.cursor()
    query_data2 = f"SELECT nombre_descrip FROM categorias ORDER BY id_categoria"
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

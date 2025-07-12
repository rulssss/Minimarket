from archivos_py.db.connection import get_connection
from psycopg2 import errors
from datetime import datetime

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
    

def traer_movimientos_por_usuario(usuario_seleccionado):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT m.id_usuario, m.fecha_hora, m.tipo_accion, m.entidad_afectada, m.descripcion FROM movimientos m INNER JOIN usuarios u ON m.id_usuario = u.id_usuario WHERE u.nombre = '{usuario_seleccionado}' ORDER BY m.fecha_hora DESC"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data  # Devuelve una lista con todos los movimientos realizados por el usuario seleccionado

def traer_movimientos_por_fecha(fecha_seleccionada):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT m.id_usuario, m.fecha_hora, m.tipo_accion, m.entidad_afectada, m.descripcion FROM movimientos m INNER JOIN usuarios u ON m.id_usuario = u.id_usuario WHERE DATE(m.fecha_hora) = '{fecha_seleccionada}' ORDER BY m.fecha_hora DESC"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data  # Devuelve una lista con todos los movimientos realizados en la fecha seleccionada

def traer_movimientos_por_accion(accion_seleccionada):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT m.id_usuario, m.fecha_hora, m.tipo_accion, m.entidad_afectada, m.descripcion FROM movimientos m INNER JOIN usuarios u ON m.id_usuario = u.id_usuario WHERE m.tipo_accion = '{accion_seleccionada}' ORDER BY m.fecha_hora DESC"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data  # Devuelve una lista con todos los movimientos realizados con la acción seleccionada

def traer_metodo_pago_id(valor):

    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT id_mp FROM metodos_pago WHERE nombre_mp = '{valor}'" #trae el id del metodo de pago
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data[0][0]

def traer_todos_metodos_pago():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT id_mp, nombre_mp FROM metodos_pago")
        metodos = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return metodos
    except Exception as e:
        print(f"Error al obtener métodos de pago: {e}")
        return []
    


def traer_datos_ventas_metodo_o_usuario(id, fecha):
    conn = get_connection()
    cursor = conn.cursor()

    if fecha and "-" in fecha:
        partes = fecha.split("-")
        anio = partes[0]
        mes = partes[1] if len(partes) > 1 else None
        dia = partes[2] if len(partes) > 2 else None
        
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = %s
        """
        parametros = [int(anio)]
        
        if mes:
            query += " AND EXTRACT(MONTH FROM v.fecha_hora) = %s"
            parametros.append(int(mes))
            
            if dia:
                query += " AND EXTRACT(DAY FROM v.fecha_hora) = %s"
                parametros.append(int(dia))
        
        query += " AND (v.id_usuario = %s OR v.id_metodo_pago = %s)"
        parametros.extend([id, id])
        cursor.execute(query, parametros)
        
    elif fecha:
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = %s
              AND (v.id_usuario = %s OR v.id_metodo_pago = %s)
        """
        cursor.execute(query, (int(fecha), id, id))
    else:
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE (v.id_usuario = %s OR v.id_metodo_pago = %s)
        """
        cursor.execute(query, (id, id))
    
    resultados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return resultados

def traer_datos_compras_metodo_o_usuario(id, fecha):
    conn = get_connection()
    cursor = conn.cursor()

    if fecha and "-" in fecha:
        partes = fecha.split("-")
        anio = partes[0]
        mes = partes[1] if len(partes) > 1 else None
        dia = partes[2] if len(partes) > 2 else None
        
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
            WHERE EXTRACT(YEAR FROM c.fecha_hora) = %s
        """
        parametros = [int(anio)]
        
        if mes:
            query += " AND EXTRACT(MONTH FROM c.fecha_hora) = %s"
            parametros.append(int(mes))
            
            if dia:
                query += " AND EXTRACT(DAY FROM c.fecha_hora) = %s"
                parametros.append(int(dia))
        
        query += " AND (c.id_usuario = %s OR c.id_metodo_pago = %s)"
        parametros.extend([id, id])
        cursor.execute(query, parametros)
        
    elif fecha:
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
            WHERE EXTRACT(YEAR FROM c.fecha_hora) = %s
              AND (c.id_usuario = %s OR c.id_metodo_pago = %s)
        """
        cursor.execute(query, (int(fecha), id, id))
    else:
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
            WHERE (c.id_usuario = %s OR c.id_metodo_pago = %s)
        """
        cursor.execute(query, (id, id))
    
    resultados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return resultados


def traer_metodo_pago(metodo): #traer el nombre del metodo de pago a traves del id
    conn = get_connection()
    cursor = conn.cursor()
    query_nombre = f"SELECT nombre_mp FROM metodos_pago WHERE id_mp = {metodo}"
    cursor.execute(query_nombre)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data[0][0]



def traer_datos_arqueo_ventas_fecha(fecha):

    conn = get_connection()
    cursor = conn.cursor()
    
    if fecha and "-" in fecha:
        partes = fecha.split("-")
        anio = partes[0]
        mes = partes[1] if len(partes) > 1 else None
        dia = partes[2] if len(partes) > 2 else None
        
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = %s
        """
        parametros = [int(anio)]
        
        if mes:
            query += " AND EXTRACT(MONTH FROM v.fecha_hora) = %s"
            parametros.append(int(mes))
            
            if dia:
                query += " AND EXTRACT(DAY FROM v.fecha_hora) = %s"
                parametros.append(int(dia))
        
        cursor.execute(query, parametros)
        
    elif fecha:
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = %s
        """
        cursor.execute(query, (int(fecha),))
    else:
        query = """
            SELECT v.id_usuario, v.fecha_hora, v.id_metodo_pago, 
                   dv.id_producto, dv.cantidad, dv.precio_unitario_venta
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        """
        cursor.execute(query)

    resultados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return resultados

def traer_datos_arqueo_compras_fecha(fecha):
    conn = get_connection()
    cursor = conn.cursor()

    if fecha and "-" in fecha:
        partes = fecha.split("-")
        anio = partes[0]
        mes = partes[1] if len(partes) > 1 else None
        dia = partes[2] if len(partes) > 2 else None
        
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
            WHERE EXTRACT(YEAR FROM c.fecha_hora) = %s
        """
        parametros = [int(anio)]
        
        if mes:
            query += " AND EXTRACT(MONTH FROM c.fecha_hora) = %s"
            parametros.append(int(mes))
            
            if dia:
                query += " AND EXTRACT(DAY FROM c.fecha_hora) = %s"
                parametros.append(int(dia))
        
        cursor.execute(query, parametros)
        
    elif fecha:
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
            WHERE EXTRACT(YEAR FROM c.fecha_hora) = %s
        """
        cursor.execute(query, (int(fecha),))
    else:
        query = """
            SELECT c.id_usuario, c.fecha_hora, c.id_metodo_pago,
                   dc.id_producto, dc.cantidad, dc.precio_unitario
            FROM compras c
            INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        """
        cursor.execute(query)
    
    resultados = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return resultados


def traer_metodos_de_pago(): # trae todos los metodos de pago de la base de datos
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT nombre_mp FROM metodos_pago"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def traer_ventas_totales_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE DATE(v.fecha_hora) = '{fecha_selecc}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del dia actual


def traer_ganancias_totales_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE DATE(v.fecha_hora) = '{fecha_selecc}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del dia actual

def traer_compras_totales_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dc.precio_unitario * dc.cantidad)
        FROM compras c
        INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        WHERE DATE(c.fecha_hora) = '{fecha_selecc}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del dia actual

def traer_numero_de_compras_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM compras c
        WHERE DATE(c.fecha_hora) = '{fecha_selecc}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del dia actual

def traer_compras_totales_mes(anio, mes):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dc.precio_unitario * dc.cantidad)
        FROM compras c
        INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        WHERE EXTRACT(YEAR FROM c.fecha_hora) = {anio} AND EXTRACT(MONTH FROM c.fecha_hora) = {mes}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del mes actual

def traer_numero_de_compras_mes(anio, mes):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM compras c
        WHERE EXTRACT(YEAR FROM c.fecha_hora) = {anio} AND EXTRACT(MONTH FROM c.fecha_hora) = {mes}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del mes actual

def traer_compras_totales_ano_actual(anio):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dc.precio_unitario * dc.cantidad)
        FROM compras c
        INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        WHERE EXTRACT(YEAR FROM c.fecha_hora) = {anio}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del año actual

def traer_numero_de_compras_ano_actual(anio):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM compras c
        WHERE EXTRACT(YEAR FROM c.fecha_hora) = {anio}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de compras del año actual


def traer_ventas_por_metodo_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT v.id_metodo_pago, SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE DATE(v.fecha_hora) = '{fecha_selecc}'
        GROUP BY v.id_metodo_pago
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en un diccionario con el id del método de pago como clave y la suma como valor
    resultados = {row[0]: row[1] for row in data}
    return resultados  # Devuelve un diccionario con los resultados

def traer_compras_por_metodo_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT c.id_metodo_pago, SUM(dc.precio_unitario * dc.cantidad)
        FROM compras c
        INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        WHERE DATE(c.fecha_hora) = '{fecha_selecc}'
        GROUP BY c.id_metodo_pago
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en un diccionario con el id del método de pago como clave y la suma como valor
    resultados = {row[0]: row[1] for row in data}
    return resultados  # Devuelve un diccionario con los resultados

def traer_ventas_por_metodo_mes(anio, mes):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT v.id_metodo_pago, SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {anio} AND EXTRACT(MONTH FROM v.fecha_hora) = {mes}
        GROUP BY v.id_metodo_pago
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en un diccionario con el id del método de pago como clave y la suma como valor
    resultados = {row[0]: row[1] for row in data}
    return resultados  # Devuelve un diccionario con los resultados

def traer_compras_por_metodo_mes(anio, mes):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT c.id_metodo_pago, SUM(dc.precio_unitario * dc.cantidad)
        FROM compras c
        INNER JOIN detalle_compras dc ON c.id_compra = dc.id_compra
        WHERE EXTRACT(YEAR FROM c.fecha_hora) = {anio} AND EXTRACT(MONTH FROM c.fecha_hora) = {mes}
        GROUP BY c.id_metodo_pago
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en un diccionario con el id del método de pago como clave y la suma como valor
    resultados = {row[0]: row[1] for row in data}
    return resultados  # Devuelve un diccionario con los resultados

def traer_ventas_por_metodo_ano(anio):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT v.id_metodo_pago, SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {anio}
        GROUP BY v.id_metodo_pago
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en un diccionario con el id del método de pago como clave y la suma como valor
    resultados = {row[0]: row[1] for row in data}
    return resultados  # Devuelve un diccionario con los resultados


def traer_numero_de_ventas_ano(anio):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {anio}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del año actual

def traer_numero_de_ventas_mes(anio, mes):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {anio} AND EXTRACT(MONTH FROM v.fecha_hora) = {mes}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del mes actual

def traer_numero_de_ventas_dia(fecha_selecc):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE DATE(v.fecha_hora) = '{fecha_selecc}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del dia actual

def traer_ventas_totales_ano_actual(ano_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del año actual


def traer_ganancias_totales_ano_actual(ano_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del año actual

def traer_ganancias_totales_mes(ano_actual, mes_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del mes actual

def traer_ventas_totales_mes(ano_actual, mes_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del mes actual

def traer_numero_de_ventas_ano_actual(ano_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del año actual


def traer_venta_promedio_ano_actual(ano_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT AVG(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del año actual


def traer_ventas_ano_actual(ano_actual, meses):
    conn = get_connection()
    cursor = conn.cursor()
    ventas_por_mes = []

    global month_mapping

    for mes in meses:
        mes_numero = month_mapping.get(mes, mes)  # Map month name to number, or keep as is if already a number
        query = f"""
            SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
              AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_numero}
        """
        cursor.execute(query)
        data = cursor.fetchall()
        ventas_por_mes.append(data[0][0] if data[0][0] is not None else 0)
    
    cursor.close()
    conn.close()
    return ventas_por_mes  # devuelve una lista con las ventas de cada mes en orden


def traer_ganancias_ano_actual(ano_actual, meses):
    conn = get_connection()
    cursor = conn.cursor()
    ganancias_por_mes = []
    global month_mapping
    for mes in meses:
        mes_numero = month_mapping.get(mes, mes)  # Map month name to number, or keep as is if already a number
        query = f"""
            SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
              AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_numero}
        """
        cursor.execute(query)
        data = cursor.fetchall()
        ganancias_por_mes.append(data[0][0] if data[0][0] is not None else 0)
    cursor.close()
    conn.close()
    return ganancias_por_mes  # devuelve una lista con las ganancias de cada mes en orden

def traer_metodos_pago_y_su_id(): # trae todos los metodos de pago de la base de datos
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM metodos_pago"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def traer_datos_por_metodo_y_mes(ano_actual, metodo, meses):
    conn = get_connection()
    cursor = conn.cursor()
    datos_por_mes = []

    global month_mapping

    for mes in meses:
        mes_numero = month_mapping.get(mes, mes)  # Map month name to number, or keep as is if already a number
        query = f"""
            SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
              AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_numero}
              AND v.id_metodo_pago = {metodo}
        """
        cursor.execute(query)
        data = cursor.fetchall()
        datos_por_mes.append(data[0][0] if data[0][0] is not None else 0)
    
    cursor.close()
    conn.close()
    return datos_por_mes  # devuelve una lista con las ventas de cada mes en orden

def traer_venta_promedio_mes(ano_actual, mes_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT AVG(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(MONTH FROM v.fecha_hora) = {mes_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del mes actual

def traer_numero_de_ventas_semana(ano_actual, semana_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas de la semana actual

def traer_venta_promedio_semana(ano_actual, semana_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT AVG(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias de la semana actual

def traer_ganancias_totales_semana(ano_actual, semana_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias de la semana actual

def traer_ventas_semana_actual(ano_actual, semana_actual, dias_semana):
    conn = get_connection()
    cursor = conn.cursor()
    ventas_por_dia = []

    global day_mapping

    for dia in dias_semana:
        dia_numero = day_mapping.get(dia, dia)  # Map day name to number (1-7)
        query = """
            SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = %s
              AND EXTRACT(WEEK FROM v.fecha_hora) = %s
              AND EXTRACT(DOW FROM v.fecha_hora) = %s  -- PostgreSQL: 0=domingo, 1=lunes, ..., 6=sábado
        """
        cursor.execute(query, (ano_actual, semana_actual, dia_numero))
        data = cursor.fetchall()
        ventas_por_dia.append(data[0][0] if data[0][0] is not None else 0)

    conn.close()
    return ventas_por_dia  # Devuelve una lista con las ventas de cada día de la semana en orden

def traer_ganancias_semana_actual(ano_actual, semana_actual, dias_semana):
    conn = get_connection()
    cursor = conn.cursor()
    ganancias_por_dia = []

    global day_mapping

    for dia in dias_semana:
        dia_numero = day_mapping.get(dia, dia)  # Map day name to number (1-7)
        query = f"""
            SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
              AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
              AND EXTRACT(DOW FROM v.fecha_hora) = {dia_numero - 1}  -- PostgreSQL: 0=domingo, 1=lunes, ..., 6=sábado
        """
        cursor.execute(query)
        data = cursor.fetchall()
        ganancias_por_dia.append(data[0][0] if data[0][0] is not None else 0)
    
    conn.close()
    cursor.close()
    return ganancias_por_dia  # Devuelve una lista con las ganancias de cada día de la semana en orden

def traer_datos_por_metodo_y_dia_semana(ano_actual, semana_actual, id_metodo, dias_semana):
    conn = get_connection()
    cursor = conn.cursor()
    datos_por_dia = []

    global day_mapping

    for dia in dias_semana:
        dia_numero = day_mapping.get(dia, dia)  # Map day name to number (1-7)
        query = f"""
            SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
            FROM ventas v
            INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
            WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
              AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
              AND EXTRACT(DOW FROM v.fecha_hora) = {dia_numero - 1}  -- PostgreSQL: 0=domingo, 1=lunes, ..., 6=sábado
              AND v.id_metodo_pago = {id_metodo}
        """
        cursor.execute(query)
        data = cursor.fetchall()
        datos_por_dia.append(data[0][0] if data[0][0] is not None else 0)
    
    conn.close()
    cursor.close()
    return datos_por_dia  # Devuelve una lista con las ventas de cada día de la semana en orden

def traer_ventas_totales_semana(ano_actual, semana_actual):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE EXTRACT(YEAR FROM v.fecha_hora) = {ano_actual}
          AND EXTRACT(WEEK FROM v.fecha_hora) = {semana_actual}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas de la semana actual

def traer_ventas_totales_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del periodo seleccionado

def traer_numero_de_ventas_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT COUNT(*)
        FROM ventas v
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del periodo seleccionado

def traer_venta_promedio_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT AVG(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del periodo seleccionado

def traer_ganancias_totales_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del periodo seleccionado

def traer_ventas_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT DATE(v.fecha_hora) AS dia, SUM(dv.precio_unitario_venta * dv.cantidad) AS total_ventas
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
        GROUP BY dia
        ORDER BY dia
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convertir los resultados en una lista de valores
    ventas_por_dia = [row[1] if row[1] is not None else 0 for row in data]
    return ventas_por_dia  # Devuelve una lista con las ventas por día

def traer_ganancias_periodo(periodo1, periodo2):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM((dv.precio_unitario_venta - dv.precio_unitario_compra) * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ganancias del periodo seleccionado

def traer_datos_por_metodo_y_dia_periodo(periodo1, periodo2, id_metodo):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dv.precio_unitario_venta * dv.cantidad)
        FROM ventas v
        INNER JOIN detalle_ventas dv ON v.id_venta = dv.id_venta
        WHERE v.fecha_hora BETWEEN '{periodo1}' AND '{periodo2}'
          AND v.id_metodo_pago = {id_metodo}
    """
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0] if data[0][0] is not None else 0  # devuelve el total de ventas del periodo seleccionado


def verificar_existencia_de_mp():
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT EXISTS (SELECT 1 FROM metodos_pago)"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0]

def agregar_mp_default():
    conn = get_connection()
    cursor = conn.cursor()
    query1 = f"INSERT INTO metodos_pago(nombre_mp) VALUES('Efectivo')"
    query2 = f"INSERT INTO metodos_pago(nombre_mp) VALUES('Transferencia')"
    query3 = f"INSERT INTO metodos_pago(nombre_mp) VALUES('Tarjeta de Crédito')"
    query4 = f"INSERT INTO metodos_pago(nombre_mp) VALUES('Tarjeta de Débito')"

    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)

    conn.commit()  # Confirmar los cambios en la base de datos
    cursor.close()
    conn.close()

def agregar_mp_db(lineEdit_value):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO metodos_pago(nombre_mp) VALUES('{lineEdit_value}')"
        cursor.execute(query)
        
        cursor.close()
        conn.commit()  # Confirmar los cambios en la base de datos
        
        return True

    except errors.UniqueViolation:
        return False
    
def borrar_mp_db(combobox_value):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"DELETE FROM metodos_pago WHERE nombre_mp = '{combobox_value}'"
    cursor.execute(query)
    conn.commit()
    cursor.close()

    return True

def actualizar_cantidad_productos(producto_modificado, m, s):
   
    #s controla si es una venta o una compra o si no se proceso la venta/compra, para que devuelva los valores que se agregaron o restaron si es que hay
    #m  controla si son varios arreglos o solo uno
    conn = get_connection()
    cursor = conn.cursor()

    if m:
        if s:
            for producto in producto_modificado:
                nombre = producto[0]
                cantidad = float(producto[2])
                query_update_data = f"UPDATE productos SET stock=stock-{cantidad} WHERE nombre='{nombre}'"
                cursor.execute(query_update_data)

            
            cursor.close()
            
        else:
            for producto in producto_modificado:
                nombre = producto[0]
                cantidad = float(producto[2])
                query_update_data = f"UPDATE productos SET stock=stock+{cantidad} WHERE nombre='{nombre}'"
                cursor.execute(query_update_data)
            
            cursor.close()
            
    else:
        
        nombre = producto_modificado[0][0] # nombre
        cantidad = float(producto_modificado[0][2])  # Cantidad del producto
        if s:

            query_update_data = f"UPDATE productos SET stock=stock-{cantidad} WHERE nombre='{nombre}'"
            cursor.execute(query_update_data)
        else:
            query_update_data = f"UPDATE productos SET stock=stock+{cantidad} WHERE nombre='{nombre}'"
            cursor.execute(query_update_data)
        
        cursor.close()

    return True


def agregar_a_registro(productos_seleccionados, s, usuario):
    # s define si es una venta o una compra, si es true es una venta y si es false es una compra

    conn = get_connection()
    cursor = conn.cursor()
    id_usuario = traer_id_usuario(usuario)

    # Recorrer cada producto en productos_seleccionados
    for producto in productos_seleccionados:
        
        # Asignar las variables correspondientes
        nombre = producto[0]  # Nombre del producto
        precio_compra = traer_precio_compra(nombre)
        precio = float(producto[1]) # precio del producto
        cantidad = float(producto[2])  # Cantidad del producto
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora_actual = datetime.now().strftime("%I:%M:%S %p")
        metodo_pago = producto[5]
        fecha_hora = f"{fecha} {hora_actual}"
        
        #traer id del metodo de pago seleccionado
        metodo_pago = traer_mp(metodo_pago)
        if s:
            # query para la tabla de la venta
            query_add_datatoventas = f"INSERT INTO ventas(fecha_hora, id_metodo_pago, id_usuario) VALUES('{fecha_hora}', '{metodo_pago}', {id_usuario})"
            cursor.execute(query_add_datatoventas)

            query_search_id= f"SELECT id_venta FROM ventas ORDER BY id_venta DESC LIMIT 1"
            cursor.execute(query_search_id)
            data = cursor.fetchall()
            id_venta = data[0][0]

            query_search_idprod= f"SELECT id_producto FROM productos WHERE nombre = '{nombre}'"
            cursor.execute(query_search_idprod)
            data = cursor.fetchall()
            id_prod = data[0][0]

            # query para reducir el stock en el producto
            query_update_stock = f"UPDATE productos SET stock=stock-{cantidad} WHERE id_producto={id_prod}"
            cursor.execute(query_update_stock)
            
            query_add_data = f"INSERT INTO detalle_ventas(id_venta, id_producto, cantidad, precio_unitario_venta, precio_unitario_compra) VALUES({id_venta},{id_prod},{cantidad},{precio},{precio_compra})"
            cursor.execute(query_add_data)

            conn.commit()  # Confirmar los cambios en la base de datos

            cargar_movimiento_venta(usuario)



        else:

            # query para la tabla de compras
            query_add_datatoventas = f"INSERT INTO compras(fecha_hora, id_usuario, id_metodo_pago) VALUES('{fecha_hora}', {id_usuario}, {metodo_pago})"
            cursor.execute(query_add_datatoventas)

            query_search_id= f"SELECT id_compra FROM compras ORDER BY id_compra DESC LIMIT 1"
            cursor.execute(query_search_id)
            data = cursor.fetchall()
            id_compra = data[0][0]

            query_search_idprod= f"SELECT id_producto FROM productos WHERE nombre = '{nombre}'"
            cursor.execute(query_search_idprod)
            data = cursor.fetchall()
            id_prod = data[0][0]

            # query para sumar en el stock en el producto
            query_update_stock = f"UPDATE productos SET stock=stock+{cantidad} WHERE id_producto={id_prod}"
            cursor.execute(query_update_stock)

            query_add_data = f"INSERT INTO detalle_compras(id_compra, id_producto, cantidad, precio_unitario) VALUES({id_compra},{id_prod},{cantidad},{precio})"
            cursor.execute(query_add_data)

            conn.commit()  # Confirmar los cambios en la base de datos

            cargar_movimiento_compra(usuario)

    cursor.close()
    conn.close()
    return True

def traer_precio_compra(nombre):
    conn = get_connection()
    cursor = conn.cursor()
    query_precio = f"SELECT precio_de_compra FROM productos WHERE nombre = '{nombre}'"
    cursor.execute(query_precio)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data[0][0]

def traer_mp(metodo_pago):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT id_mp FROM metodos_pago WHERE nombre_mp = '{metodo_pago}'"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    return data[0][0]


def agregar_mp_db(lineEdit_value):
    conn = get_connection()
    try:
        
        cursor = conn.cursor()
        query = f"INSERT INTO metodos_pago(nombre_mp) VALUES('{lineEdit_value}')"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

        return True

    except errors.UniqueViolation:
        return False
    
def traer_ultimo_agregado_anotador():
    conn = get_connection()
    cursor = conn.cursor()
    query_update_data = f"SELECT contenido FROM anotador ORDER BY id_anotador DESC LIMIT 1"
    cursor.execute(query_update_data)
    data = cursor.fetchall()
    cursor.close()
    
    conn.commit()
    conn.close()


    if data:

        return data[0][0]
    else:
        return  None
    
def set_text_principal(usuario):
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_connection()
    cursor = conn.cursor()
    query_update_data = f"INSERT INTO anotador(id_nota, contenido, fecha_modificacion, tipo_cambio, usuario_id) VALUES(1,'GENERAL:\n','{fecha_hora_actual}','inicial',{traer_id_usuario(usuario)})"
    cursor.execute(query_update_data)

    conn.commit()
    cursor.close()

def guardar_texto_anotador_sincrono(texto, usuario):
    """
    Función síncrona para guardar texto del anotador en la base de datos
    Retorna True si se guardó exitosamente, False en caso contrario
    """
    try:
        conn = get_connection()  
        cursor = conn.cursor()
        
        # Usar las columnas correctas de tu tabla
        id_usuario = traer_id_usuario(usuario)
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # ✅ Query corregida con las columnas reales y valores correctos
        query = """
            INSERT INTO anotador (id_nota, contenido, tipo_cambio, usuario_id, fecha_modificacion) 
            VALUES (%s, %s, %s, %s, %s)
        """
        
        # ✅ Valores correctos según tu estructura
        cursor.execute(query, (1, texto, 'editado', id_usuario, fecha_hora_actual))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
        
    except Exception as e:
        return False
    
def limpiar_anotaciones_automatico():
    """
    Limpia automáticamente la tabla anotaciones si hay más de 5 registros
    Retorna True si se limpió exitosamente, False en caso contrario
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Contar cuántos registros hay
        query_count = "SELECT COUNT(*) FROM anotador"
        cursor.execute(query_count)
        count = cursor.fetchone()[0]
        
        # Si hay más de 5 registros, limpiar
        if count > 5:
            #  Usar CTE para obtener el ID más reciente y luego eliminar
            query_delete = """
                WITH ultimo_registro AS (
                    SELECT id_anotador 
                    FROM anotador 
                    ORDER BY fecha_modificacion DESC 
                    LIMIT 1
                )
                DELETE FROM anotador 
                WHERE id_anotador NOT IN (SELECT id_anotador FROM ultimo_registro)
            """
            cursor.execute(query_delete)
            conn.commit()
           
        cursor.close()
        conn.close()
        return True
        
    except Exception as e:
        return False


####################################################################
####################################################################
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
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Aumento', 'Productos', {combobox_20_ID}, 'Aumento precios de: {combobox_20_value}')"
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

def traer_id_venta():

    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id_venta FROM ventas ORDER BY id_venta DESC LIMIT 1"
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data[0]

def traer_id_compra():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT id_compra FROM compras ORDER BY id_compra DESC LIMIT 1"
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return data[0]

def traer_prod_vendido(id_venta):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT id_producto FROM detalle_ventas WHERE id_venta = {id_venta}"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    # Devuelve el id del producto vendido, ya que solo se espera un producto por ID de venta
    return data[0][0]

def traer_prod_compra(id_compra):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT id_producto FROM detalle_compras WHERE id_compra = {id_compra}"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    # Devuelve el id del producto comprado, ya que solo se espera un producto por ID de compra
    return data[0][0]


def cargar_movimiento_venta(usuario_activo):
    
    
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_venta = traer_id_venta()
    id_prod = traer_prod_vendido(id_venta)
    prod_vendido = traer_nom_producto(id_prod)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Venta', 'Ventas', {id_venta}, 'se vendió: {prod_vendido}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True


def cargar_movimiento_agregar_metodo_pago(metodo_pago, usuario_activo):
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_entidad = traer_mp(metodo_pago)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Agregar', 'Metodos de Pago', {id_entidad}, 'Método de pago agregado: {metodo_pago}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True

def cargar_movimiento_borrar_metodo_pago(metodo_pago, usuario_activo, id):
    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Borrar', 'Metodos de Pago', {id}, 'Método de pago borrado: {metodo_pago}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True


def cargar_movimiento_compra(usuario_activo):

    id_usuario = traer_id_usuario(usuario_activo)
    fecha_hora = datetime.now().astimezone().isoformat()
    id_compra = traer_id_compra()
    id_prod = traer_prod_compra(id_compra)
    prod_comprado = traer_nom_producto(id_prod)

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Compra', 'Compras', NULL, 'se compro: {prod_comprado}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True

def traer_rol_usuario(usuario):
    conn = get_connection()
    cursor = conn.cursor()
    query = f"SELECT admin FROM usuarios WHERE nombre = '{usuario}'"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data[0][0]

def cargar_movimiento_inicio(usuario):
    id_usuario = traer_id_usuario(usuario)
    fecha_hora = datetime.now().astimezone().isoformat()
    rol = traer_rol_usuario(usuario)

    if rol:
        usuario_rol = 'administrador'
    else:
        usuario_rol = 'usuario'

    conn = get_connection()
    cursor = conn.cursor()
    query = f"INSERT INTO movimientos (id_usuario, fecha_hora, tipo_accion, entidad_afectada, id_entidad, descripcion) VALUES ({id_usuario}, '{fecha_hora}', 'Login', 'Sistema', NULL, '{usuario_rol} : {usuario}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    return True
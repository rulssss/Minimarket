import psycopg2
from psycopg2 import errors
from tkinter import messagebox


#################################################
#################################################
#################################################
#################################################

connection1 = psycopg2.connect(
host="localhost",
user="postgres",
password="Mariano302",
database="registro_usuarios",
port="5432"
)
# autocommit
connection1.autocommit = True

#################################################
#################################################
#################################################
#################################################


#################################################
#################################################
#################################################
#################################################

connection2 = psycopg2.connect(
host="localhost",
user="postgres",
password="Mariano302",
database="minimarketdb",
port="5432"
)
# autocommit
connection2.autocommit = True

#################################################
#################################################
#################################################
#################################################



#####################################
# FUNCIONES PARA CONNECTION1 LOGIN db
#####################################

def registrar_usuario(username, password, account):

    if account == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o fals epara verificar que tipo de cuenta es

    cursor= connection1.cursor()
    query_data1 = f"INSERT INTO usuarios(nombre, admin) VALUES('{username}', {account})"
    cursor.execute(query_data1)

    cursor= connection1.cursor()
    query_data = f"SELECT id_usuario FROM usuarios WHERE nombre = '{username}'"
    cursor.execute(query_data)
    data_id = cursor.fetchall()


    query_data2 = f"INSERT INTO contrasenas(id_usuario, contrasena) VALUES({data_id[0][0]}, '{password}')"
    cursor.execute(query_data2)


    cursor.close()

def hay_admin():
    cursor= connection1.cursor()
    query_data = f"SELECT id_usuario FROM usuarios WHERE admin = True"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data == []: # verifica si hay algun administrador, si no hay devuelve false y abre la ventana de registro
        return False
    else:
        return True

def actualizar_contrasena(new_password, recover_id):
    cursor= connection1.cursor()
    query_data = f"UPDATE contrasenas SET contrasena = '{new_password}' WHERE id_usuario = {recover_id}"
    cursor.execute(query_data)
    cursor.close()


def existencia_de_id(recover_id):
    cursor= connection1.cursor()
    # 
    query_data = f"SELECT id_usuario FROM usuarios WHERE id_usuario = '{recover_id}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data == []:
        return True
    else:
        return False    

    

def existe_usuario(username):
    cursor= connection1.cursor()
    query_data = f"SELECT nombre FROM usuarios WHERE nombre = '{username}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data == []:
        return True
    else: 
        return False


def verificar_contrasenia(password, username, account):
    cursor= connection1.cursor()
    query_data2 = f"SELECT usuarios.id_usuario, contrasenas.contrasena, usuarios.admin FROM usuarios JOIN contrasenas ON usuarios.id_usuario = contrasenas.id_usuario WHERE usuarios.nombre = '{username}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    ###########ORDENAR PARA CORREGIR QUE VERIFIQUE SI ES USUARIO O ADMIN  ES DECIR, QUE VEA SI ES TRUE O FALSE EN LA TABLA APRA NO TRAER TODOS LOS NOBRES

    if account == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o false para verificar que tipo de cuenta es

    if data != []:
        if data[0][1] != password or data[0][2] != account: ## verifica password igual y si el tipo es igual al seleccionado
            return True # devuelve true si alguno es distinto para tirar el mensaje de error
    else:
        return False

def obtener_id_usuario(usuario):
    cursor= connection1.cursor()
    query_data2 = f"SELECT id_usuario FROM usuarios WHERE nombre = '{usuario}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    if data != []:
        return data[0][0]
    else:
        return -1


#########################################
# FUNCIONES PARA CONECTION2 MINIMARKET db
#########################################

def traer_categorias():
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre_descrip FROM categorias ORDER BY nombre_descrip"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    return data

def traer_proveedores():
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre_proveedor FROM proveedores ORDER BY nombre_proveedor"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    
    return data

def traer_id_categoria(categoria_producto):
    cursor= connection2.cursor()
    query_data2 = f"SELECT id_categoria FROM categorias WHERE nombre_descrip = '{categoria_producto}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    
    return data[0][0]




def traer_id_proveedor(proveedor_producto):
    cursor= connection2.cursor()
    query_data2 = f"SELECT id_proveedor FROM proveedores WHERE nombre_proveedor = '{proveedor_producto}'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    return data[0][0]


def cargar_producto_actualizacion(nombre_producto, precio_producto, cantidad_producto, categoria_producto, proveedor_producto):
    
    categoria_producto = traer_id_categoria(categoria_producto)
    proveedor_producto = traer_id_proveedor(proveedor_producto)

    cursor= connection2.cursor()
    query_data2 = f"INSERT INTO productos(nombre, precio, stock, id_categoria, id_proveedor) VALUES('{nombre_producto}', {precio_producto}, {cantidad_producto}, {categoria_producto}, {proveedor_producto})"
    #verifcacion de que el producto existe
    try:
        cursor.execute(query_data2)
    except errors.UniqueViolation:
        messagebox.showerror("Error", "Esta queriendo ingresar un producto existente")

    cursor.close()

def buscar_producto(nombre_prod):
    cursor= connection2.cursor()
    query_data2 = f"SELECT EXISTS (SELECT 1 FROM productos WHERE nombre = '{nombre_prod}') AS existe" # ve si existe y devuelve true o false, ver el fetchone
    cursor.execute(query_data2)
    data = cursor.fetchone()[0]
    
    if data:
        query_data3 = f"DELETE FROM productos WHERE nombre = '{nombre_prod}'"
        cursor.execute(query_data3)
        cursor.close()
        return True
        
    else: 
        cursor.close()
        return False
        
    

def traer_todos_los_productos():
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre, precio, stock, nombre_descrip, nombre_proveedor FROM productos JOIN categorias ON productos.id_categoria = categorias.id_categoria JOIN proveedores ON productos.id_proveedor = proveedores.id_proveedor ORDER BY productos.nombre"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    return data



def actualizar_producto(nombre_producto, precio_producto, categoria_producto, proveedor_producto):
    
    cursor= connection2.cursor()
    query_search = f"SELECT id_categoria FROM categorias WHERE nombre_descrip = '{categoria_producto}'"
    cursor.execute(query_search)
    categ = cursor.fetchall()[0][0]

    query_search2 = f"SELECT id_proveedor FROM proveedores WHERE nombre_proveedor = '{proveedor_producto}'"
    cursor.execute(query_search2)
    prov = cursor.fetchall()[0][0]

    query_data2 = f"UPDATE productos SET precio = {precio_producto}, id_categoria = {categ}, id_proveedor = {prov}  WHERE nombre = '{nombre_producto}'"
    cursor.execute(query_data2)
    cursor.close()
    
    

def cargar_proveedor(nombre_producto, num_telefono, mail):
    cursor= connection2.cursor()
    query_data2 = f"INSERT INTO proveedores(nombre_proveedor, telefono, mail) VALUES('{nombre_producto}', {num_telefono}, '{mail}')"

    try:
        cursor.execute(query_data2)
        cursor.close()
        return True
    except errors.UniqueViolation:
        return False



def buscar_proveedor(nombre_prov):
    cursor= connection2.cursor()
    query_data2 = f"SELECT EXISTS (SELECT 1 FROM proveedores WHERE nombre_proveedor = '{nombre_prov}') AS existe" # ve si existe y devuelve true o false, ver el fetchone
    cursor.execute(query_data2)
    data = cursor.fetchone()[0]

    if data:
        query_data3 = f"DELETE FROM proveedores WHERE nombre_proveedor = '{nombre_prov}'"
        cursor.execute(query_data3)
        cursor.close()
        return True
        
    else: 
        cursor.close()
        return False
    


def traer_todos_los_proveedores():
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre_proveedor, telefono, mail FROM proveedores ORDER BY nombre_proveedor"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    return data


def actualizar_proveedor(nombre_proveedor, num_proveedor, mail_producto):
    cursor= connection2.cursor()
    query_data2 = f"UPDATE proveedores SET telefono = {num_proveedor}, mail = '{mail_producto}' WHERE nombre_proveedor = '{nombre_proveedor}'"
    cursor.execute(query_data2)
    cursor.close()
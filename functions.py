import psycopg2
from psycopg2 import errors
from tkinter import messagebox
import tkinter as tk
from datetime import datetime
import os
import sys
import json
import hashlib
import uuid

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
# FUNCIONES PARA CONNECTION2 LOGIN db
#####################################

def registrar_usuario(username, password, account):

    if account == "Administrador":
        account = True
    else:
        account = False     #Aacomoda la variable account a un true o fals epara verificar que tipo de cuenta es

    cursor= connection2.cursor()
    query_data1 = f"INSERT INTO usuarios(nombre, admin) VALUES('{username}', {account})"
    cursor.execute(query_data1)

    cursor= connection2.cursor()
    query_data = f"SELECT id_usuario FROM usuarios WHERE nombre = '{username}'"
    cursor.execute(query_data)
    data_id = cursor.fetchall()


    query_data2 = f"INSERT INTO contrasenas(id_usuario, contrasena) VALUES({data_id[0][0]}, '{password}')"
    cursor.execute(query_data2)


    cursor.close()

def hay_admin():
    cursor= connection2.cursor()
    query_data = f"SELECT id_usuario FROM usuarios WHERE admin = True"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data == []: # verifica si hay algun administrador, si no hay devuelve false y abre la ventana de registro
        return False
    else:
        return True

def actualizar_contrasena(new_password, recover_id):
    cursor= connection2.cursor()
    query_data = f"UPDATE contrasenas SET contrasena = '{new_password}' WHERE id_usuario = {recover_id}"
    cursor.execute(query_data)
    cursor.close()


def existencia_de_id(recover_id):
    cursor= connection2.cursor()
    # 
    query_data = f"SELECT id_usuario FROM usuarios WHERE id_usuario = '{recover_id}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    if data != []:
        return True
    else:
        return False    

    

def existe_usuario(username):
    cursor= connection2.cursor()
    query_data = f"SELECT nombre FROM usuarios WHERE nombre = '{username}'"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()
    
    if data != []:
        return True
    else: 
        return False


def verificar_contrasenia(password, username, account):
    cursor= connection2.cursor()
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
    cursor= connection2.cursor()
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


def cargar_producto_actualizacion(id_producto, nombre_producto, precio_compra_producto, precio_venta_producto, cantidad_producto, categoria_producto, proveedor_producto):
    
    categoria_producto = traer_id_categoria(categoria_producto)
    proveedor_producto = traer_id_proveedor(proveedor_producto)

    cursor= connection2.cursor()
    query_data2 = f"INSERT INTO productos(id_producto, nombre, precio_de_compra, precio_de_venta, stock, id_categoria, id_proveedor) VALUES({id_producto}, '{nombre_producto}', {precio_compra_producto}, {precio_venta_producto}, {cantidad_producto}, {categoria_producto}, {proveedor_producto})"
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
    query_data2 = f"SELECT id_producto, nombre, precio_de_compra, precio_de_venta, stock, nombre_descrip, nombre_proveedor FROM productos JOIN categorias ON productos.id_categoria = categorias.id_categoria JOIN proveedores ON productos.id_proveedor = proveedores.id_proveedor ORDER BY productos.nombre"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    return data



def actualizar_producto(nombre_prdoucto, precio_compra_producto, precio_venta_producto, cantidad, categoria_producto, proveedor_producto):
    
    cursor= connection2.cursor()
    query_search = f"SELECT id_categoria FROM categorias WHERE nombre_descrip = '{categoria_producto}'"
    cursor.execute(query_search)
    categ = cursor.fetchall()[0][0]

    query_search2 = f"SELECT id_proveedor FROM proveedores WHERE nombre_proveedor = '{proveedor_producto}'"
    cursor.execute(query_search2)
    prov = cursor.fetchall()[0][0]

    query_data2 = f"UPDATE productos SET precio_de_compra = {precio_compra_producto}, precio_de_venta = {precio_venta_producto}, id_categoria = {categ}, id_proveedor = {prov}, stock = {cantidad}  WHERE nombre = '{nombre_prdoucto}'"
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


def cargar_categoria(nombre_categoria):
    cursor= connection2.cursor()
    query_data2 = f"INSERT INTO categorias(nombre_descrip) VALUES('{nombre_categoria}')"

    try:
        cursor.execute(query_data2)
        cursor.close()
        return True
    except errors.UniqueViolation:
        return False
    
def existe_categoria():
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre_descrip FROM categorias WHERE nombre_descrip = 'Sin categoria'"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    if data != []:
        return False
    else:
        return True


def crear_categuno():
    cursor= connection2.cursor()
    query_data2 = f"INSERT INTO categorias(id_categoria, nombre_descrip) VALUES(1, 'Sin categoria')"
    cursor.execute(query_data2)
    cursor.close()
    
def buscar_categoria(nombre_categ):
    cursor= connection2.cursor()
    query_data2 = f"SELECT EXISTS (SELECT 1 FROM categorias WHERE nombre_descrip = '{nombre_categ}') AS existe" # ve si existe y devuelve true o false, ver el fetchone
    cursor.execute(query_data2)
    data = cursor.fetchone()[0]

    if data:
        try:
            query_data3 = f"DELETE FROM categorias WHERE nombre_descrip = '{nombre_categ}'"
            cursor.execute(query_data3)
            cursor.close()
        except errors.ForeignKeyViolation:
            query_data4 = f"SELECT nombre FROM productos WHERE id_categoria= {traer_id_categoria(nombre_categ)}"
            cursor.execute(query_data4)
            data = cursor.fetchall()
        
            for prod in data[0]:
                query_data5 = f"UPDATE productos SET id_categoria = 1 WHERE nombre = '{prod}'"
                cursor.execute(query_data5)

            query_data3 = f"DELETE FROM categorias WHERE nombre_descrip = '{nombre_categ}'"
            cursor.execute(query_data3)


            cursor.close()
        return True
        
    else: 
        cursor.close()
        return False


def traer_todas_las_categorias():
    cursor= connection2.cursor()
    query_data2 = f"SELECT id_categoria, nombre_descrip FROM categorias ORDER BY nombre_descrip"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()
    return data


def ventana_confirmacion():
    resultado = tk.BooleanVar()
    
    # Crear una nueva ventana (modal)
    confirm_window = tk.Toplevel()
    confirm_window.title("Confirmación")
    confirm_window.geometry("400x200")  # Ajustar el tamaño a uno más grande
    confirm_window.config(bg="white")  # Fondo blanco, típico de ventanas de Windows
    confirm_window.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana emergente
    
    confirm_window.resizable(False, False)  # Bloquear el cambio de tamaño de la ventana

    # Cargar la imagen del icono
    icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
    confirm_window.iconbitmap(icon_path)
    # Centrando la ventana
    screen_width = confirm_window.winfo_screenwidth()
    screen_height = confirm_window.winfo_screenheight()
    window_width =500
    window_height = 200
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Etiqueta con el mensaje
    label = tk.Label(confirm_window, text="¡ATENCION!\n Esta a punto de borrar todos los datos\n incluyendo los datos del login.", font=("Segoe UI", 12), bg="white")
    label.pack(pady=(40, 0))  # Ajustar el espaciado para mayor separación
    

    # Función para manejar el botón "Sí"
    def on_yes():
        resultado.set(True)
        confirm_window.destroy()

    # Función para manejar el botón "No"
    def on_no():
        resultado.set(False)
        confirm_window.destroy()

    # Crear el marco para los botones
    button_frame = tk.Frame(confirm_window, bg="white")
    button_frame.pack(pady=20)

    # Botones
    btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12,    "bold"))
    btn_yes.pack(side=tk.LEFT, padx=15)
    btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12,     "bold"))
    btn_no.pack(side=tk.LEFT, padx=15)

    confirm_window.protocol("WM_DELETE_WINDOW", on_no)
    confirm_window.wait_window()
    

    return resultado.get()

def clear_data():
    
    v = ventana_confirmacion()
    cursor = connection2.cursor()
    if v:
        
        query_data2 = f"TRUNCATE categorias CASCADE"
        cursor.execute(query_data2)

        query_data3 = f"TRUNCATE proveedores CASCADE"
        cursor.execute(query_data3)

        query_data4 = f"TRUNCATE contrasenas CASCADE"
        cursor.execute(query_data4)

        query_data5 = f"TRUNCATE usuarios CASCADE"
        cursor.execute(query_data5)

        messagebox.showinfo("Datos borrados", "Todos los datos han sido borrados.")
            
    cursor.close()

    


def controlar_cantidades(producto_modificado, s):
    
    nombre = producto_modificado[0]
    cantidad = int(producto_modificado[2])

    cursor = connection2.cursor()
    query_update_data = f"SELECT stock FROM productos WHERE nombre='{nombre}'"
    cursor.execute(query_update_data)
    data = cursor.fetchall()
    cursor.close()
      
    op = data[0][0] - cantidad
    
    if s:
        
        if op >= 0 and cantidad > 0:
            d = True
        else:
            d = False
            messagebox.showinfo("Error", f"Cantidad de el producto insuficiente.\nCantidad restante: {data[0][0]}")
            
    else:
        d = False
        

    return d


def actualizar_cantidad_productos(productos_modificado, s, l, m):
    

    cursor = connection2.cursor()

    if l:

        for i in productos_modificado:
            nombre = i[0] # nombre
            cantidad = i[2]  # Cantidad del producto

            if m:
                query_update_data = f"UPDATE productos SET stock=stock-{cantidad} WHERE nombre='{nombre}'"
                cursor.execute(query_update_data)


            else:
                
                query_update_data = f"UPDATE productos SET stock=stock+{cantidad} WHERE nombre='{nombre}'"
                cursor.execute(query_update_data)


    else:
       
        nombre = productos_modificado[0][0] # nombre
        
        cantidad = int(productos_modificado[0][2])  # Cantidad del producto


        if s:
            
            query_update_data = f"UPDATE productos SET stock=stock-{cantidad} WHERE nombre='{nombre}'"
            cursor.execute(query_update_data)

        else:
            query_update_data = f"UPDATE productos SET stock=stock+{cantidad} WHERE nombre='{nombre}'"
            cursor.execute(query_update_data)

    cursor.close()



def anadir_a_registro(productos_seleccionados, s, usuario):
    
    cursor = connection2.cursor()
    query_id_usuario = f"SELECT id_usuario FROM usuarios WHERE nombre = '{usuario}'"
    cursor.execute(query_id_usuario)
    data = cursor.fetchall()
    id_usuario = data[0][0]
    # Recorrer cada producto en productos_seleccionados
    for producto in productos_seleccionados:
        # Asignar las variables correspondientes
        nombre = producto[0]  # Nombre del producto
        precio_str = producto[1].replace('$', '')  # Eliminar el símbolo de pesos
        precio = float(precio_str)  # Convertir a float
        cantidad = int(producto[2])  # Cantidad del producto
        total_venta = precio * cantidad  # Precio total de la venta
        fecha = datetime.now().strftime("%Y-%m-%d")
        hora_actual = datetime.now().strftime("%I:%M:%S %p")
        metodo_pago = producto[5]
        
        
        if s:
            # query para la tabla de la venta
            query_add_datatoventas = f"INSERT INTO ventas(fecha, total, hora, metodo_pago, id_usuario) VALUES('{fecha}', {total_venta},'{hora_actual}', '{metodo_pago}', {id_usuario})"
            cursor.execute(query_add_datatoventas)

            query_search_id= f"SELECT id_venta FROM ventas ORDER BY id_venta DESC LIMIT 1"
            cursor.execute(query_search_id)
            data = cursor.fetchall()
            id_venta = data[0][0]

            query_search_idprod= f"SELECT id_producto FROM productos WHERE nombre = '{nombre}'"
            cursor.execute(query_search_idprod)
            data = cursor.fetchall()
            id_prod = data[0][0]
            

            query_add_data = f"INSERT INTO detalle_ventas(id_venta, id_producto, cantidad, precio_unitario) VALUES({id_venta},{id_prod},{cantidad},{precio})"
            cursor.execute(query_add_data)
            

        else:

            # query para la tabla de compras
            query_add_datatoventas = f"INSERT INTO compras(fecha, total, hora, id_usuario) VALUES('{fecha}', {total_venta}, '{hora_actual}', {id_usuario})"
            cursor.execute(query_add_datatoventas)

            query_search_id= f"SELECT id_compra FROM compras ORDER BY id_compra DESC LIMIT 1"
            cursor.execute(query_search_id)
            data = cursor.fetchall()
            id_compra = data[0][0]

            query_search_idprod= f"SELECT id_producto FROM productos WHERE nombre = '{nombre}'"
            cursor.execute(query_search_idprod)
            data = cursor.fetchall()
            id_prod = data[0][0]

            query_add_data = f"INSERT INTO detalle_compras(id_compra, id_producto, cantidad, precio_unitario) VALUES({id_compra},{id_prod},{cantidad},{precio})"
            cursor.execute(query_add_data)

    cursor.close()


def traer_todos_losdatos_ventaocompra(s):

    cursor = connection2.cursor()
    if s:
        query_update_data = f"SELECT * FROM ventas ORDER BY id_venta DESC"
        cursor.execute(query_update_data)
        data = cursor.fetchall()
        
        
    else:
        query_update_data = f"SELECT * FROM compras ORDER BY id_compra DESC"
        cursor.execute(query_update_data)
        data = cursor.fetchall()
    

    cursor.close()
    return data


def totales(ventas_filtradas, compras_filtradas, s):
    total_contado = 0
    total_mercado_pago = 0
    total_cuenta_corriente = 0
    total_compras = 0
    total_ventas= 0
    
    for venta in ventas_filtradas:
        metodo_pago = venta[4]
        precio = venta[2]

        if metodo_pago == 'Contado':
            total_contado += precio
        elif metodo_pago == 'Mercado Pago':
            total_mercado_pago += precio
        elif metodo_pago == 'Cuenta Corriente':
            total_cuenta_corriente += precio
    
    for compra in compras_filtradas:
        precio = float(compra[2])  # precio
        
        total_compras += precio
        
    total_ventas = total_contado + total_mercado_pago + total_cuenta_corriente

    if s:
        return f"Ventas Total: $ {round(total_ventas, 2)}", f"Ventas Contado: $ {round(total_contado, 2)}", f"Ventas Mercado Pago: $ {round(total_mercado_pago, 2)}", f"Ventas Cuenta Corriente: $ {round(total_cuenta_corriente, 2)}", f"Compras Total: $ {round(total_compras, 2)}"
    else:
        return f"Ventas Contado: $ {round(total_contado, 2)}", f"Ventas Mercado Pago: $ {round(total_mercado_pago, 2)}", f"Ventas Cuenta Corriente: $ {round(total_cuenta_corriente, 2)}", f"Compras Total: $ {round(total_compras, 2)}"

def traer_detalles(s, id):

    cursor = connection2.cursor()

    if s:
        
        query_search_data = f"""
        SELECT dv.id_detalle, dv.id_venta, p.nombre, dv.cantidad, dv.precio_unitario
        FROM detalle_ventas dv
        JOIN productos p ON dv.id_producto = p.id_producto
        WHERE dv.id_venta={id}
        """
        cursor.execute(query_search_data)
        data = cursor.fetchall()
       
        
    else:
    
        query_search_data = f"""
        SELECT dc.id_detalle, dc.id_compra, p.nombre, dc.cantidad, dc.precio_unitario
        FROM detalle_compras dc
        JOIN productos p ON dc.id_producto = p.id_producto
        WHERE dc.id_compra={id}
        """
        cursor.execute(query_search_data)
        data = cursor.fetchall()
        

    cursor.close()
    return data



def traer_usuario(ventas_filtradas):
    id_usuario = ventas_filtradas[0][5]
    cursor= connection2.cursor()
    query_data2 = f"SELECT nombre FROM usuarios WHERE id_usuario = {id_usuario}"
    cursor.execute(query_data2)
    data = cursor.fetchall()
    cursor.close()

    return data[0][0]


def traer_producto(barcode):
    cursor= connection2.cursor()
    #query_data2 = f"SELECT id_producto, nombre, precio_de_compra, precio_de_venta, stock, id_categoria, id_proveedor FROM productos WHERE id_producto = {barcode}"
    if barcode != "":
        query_data2 = f"SELECT p.id_producto, p.nombre, p.precio_de_compra, p.precio_de_venta, p.stock, c.nombre_descrip, pr.nombre_proveedor FROM productos p JOIN categorias c ON p.id_categoria = c.id_categoria JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor WHERE p.id_producto = {barcode}"
        cursor.execute(query_data2)
        data = cursor.fetchall()
        cursor.close()
        if data != []:
            return data[0]
        else: 
            messagebox.showerror("Error", "Producto no existente")
            return 
    else:
        pass


######## funciones para la verificacion del codigfo de activacion#############

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_user_data_path(filename):
    """ Get path to the user's data directory """
    user_data_dir = os.path.join(os.getenv('APPDATA'), 'MyApp')
    os.makedirs(user_data_dir, exist_ok=True)
    return os.path.join(user_data_dir, filename)

import tkinter as tk
from tkinter import ttk, messagebox
from functions import *
from tkinter import Toplevel, Label, Entry, Button, Frame, font
import re
from datetime import datetime, date
import calendar
import keyboard
from PIL import Image, ImageTk
import string
import time


### TODA LA VENTANA DE EL MINIMARKET 


class Datos:
    def __init__(self, master, minimarket):
        self.master = master
        self.minimarket = minimarket

    def mostrar(self):
        # Limpiar el contenedor principal
        for widget in self.master.winfo_children():
            widget.destroy()

        # Etiqueta inicial
        etiqueta = tk.Label(self.master, text="Contenido de Datos", bg="white", font=("Segoe UI", 10, "bold"))
        etiqueta.grid(row=0, column=0, pady=10, sticky="ew")

        # Crear botones
        botones = [
            ("Agregar Producto", self.agregar_producto),
            ("Borrar Producto", self.borrar_producto),
            ("Editar Producto", self.editar_producto),
            ("Visualizar Productos", self.visualizar_productos),
            ("Agregar Proveedor", self.agregar_proveedor),
            ("Borrar Proveedor", self.borrar_proveedor),
            ("Editar Proveedor", self.editar_proveedor),
            ("Visualizar Proveedores", self.visualizar_proveedores),
            ("Agregar Categoría", self.agregar_categoria),
            ("Borrar Categoría", self.borrar_categoria),
            ("Visualizar Categorías", self.visualizar_categorias),
        ]

        # Configurar el peso de las filas y columnas para que sean responsivas
        self.master.grid_columnconfigure(0, weight=1)
        for i in range(len(botones) + 3):  # +3 para incluir la etiqueta y el botón "Borrar Datos"
            self.master.grid_rowconfigure(i, weight=1)

        row = 1
        for i, (texto, comando) in enumerate(botones):
            boton = tk.Button(self.master, text=texto, command=comando, height=1, width=20, bg="#e0e0e0", fg="black", font=("Segoe UI", 12, "bold"), activebackground="#c0c0c0", activeforeground="white", relief="groove", bd=2)
            boton.grid(row=row, column=0, pady=0, padx=10, sticky="n")
            row += 1

            # Agregar una línea sutil estilo "hr" después de cada 4 botones
            if (i + 1) % 4 == 0:
                separator = tk.Frame(self.master, bg="gray", height=2)
                separator.grid(row=row, column=0, pady=(0, 20), sticky="ew")
                row += 1

        # Botón "Borrar Datos" en la parte inferior
        boton_borrar_datos = tk.Button(self.master, text="Borrar Datos", height=1, width=20, command=self.borrar_datos, bg="red", fg="white", font=("Segoe UI", 12, "bold"), bd=2)
        boton_borrar_datos.grid(row=row, column=0, pady=30, sticky="n")




    def agregar_producto(self):
        # Crear una ventana secundaria
        ventana = Toplevel()
        ventana.title("Añadir Producto")
        ventana.geometry("1200x300")  # Ajusta el tamaño según necesites
        ventana.resizable(False, False)  # Evita que se redimensione
        ventana.configure(bg="white")
       
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)
        # Hacer la ventana modal
        ventana.grab_set()

        # Centrar la ventana en la pantalla
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 1000
        else:
            ancho_ventana = 1300

        alto_ventana = 320
        x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(ventana, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Ingrese los datos del producto:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=6, pady=(10, 30), padx=(190,0)
        )

        # Etiquetas e Inputs
        Label(frame, text="ID del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        input_id = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_id.grid(row=2, column=0, padx=(30,10), pady=5)

        Label(frame, text="Nombre del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        input_nombre = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_nombre.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="Precio de Compra", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        input_precio_compra = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=("%S"))
        input_precio_compra.grid(row=2, column=2, padx=10, pady=5)

        Label(frame, text="Precio de Venta", bg="white", font=("Segoe UI", 12)).grid(row=1, column=3, padx=10, pady=5)
        input_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=("%S"))
        input_precio.grid(row=2, column=3, padx=10, pady=5)

        Label(frame, text="Cantidad", bg="white", font=("Segoe UI", 12)).grid(row=1, column=4, padx=10, pady=5)
        input_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key")
        input_cantidad.grid(row=2, column=4, padx=10, pady=5)

        # Combobox para categorias
        categorias_tuplas = traer_categorias()
        categorias = [categoria[0] for categoria in categorias_tuplas]
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12)).grid(row=1, column=5, padx=10, pady=5)
        combobox_busqueda1 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda1['values'] = categorias
        combobox_busqueda1.grid(row=2, column=5, padx=10, pady=5)
        combobox_busqueda1.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        # Combobox para proveedores
        proveedores_tuplas = traer_proveedores()
        proveedores = [proveedor[0] for proveedor in proveedores_tuplas]
        Label(frame, text="Proveedores", bg="white", font=("Segoe UI", 12)).grid(row=1, column=6, padx=10, pady=5)
        combobox_busqueda2 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda2['values'] = proveedores
        combobox_busqueda2.grid(row=2, column=6, padx=(10,30), pady=5)
        combobox_busqueda2.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(ventana, bg="white")
        button_frame.pack(pady=(0, 30))

        def on_yes():
            id_producto = input_id.get()
            nombre_producto = input_nombre.get()
            precio_compra_producto = input_precio_compra.get()
            precio_venta_producto = input_precio.get()
            cantidad_producto = input_cantidad.get()
            categoria_producto = combobox_busqueda1.get()
            proveedor_producto = combobox_busqueda2.get()

            # Verifica si los valores de precio y cantidad son válidos (números enteros o decimales)
            if not bool(re.match("^[A-Za-z0-9 ]*$", nombre_producto)):
                advertencia_label.config(text="No acepta ',.-/()'")
                return
            if not bool(re.match("^[0-9.]*$", precio_compra_producto and precio_venta_producto and cantidad_producto)):
                advertencia_label.config(text="Solo acepta números y decimales")
                return
            
            if not bool(re.match("^[0-9]*$", id_producto)):
                advertencia_label.config(text="Solo acepta números enteros")
                return
            
            
            if not id_producto or not cantidad_producto or not nombre_producto or not precio_compra_producto or not precio_venta_producto or not categoria_producto or not proveedor_producto:
                advertencia_label.config(text="No acepta vacios")
                return

            cargar_producto_actualizacion(id_producto, nombre_producto, precio_compra_producto, precio_venta_producto, cantidad_producto, categoria_producto, proveedor_producto)
            self.minimarket.mostrar_arbol_productos_cat_prov()  # mostrar productos actualizados
            on_no()

        def on_no():
            ventana.destroy()

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(7):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        ventana.protocol("WM_DELETE_WINDOW", on_no)

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: on_yes())
        
    def borrar_producto(self):
        # Crear la ventana
        ventana = tk.Toplevel()
        ventana.title("Borrar Producto")
        ventana.geometry("300x150")  # Tamaño de la ventana
        ventana.resizable(False, False)  # Evita que se redimensione
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)

        # Hacer la ventana modal
        ventana.grab_set()

        # Configurar el color de fondo de la ventana a blanco
        ventana.configure(bg="white")
        

        # Obtener el tamaño de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana

        if screen_width < 1100:

            window_width = 400
            window_height = 270
        else:
            window_width = 500
            window_height = 290

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        # Ubicar la ventana en el centro de la pantalla
        ventana.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Label para el nombre del producto
        label_nombre = tk.Label(ventana, text="Nombre del Producto:", bg="white", font=("Segoe UI", 16, "bold"))
        label_nombre.pack(pady=10)

        # Entry para el nombre del producto con fondo #d7d7d7
        entry_nombre = tk.Entry(ventana, bg="#d7d7d7", font=("Segoe UI", 16), width=25)
        entry_nombre.pack(pady=5)

            # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack()
        
        # Función para confirmar y devolver el valor ingresado
        def confirmar():
            nombre_prod = entry_nombre.get()

            if not nombre_prod:  # Verificar si está vacío
                advertencia_label.config(text="No admite nombre vacío")
                return  # No hacer nada más si está vacío

            if bool(re.match("^[A-Za-z0-9 ]*$", nombre_prod)):  # Verificar si contiene letras y números
                v = buscar_producto(nombre_prod) # creada, y sida true lo borra al instante, si hace falta en otra instancia crear otra funcion solo para borrar
                if v:
                    
                    messagebox.showinfo("Borrar Producto", "Producto borrado con éxito.")
                    self.minimarket.mostrar_arbol_productos_cat_prov()
                    ventana.destroy()  # Cerrar la ventana
                else:
                    messagebox.showinfo("Borrar Producto", "No se encontró el producto.")

            else:
                advertencia_label.config(text="Solo admite letras y números.")

        # Botón de borrar
        boton_confirmar = tk.Button(ventana, text="Borrar", command=confirmar, bg="#ef3232", relief="groove", font=("Segoe UI", 16, "bold"), fg="black", width=12)
        boton_confirmar.pack(pady=10)

        def cerrar():
            ventana.destroy()  # Cerrar la ventana

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar, bg="lightgrey", font=("Segoe UI", 14, "bold"), fg="black", relief="groove")
        boton_cerrar.pack(pady=5)

        ventana.protocol("WM_DELETE_WINDOW", cerrar)
        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: confirmar())
        
        # Iniciar el bucle principal de la ventana
        ventana.mainloop()

    def editar_producto(self):
        def filtrar_productos():
            value = combobox_nombre.get().lower()
            if value == '':
                combobox_nombre['values'] = producto_list
            else:
                data = []
                for item in producto_list:
                    if value in item.lower():
                        data.append(item)
                combobox_nombre['values'] = data
            combobox_nombre.event_generate('<Down>')

        def on_key_release(event):
            global filtro_timer
            if filtro_timer:
                confirm_window.after_cancel(filtro_timer)  # Cancelar temporizador anterior
            filtro_timer = confirm_window.after(1200, filtrar_productos)  # Esperar 1500 milisegundos

        confirm_window = Toplevel()
        confirm_window.title("Editar Producto")
        confirm_window.geometry("1200x300")  # Ajusta el tamaño según necesites
        confirm_window.resizable(False, False)  # Evita que se redimensione
        confirm_window.configure(bg="white")

        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        confirm_window.iconbitmap(icon_path)
       

        # Inicializar filtro_timer
        global filtro_timer
        filtro_timer = None

        # Hacer la ventana modal
        confirm_window.grab_set()

        # Centrar la ventana en la pantalla
        confirm_window.update_idletasks()
        screen_width = confirm_window.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 1000
        else:
            ancho_ventana = 1200

        alto_ventana = 320
        x = (confirm_window.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (confirm_window.winfo_screenheight() // 2) - (alto_ventana // 2)
        confirm_window.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(confirm_window, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Editar Producto:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=7, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="ID del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        entry_id = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), state='readonly')
        entry_id.grid(row=2, column=0, padx=(30,10), pady=5)

        Label(frame, text="Nombre del producto", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        combobox_nombre = ttk.Combobox(frame, font=("Segoe UI", 16), state="normal", height=5)
        combobox_nombre.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="Precio de Compra", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        entry_precio_compra = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_precio_compra.grid(row=2, column=2, padx=10, pady=5)

        Label(frame, text="Precio de Venta", bg="white", font=("Segoe UI", 12)).grid(row=1, column=3, padx=10, pady=5)
        entry_precio = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_precio.grid(row=2, column=3, padx=10, pady=5)

        Label(frame, text="Stock", bg="white", font=("Segoe UI", 12)).grid(row=1, column=4, padx=10, pady=5)
        entry_cantidad = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_cantidad.grid(row=2, column=4, padx=10, pady=5)

        # Combobox para categorias
        categorias_tuplas = traer_categorias()
        categorias = [categoria[0] for categoria in categorias_tuplas]
        Label(frame, text="Categoria", bg="white", font=("Segoe UI", 12)).grid(row=1, column=5, padx=10, pady=5)
        combobox_busqueda1 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda1['values'] = categorias
        combobox_busqueda1.grid(row=2, column=5, padx=10, pady=5)
        combobox_busqueda1.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        # Combobox para proveedores
        proveedores_tuplas = traer_proveedores()
        proveedores = [proveedor[0] for proveedor in proveedores_tuplas]
        Label(frame, text="Proveedores", bg="white", font=("Segoe UI", 12)).grid(row=1, column=6, padx=10, pady=5)
        combobox_busqueda2 = ttk.Combobox(frame, font=("Segoe UI", 16), state="readonly", height=5)
        combobox_busqueda2['values'] = proveedores
        combobox_busqueda2.grid(row=2, column=6, padx=(10,30), pady=5)
        combobox_busqueda2.option_add('*TCombobox*Listbox.font', ('Segoe UI', 15))

        productos = traer_todos_los_productos()  # Obtener los productos
        producto_list = [producto[1] for producto in productos]  # Lista con los nombres de los productos
        combobox_nombre['values'] = producto_list
        combobox_nombre.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))

        # Vincular la función de autocompletar al evento de escritura
        combobox_nombre.bind('<KeyRelease>', on_key_release)

        # Crear el Label de advertencia
        advertencia_label = tk.Label(confirm_window, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(pady=(0, 30))

        def cargar_datos_producto(event):
            producto_seleccionado = combobox_nombre.get()
            for producto in productos:
                if producto[1] == producto_seleccionado:  # Comparar con el nombre del producto
                    entry_id.config(state='normal')
                    entry_id.delete(0, tk.END)
                    entry_id.insert(0, producto[0])  # ID del producto
                    entry_id.config(state='readonly')


                    entry_precio_compra.delete(0, tk.END)
                    entry_precio_compra.insert(0, producto[2])  # Precio de compra

                    entry_precio.delete(0, tk.END)
                    entry_precio.insert(0, producto[3])  # Precio de venta

                    entry_cantidad.config(state='normal')
                    entry_cantidad.delete(0, tk.END)
                    entry_cantidad.insert(0, producto[4])  # Cantidad
                    

                    combobox_busqueda1.config(state='normal')
                    combobox_busqueda1.set(producto[5])  # Categoria
                    combobox_busqueda1.config(state='readonly')

                    combobox_busqueda2.config(state='normal')
                    combobox_busqueda2.set(producto[6])  # Proveedor
                    combobox_busqueda2.config(state='readonly')

        combobox_nombre.bind("<<ComboboxSelected>>", cargar_datos_producto)

        def on_yes():
            id_producto = entry_id.get()
            nombre_producto = combobox_nombre.get()
            precio_compra_producto = entry_precio_compra.get()
            precio_venta_producto = entry_precio.get()
            cantidad = entry_cantidad.get()
            categoria_producto = combobox_busqueda1.get()
            proveedor_producto = combobox_busqueda2.get()

            producto_seleccionado = combobox_nombre.get()
            for producto in productos:
                if producto[1] == producto_seleccionado:
                    precio_anterior_compra = producto[2]
                    precio_anterior_venta = producto[3]
                    cantidad_ant = producto[4]
                    categ_ant = producto[5]
                    prov_ant = producto[6]

            def es_numero_decimal(valor):
                try:
                    float(valor)  # Intenta convertir a número flotante
                    return True
                except ValueError:
                    return False
                
            if nombre_producto:
               
                if es_numero_decimal(precio_venta_producto) and es_numero_decimal(precio_compra_producto) and es_numero_decimal(cantidad):
                    
                    if (float(precio_anterior_venta) == float(precio_venta_producto)) and (categ_ant == categoria_producto) and (prov_ant == proveedor_producto) and (float(precio_anterior_compra) == float(precio_compra_producto) and (float(cantidad) == float(cantidad_ant))):
                        advertencia_label.config(text="Actualice el producto por favor")
                    else:
                        actualizar_producto(nombre_producto, precio_compra_producto, precio_venta_producto, cantidad, categoria_producto, proveedor_producto)
                        self.minimarket.mostrar_arbol_productos_cat_prov()  # mostrar productos actualizados
                        on_no()
                    return
                else:
                    advertencia_label.config(text="Solo acepta números y decimales")
                    return
            else:
                advertencia_label.config(text="No acepta vacios")
                return

        def on_no():
            confirm_window.destroy()  # Cerrar la ventana

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(7):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        confirm_window.protocol("WM_DELETE_WINDOW", on_no)

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        confirm_window.bind('<Return>', lambda event: on_yes())

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        confirm_window.bind('<Return>', lambda event: on_yes())

         # Inicializar el valor de barcode y el tiempo de la última tecla presionada
        barcode = ""
        last_time = time.time()

        # Función para manejar la entrada del lector de código de barras
        def on_key_press(event):
            nonlocal barcode, last_time
            current_time = time.time()

            # Si el tiempo entre teclas es mayor a 0.1 segundos, reiniciar el barcode
            if current_time - last_time > 0.1:
                barcode = ""

            last_time = current_time

            if event.name == 'enter':
                producto = traer_producto(barcode)  # Llamar a la función traer_producto con el código de barras
                if producto:
                    entry_id.config(state="normal")
                    entry_id.delete(0, tk.END)
                    entry_id.insert(0, producto[0])
                    entry_id.config(state="readonly")

                    combobox_nombre.set(producto[1])

                    entry_precio_compra.config(state="normal")
                    entry_precio_compra.delete(0, tk.END)
                    entry_precio_compra.insert(0, producto[2])
                    

                    entry_precio.config(state="normal")
                    entry_precio.delete(0, tk.END)
                    entry_precio.insert(0, producto[3])
                    

                    entry_cantidad.config(state="normal")
                    entry_cantidad.delete(0, tk.END)
                    entry_cantidad.insert(0, producto[4])
                    

                    combobox_busqueda1.config(state="normal")
                    combobox_busqueda1.delete(0, tk.END)
                    combobox_busqueda1.insert(0, producto[5])
                    

                    combobox_busqueda2.config(state="normal")
                    combobox_busqueda2.delete(0, tk.END)
                    combobox_busqueda2.insert(0, producto[6])
                   

                    
                barcode = ""
            elif event.name.isdigit():
                barcode += event.name

        # Vincular la función de escaneo de código de barras
        keyboard.on_press(on_key_press)

        confirm_window.mainloop()

    def visualizar_productos(self):
       self.minimarket.mostrar_arbol_productos_cat_prov()


    def agregar_proveedor(self):
        
        # Crear una ventana secundaria
        ventana = Toplevel()
        ventana.title("Añadir Proveedor")
        ventana.geometry("1200x300")  # Ajusta el tamaño según necesites
        ventana.resizable(False, False)  # Evita que se redimensione
        ventana.configure(bg="white")
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)

        # Hacer la ventana modal
        ventana.grab_set()

        # Centrar la ventana en la pantalla
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 700
        else:
            ancho_ventana = 800

        alto_ventana = 320
        x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(ventana, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Ingrese los datos del proveedor:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=5, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="Nombre del proveedor", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        input_nombre = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_nombre.grid(row=2, column=0, padx=(30,10), pady=5)


        Label(frame, text="Número de telefono", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        input_telefono = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(    "%S"))
        input_telefono.grid(row=2, column=1, padx=10, pady=5)

        Label(frame, text="mail (opcional)", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        input_mail = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16), validate="key", validatecommand=(    "%S"))
        input_mail.grid(row=2, column=2, padx=10, pady=5)


        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(ventana, bg="white")
        button_frame.pack(pady=(0, 30))

        def on_yes():
            nombre_proveedor = input_nombre.get()
            num_telefono = input_telefono.get()
            mail = input_mail.get()

            # Verifica si los valores de precio y cantidad son válidos (números enteros o decimales)
            if not bool(re.match("^[A-Za-z0-9 ]*$", nombre_proveedor)):
                advertencia_label.config(text="No acepta ',.-/()'")
                return
            if not bool(re.match("^[0-9]*$", num_telefono)):
                advertencia_label.config(text="Solo acepta números")
                return
            if  not nombre_proveedor or not num_telefono:
                advertencia_label.config(text="No acepta vacios")
                return
    
            
            

            if cargar_proveedor(nombre_proveedor, num_telefono, mail):
                messagebox.showinfo("Proveedor", "Proveedor cargado con éxito")

            else: 
                messagebox.showerror("Error", "Esta queriendo ingresar un campo ya existente")
                return

            self.minimarket.mostrar_arbol_proveedores()
            
            on_no()

        def on_no():
            ventana.destroy()

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12,    "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12,     "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(4):
            frame.grid_columnconfigure(i, weight=2)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        ventana.protocol("WM_DELETE_WINDOW", on_no)

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: on_yes())

    def borrar_proveedor(self):

        # Crear la ventana
        ventana = tk.Toplevel()
        ventana.title("Borrar Proveedor")
        ventana.geometry("300x150")  # Tamaño de la ventana
        ventana.resizable(False, False)  # Evita que se redimensione
        
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)
        # Hacer la ventana modal
        ventana.grab_set()

        # Configurar el color de fondo de la ventana a blanco
        ventana.configure(bg="white")
        

        # Obtener el tamaño de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana

        if screen_width < 1100:

            window_width = 400
            window_height = 270
        else:
            window_width = 500
            window_height = 290

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        # Ubicar la ventana en el centro de la pantalla
        ventana.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Label para el nombre del producto
        label_nombre = tk.Label(ventana, text="Nombre del Proveedor:", bg="white", font=("Segoe UI", 16, "bold"))
        label_nombre.pack(pady=10)

        # Entry para el nombre del prodveedor con fondo #d7d7d7
        entry_nombre = tk.Entry(ventana, bg="#d7d7d7", font=("Segoe UI", 16), width=25)
        entry_nombre.pack(pady=5)

            # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack()
        
        # Función para confirmar y devolver el valor ingresado
        def confirmar():
            nombre_prov = entry_nombre.get()

            if not nombre_prov:  # Verificar si está vacío
                advertencia_label.config(text="No admite nombre vacío")
                return  # No hacer nada más si está vacío

            if bool(re.match("^[A-Za-z0-9 ]*$", nombre_prov)):  # Verificar si contiene letras y números
                v = buscar_proveedor(nombre_prov) # creada, y sida true lo borra al instante, si hace falta en otra instancia crear otra funcion solo para borrar
                if v:
                    messagebox.showinfo("Borrar Proveedor", "Proveedor borrado con éxito.")
                    self.minimarket.mostrar_arbol_proveedores()
                    ventana.destroy()  # Cerrar la ventana
                else:
                    messagebox.showinfo("Borrar Proveedor", "No se encontró el proveedor.")

            else:
                advertencia_label.config(text="Solo admite letras y números.")

        # Botón de borrar
        boton_confirmar = tk.Button(ventana, text="Borrar", command=confirmar, bg="#ef3232", relief="groove", font=("Segoe UI", 16, "bold"), fg="black", width=12)
        boton_confirmar.pack(pady=10)

        def cerrar():
            ventana.destroy()  # Cerrar la ventana

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar, bg="lightgrey", font=("Segoe UI", 14, "bold"), fg="black", relief="groove")
        boton_cerrar.pack(pady=5)

        ventana.protocol("WM_DELETE_WINDOW", cerrar)

        # Vincular el evento de la tecla Enter al botón de borrar
        ventana.bind('<Return>', lambda event: confirmar())

        # Iniciar el bucle principal de la ventana
        ventana.mainloop()

    def editar_proveedor(self):
        def filtrar_productos():
            value = combobox_nombre.get().lower()
            if value == '':
                combobox_nombre['values'] = proveedor_list
            else:
                data = []
                for item in proveedor_list:
                    if value in item.lower():
                        data.append(item)
                combobox_nombre['values'] = data
            combobox_nombre.event_generate('<Down>')

        def on_key_release(event):
            global filtro_timer
            if filtro_timer:
                confirm_window.after_cancel(filtro_timer)  # Cancelar temporizador anterior
            filtro_timer = confirm_window.after(1200, filtrar_productos)  # Esperar 1500 milisegundos

        confirm_window = Toplevel()
        confirm_window.title("Editar Producto")
        confirm_window.geometry("1200x300")  # Ajusta el tamaño según necesites
        confirm_window.resizable(False, False)  # Evita que se redimensione
        confirm_window.configure(bg="white")
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        confirm_window.iconbitmap(icon_path)

        # Inicializar filtro_timer
        global filtro_timer
        filtro_timer = None

        # Hacer la ventana modal
        confirm_window.grab_set()

        # Centrar la ventana en la pantalla
        confirm_window.update_idletasks()
        screen_width = confirm_window.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        if screen_width < 1100:
            ancho_ventana = 700
        else:
            ancho_ventana = 900

        alto_ventana = 320
        x = (confirm_window.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (confirm_window.winfo_screenheight() // 2) - (alto_ventana // 2)
        confirm_window.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(confirm_window, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Editar Proveedor:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=5, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="Nombre del proveedor", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=10, pady=5)
        combobox_nombre = ttk.Combobox(frame, font=("Segoe UI", 16), state="normal", height=5)
        combobox_nombre.grid(row=2, column=0, padx=(30,10), pady=5)

        proveedores = traer_todos_los_proveedores()  # Obtener los productos
        proveedor_list = [proveedor[0] for proveedor in proveedores]  # Lista con los nombres de los productos
        combobox_nombre['values'] = proveedor_list
        combobox_nombre.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))

        # Vincular la función de autocompletar al evento de escritura
        combobox_nombre.bind('<KeyRelease>', on_key_release)

        # Campo de precio editable
        Label(frame, text="Número de telefono", bg="white", font=("Segoe UI", 12)).grid(row=1, column=1, padx=10, pady=5)
        entry_num = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_num.grid(row=2, column=1, padx=10, pady=5)

        # Campo de cantidad no editable
        Label(frame, text="Mail", bg="white", font=("Segoe UI", 12)).grid(row=1, column=2, padx=10, pady=5)
        entry_mail = Entry(frame, width=20, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        entry_mail.grid(row=2, column=2, padx=10, pady=5)


        # Crear el Label de advertencia
        advertencia_label = tk.Label(confirm_window, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(pady=(0, 30))

        def cargar_datos_proveedor(event):
            proveedor_seleccionado = combobox_nombre.get()
            for proveedor in proveedores:
                if proveedor[0] == proveedor_seleccionado:
                    entry_num.delete(0, tk.END)
                    entry_num.insert(0, proveedor[1])  # Precio actual

                    entry_mail.config(state='normal')
                    entry_mail.delete(0, tk.END)
                    entry_mail.insert(0, proveedor[2])  # Cantidad
                    

        combobox_nombre.bind("<<ComboboxSelected>>", cargar_datos_proveedor)

        def on_yes():
            nombre_proveedor = combobox_nombre.get()
            num_proveedor = entry_num.get()
            mail_producto = entry_mail.get()

            proveedor_seleccionado = combobox_nombre.get()
            for proveedor in proveedores:
                if proveedor[0] == proveedor_seleccionado:
                    num_anterior = proveedor[1]
                    mail_ant = proveedor[2]
                    

            def es_numero_decimal(valor):
                try:
                    float(valor)  # Intenta convertir a número flotante
                    return True
                except ValueError:
                    return False

            if es_numero_decimal(num_proveedor):
                if (float(num_anterior) == float(num_proveedor)) and (mail_ant == mail_producto):
                    advertencia_label.config(text="Actualice el producto por favor")
                else:
                    actualizar_proveedor(nombre_proveedor, num_proveedor, mail_producto)
                    self.minimarket.mostrar_arbol_proveedores()
                    on_no()
                return
            else:
                advertencia_label.config(text="Seleccione un producto")
                return

        def on_no():
            confirm_window.destroy()  # Cerrar la ventana

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(5):
            frame.grid_columnconfigure(i, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        confirm_window.protocol("WM_DELETE_WINDOW", on_no)

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        confirm_window.bind('<Return>', lambda event: on_yes())

        confirm_window.mainloop()

    def visualizar_proveedores(self):
        self.minimarket.mostrar_arbol_proveedores()

    def agregar_categoria(self):
        # Crear una ventana secundaria
        ventana = Toplevel()
        ventana.title("Agregar Categoria")
        ventana.geometry("1200x300")  # Ajusta el tamaño según necesites
        ventana.resizable(False, False)  # Evita que se redimensione
        ventana.configure(bg="white")
       
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)

        # Hacer la ventana modal
        ventana.grab_set()

        # Centrar la ventana en la pantalla
        ventana.update_idletasks()
        screen_width = ventana.winfo_screenwidth()

        # Ajustar el ancho de la ventana según el ancho de la pantalla
        
        ancho_ventana = 500

        alto_ventana = 300
        x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Crear un frame contenedor central en la ventana secundaria
        frame = Frame(ventana, bg="white")
        frame.pack(fill="both", expand=False)

        # Título central
        Label(frame, text="Ingrese el nombre de la categoría:", bg="white", font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=5, pady=(10, 30)
        )

        # Etiquetas e Inputs
        Label(frame, text="Nombre de la categoria:", bg="white", font=("Segoe UI", 12)).grid(row=1, column=0, padx=(100, 0), pady=5)
        input_nombre = Entry(frame, width=23, bg="#e0e0e0", relief="groove", font=("Segoe UI", 16))
        input_nombre.grid(row=2, column=0, padx=(105,0), pady=5)


        # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack(pady=5)

        # Crear un frame para los botones
        button_frame = tk.Frame(ventana, bg="white")
        button_frame.pack(pady=(0, 30))

        def on_yes():
            nombre_categoria = input_nombre.get()

            # Verifica si los valores de precio y cantidad son válidos (números enteros o decimales)
            if not bool(re.match("^[A-Za-z0-9 ]*$", nombre_categoria)):
                advertencia_label.config(text="No acepta ',.-/()'")
                return

            if  not nombre_categoria:
                advertencia_label.config(text="No acepta vacios")
                return
            

            if cargar_categoria(nombre_categoria):
                messagebox.showinfo("Proveedor", "Categoria cargada con éxito")

            else: 
                advertencia_label.config(text="Categoría ya existente")
                return

            self.minimarket.mostrar_arbol_categorias()
            on_no()

        def on_no():
            ventana.destroy()

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_yes, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12,    "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_no, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12,     "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)

        # Configurar peso de filas y columnas para centrar
        for i in range(4):
            frame.grid_columnconfigure(i, weight=2)
        frame.grid_rowconfigure(0, weight=1)

        # Vincular el evento de cierre de la ventana a la función on_no
        ventana.protocol("WM_DELETE_WINDOW", on_no)

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: on_yes())

    def borrar_categoria(self):
        # Crear la ventana
        ventana = tk.Toplevel()
        ventana.title("Borrar Categoría")
        ventana.geometry("300x150")  # Tamaño de la ventana
        ventana.resizable(False, False)  # Evita que se redimensione
        ventana.grab_set()
       
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)
        

        # Configurar el color de fondo de la ventana a blanco
        ventana.configure(bg="white")
        

        # Obtener el tamaño de la pantalla
        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana

        if screen_width < 1100:

            window_width = 400
            window_height = 270
        else:
            window_width = 500
            window_height = 290

        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))

        # Ubicar la ventana en el centro de la pantalla
        ventana.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Label para el nombre del producto
        label_nombre = tk.Label(ventana, text="Nombre de la categoría:", bg="white", font=("Segoe UI", 16, "bold"))
        label_nombre.pack(pady=10)

        # Entry para el nombre del prodveedor con fondo #d7d7d7
        entry_nombre = tk.Entry(ventana, bg="#d7d7d7", font=("Segoe UI", 16), width=25)
        entry_nombre.pack(pady=5)

            # Crear el Label de advertencia
        advertencia_label = tk.Label(ventana, text="", font=("Segoe UI", 12, "bold"), fg="red", bg="white")
        advertencia_label.pack()
        
        # Función para confirmar y devolver el valor ingresado
        def confirmar():
            nombre_categ = entry_nombre.get()

            if not nombre_categ:  # Verificar si está vacío
                advertencia_label.config(text="No admite nombre vacío")
                return  # No hacer nada más si está vacío

            if bool(re.match("^[A-Za-z0-9 ]*$", nombre_categ)):  # Verificar si contiene letras y números
                v = buscar_categoria(nombre_categ) # creada, y sida true lo borra al instante, si hace falta en otra instancia crear otra funcion solo para borrar
                if v:
                    messagebox.showinfo("Borrar Categoria", "Catgoría borrada con éxito.")
                    self.minimarket.mostrar_arbol_categorias()
                    ventana.destroy()  # Cerrar la ventana
                else:
                    advertencia_label.config(text="No se encontro la categoría")

            else:
                advertencia_label.config(text="Solo admite letras y números.")

        # Botón de borrar
        boton_confirmar = tk.Button(ventana, text="Borrar", command=confirmar, bg="#ef3232", relief="groove", font=("Segoe UI", 16, "bold"), fg="black", width=12)
        boton_confirmar.pack(pady=10)

        def cerrar():
            ventana.destroy()  # Cerrar la ventana

        # Botón para cerrar la ventana
        boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar, bg="lightgrey", font=("Segoe UI", 14, "bold"), fg="black", relief="groove")
        boton_cerrar.pack(pady=5)

        ventana.protocol("WM_DELETE_WINDOW", cerrar)

        # Vincular el evento de la tecla Enter al botón de borrar
        ventana.bind('<Return>', lambda event: confirmar())

        # Iniciar el bucle principal de la ventana
        ventana.mainloop()

    
    def visualizar_categorias(self):
        self.minimarket.mostrar_arbol_categorias()


    def borrar_datos(self):
        


        # Crear una nueva ventana para la selección
        confirm_window = tk.Toplevel()
        confirm_window.title("Borrar Datos")
        confirm_window.geometry("400x250")  # Ajustar el tamaño
        confirm_window.config(bg="white")
        confirm_window.resizable(False, False)  # Evitar que se redimensione
        
        confirm_window.resizable(False, False)  # Evitar que se redimensione
        confirm_window.grab_set()  # Hacer la ventana modal

        # Centrando la ventana
        screen_width = confirm_window.winfo_screenwidth()
        screen_height = confirm_window.winfo_screenheight()
        window_width = 400
        window_height = 150
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        confirm_window.iconbitmap(icon_path)

        # Crear etiquetas y casillas de verificación para seleccionar qué borrar
        label = tk.Label(confirm_window, text="¿Desea borrar todos los datos?", font=("Segoe UI", 14), bg="white")
        label.pack(pady=10)


        # Función para manejar el botón "Aceptar"
        def on_accept():
            # Pasar las selecciones como parámetros a la función clear_data
            clear_data()
            confirm_window.destroy()

        # Función para manejar el botón "Cancelar"
        def on_cancel():
            confirm_window.destroy()

        # Crear el marco para los botones
        button_frame = tk.Frame(confirm_window, bg="white")
        button_frame.pack(pady=20)

        # Botones
        btn_yes = tk.Button(button_frame, text="Aceptar", command=on_accept, width=12, relief="groove", bg="#d7d7d7", fg="black", font=("Segoe UI", 12,    "bold"))
        btn_yes.pack(side=tk.LEFT, padx=15)

        btn_no = tk.Button(button_frame, text="Cancelar", command=on_cancel, width=12, relief="groove", bg="#ef3232", fg="black", font=("Segoe UI", 12,     "bold"))
        btn_no.pack(side=tk.LEFT, padx=15)


        confirm_window.mainloop()

    

class BuscarDatos:
    def __init__(self, master, minimarket, username):
        self.master = master
        self.minimarket = minimarket
        self.username = username

    def mostrar(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Contenido de Buscar Datos", bg="white",font=("Segoe UI", 10, "bold") ).pack(pady=10)


        # Botones "Datos por Día" y "Datos por Mes"
        botones = [
            ("Arqueo", self.datos_por_dia),
            ("Datos por Mes", self.datos_por_mes)
        ]

        for texto, comando in botones:
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)


    global datos_dia_abierto
    datos_dia_abierto = False

    def datos_por_dia(self):


        global datos_dia_abierto

        if datos_dia_abierto:
            return
        
        datos_dia_abierto = True

        ventana = tk.Toplevel()
        ventana.title("Seleccionar Fecha")
        ventana.configure(bg="white")
        ventana.update_idletasks()
        width = 1000
        height = 800
        x = (ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (ventana.winfo_screenheight() // 2) - (height // 2)
        ventana.geometry(f"{width}x{height}+{x}+{y}")
       
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)

        main_frame = tk.Frame(ventana, bg="white")
        main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        ventana.grid_columnconfigure(0, weight=1)
        ventana.grid_rowconfigure(0, weight=1)

        label_fecha = tk.Label(main_frame, text="Seleccione una Fecha:", bg="white", font=("Segoe UI", 16))
        label_fecha.grid(row=0, column=0, pady=10, sticky='n')

        fecha_actual = datetime.now()
        dia_actual = fecha_actual.day
        mes_actual = fecha_actual.month
        anio_actual = fecha_actual.year

        fecha_frame = tk.Frame(main_frame, bg="white")
        fecha_frame.grid(row=1, column=0, pady=5, sticky='n')

        fecha_frame.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))
        dias = list(range(1, 32))
        combobox_dia = ttk.Combobox(fecha_frame, values=dias, state="readonly", font=("Segoe UI", 16))
        combobox_dia.set(dia_actual)
        combobox_dia.grid(row=0, column=0, padx=5, sticky="ew")

        meses = list(range(1, 13))
        combobox_mes = ttk.Combobox(fecha_frame, values=meses, state="readonly", font=("Segoe UI", 16))
        combobox_mes.set(mes_actual)
        combobox_mes.grid(row=0, column=1, padx=5, sticky="ew")

        anios = list(range(2023, anio_actual + 1))
        combobox_anio = ttk.Combobox(fecha_frame, values=anios, state="readonly", font=("Segoe UI", 16))
        combobox_anio.set(anio_actual)
        combobox_anio.grid(row=0, column=2, padx=5, sticky="ew")

        # Configurar el peso de las columnas para que se ajusten al tamaño de la ventana
        fecha_frame.grid_columnconfigure(0, weight=1)
        fecha_frame.grid_columnconfigure(1, weight=1)
        fecha_frame.grid_columnconfigure(2, weight=1)

        resultados_frame = tk.Frame(main_frame, bg="white")
        resultados_frame.grid(row=2, column=0, pady=20, sticky='nsew')
        main_frame.grid_rowconfigure(2, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        total_contado = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_contado.grid(row=0, column=0, sticky='w', padx=(10, 5))

        total_mercado_pago = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_mercado_pago.grid(row=1, column=0, sticky='w', padx=(10, 5))

        total_cuenta_corriente = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_cuenta_corriente.grid(row=2, column=0, sticky='w', padx=(10, 5))

        ventas_frame = tk.Frame(resultados_frame)
        ventas_frame.grid(row=3, column=0, sticky='nsew', padx=10, pady=(20, 0), columnspan=2)
        resultados_frame.grid_rowconfigure(3, weight=1)
        resultados_frame.grid_columnconfigure(0, weight=1)

        scrollbar_ventas = tk.Scrollbar(ventas_frame)
        scrollbar_ventas.pack(side=tk.RIGHT, fill=tk.Y)

        text_ventas = tk.Text(ventas_frame, bg="white", font=("Segoe UI", 16), height=7, yscrollcommand=scrollbar_ventas.set)
        text_ventas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_ventas.config(state=tk.DISABLED)

        scrollbar_ventas.config(command=text_ventas.yview)

        total_compras = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_compras.grid(row=4, column=0, sticky='w', padx=10, pady=(10, 5))

        compras_frame = tk.Frame(resultados_frame)
        compras_frame.grid(row=5, column=0, sticky='nsew', padx=10, columnspan=2)
        resultados_frame.grid_rowconfigure(5, weight=1)

        scrollbar_compras = tk.Scrollbar(compras_frame)
        scrollbar_compras.pack(side=tk.RIGHT, fill=tk.Y)

        text_compras = tk.Text(compras_frame, bg="white", font=("Segoe UI", 18), height=7, yscrollcommand=scrollbar_compras.set)
        text_compras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_compras.config(state=tk.DISABLED)

        scrollbar_compras.config(command=text_compras.yview)

        total_contado['text'], total_mercado_pago['text'], total_cuenta_corriente['text'], total_compras['text'] = "Ventas Contado: $ 0", "Ventas Mercado Pago: $ 0", "Ventas Cuenta Corriente: $ 0", "Compras Total: $ 0"

        def aceptar():
            dia_seleccionado = combobox_dia.get()
            mes_seleccionado = combobox_mes.get()
            anio_seleccionado = combobox_anio.get()

            if dia_seleccionado and mes_seleccionado and anio_seleccionado:
                fecha_seleccionada = f"{anio_seleccionado}-{str(mes_seleccionado).zfill(2)}-{str(dia_seleccionado).zfill(2)}"
                fecha_seleccionada_date = datetime.strptime(fecha_seleccionada, "%Y-%m-%d").date()

                all_data_ventas = traer_todos_losdatos_ventaocompra(True)
                all_data_compras = traer_todos_losdatos_ventaocompra(False)

                ventas_filtradas = [venta for venta in all_data_ventas if venta[1] == fecha_seleccionada_date]
                compras_filtradas = [compra for compra in all_data_compras if compra[1] == fecha_seleccionada_date]

                total_contado['text'], total_mercado_pago['text'], total_cuenta_corriente['text'], total_compras['text'] = totales(ventas_filtradas, compras_filtradas, s=False)


                ventas_texto = "\n".join([f"id_venta: {venta[0]} | Fecha: {venta[1]} | Total: ${venta[2]} | Hora: {venta[3]} | Método de Pago: {venta[4]} | Vendedor: {traer_usuario(ventas_filtradas)}" for venta in ventas_filtradas])
                text_ventas.config(state=tk.NORMAL)
                text_ventas.delete(1.0, tk.END)
                text_ventas.insert(tk.END, ventas_texto if ventas_texto else "No hay ventas para esta fecha.")
                text_ventas.config(state=tk.DISABLED)

                compras_texto = "\n".join([f"id_compra: {compra[0]} | Fecha: {compra[1]} | Total: ${compra[2]} | Hora: {compra[3]} | Comprador: {traer_usuario(ventas_filtradas)}" for compra in compras_filtradas])
                text_compras.config(state=tk.NORMAL)
                text_compras.delete(1.0, tk.END)
                text_compras.insert(tk.END, compras_texto if compras_texto else "No hay compras para esta fecha.")
                text_compras.config(state=tk.DISABLED)

        def cerrar():
            global datos_dia_abierto
            datos_dia_abierto = False
            ventana.destroy()

        global datos_id_abierto
        datos_id_abierto = False

        def mostrar_detalles(ventas_compras, tipo):
            detalles_texto = "\n".join([
                f"id_detalle: {detalle[0]} | id_{'venta' if tipo else 'compra'}: {detalle[1]} | id_producto: {detalle[2]} | Cantidad: {detalle[3]:.1f} | Precio Unitario: ${detalle[4]:.2f}"
                for detalle in ventas_compras
            ])
            return detalles_texto if detalles_texto else "No hay registros disponibles."

        def ver_detalle():
            global datos_id_abierto

            if datos_id_abierto:
                return

            datos_id_abierto = True

            # Crear la ventana hija con Toplevel
            ventana = tk.Toplevel()
            ventana.title("ID detalle")
            ventana.iconbitmap(resource_path("resources/r.ico"))
            ventana.configure(bg="white")
            ventana.geometry("1000x700")  # Establecer la altura fija de 700px

            # Deshabilitar la opción de redimensionar la ventana
            ventana.resizable(False, False)

            # Centrar la ventana en la pantalla
            ventana.update_idletasks()
            width = 1000
            height = 350
            x = (ventana.winfo_screenwidth() // 2) - (width // 2)
            y = (ventana.winfo_screenheight() // 2) - (height // 2)
            ventana.geometry(f"{width}x{height}+{x}+{y}")

            # Crear contenido de la ventana
            main_frame = tk.Frame(ventana, bg="white")
            main_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

            ventana.grid_rowconfigure(0, weight=1)
            ventana.grid_columnconfigure(0, weight=1)

            label_titulo = tk.Label(main_frame, text="Inserte el ID de venta o compra para ver su detalle", bg="white", font=("Segoe UI", 16))
            label_titulo.grid(row=0, column=0, columnspan=2, pady=10, sticky='n')

            # ComboBox para seleccionar entre "Venta" y "Compra"
            tipo_var = tk.StringVar()
            combobox_tipo = ttk.Combobox(main_frame, textvariable=tipo_var, values=["Venta", "Compra"], state="readonly", font=("Segoe UI", 16), width=30)
            combobox_tipo.set("Venta")
            combobox_tipo.grid(row=1, column=0, columnspan=2, pady=10)

            # Entry para ingresar el ID de venta o compra
            id_var = tk.StringVar()
            entry_id = tk.Entry(main_frame, textvariable=id_var, font=("Segoe UI", 16), width=10, bg="#e0e0e0")
            entry_id.grid(row=2, column=0, columnspan=2, pady=10)

            resultados_frame = tk.Frame(main_frame, bg="white")
            resultados_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky='nsew')
            main_frame.grid_rowconfigure(3, weight=1)
            main_frame.grid_columnconfigure(0, weight=1)

            text_resultado = tk.Text(resultados_frame, bg="white", font=("Segoe UI", 17), state=tk.DISABLED)
            text_resultado.pack(fill=tk.BOTH, expand=True)

            scrollbar_resultado = tk.Scrollbar(resultados_frame, command=text_resultado.yview)
            scrollbar_resultado.pack(side=tk.RIGHT, fill=tk.Y)
            text_resultado.config(yscrollcommand=scrollbar_resultado.set)

            # Función para buscar detalles
            def buscar_detalle():
                id_seleccionado = entry_id.get().strip()  # Obtener directamente el valor del Entry

                if id_seleccionado.isdigit():
                    s = True if combobox_tipo.get() == "Venta" else False
                    detalles = traer_detalles(s=s, id=int(id_seleccionado))
                    
                    detalles_texto = mostrar_detalles(detalles, s)
                    

                    # Mostrar los detalles en el Text widget
                    text_resultado.config(state=tk.NORMAL)
                    text_resultado.delete(1.0, tk.END)
                    text_resultado.insert(tk.END, detalles_texto)
                    text_resultado.config(state=tk.DISABLED)
                else:
                    # Mostrar mensaje de error si el ID no es un número válido
                    text_resultado.config(state=tk.NORMAL)
                    text_resultado.delete(1.0, tk.END)
                    text_resultado.insert(tk.END, "Por favor, ingrese un ID numérico válido.")
                    text_resultado.config(state=tk.DISABLED)

            # Función para cerrar la ventana hija
            def cerrar():
                global datos_id_abierto
                datos_id_abierto = False
                ventana.destroy()

            boton_buscar = tk.Button(main_frame, text="Buscar", command=buscar_detalle, bg="lightgrey", font=("Segoe UI", 12, "bold"), cursor="hand2", fg="black", relief="groove", width=10)
            boton_buscar.grid(row=4, column=0, pady=10, padx=(115,0))

            boton_cerrar = tk.Button(main_frame, text="Cerrar", command=cerrar, bg="#ef3232", font=("Segoe UI", 12, "bold"), cursor="hand2", fg="black", relief="groove", width=10)
            boton_cerrar.grid(row=4, column=1, pady=10)
            
            # Configurar el protocolo para manejar el cierre de la ventana hija
            ventana.protocol("WM_DELETE_WINDOW", cerrar)
            
            # Vincular el evento de la tecla Enter al botón "Buscar"
            ventana.bind('<Return>', lambda event: buscar_detalle())

            ventana.mainloop()

        boton_aceptar = tk.Button(main_frame, text="Aceptar", command=aceptar, bg="lightgrey", font=("Segoe UI", 14, "bold"), cursor="hand2", fg="black", relief="groove")
        boton_aceptar.grid(row=3, column=0, pady=10, sticky='n')

        boton_aceptar = tk.Button(main_frame, text="Ver detalle de venta", command=ver_detalle, bg="lightgrey", font=("Segoe UI", 14, "bold"), cursor="hand2", fg="black", relief="groove")
        boton_aceptar.grid(row=4, column=0, pady=10, sticky='n')

        boton_cerrar = tk.Button(main_frame, text="Cerrar", command=cerrar, bg="#ef3232", font=("Segoe UI", 14, "bold"), cursor="hand2", fg="black", relief="groove")
        boton_cerrar.grid(row=5, column=0, pady=(70, 10), sticky='n')

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: aceptar())

        # Vincular el evento de cierre de la ventana a la función cerrar
        ventana.protocol("WM_DELETE_WINDOW", cerrar)

        ventana.mainloop()
    
    def datos_por_mes(self):
        ventana = tk.Toplevel()
        ventana.title("Seleccionar Mes y Año")
       
        ventana.configure(bg="white")
        ventana.update_idletasks()
        width = 700
        height = 850
        x = (ventana.winfo_screenwidth() // 2) - (width // 2)
        y = (ventana.winfo_screenheight() // 2) - (height // 2)
        ventana.geometry(f"{width}x{height}+{x}+{y}")
        ventana.grab_set()
        ventana.resizable(False, False)
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana.iconbitmap(icon_path)
        

        ventana.grid_rowconfigure(0, weight=1)
        ventana.grid_columnconfigure(0, weight=1)

        main_frame = tk.Frame(ventana, bg="white")
        main_frame.grid(pady=20, padx=20, sticky='nsew')
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)

        label_fecha = tk.Label(main_frame, text="Seleccione Mes y Año:", bg="white", font=("Segoe UI", 16))
        label_fecha.grid(row=0, column=0, pady=10, sticky='n')

        fecha_actual = datetime.now()
        mes_actual = fecha_actual.month
        anio_actual = fecha_actual.year

        fecha_frame = tk.Frame(main_frame, bg="white")
        fecha_frame.grid(row=1, column=0, pady=5, sticky='n')

        fecha_frame.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))

        # Combobox para seleccionar el mes
        meses = list(range(1, 13))
        combobox_mes = ttk.Combobox(fecha_frame, values=meses, state="readonly", font=("Segoe UI", 16), width=5)
        combobox_mes.set(mes_actual)
        combobox_mes.grid(row=0, column=0, padx=5, sticky='ew')

        # Combobox para seleccionar el año
        anios = list(range(2023, anio_actual + 1))
        combobox_anio = ttk.Combobox(fecha_frame, values=anios, state="readonly", font=("Segoe UI", 16), width=7)
        combobox_anio.set(anio_actual)
        combobox_anio.grid(row=0, column=1, padx=5, sticky='ew')

        fecha_frame.grid_columnconfigure(0, weight=1)
        fecha_frame.grid_columnconfigure(1, weight=1)

        resultados_frame = tk.Frame(main_frame, bg="white")
        resultados_frame.grid(row=2, column=0, pady=10, sticky='nsew')
        resultados_frame.grid_rowconfigure(4, weight=1)
        resultados_frame.grid_rowconfigure(6, weight=1)
        resultados_frame.grid_columnconfigure(0, weight=1)

        total_ventas = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_ventas.grid(row=0, column=0, sticky='w', padx=(10, 5))

        total_contado = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_contado.grid(row=1, column=0, sticky='w', padx=(10, 5))

        total_mercado_pago = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_mercado_pago.grid(row=2, column=0, sticky='w', padx=(10, 5))

        total_cuenta_corriente = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_cuenta_corriente.grid(row=3, column=0, sticky='w', padx=(10, 5))

        ventas_frame = tk.Frame(resultados_frame)
        ventas_frame.grid(row=4, column=0, sticky='nsew', padx=10, pady=(10, 0))

        scrollbar_ventas = tk.Scrollbar(ventas_frame)
        scrollbar_ventas.pack(side=tk.RIGHT, fill=tk.Y)

        text_ventas = tk.Text(ventas_frame, bg="white", font=("Segoe UI", 15), height=8, width=100, yscrollcommand=scrollbar_ventas.set)
        text_ventas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_ventas.config(state=tk.DISABLED)

        scrollbar_ventas.config(command=text_ventas.yview)

        total_compras = tk.Label(resultados_frame, text="", bg="white", font=("Segoe UI", 20, "bold"))
        total_compras.grid(row=5, column=0, sticky='w', padx=10, pady=(5, 5))

        compras_frame = tk.Frame(resultados_frame)
        compras_frame.grid(row=6, column=0, sticky='nsew', padx=10)

        scrollbar_compras = tk.Scrollbar(compras_frame)
        scrollbar_compras.pack(side=tk.RIGHT, fill=tk.Y)

        text_compras = tk.Text(compras_frame, bg="white", font=("Segoe UI", 15), height=8, width=100, yscrollcommand=scrollbar_compras.set)
        text_compras.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        text_compras.config(state=tk.DISABLED)

        scrollbar_compras.config(command=text_compras.yview)

        total_ventas['text'], total_contado['text'], total_mercado_pago['text'], total_cuenta_corriente['text'], total_compras['text'] = "Ventas Total: $ 0", "Ventas Contado: $ 0", "Ventas Mercado Pago: $ 0", "Ventas Cuenta Corriente: $ 0", "Compras Total: $ 0"

        def ajustar_fuente(event=None):
            width = ventana.winfo_width()
            height = ventana.winfo_height()
            new_size = min(max(int(width / 50), 10), 20)
            for widget in [label_fecha, total_ventas, total_contado, total_mercado_pago, total_cuenta_corriente, total_compras]:
                widget.config(font=("Segoe UI", new_size, "bold"))
            for widget in [combobox_mes, combobox_anio, text_ventas, text_compras]:
                widget.config(font=("Segoe UI", new_size))

        ventana.bind('<Configure>', ajustar_fuente)
        ajustar_fuente()  # Llamar a la función manualmente para ajustar la fuente inicialmente

        def aceptar():
            mes_seleccionado = combobox_mes.get()
            anio_seleccionado = combobox_anio.get()

            if mes_seleccionado and anio_seleccionado:
                fecha_inicio = date(int(anio_seleccionado), int(mes_seleccionado), 1)
                ultimo_dia_mes = calendar.monthrange(int(anio_seleccionado), int(mes_seleccionado))[1]
                fecha_fin = date(int(anio_seleccionado), int(mes_seleccionado), ultimo_dia_mes)

                all_data_ventas = traer_todos_losdatos_ventaocompra(s=True)
                all_data_compras = traer_todos_losdatos_ventaocompra(s=False)

                ventas_filtradas = [venta for venta in all_data_ventas if fecha_inicio <= venta[1] <= fecha_fin]
                compras_filtradas = [compra for compra in all_data_compras if fecha_inicio <= compra[1] <= fecha_fin]
                

                total_ventas['text'], total_contado['text'], total_mercado_pago['text'], total_cuenta_corriente['text'], total_compras['text'] = totales(ventas_filtradas, compras_filtradas, s=True)
                ventas_texto = "\n".join([f"id venta: {venta[0]} | Fecha: {venta[1]} | Total: {venta[2]} | Hora: {venta[3]} | Metodo de pago: {venta[4]} | Vendedor: {traer_usuario(ventas_filtradas)}"  for venta in ventas_filtradas])
                text_ventas.config(state=tk.NORMAL)
                text_ventas.delete(1.0, tk.END)
                text_ventas.insert(tk.END, ventas_texto if ventas_texto else "No hay ventas para este mes.")
                text_ventas.config(state=tk.DISABLED)

                compras_texto = "\n".join([f"id compra: {compra[0]} | Fecha: {compra[1]} | Total: {compra[2]} | Hora: {compra[3]} | Comprador: {traer_usuario(ventas_filtradas)}" for compra in compras_filtradas])

                text_compras.config(state=tk.NORMAL)
                text_compras.delete(1.0, tk.END)
                text_compras.insert(tk.END, compras_texto if compras_texto else "No hay compras para este mes.")
                text_compras.config(state=tk.DISABLED)

        def cerrar():
            ventana.destroy()

        boton_aceptar = tk.Button(main_frame, text="Aceptar", command=aceptar, bg="#32ef32", font=("Segoe UI", 14, "bold"), cursor="hand2", fg="black", relief="groove", width=20)
        boton_aceptar.grid(row=3, column=0, pady=5, sticky='ew')

        boton_cerrar = tk.Button(main_frame, text="Cerrar", command=cerrar, bg="lightgrey", font=("Segoe UI", 14, "bold"), cursor="hand2", fg="black", relief="groove", width=20)
        boton_cerrar.grid(row=4, column=0, pady=5, sticky='ew')

        # Vincular el evento de la tecla Enter al botón "Aceptar"
        ventana.bind('<Return>', lambda event: aceptar())

        ventana.mainloop()
        
        
        


class Administracion:
    def __init__(self, master, minimarket, usuario):
        
        self.master = master
        self.minimarket = minimarket
        self.usuario = usuario

    def mostrar(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Contenido de Administración", bg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)
        # Botones "Facturero" y "Compras"
        botones = [
            ("Facturero", self.facturero),
            ("Compras", self.compras)
        ]

        for texto, comando in botones:
            tk.Button(self.master,text=texto,command=comando,height=1,  width=20,  bg="#e0e0e0",  fg="black", font=("Segoe UI", 12, "bold"),  activebackground="#c0c0c0",  activeforeground="white", relief="groove",  bd=2  ).pack(pady=9)

        # Crear el widget Text para el anotador
        self.text_anotador = tk.Text(self.master, font=("Segoe UI", 12), height=10)
        self.text_anotador.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Cargar las notas guardadas
        self.minimarket.cargar_notas()

    # Lista para almacenar los productos seleccionados
    productos_seleccionados = []


    # Métodos de ejemplo para los botones
    def facturero(self):
        
    
        self.minimarket.mostrar_arbol_productos()
    
        
    
        # Crear la ventana principal
        ventana_facturero = tk.Toplevel()
        ventana_facturero.title("Facturero")
        ventana_facturero.resizable(False, False)  # Evita que se redimensione
    
        # Centrar la ventana
        ventana_facturero_width = 600  # Ancho deseado
        ventana_facturero_height = 760  # Alto deseado
        screen_width = ventana_facturero.winfo_screenwidth()
        screen_height = ventana_facturero.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (ventana_facturero_width / 2))
        y_coordinate = int((screen_height / 2) - (ventana_facturero_height / 2))
        ventana_facturero.geometry(f"{ventana_facturero_width}x{ventana_facturero_height}+{x_coordinate}+{y_coordinate}")
        ventana_facturero.transient(self.master)
        ventana_facturero.grab_set()  # Asegura que todos los eventos se dirijan a esta ventana hasta que se cierre
        
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana_facturero.iconbitmap(icon_path)

        ventana_facturero.attributes('-topmost', True)



        # Crear el frame superior
        frame_superior = tk.Frame(ventana_facturero, bd=2, relief="groove")
        frame_superior.pack(side="top", fill="x", padx=10, pady=10)


        # Crear el Label de advertencia
        advertencia_label = tk.Label(frame_superior, text="\n", font=("Segoe UI", 12, "bold"), fg="red")
        advertencia_label.grid(row=7, column=0, columnspan=3, pady=5, sticky="ew")

        ids = traer_todos_los_productos()
        producto_ids = [producto_id[0] for producto_id in ids]
        # Crear campos de entrada solo para mostrar los datos (readonly)
        tk.Label(frame_superior, text="ID:", font=("Segoe UI", 13)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        producto_id = ttk.Combobox(frame_superior, values=producto_ids, font=("Segoe UI", 13), height=5)
        producto_id.grid(row=0, column=1, padx=5, pady=5)
        producto_id.selection_range(0, tk.END)

        filtro_id = None

        # Función para filtrar productos con retraso
        def filtrar_productos_ids_con_retraso(event):
            nonlocal filtro_id
            if filtro_id:
                ventana_facturero.after_cancel(filtro_id)  # Cancelar el filtro anterior si existe
            
            filtro_id = ventana_facturero.after(1000, lambda: filtrar_productos_ids(event))  # Esperar 1 segundo antes de filtrar

        # Función para filtrar productos y permitir escritura continua
        def filtrar_productos_ids(event):
            entrada = producto_id.get()  # Captura el texto ingresado
            try:
                entrada_int = int(entrada)  # Convertir la entrada a entero
                filtrados = [prod_id for prod_id in producto_ids if str(entrada_int) in str(prod_id)]  # Filtrar productos

            except ValueError:
                filtrados = []  # Si la entrada no es un número válido, no filtrar nada

            producto_id['values'] = filtrados  # Actualizar las opciones del combobox

            # Resaltar el texto en el combobox
            producto_id.selection_range(0, 'end')
            

            if filtrados:
                producto_id.event_generate('<Down>')  # Mostrar opciones filtradas

        # Vincular el evento KeyRelease para que espere 1 segundo antes de filtrar
        producto_id.bind('<KeyRelease>', filtrar_productos_ids_con_retraso)
    
        # Crear combobox para el nombre del producto
        tk.Label(frame_superior, text="Nombre del producto:", font=("Segoe UI", 13)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
        # Llenar el combobox con los nombres de los productos
        productos = traer_todos_los_productos()
        nombres_productos = [producto[1] for producto in productos]  # Extraer los nombres de los productos
        nombre_producto_combobox = ttk.Combobox(frame_superior, values=nombres_productos, font=("Segoe UI", 13), height=5)
        nombre_producto_combobox.set("Seleccionar nombre")
        nombre_producto_combobox.grid(row=1, column=1, padx=5, pady=5)
    
        # Variable para manejar el retraso
        filtro_id = None
    
        # Función para filtrar productos con retraso
        def filtrar_productos_con_retraso(event):
            nonlocal filtro_id
            if filtro_id:
                ventana_facturero.after_cancel(filtro_id)  # Cancelar el filtro anterior si existe
    
            filtro_id = ventana_facturero.after(1000, lambda: filtrar_productos(event))  # Esperar 1 segundo antes de filtrar
            
        # Función para filtrar productos y permitir escritura continua
        def filtrar_productos(event):
            entrada = nombre_producto_combobox.get().lower()  # Captura el texto ingresado
            filtrados = [prod for prod in nombres_productos if entrada in prod.lower()]  # Filtrar productos
            nombre_producto_combobox['values'] = filtrados  # Actualizar las opciones del combobox
    
            # Resaltar el texto en el combobox
            nombre_producto_combobox.selection_range(0, 'end')
    
            if filtrados:
                nombre_producto_combobox.event_generate('<Down>')  # Mostrar opciones filtradas

            
    
        # Vincular el evento KeyRelease para que espere 1 segundo antes de filtrar
        nombre_producto_combobox.bind('<KeyRelease>', filtrar_productos_con_retraso)
    
    
        tk.Label(frame_superior, text="Precio de venta:", font=("Segoe UI", 13)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        precio_producto_venta = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        precio_producto_venta.grid(row=2, column=1, padx=5, pady=5)
    
        tk.Label(frame_superior, text="Cantidad:", font=("Segoe UI", 13)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        cantidad_producto = tk.Entry(frame_superior, font=("Segoe UI", 13))  # Estado normal para permitir edición
        cantidad_producto.grid(row=3, column=1, padx=5, pady=5)
        cantidad_producto.insert(0, "0")  # Valor predeterminado de "0"
    
        tk.Label(frame_superior, text="Categoría:", font=("Segoe UI", 13)).grid(row=4, column=0, padx=5, pady=5, sticky="e")
        categoria = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        categoria.grid(row=4, column=1, padx=4, pady=5)
    
        tk.Label(frame_superior, text="Proveedor:", font=("Segoe UI", 13)).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        proveedor_producto = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        proveedor_producto.grid(row=5, column=1, padx=5, pady=5)
    
        # Crear combobox para el metodo de pago:
        tk.Label(frame_superior, text="Metodo de pago:", font=("Segoe UI", 13)).grid(row=6, column=0, padx=5, pady=5, sticky="e")
        frame_superior.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))
    
        # Llenar el combobox con los nombres de los metodos de pago
        metodos = [('Contado',), ('Cuenta Corriente',), ('Mercado Pago',)]
        nombres_metodos = [metodo[0] for metodo in metodos]  # Extraer los nombres de los productos
        nombre_metodos_combobox = ttk.Combobox(frame_superior, values=nombres_metodos, state="readonly", font=("Segoe UI", 13), height=5)
        nombre_metodos_combobox.grid(row=6, column=1, padx=5, pady=5)
    
        # Crear el área de texto para mostrar los productos añadidos
        tk.Label(ventana_facturero, text="Productos seleccionados:", font=("Segoe UI", 13)).pack(pady=5)
        result_text = tk.Text(ventana_facturero, height=8, width=55, state="normal", font=("Segoe UI", 16))
        result_text.pack(padx=10, pady=5)
        result_text.config(state="disabled")  # Iniciar en estado "disabled" (no editable)
    
        # Crear etiqueta para mostrar el total de la compra
        total_label = tk.Label(ventana_facturero, text="Total: $0.00", font=("Segoe UI", 13, "bold"))
        total_label.pack(side="right", padx=(0,20), pady=10)
    
        # Función para actualizar los datos del producto seleccionado
        def actualizar_datos_producto(event):
            # Obtener el nombre seleccionado del combobox
            nombre_seleccionado = nombre_producto_combobox.get()
            id_seleccionado = producto_id.get()
            # Buscar los datos del producto seleccionado
            for producto in productos:
                if producto[1] == nombre_seleccionado or str(producto[0]) == id_seleccionado:
                    # Actualizar los campos con los datos del producto seleccionado
                    producto_id.config(state="normal")
                    producto_id.delete(0, tk.END)
                    producto_id.insert(0, producto[0])  # ID
                    producto_id.selection_range(0, tk.END)

                    nombre_producto_combobox.set(producto[1])  # Nombre
    
                    precio_producto_venta.config(state="normal")
                    precio_producto_venta.delete(0, tk.END)
                    precio_producto_venta.insert(0, producto[3])  # Precio
                    precio_producto_venta.config(state="readonly")
    
                    cantidad_producto.delete(0, tk.END)
                    cantidad_producto.insert(0, "1")  # Dejar cantidad editable con valor predeterminado 1
    
                    categoria.config(state="normal")
                    categoria.delete(0, tk.END)
                    categoria.insert(0, producto[5])  # categoria
                    categoria.config(state="readonly")
    
                    proveedor_producto.config(state="normal")
                    proveedor_producto.delete(0, tk.END)
                    proveedor_producto.insert(0, producto[6])  # Proveedor
                    proveedor_producto.config(state="readonly")

                    nombre_metodos_combobox.set("Contado")

                    cantidad_producto.focus_set()
                    break
                
        # Función para añadir el producto seleccionado al arreglo y mostrarlo en el área de texto
        def añadir_producto():
            nombre_seleccionado = nombre_producto_combobox.get()
            cantidad_seleccionada = cantidad_producto.get()  # Obtener la cantidad modificada por el usuario
            metodo_pago_seleccionado = nombre_metodos_combobox.get()  # Obtener el método de pago elegido en el combobox
    
            if nombre_seleccionado and cantidad_seleccionada.isdecimal():
                for producto in productos:
                    if producto[1] == nombre_seleccionado:
                        total = float(producto[3]) * float(cantidad_seleccionada)
                        producto_modificado = (producto[1], f"{float(producto[3]):.2f}", cantidad_seleccionada, producto[5], producto[6], metodo_pago_seleccionado, f"Total: {total:.2f}")
    
                        # Comprobar si la cantidad es accesible, y en caso de error informar que no se puede realizar esa venta
                        s = True
                        d = controlar_cantidades(producto_modificado, s, advertencia_label)
                        if d:
                            self.productos_seleccionados.append(producto_modificado)
    
                            # Insertar el producto en el área de texto y editar tabla
                            actualizar_cantidad_productos([producto_modificado], s, l=False, m=False)
    
                            self.minimarket.mostrar_arbol_productos()
    
                            result_text.config(state="normal")  # Permitir escritura temporal
                            result_text.insert(tk.END, f"{producto_modificado}\n")  # Mostrar producto en el Text
                            result_text.config(state="disabled")  # Bloquear nuevamente para no permitir ediciones
                            result_text.see(tk.END)  # Desplazarse al final automáticamente

                            # Limpiar los campos de entrada
                            producto_id.config(state="normal")
                            producto_id.delete(0, tk.END)   
                            producto_id.set("")
                            producto_id.selection_range(0, tk.END)


                            nombre_producto_combobox.set("Seleccionar nombre")
                            precio_producto_venta.config(state="normal")
                            precio_producto_venta.delete(0, tk.END)
                            precio_producto_venta.config(state="readonly")

                            cantidad_producto.delete(0, tk.END)
                            cantidad_producto.insert(0, "0")

                            categoria.config(state="normal")
                            categoria.delete(0, tk.END)
                            categoria.config(state="readonly")

                            proveedor_producto.config(state="normal")
                            proveedor_producto.delete(0, tk.END)
                            proveedor_producto.config(state="readonly")

                            nombre_metodos_combobox.set("")

                            # Colocar el cursor en el campo de ID del producto
                            producto_id.focus_set()

                            # Ocultar el Label de advertencia después de 3 segundos
                            advertencia_label.after(3000, lambda: advertencia_label.config(text="\n"))
                            
                            # Actualizar el total de la compra
                            actualizar_total()
    
                            break
            else:
                advertencia_label.config(text="Por favor, complete \ntodos los campos correctamente")
    
        # Función para borrar el último producto añadido
        def borrar_ultimo_producto():
            if self.productos_seleccionados:
                s = False
                actualizar_cantidad_productos([self.productos_seleccionados[-1]], s, l=False, m=False)
    
                self.minimarket.mostrar_arbol_productos()
    
                self.productos_seleccionados.pop()  # Eliminar el último producto añadido
                # Limpiar y actualizar el área de texto
                result_text.config(state="normal")
                result_text.delete(1.0, tk.END)  # Borrar todo el contenido del área de texto
                for producto in self.productos_seleccionados:
                    result_text.insert(tk.END, f"{producto}\n")  # Reinsertar los productos restantes
                result_text.config(state="disabled")
                result_text.see(tk.END)
    
                # Actualizar el total de la compra
                actualizar_total()
    
        # Función para actualizar el total de la compra
        def actualizar_total():
            total = sum(float(producto[6].replace("Total: ", "")) for producto in self.productos_seleccionados)
            total_label.config(text=f"Total: ${total:.2f}")
    
        def procesar_productos():
            
            s = True
            anadir_a_registro(self.productos_seleccionados, s, self.usuario)
            # actualizar_cantidad_productos(productos_seleccionados, s)
    
            # Limpia el arreglo
            self.productos_seleccionados.clear()
    
            self.minimarket.mostrar_arbol_productos()  # Muestra todos los productos actualizados
    
            # Limpiar el área de texto y el total
            result_text.config(state="normal")
            result_text.delete(1.0, tk.END)
            result_text.config(state="disabled")
            total_label.config(text="Total: $0.00")

            # Limpiar los campos de entrada
            producto_id.config(state="normal")
            producto_id.delete(0, tk.END)
            producto_id.set("")
            producto_id.selection_range(0, tk.END)
            

            nombre_producto_combobox.set("Seleccionar nombre")
            precio_producto_venta.config(state="normal")
            precio_producto_venta.delete(0, tk.END)
            precio_producto_venta.config(state="readonly")

            cantidad_producto.delete(0, tk.END)
            cantidad_producto.insert(0, "0")

            categoria.config(state="normal")
            categoria.delete(0, tk.END)
            categoria.config(state="readonly")

            proveedor_producto.config(state="normal")
            proveedor_producto.delete(0, tk.END)
            proveedor_producto.config(state="readonly")

            nombre_metodos_combobox.set("")

            # Colocar el cursor en el campo de ID del producto
            producto_id.focus_set()

    
    
        # Crear botón "Borrar Último Agregado"
        boton_borrar = tk.Button(frame_superior, text="Borrar Último Agregado", font=("Segoe UI", 10, "bold"), relief="groove", bg="#ef3232", fg="black", command=borrar_ultimo_producto)
        boton_borrar.grid(row=8, column=0, padx=(15,5), pady=5, sticky="w")  # Posicionar a la izquierda
    
        # Crear botón "Añadir"
        boton_añadir = tk.Button(frame_superior, text="Añadir", font=("Segoe UI", 13, "bold"), command=añadir_producto, relief="groove", fg="black", bg="#d7d7d7")
        boton_añadir.grid(row=8, column=1, padx=5, pady=5)
    
        # Crear frame inferior para botones "Procesar" y "Cerrar"
        frame_botones = tk.Frame(ventana_facturero)
        frame_botones.place(x=10, y=708)

    
        # Botón "Cerrar"
        def cerrar_ventana():
            
    
            s = False
            actualizar_cantidad_productos(self.productos_seleccionados, s, l=True, m=False)
    
            self.minimarket.mostrar_arbol_productos()
    
            self.productos_seleccionados.clear()
    
            
            ventana_facturero.destroy()
    
        # Botón "Cerrar"
        boton_cerrar = tk.Button(frame_botones, text="Cerrar", font=("Segoe UI", 13, "bold"), command=cerrar_ventana, relief="groove", fg="black", bg="#ef3232")
        boton_cerrar.pack(side="left", padx=20)
    
        # Botón "Procesar"
        boton_procesar = tk.Button(frame_botones, text="Procesar", width=15, font=("Segoe UI", 13, "bold"), command=procesar_productos, relief="groove", fg="black", bg="#d7d7d7")
        boton_procesar.pack(side="right", padx=(90,0))

        # Vincular el evento de la tecla Enter al botón "Añadir"
        ventana_facturero.bind('<Return>', lambda event: añadir_producto())

         # Vincular el evento de selección en el combobox
        producto_id.bind("<<ComboboxSelected>>", actualizar_datos_producto)
        # Vincular el evento de selección en el combobox
        nombre_producto_combobox.bind("<<ComboboxSelected>>", actualizar_datos_producto)
        
        # Vincular el evento de cierre de la ventana para restablecer facturero_abierto
        ventana_facturero.protocol("WM_DELETE_WINDOW", cerrar_ventana)

        # Inicializar el valor de barcode y el tiempo de la última tecla presionada
        barcode = ""
        last_time = time.time()

        # Función para manejar la entrada del lector de código de barras
        def on_key_press(event):
            nonlocal barcode, last_time
            current_time = time.time()

            # Si el tiempo entre teclas es mayor a 0.1 segundos, reiniciar el barcode
            if current_time - last_time > 0.1:
                barcode = ""

            last_time = current_time

            if event.name == 'enter':
                producto = traer_producto(barcode)  # Llamar a la función traer_producto con el código de barras
                if producto:
                    producto_id.config(state="normal")
                    producto_id.delete(0, tk.END)
                    producto_id.insert(0, producto[0])
                    producto_id.selection_range(0, tk.END)

                    nombre_producto_combobox.set(producto[1])

                    precio_producto_venta.config(state="normal")
                    precio_producto_venta.delete(0, tk.END)
                    precio_producto_venta.insert(0, producto[3])
                    precio_producto_venta.config(state="readonly")

                    cantidad_producto.delete(0, tk.END)
                    cantidad_producto.insert(0, "1")

                    categoria.config(state="normal")
                    categoria.delete(0, tk.END)
                    categoria.insert(0, producto[5])
                    categoria.config(state="readonly")

                    proveedor_producto.config(state="normal")
                    proveedor_producto.delete(0, tk.END)
                    proveedor_producto.insert(0, producto[6])
                    proveedor_producto.config(state="readonly")

                    nombre_metodos_combobox.set("Contado")

                    cantidad_producto.focus_set()

                barcode = ""
            elif event.name.isdigit():
                barcode += event.name
                

        # Colocar el cursor en el campo de ID del producto
        producto_id.focus_set()
        # Vincular la función de escaneo de código de barrasd

        # Vincular la función de escaneo de código de barras
        keyboard.on_press(on_key_press)
        ventana_facturero.mainloop()

    # Lista para almacenar los productos seleccionados
    compras_seleccionadas = []

    def compras(self):

        global compra_abierto
        
    
        self.minimarket.mostrar_arbol_productos()
            
    
    
    
        # Crear la ventana principal
        ventana_compra = tk.Toplevel()
        ventana_compra.title("Compras")
        ventana_compra.resizable(False, False)  # Evita que se redimensione
    
        # Centrar la ventana
        ventana_compra_width = 600  # Ancho deseado
        ventana_compra_height = 760  # Alto deseado
        screen_width = ventana_compra.winfo_screenwidth()
        screen_height = ventana_compra.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (ventana_compra_width / 2))
        y_coordinate = int((screen_height / 2) - (ventana_compra_height / 2))
        ventana_compra.geometry(f"{ventana_compra_width}x{ventana_compra_height}+{x_coordinate}+{y_coordinate}")
        ventana_compra.focus_force()
        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        ventana_compra.iconbitmap(icon_path)

        ventana_compra.attributes('-topmost', True)
    
        # Crear el frame superior
        frame_superior = tk.Frame(ventana_compra, bd=2, relief="groove")
        frame_superior.pack(side="top", fill="x", padx=10, pady=10)

        # Crear el Label de advertencia
        advertencia_label = tk.Label(frame_superior, text="\n", font=("Segoe UI", 12, "bold"), fg="red")
        advertencia_label.grid(row=7, column=0, columnspan=3, pady=5, sticky="ew")
        
        ids = traer_todos_los_productos()
        producto_ids = [producto_id[0] for producto_id in ids]
        # Crear campos de entrada solo para mostrar los datos (readonly)
        tk.Label(frame_superior, text="ID:", font=("Segoe UI", 13)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        producto_id = ttk.Combobox(frame_superior, values=producto_ids, font=("Segoe UI", 13), height=5)
        producto_id.grid(row=0, column=1, padx=5, pady=5)
        producto_id.selection_range(0, tk.END)
        
        # Función para filtrar productos con retraso
        def filtrar_productos_ids_con_retraso(event):
            nonlocal filtro_id
            if filtro_id:
                ventana_compra.after_cancel(filtro_id)  # Cancelar el filtro anterior si existe

            filtro_id = ventana_compra.after(1000, lambda: filtrar_productos_ids(event))  # Esperar 1 segundo antes de filtrar

        # Función para filtrar productos y permitir escritura continua
        def filtrar_productos_ids(event):
            entrada = producto_id.get()  # Captura el texto ingresado
            try:
                entrada_int = int(entrada)  # Convertir la entrada a entero
                filtrados = [prod_id for prod_id in producto_ids if str(entrada_int) in str(prod_id)]  # Filtrar productos
            except ValueError:
                filtrados = []  # Si la entrada no es un número válido, no filtrar nada

            producto_id['values'] = filtrados  # Actualizar las opciones del combobox

            # Resaltar el texto en el combobox
            producto_id.selection_range(0, 'end')

            if filtrados:
                producto_id.event_generate('<Down>')  # Mostrar opciones filtradas

        # Vincular el evento KeyRelease para que espere 1 segundo antes de filtrar
        producto_id.bind('<KeyRelease>', filtrar_productos_ids_con_retraso)

        # Crear combobox para el nombre del producto
        tk.Label(frame_superior, text="Nombre del producto:", font=("Segoe UI", 13)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
    
    
        # Llenar el combobox con los nombres de los productos
        productos = traer_todos_los_productos()
        nombres_productos = [producto[1] for producto in productos]  # Extraer los nombres de los productos
        nombre_producto_combobox = ttk.Combobox(frame_superior, values=nombres_productos, font=("Segoe UI", 13), height=5)
        nombre_producto_combobox.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))
        nombre_producto_combobox.set("Seleccionar nombre")
        nombre_producto_combobox.grid(row=1, column=1, padx=5, pady=5)
    
        # Variable para manejar el retraso
        filtro_id = None
    
        # Función para filtrar productos con retraso
        def filtrar_productos_con_retraso(event):
            nonlocal filtro_id
            if filtro_id:
                ventana_compra.after_cancel(filtro_id)  # Cancelar el filtro anterior si existe
    
            filtro_id = ventana_compra.after(1000, lambda: filtrar_productos(event))  # Esperar 1 segundo antes de filtrar
    
        # Función para filtrar productos y permitir escritura continua
        def filtrar_productos(event):
            entrada = nombre_producto_combobox.get().lower()  # Captura el texto ingresado
            filtrados = [prod for prod in nombres_productos if entrada in prod.lower()]  # Filtrar productos
            nombre_producto_combobox['values'] = filtrados  # Actualizar las opciones del combobox
    
            # Resaltar el texto en el combobox
            nombre_producto_combobox.selection_range(0, 'end')
            
            if filtrados:
                nombre_producto_combobox.event_generate('<Down>')  # Mostrar opciones filtradas
        
        # Vincular el evento KeyRelease para que espere 1 segundo antes de filtrar
        nombre_producto_combobox.bind('<KeyRelease>', filtrar_productos_con_retraso)
    
        tk.Label(frame_superior, text="Precio de compra:", font=("Segoe UI", 13)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
        precio_producto_compra = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        precio_producto_compra.grid(row=2, column=1, padx=5, pady=5)
    
        tk.Label(frame_superior, text="Cantidad:", font=("Segoe UI", 13)).grid(row=3, column=0, padx=5, pady=5, sticky="e")
        cantidad_producto = tk.Entry(frame_superior, font=("Segoe UI", 13))  # Estado normal para permitir edición
        cantidad_producto.grid(row=3, column=1, padx=5, pady=5)
        cantidad_producto.insert(0, "0")  # Valor predeterminado de ""
    
        tk.Label(frame_superior, text="Categoría:", font=("Segoe UI", 13)).grid(row=4, column=0, padx=5, pady=5, sticky="e")
        categoria = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        categoria.grid(row=4, column=1, padx=4, pady=5)
    
        tk.Label(frame_superior, text="Proveedor:", font=("Segoe UI", 13)).grid(row=5, column=0, padx=5, pady=5, sticky="e")
        proveedor_producto = tk.Entry(frame_superior, state="readonly", font=("Segoe UI", 13))
        proveedor_producto.grid(row=5, column=1, padx=5, pady=5)
    
        # Crear combobox para el metodo de pago:
        tk.Label(frame_superior, text="Metodo de pago:", font=("Segoe UI", 13)).grid(row=6, column=0, padx=5, pady=5, sticky="e")
        frame_superior.option_add('*TCombobox*Listbox.font', ('Segoe UI', 16))
    
        # Llenar el combobox con los nombres de los metodos de pago
        metodos = [('Contado',), ('Cuenta Corriente',), ('Mercado Pago',)]
        nombres_metodos = [metodo[0] for metodo in metodos]  # Extraer los nombres de los productos
        nombre_metodos_combobox = ttk.Combobox(frame_superior, values=nombres_metodos, state="readonly", font=("Segoe UI", 13), height=5)
        nombre_metodos_combobox.grid(row=6, column=1, padx=5, pady=5)

        # Crear el área de texto para mostrar los productos añadidos
        tk.Label(ventana_compra, text="Productos seleccionados:",font=("Segoe UI", 13) ).pack(pady=5)
        result_text = tk.Text(ventana_compra, height=8, width=55, state="normal", font=("Segoe UI", 16))
        result_text.pack(padx=10, pady=5)
        result_text.config(state="disabled")  # Iniciar en estado "disabled" (no editable)

        # Crear etiqueta para mostrar el total de la compra
        total_label = tk.Label(ventana_compra, text="Total: $0.00", font=("Segoe UI", 13, "bold"))
        total_label.pack(side="right", padx=20, pady=10)
    
        # Función para actualizar los datos del producto seleccionado
        def actualizar_datos_producto(event):
            # Obtener el nombre seleccionado del combobox
            nombre_seleccionado = nombre_producto_combobox.get()
            id_seleccionado = producto_id.get()
            # Buscar los datos del producto seleccionado
            for producto in productos:
                if producto[1] == nombre_seleccionado or str(producto[0]) == id_seleccionado:
                    # Actualizar los campos con los datos del producto seleccionado
                    producto_id.config(state="normal")
                    producto_id.delete(0, tk.END)
                    producto_id.insert(0, producto[0])  # id producto
                    

                    nombre_producto_combobox.set(producto[1])  # Nombre
    
                    precio_producto_compra.config(state="normal")
                    precio_producto_compra.delete(0, tk.END)
                    precio_producto_compra.insert(0, producto[2])  # Precio
                    precio_producto_compra.config(state="readonly")
    
                    cantidad_producto.delete(0, tk.END)
                    cantidad_producto.insert(0, "1")  # Dejar cantidad editable con valor predeterminado 1
    
                    categoria.config(state="normal")
                    categoria.delete(0, tk.END)
                    categoria.insert(0, producto[5])  # categoria
                    categoria.config(state="readonly")
    
                    proveedor_producto.config(state="normal")
                    proveedor_producto.delete(0, tk.END)
                    proveedor_producto.insert(0, producto[6])  # Proveedor
                    proveedor_producto.config(state="readonly")

                    nombre_metodos_combobox.set("Contado")

                    cantidad_producto.focus_set()

                    break
                
        # Función para añadir el producto seleccionado al arreglo y mostrarlo en el área de texto
        def añadir_producto():
        
           nombre_seleccionado = nombre_producto_combobox.get()
           cantidad_seleccionada = cantidad_producto.get()  # Obtener la cantidad modificada por el usuario
           if nombre_seleccionado and cantidad_seleccionada.isdecimal():
               for producto in productos:
                   if producto[1] == nombre_seleccionado:
                        
                        # Obtener la hora actual
                        hora_actual = datetime.now().strftime("%H:%M:%S")
                        
    
                        # Convertir la hora actual a un objeto de tipo time para poder compararlo
                        hora_objeto = datetime.strptime(hora_actual, "%H:%M:%S").time()
    
                        # Definir la hora de comparación (12:00:00)
                        hora_comparacion = datetime.strptime("12:00:00", "%H:%M:%S").time()
    
                        # Comparar si la hora actual es mayor a las 12:00
                        if hora_objeto > hora_comparacion:
                            hora = "Tarde"
                        else:
                            hora = "Manana"
                        total = float(producto[3]) * float(cantidad_seleccionada)
                        producto_modificado = (producto[1], f"{float(producto[2]):.2f}", cantidad_seleccionada, producto[5], producto[6], hora, f" Total: {total:.2f}")
                        
                        s = False
                        d = controlar_cantidades(producto_modificado, s, advertencia_label) 
                        
                        if d:
                            tk.messagebox.showerror("Añadir Producto", "Asegurese de que haya una cantidad razonable.")
    
                        else:
                            self.compras_seleccionadas.append(producto_modificado)
                            
                            # Insertar el producto en el área de texto y en tabla
                            actualizar_cantidad_productos(self.compras_seleccionadas, s, l = False, m= False)
                            
                            self.minimarket.mostrar_arbol_productos()

                            result_text.config(state="normal")  # Permitir escritura temporal
                            result_text.insert(tk.END, f"{producto_modificado}\n")  # Mostrar producto en el Text
                            result_text.config(state="disabled")  # Bloquear nuevamente para no permitir ediciones
                            result_text.see(tk.END)  # Desplazarse al final automáticamente

                            # Limpiar los campos de entrada
                            producto_id.config(state="normal")
                            producto_id.delete(0, tk.END)
                            producto_id.set("")
            

                            nombre_producto_combobox.set("Seleccionar nombre")
                            precio_producto_compra.config(state="normal")
                            precio_producto_compra.delete(0, tk.END)
                            precio_producto_compra.config(state="readonly")

                            cantidad_producto.delete(0, tk.END)
                            cantidad_producto.insert(0, "0")

                            categoria.config(state="normal")
                            categoria.delete(0, tk.END)
                            categoria.config(state="readonly")

                            proveedor_producto.config(state="normal")
                            proveedor_producto.delete(0, tk.END)
                            proveedor_producto.config(state="readonly")

                            nombre_metodos_combobox.set("")

                            # Ocultar el Label de advertencia después de 3 segundos
                            advertencia_label.after(3000, lambda: advertencia_label.config(text="\n"))

                            producto_id.focus_set()

                            # Actualizar el total de la compra
                            actualizar_total()

                            
            
           else:
            advertencia_label.config(text="Por favor, complete \ntodos los campos correctamente")             
                        
                        
        # Función para borrar el último producto añadido
        def borrar_ultimo_producto():
            if self.compras_seleccionadas:
                s = True
                
                actualizar_cantidad_productos([self.compras_seleccionadas[-1]], s, l=False, m= False)

                self.minimarket.mostrar_arbol_productos()
                
                self.compras_seleccionadas.pop()  # Eliminar el último producto añadido
                # Limpiar y actualizar el área de texto
                result_text.config(state="normal")
                result_text.delete(1.0, tk.END)  # Borrar todo el contenido del área de texto
                for producto in self.compras_seleccionadas:
                    result_text.insert(tk.END, f"{producto}\n")  # Reinsertar los productos restantes
                result_text.config(state="disabled")
                result_text.see(tk.END)

                # Actualizar el total de la compra
                actualizar_total()

        def actualizar_total():
            total = sum(float(producto[1]) * int(producto[2]) for producto in self.compras_seleccionadas)
            total_label.config(text=f"Total: ${total:.2f}")
    
        def procesar_productos():
            s = False
            
            anadir_a_registro(self.compras_seleccionadas, s, self.usuario)
            #limpia el arreglo
            self.compras_seleccionadas.clear()

            self.minimarket.mostrar_arbol_productos() #muestra todos los prod actualizados

            # Limpiar el área de texto y el total
            result_text.config(state="normal")
            result_text.delete(1.0, tk.END)
            result_text.config(state="disabled")
            total_label.config(text="Total: $0.00")

            # Limpiar los campos de entrada
            producto_id.config(state="normal")
            producto_id.delete(0, tk.END)
            producto_id.set("0000000000")
            

            nombre_producto_combobox.set("Seleccionar nombre")
            precio_producto_compra.config(state="normal")
            precio_producto_compra.delete(0, tk.END)
            precio_producto_compra.config(state="readonly")

            cantidad_producto.delete(0, tk.END)
            cantidad_producto.insert(0, "0")

            categoria.config(state="normal")
            categoria.delete(0, tk.END)
            categoria.config(state="readonly")

            proveedor_producto.config(state="normal")
            proveedor_producto.delete(0, tk.END)
            proveedor_producto.config(state="readonly")

            nombre_metodos_combobox.set("")
        
            producto_id.focus_set()
        
    
         # Crear botón "Borrar Último Agregado"
        boton_borrar = tk.Button(frame_superior, text="Borrar Último Agregado", font=("Segoe UI", 10, "bold"), relief="groove", bg="#ef3232", fg="black", command=borrar_ultimo_producto)
        boton_borrar.grid(row=8, column=0, padx=5, pady=5, sticky="w")  # Posicionar a la izquierda
    
        # Crear botón "Añadir"
        boton_añadir = tk.Button(frame_superior, text="Añadir", font=("Segoe UI", 13, "bold"), command=añadir_producto, relief="groove", fg="black", bg="#d7d7d7")
        boton_añadir.grid(row=8, column=1, padx=5, pady=5)
    
        # Crear frame inferior para botones "Procesar" y "Cerrar"
        frame_botones = tk.Frame(ventana_compra)
        frame_botones.place(x=10, y=708)
    
        # Botón "Cerrar"
        def cerrar_ventana():
        
            s = False
            actualizar_cantidad_productos(self.compras_seleccionadas, s, l=True, m= True)
            self.minimarket.mostrar_arbol_productos() 

            self.compras_seleccionadas.clear()            
            
            ventana_compra.destroy()
    
        # Botón "Cerrar"
        boton_cerrar = tk.Button(frame_botones, text="Cerrar", font=("Segoe UI", 13, "bold"), command=cerrar_ventana, relief="groove", fg="black", bg="#ef3232")
        boton_cerrar.pack(side="left", padx=20)
    
    
        # Botón "Procesar"
        boton_procesar = tk.Button(frame_botones, text="Procesar", width=15, font=("Segoe UI", 13, "bold"), command=procesar_productos, relief="groove", fg="black", bg="#d7d7d7")
        boton_procesar.pack(side="right", padx=(90,0))


        # Vincular el evento de la tecla Enter al botón "Añadir"
        ventana_compra.bind('<Return>', lambda event: añadir_producto())
        
        # Vincular el evento de selección en el combobox
        producto_id.bind("<<ComboboxSelected>>", actualizar_datos_producto)
        # Vincular el evento de selección en el combobox
        nombre_producto_combobox.bind("<<ComboboxSelected>>", actualizar_datos_producto)
        ventana_compra.protocol("WM_DELETE_WINDOW", cerrar_ventana)
        

        # Inicializar el valor de barcode y el tiempo de la última tecla presionada
        barcode = ""
        last_time = time.time()

        # Función para manejar la entrada del lector de código de barras
        def on_key_press(event):
            nonlocal barcode, last_time
            current_time = time.time()

            # Si el tiempo entre teclas es mayor a 0.1 segundos, reiniciar el barcode
            if current_time - last_time > 0.1:
                barcode = ""

            last_time = current_time

            if event.name == 'enter':
                producto = traer_producto(barcode)  # Llamar a la función traer_producto con el código de barras
                if producto:
                    producto_id.config(state="normal")
                    producto_id.delete(0, tk.END)
                    producto_id.insert(0, producto[0])
                    producto_id.set("0000000000")
                    

                    nombre_producto_combobox.set(producto[1])
                    precio_producto_compra.config(state="normal")
                    precio_producto_compra.delete(0, tk.END)
                    precio_producto_compra.insert(0, producto[2])
                    precio_producto_compra.config(state="readonly")

                    cantidad_producto.delete(0, tk.END)
                    cantidad_producto.insert(0, "1")

                    categoria.config(state="normal")
                    categoria.delete(0, tk.END)
                    categoria.insert(0, producto[5])
                    categoria.config(state="readonly")

                    proveedor_producto.config(state="normal")
                    proveedor_producto.delete(0, tk.END)
                    proveedor_producto.insert(0, producto[6])
                    proveedor_producto.config(state="readonly")

                    nombre_metodos_combobox.set("Contado")

                    cantidad_producto.focus_set()
                    
                barcode = ""
            elif event.name.isdigit():
                barcode += event.name

        # Colocar el cursor en el campo de ID del producto
        producto_id.focus_set()

        # Vincular la función de escaneo de código de barras
        keyboard.on_press(on_key_press)
    
        ventana_compra.mainloop()


## ventana para el minimarket 

class Minimarket:
    def __init__(self, master, username, account_type):
        self.master = master
        self.master.title("rls")

        

        # Configurar la ventana para que tome el tamaño de la pantalla sin ser pantalla completa
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry(f"{screen_width}x{screen_height}")
        self.master.update_idletasks()  # Asegura que la geometría se actualice
        self.master.state('zoomed')  # Maximiza la ventana
        self.master.minsize(800, 600)  # Tamaño mínimo de la ventana

        # Cargar la imagen del icono
        icon_path = resource_path("resources/r.ico")  # Ruta relativa a la imagen del icono
        self.master.iconbitmap(icon_path)

        # Mostrar ID del usuario de forma transparente y bienvenida
        self.mostrar_id_inicio(username)
        
        ######### Crear el Notebook vertical a la izquierda #########
        self.notebook = ttk.Notebook(self.master, style="CustomNotebook.TNotebook")
        self.notebook.place(x=0, y=0, width=310, height=screen_height)

        # Mostrar pestañas según el tipo de cuenta
        if account_type:  # Si es True, mostrar todas las pestañas

            # Crear pestañas del Notebook
            self.tab_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_buscar_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_administracion = tk.Frame(self.notebook, bg="#d7d7d7")

            self.notebook.add(self.tab_datos, text="Datos")
            self.notebook.add(self.tab_buscar_datos, text="Buscar Datos")
            self.notebook.add(self.tab_administracion, text="Administración")
            
            ######### Crear el área blanca dinámica justo debajo del Notebook #########
            self.contenido = tk.Frame(self.tab_datos, bg="white", bd=0, highlightthickness=0)
            self.contenido.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.contenido_bd = tk.Frame(self.tab_buscar_datos, bg="white", bd=0, highlightthickness=0)
            self.contenido_bd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.contenido_ad = tk.Frame(self.tab_administracion, bg="white", bd=0, highlightthickness=0)
            self.contenido_ad.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            # Crear instancias de las clases de contenido
            self.datos = Datos(self.contenido, self)
            self.buscar_datos = BuscarDatos(self.contenido_bd, self, username)
            self.administracion = Administracion(self.contenido_ad, self, username)

            # Vincular el cambio de pestaña a un evento
            self.notebook.bind("<<NotebookTabChanged>>", self.cambiar_pestana_administrador)

        else:  # Si es False, mostrar solo Buscar Datos y Administración

            # Crear pestañas del Notebook
            self.tab_buscar_datos = tk.Frame(self.notebook, bg="#d7d7d7")
            self.tab_administracion = tk.Frame(self.notebook, bg="#d7d7d7")

            self.notebook.add(self.tab_buscar_datos, text="Buscar Datos")
            self.notebook.add(self.tab_administracion, text="Administración")

            ######### Crear el área blanca dinámica justo debajo del Notebook ########
            self.contenido_bd = tk.Frame(self.tab_buscar_datos, bg="white", bd=0, highlightthickness=0)
            self.contenido_bd.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.contenido_ad = tk.Frame(self.tab_administracion, bg="white", bd=0, highlightthickness=0)
            self.contenido_ad.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            self.buscar_datos = BuscarDatos(self.contenido_bd, self, username)
            self.administracion = Administracion(self.contenido_ad, self, username)

            # Vincular el cambio de pestaña a un evento
            self.notebook.bind("<<NotebookTabChanged>>", self.cambiar_pestana_usuario)

        # Configurar estilo para eliminar bordes del Notebook
        # Configurar estilo para aumentar tamaño de fuente y cambiar colores de las pestañas
        style = ttk.Style()
        style.configure("CustomNotebook.TNotebook", borderwidth=0, background="white")
        style.configure("CustomNotebook.TNotebook.Tab", font=("Segoe UI", 11), padding=[10, 5])
        style.map("CustomNotebook.TNotebook.Tab", background=[("selected", "#d1e0e0")], foreground=[("selected", "#000000")])

        # Mostrar contenido inicial según el tipo de cuenta
        if account_type:  # Si es True, mostrar la pestaña de Datos
            self.mostrar_datos()
        else:  # Si es False, mostrar la pestaña de Buscar Datos por defecto
            self.mostrar_buscar_datos()

        # Vincular el evento de cambio de tamaño de la ventana
        self.master.bind("<Configure>", self.ajustar_tamano)

        # Vincular el evento de cierre de la ventana para guardar las notas
        self.master.protocol("WM_DELETE_WINDOW", self.guardar_notas_y_cerrar)

    def ajustar_tamano(self, event):
        # Ajustar el tamaño del notebook y el frame derecho
        self.notebook.place(x=0, y=0, width=310, height=self.master.winfo_height())
        if hasattr(self, 'frame_derecho'):
            self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))


    def mostrar_arbol_productos(self):
        # Limpiar el área derecha si ya hay contenido
        self.borrar_frame_derecho()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")

        # Frame derecho para mostrar la tabla
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

        # Título para la tabla
        label_tabla = tk.Label(self.frame_derecho, text="Productos", font=("Segoe UI", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)
            


        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(self.frame_derecho, columns=("ID","nombre", "precio compra", "precio venta", "stock", "categoria", "proveedor"), show="headings", height=10)

        # Definir las columnas con doble clic
        tree.heading("ID", text="ID", command=lambda: contador_clic("ID"))
        tree.heading("nombre", text="Nombre", command=lambda: contador_clic("nombre"))
        tree.heading("precio compra", text="Precio compra", command=lambda: contador_clic("precio compra"))
        tree.heading("precio venta", text="Precio venta", command=lambda: contador_clic("precio venta"))
        tree.heading("stock", text="Stock", command=lambda: contador_clic("stock"))
        tree.heading("categoria", text="Categoria", command=lambda: contador_clic("categoria"))
        tree.heading("proveedor", text="Proveedor", command=lambda: contador_clic("proveedor"))

        # Definir el ancho de las columnas
        tree.column("ID", width=100, anchor="center")
        tree.column("nombre", width=100, anchor="center")
        tree.column("precio compra", width=100, anchor="center")
        tree.column("precio venta", width=100, anchor="center")
        tree.column("stock", width=100, anchor="center")
        tree.column("categoria", width=100, anchor="center")
        tree.column("proveedor", width=100, anchor="center")

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

        # funciones para copiar columna:

        # Inicializar un diccionario para contar los clics en cada columna
        click_counter = {"ID":0, " nombre": 0, "precio compra": 0, "precio venta": 0, "stock": 0, "categoria": 0, "proveedor": 0}
    

        # Función para contar clics y copiar la columna si hay dos clics consecutivos
        def contador_clic(columna):
            # Incrementar el contador para la columna seleccionada
            click_counter[columna] += 1

            # Si se hace clic dos veces, copiar la columna y resetear el contador
            if click_counter[columna] == 2:
                copiar_columna(columna)
                click_counter[columna] = 0
            else:
                # Resetear los contadores de las demás columnas
                for col in click_counter:
                    if col != columna:
                        click_counter[col] = 0


        # Función para copiar la columna seleccionada al portapapeles
        def copiar_columna(columna):
            # Obtener los índices de las filas y el índice de la columna
            valores_columna = []
            columna_index = tree["columns"].index(columna)

            # Extraer todos los valores de la columna seleccionada
            for item in tree.get_children():
                valor = tree.item(item)['values'][columna_index]
                valores_columna.append(str(valor))

            # Unir los valores con saltos de línea y copiarlos al portapapeles
            self.master.clipboard_clear()  # Limpiar el portapapeles
            self.master.clipboard_append("\n".join(valores_columna))  # Copiar al portapapeles
            self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

            # Mostrar mensaje emergente
            mostrar_mensaje_copiado()

        # Variable para realizar seguimiento de los clics
        global primer_click
        primer_click = None

        # Función para copiar una fila completa al portapapeles
        def copiar_fila(event):
            global primer_click

            # Identificar la fila sobre la que se ha hecho clic
            item = tree.identify_row(event.y)

            # Si no se ha hecho clic sobre ninguna fila (fuera del área de filas)
            if not item:
                return

            # Si ya se ha hecho un primer clic en esta fila
            if primer_click == item:
                # Obtener los valores de la fila
                valores_fila = tree.item(item)['values']

                # Unir los valores con tabuladores o saltos de línea, y copiarlos al portapapeles
                fila_copiada = "\t".join(str(valor) for valor in valores_fila)  # Usa tabuladores para separar los valores
                self.master.clipboard_clear()  # Limpiar el portapapeles
                self.master.clipboard_append(fila_copiada)  # Copiar al portapapeles
                self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

                # Mostrar mensaje emergente
                mostrar_mensaje_copiado()

                # Reiniciar el contador de clics
                primer_click = None
            else:
                # Si es el primer clic en la fila, guardamos esa fila
                primer_click = item

        # Función para mostrar el mensaje "Copiado al portapapeles"
        def mostrar_mensaje_copiado():
            # Crear la ventana del mensaje
            mensaje = tk.Toplevel(self.master)
            mensaje.title("Mensaje Copiado")

            # Obtener las dimensiones de la ventana principal
            ventana_width = self.master.winfo_width()
            ventana_height = self.master.winfo_height()

            # Obtener las dimensiones del mensaje
            mensaje_width = 300
            mensaje_height = 50

            # Calcular la posición para centrar el mensaje
            position_top = self.master.winfo_rooty() + (ventana_height // 2) - (mensaje_height // 2)
            position_left = self.master.winfo_rootx() + (ventana_width // 2) - (mensaje_width // 2)

            # Hacer la ventana pequeña, sin bordes y transparente
            mensaje.geometry(f"{mensaje_width}x{mensaje_height}+{position_left}+{position_top}")
            mensaje.overrideredirect(True)  # Eliminar los bordes de la ventana
            mensaje.config(bg="black")  # Fondo negro semitransparente
            mensaje.attributes("-alpha", 0.7)  # Hacerla semi-transparente

            # Etiqueta con el mensaje
            label = tk.Label(mensaje, text="Copiado al portapapeles", fg="white", font=("Arial", 16, "bold"), bg="black")
            label.pack(expand=True)

            # Cerrar el mensaje después de 2 segundos
            mensaje.after(2000, mensaje.destroy)  # 2000 ms = 2 segundos

        # Asociar el evento de clic en la fila
        tree.bind("<ButtonRelease-1>", copiar_fila)

        

        def mostrar_productos():
            all_data = traer_todos_los_productos()
            return all_data


        def actualizar_filtro(event=None):
            all_data2 = traer_todos_los_productos()
                # Obtener el texto ingresado en el Entry
            texto_busqueda = mostrar_productos.entry_busqueda.get().lower()
            # Limpiar la tabla para mostrar los nuevos resultados
            for item in tree.get_children():
                tree.delete(item)
            # Filtrar productos que contengan el texto ingresado
            if texto_busqueda == "":
                productos_a_mostrar = all_data2  # Mostrar todos los productos si no se ha ingresado texto
            else:
                productos_a_mostrar = [p for p in all_data2 if texto_busqueda in p[1].lower()]
            # Insertar los productos filtrados en la tabla
            if productos_a_mostrar:
                # Aplicar estilo a las filas con el tag "rojo"
                tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
                for i in productos_a_mostrar:
                    # Determina el color según el valor de i[2]
                    tag = ("rojo",) if i[4] < 5 else ()
                    # Insertar una fila vacía para crear espacio
                    tree.insert("", "end", values=("", "", "", "", "", "", ""))
                    tree.insert("", "end", values=(i[0], i[1], f"${i[2]:.2f}", f"${i[3]:.2f}", i[4], i[5], i[6]), tags=tag)
            else:
                tree.insert("", "end", values=("No se encontraron productos", "", "", "", "", "", ""))

        def mostrar_todos_los_productos(s = mostrar_productos()): # cambiar por funcion que traiga todos los datos
            # Limpiar la tabla para mostrar los productos
            for item in tree.get_children():
                tree.delete(item)
            # Configurar el tag para texto en rojo
            tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
            # Insertar todos los productos en la tabla
            for i in s:
                tree.insert("", "end", values=("", "", "", "", "", "", ""))
                # Verificar si el valor en la posición 2 es menor a -5
                # Determina el color según el valor de i[2]
                tag = ("rojo",) if i[4] < 5 else ()
                # Insertar el producto con el tag "rojo"
                tree.insert("", "end", values=(f"{i[0]}", i[1], f"${i[2]:.2f}", f"${i[3]:.2f}", i[4], i[5], i[6]), tags=tag)
            

     
        mostrar_productos.entry_busqueda = ttk.Entry(self.frame_derecho, font=("Segoe UI", 14))
        mostrar_productos.entry_busqueda.place(x=10, y=50)  # Ajustar la posición
        mostrar_productos.entry_busqueda.bind("<KeyRelease>", actualizar_filtro)  # Detectar cada tecla que el usuario presiona


        
        # Mostrar todos los productos inmediatamente cuando se abre el Entry    
        mostrar_todos_los_productos()

    
    def mostrar_arbol_productos_cat_prov(self):
        # Limpiar el área derecha si ya hay contenido
        self.borrar_frame_derecho()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")

        # Frame derecho para mostrar la tabla
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

        # Título para la tabla
        label_tabla = tk.Label(self.frame_derecho, text="Productos", font=("Segoe UI", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)

        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(self.frame_derecho, columns=("ID", "nombre", "precio compra", "precio venta", "stock", "categoria", "proveedor"), show="headings", height=10)

        # Definir las columnas con doble clic
        columnas = ["ID", "nombre", "precio compra", "precio venta", "stock", "categoria", "proveedor"]
        for col in columnas:
            tree.heading(col, text=col.capitalize(), command=lambda c=col: contador_clic(c))
            tree.column(col, width=100, anchor="center")

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

        # Inicializar un diccionario para contar los clics en cada columna
        click_counter = {col: 0 for col in columnas}

        # Función para contar clics y copiar la columna si hay dos clics consecutivos
        def contador_clic(columna):
            click_counter[columna] += 1
            if click_counter[columna] == 2:
                copiar_columna(columna)
                click_counter[columna] = 0
            else:
                for col in click_counter:
                    if col != columna:
                        click_counter[col] = 0

        # Función para copiar la columna seleccionada al portapapeles
        def copiar_columna(columna):
            valores_columna = [tree.item(item)['values'][tree["columns"].index(columna)] for item in tree.get_children()]
            self.master.clipboard_clear()
            self.master.clipboard_append("\n".join(map(str, valores_columna)))
            self.master.update()
            mostrar_mensaje_copiado()

        # Variable para realizar seguimiento de los clics
        global primer_click
        primer_click = None

        # Función para copiar una fila completa al portapapeles
        def copiar_fila(event):
            global primer_click
            item = tree.identify_row(event.y)
            if not item:
                return
            if primer_click == item:
                valores_fila = tree.item(item)['values']
                fila_copiada = "\t".join(map(str, valores_fila))
                self.master.clipboard_clear()
                self.master.clipboard_append(fila_copiada)
                self.master.update()
                mostrar_mensaje_copiado()
                primer_click = None
            else:
                primer_click = item

        # Función para mostrar el mensaje "Copiado al portapapeles"
        def mostrar_mensaje_copiado():
            mensaje = tk.Toplevel(self.master)
            mensaje.title("Mensaje Copiado")
            ventana_width = self.master.winfo_width()
            ventana_height = self.master.winfo_height()
            mensaje_width = 300
            mensaje_height = 50
            position_top = self.master.winfo_rooty() + (ventana_height // 2) - (mensaje_height // 2)
            position_left = self.master.winfo_rootx() + (ventana_width // 2) - (mensaje_width // 2)
            mensaje.geometry(f"{mensaje_width}x{mensaje_height}+{position_left}+{position_top}")
            mensaje.overrideredirect(True)
            mensaje.config(bg="black")
            mensaje.attributes("-alpha", 0.7)
            label = tk.Label(mensaje, text="Copiado al portapapeles", fg="white", font=("Arial", 16, "bold"), bg="black")
            label.pack(expand=True)
            mensaje.after(2000, mensaje.destroy)

        # Asociar el evento de clic en la fila
        tree.bind("<ButtonRelease-1>", copiar_fila)

        def mostrar_productos():
            return traer_todos_los_productos()

        def actualizar_filtro(event=None):
            all_data2 = traer_todos_los_productos()
            texto_busqueda = mostrar_productos.entry_busqueda.get().lower()
            seleccion = combobox_opcion.get()
            nombre_seleccionado = combobox_nombre.get().lower()
            for item in tree.get_children():
                tree.delete(item)
            if seleccion == "Categoria":
                productos_a_mostrar = [p for p in all_data2 if texto_busqueda in p[1].lower() and p[5].lower() == nombre_seleccionado]
            elif seleccion == "Proveedor":
                productos_a_mostrar = [p for p in all_data2 if texto_busqueda in p[1].lower() and p[6].lower() == nombre_seleccionado]
            else:
                productos_a_mostrar = all_data2
            tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
            
            for i in productos_a_mostrar:
                tag = ("rojo",) if i[4] < 5 else ()
                tree.insert("", "end", values=("", "", "", "", "", "", ""))
                tree.insert("", "end", values=(i[0], i[1], f"${i[2]:.2f}", f"${i[3]:.2f}", i[4], i[5], i[6]), tags=tag)

        def mostrar_todos_los_productos(s=mostrar_productos()):
            for item in tree.get_children():
                tree.delete(item)
            tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
            for i in s:
                tag = ("rojo",) if i[4] < 5 else ()
                tree.insert("", "end", values=("", "", "", "", "", "", ""))
                tree.insert("", "end", values=(i[0], i[1], f"${i[2]:.2f}", f"${i[3]:.2f}", i[4], i[5], i[6]), tags=tag)

        mostrar_productos.entry_busqueda = ttk.Entry(self.frame_derecho, font=("Segoe UI", 14))
        mostrar_productos.entry_busqueda.place(x=10, y=50)
        mostrar_productos.entry_busqueda.bind("<KeyRelease>", actualizar_filtro)

        # Combobox para categorías
        tk.Label(self.frame_derecho, text="Seleccione cat o prov :", font=("Segoe UI", 12)).place(relx=0.72, rely=0.01)
        combobox_opcion = ttk.Combobox(self.frame_derecho, font=("Segoe UI", 12), state="readonly", height=5)
        combobox_opcion['values'] = ["Categoria", "Proveedor"]
        combobox_opcion.option_add('*TCombobox*Listbox.font', ('Segoe UI', 12))
        combobox_opcion.place(relx=0.83, rely=0.01, width=200)

        # Combobox para proveedores
        tk.Label(self.frame_derecho, text="Seleccione el nombre :", font=("Segoe UI", 12)).place(relx=0.72, rely=0.05)
        combobox_nombre = ttk.Combobox(self.frame_derecho, font=("Segoe UI", 12), state="readonly", height=5)
        combobox_nombre.place(relx=0.83, rely=0.05, width=200)

        def actualizar_combobox(event):
            seleccion = combobox_opcion.get()
            combobox_nombre.set("")
            if seleccion == "Categoria":
                categorias = [categoria[0] for categoria in traer_categorias()]
                combobox_nombre['values'] = categorias
            elif seleccion == "Proveedor":
                proveedores = [proveedor[0] for proveedor in traer_proveedores()]
                combobox_nombre['values'] = proveedores

        combobox_opcion.bind("<<ComboboxSelected>>", actualizar_combobox)

        def actualizar_filtro_combobox(event=None):
            all_data2 = traer_todos_los_productos()
            seleccion = combobox_opcion.get()
            nombre_seleccionado = combobox_nombre.get().lower()
            for item in tree.get_children():
                tree.delete(item)
            if seleccion == "Categoria":
                productos_a_mostrar = [p for p in all_data2 if p[5].lower() == nombre_seleccionado]
            elif seleccion == "Proveedor":
                productos_a_mostrar = [p for p in all_data2 if p[6].lower() == nombre_seleccionado]
            else:
                productos_a_mostrar = all_data2
            tree.tag_configure("rojo", foreground="red", font=("Segoe UI", 14, "bold"))
            for i in productos_a_mostrar:
                tag = ("rojo",) if i[2] < 5 else ()
                tree.insert("", "end", values=("", "", "", "", "", "", ""))
                tree.insert("", "end", values=(i[0], i[1], f"${i[2]:.2f}", f"${i[3]:.2f}", i[4], i[5], i[6]), tags=tag)

        combobox_nombre.bind("<<ComboboxSelected>>", actualizar_filtro_combobox)

        # Mostrar todos los productos inmediatamente cuando se abre el Entry
        mostrar_todos_los_productos()

        

    def borrar_frame_derecho(self):
        if hasattr(self, 'frame_derecho'):
            self.frame_derecho.destroy()
            
            

    def mostrar_arbol_proveedores(self):
        # derribar frame derecho antes de sobreescribirlo
        self.borrar_frame_derecho()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")
        
        # Frame derecho para mostrar la tabla
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

        # Título para la tabla
        label_tabla = tk.Label(self.frame_derecho, text="Proveedores", font=("Segoe UI", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)

        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(self.frame_derecho, columns=("nombre", "telefono", "mail"), show="headings", height=10)

        # Definir las columnas con doble clic
        tree.heading("nombre", text="Nombre", command=lambda: contador_clic("nombre"))
        tree.heading("telefono", text="Telefono", command=lambda: contador_clic("telefono"))
        tree.heading("mail", text="Mail", command=lambda: contador_clic("mail"))
       

        # Definir el ancho de las columnas
        tree.column("nombre", width=100, anchor="center")
        tree.column("telefono", width=100, anchor="center")
        tree.column("mail", width=100, anchor="center")

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

        # funciones para copiar columna:

        # Inicializar un diccionario para contar los clics en cada columna
        click_counter = {"nombre": 0, "telefono": 0, "mail": 0}

        # Función para contar clics y copiar la columna si hay dos clics consecutivos
        def contador_clic(columna):
            # Incrementar el contador para la columna seleccionada
            click_counter[columna] += 1

            # Si se hace clic dos veces, copiar la columna y resetear el contador
            if click_counter[columna] == 2:
                copiar_columna(columna)
                click_counter[columna] = 0
            else:
                # Resetear los contadores de las demás columnas
                for col in click_counter:
                    if col != columna:
                        click_counter[col] = 0

        # Función para copiar la columna seleccionada al portapapeles
        def copiar_columna(columna):
            # Obtener los índices de las filas y el índice de la columna
            valores_columna = []
            columna_index = tree["columns"].index(columna)

            # Extraer todos los valores de la columna seleccionada
            for item in tree.get_children():
                valor = tree.item(item)['values'][columna_index]
                valores_columna.append(str(valor))

            # Unir los valores con saltos de línea y copiarlos al portapapeles
            self.master.clipboard_clear()  # Limpiar el portapapeles
            self.master.clipboard_append("\n".join(valores_columna))  # Copiar al portapapeles
            self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

            # Mostrar mensaje emergente
            mostrar_mensaje_copiado()

        # Variable para realizar seguimiento de los clics
        global primer_click
        primer_click = None

        # Función para copiar una fila completa al portapapeles
        def copiar_fila(event):
            global primer_click

            # Identificar la fila sobre la que se ha hecho clic
            item = tree.identify_row(event.y)

            # Si no se ha hecho clic sobre ninguna fila (fuera del área de filas)
            if not item:
                return

            # Si ya se ha hecho un primer clic en esta fila
            if primer_click == item:
                # Obtener los valores de la fila
                valores_fila = tree.item(item)['values']

                # Unir los valores con tabuladores o saltos de línea, y copiarlos al portapapeles
                fila_copiada = "\t".join(str(valor) for valor in valores_fila)  # Usa tabuladores para separar los valores
                self.master.clipboard_clear()  # Limpiar el portapapeles
                self.master.clipboard_append(fila_copiada)  # Copiar al portapapeles
                self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

                # Mostrar mensaje emergente
                mostrar_mensaje_copiado()

                # Reiniciar el contador de clics
                primer_click = None
            else:
                # Si es el primer clic en la fila, guardamos esa fila
                primer_click = item

        # Función para mostrar el mensaje "Copiado al portapapeles"
        def mostrar_mensaje_copiado():
            # Crear la ventana del mensaje
            mensaje = tk.Toplevel(self.master)
            mensaje.title("Mensaje Copiado")

            # Obtener las dimensiones de la ventana principal
            ventana_width = self.master.winfo_width()
            ventana_height = self.master.winfo_height()

            # Obtener las dimensiones del mensaje
            mensaje_width = 300
            mensaje_height = 50

            # Calcular la posición para centrar el mensaje
            position_top = self.master.winfo_rooty() + (ventana_height // 2) - (mensaje_height // 2)
            position_left = self.master.winfo_rootx() + (ventana_width // 2) - (mensaje_width // 2)

            # Hacer la ventana pequeña, sin bordes y transparente
            mensaje.geometry(f"{mensaje_width}x{mensaje_height}+{position_left}+{position_top}")
            mensaje.overrideredirect(True)  # Eliminar los bordes de la ventana
            mensaje.config(bg="black")  # Fondo negro semitransparente
            mensaje.attributes("-alpha", 0.7)  # Hacerla semi-transparente

            # Etiqueta con el mensaje
            label = tk.Label(mensaje, text="Copiado al portapapeles", fg="white", font=("Arial", 16, "bold"), bg="black")
            label.pack(expand=True)

            # Cerrar el mensaje después de 2 segundos
            mensaje.after(2000, mensaje.destroy)  # 2000 ms = 2 segundos

        # Asociar el evento de clic en la fila
        tree.bind("<ButtonRelease-1>", copiar_fila)


        def mostrar_proveedores():
            all_data = traer_todos_los_proveedores()
            return all_data
   
        def actualizar_filtro(event=None):
            all_data2 = traer_todos_los_proveedores()
                # Obtener el texto ingresado en el Entry
            texto_busqueda = mostrar_proveedores.entry_busqueda.get().lower()
            # Limpiar la tabla para mostrar los nuevos resultados
            for item in tree.get_children():
                tree.delete(item)
            # Filtrar productos que contengan el texto ingresado
            if texto_busqueda == "":
                proveedores_a_mostrar = all_data2  # Mostrar todos los productos si no se ha ingresado texto
            else:
                proveedores_a_mostrar = [p for p in all_data2 if texto_busqueda in p[0].lower()]
            # Insertar los productos filtrados en la tabla
            if proveedores_a_mostrar:
                for i in proveedores_a_mostrar:
                    
                    # Insertar una fila vacía para crear espacio
                    tree.insert("", "end", values=("", "", ""))
                    tree.insert("", "end", values=(f"{i[0]} {i[1]} {i[2]}"))
            else:
                tree.insert("", "end", values=("No se encontraron proveedores", "", ""))

        def mostrar_todos_los_proveedores(s = mostrar_proveedores()): # cambiar por funcion que traiga todos los datos
            # Limpiar la tabla para mostrar los productos
            for item in tree.get_children():
                tree.delete(item)
            # Configurar el tag para texto en rojo
            # Insertar todos los productos en la tabla
            for i in s:
                tree.insert("", "end", values=("", "", ""))
                tree.insert("", "end", values=(f"{i[0]} {i[1]} {i[2]}"))
            

     
        mostrar_proveedores.entry_busqueda = ttk.Entry(self.frame_derecho, font=("Segoe UI", 14))
        mostrar_proveedores.entry_busqueda.place(x=10, y=50)  # Ajustar la posición
        mostrar_proveedores.entry_busqueda.bind("<KeyRelease>", actualizar_filtro)  # Detectar cada tecla que el usuario presiona

        
        # Mostrar todos los productos inmediatamente cuando se abre el Entry    
        mostrar_todos_los_proveedores()

    def mostrar_arbol_categorias(self):
        # derribar frame derecho antes de sobreescribirlo
        self.borrar_frame_derecho()

        # Estilo personalizado para agrandar la fuente de la tabla y aumentar la altura de las filas
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 16, "bold"))  # Agranda la fuente de los encabezados
        style.configure("Treeview", font=("Segoe UI", 14), rowheight=30)   # Agranda la fuente de las filas y ajusta la altura
        style.configure("Rojo.TLabel", foreground="red")

        # Frame derecho para mostrar la tabla
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.place(x=320, y=0, width=max(self.master.winfo_width() - 320, 480), height=max(self.master.winfo_height(), 600))

        # Título para la tabla
        label_tabla = tk.Label(self.frame_derecho, text="Categorías", font=("Segoe UI", 24, "bold"), fg="black", relief="flat")
        label_tabla.pack(pady=20)

        # Tabla (Treeview) para mostrar los productos
        tree = ttk.Treeview(self.frame_derecho, columns=("ID", "nombre"), show="headings", height=10)

        # Definir las columnas con doble clic
        tree.heading("ID", text="id", command=lambda: contador_clic("ID"))
        tree.heading("nombre", text="Nombre", command=lambda: contador_clic("nombre"))

        # Definir el ancho de las columnas
        tree.column("ID", width=100, anchor="center")
        tree.column("nombre", width=100, anchor="center")
        

        # Empaquetar la tabla
        tree.pack(fill=tk.BOTH, expand=True)

        # funciones para copiar columna:

        # Inicializar un diccionario para contar los clics en cada columna
        click_counter = {"ID": 0, "nombre": 0}

        # Función para contar clics y copiar la columna si hay dos clics consecutivos
        def contador_clic(columna):
            # Incrementar el contador para la columna seleccionada
            click_counter[columna] += 1

            # Si se hace clic dos veces, copiar la columna y resetear el contador
            if click_counter[columna] == 2:
                copiar_columna(columna)
                click_counter[columna] = 0
            else:
                # Resetear los contadores de las demás columnas
                for col in click_counter:
                    if col != columna:
                        click_counter[col] = 0

        
        # Función para copiar la columna seleccionada al portapapeles
        def copiar_columna(columna):
            # Obtener los índices de las filas y el índice de la columna
            valores_columna = []
            columna_index = tree["columns"].index(columna)

            # Extraer todos los valores de la columna seleccionada
            for item in tree.get_children():
                valor = tree.item(item)['values'][columna_index]
                valores_columna.append(str(valor))

            # Unir los valores con saltos de línea y copiarlos al portapapeles
            self.master.clipboard_clear()  # Limpiar el portapapeles
            self.master.clipboard_append("\n".join(valores_columna))  # Copiar al portapapeles
            self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

            # Mostrar mensaje emergente
            mostrar_mensaje_copiado()

        # Variable para realizar seguimiento de los clics
        global primer_click
        primer_click = None

        # Función para copiar una fila completa al portapapeles
        def copiar_fila(event):
            global primer_click

            # Identificar la fila sobre la que se ha hecho clic
            item = tree.identify_row(event.y)

            # Si no se ha hecho clic sobre ninguna fila (fuera del área de filas)
            if not item:
                return

            # Si ya se ha hecho un primer clic en esta fila
            if primer_click == item:
                # Obtener los valores de la fila
                valores_fila = tree.item(item)['values']

                # Unir los valores con tabuladores o saltos de línea, y copiarlos al portapapeles
                fila_copiada = "\t".join(str(valor) for valor in valores_fila)  # Usa tabuladores para separar los valores
                self.master.clipboard_clear()  # Limpiar el portapapeles
                self.master.clipboard_append(fila_copiada)  # Copiar al portapapeles
                self.master.update()  # Actualizar la ventana para asegurar que el portapapeles se copie

                # Mostrar mensaje emergente
                mostrar_mensaje_copiado()

                # Reiniciar el contador de clics
                primer_click = None
            else:
                # Si es el primer clic en la fila, guardamos esa fila
                primer_click = item

        # Función para mostrar el mensaje "Copiado al portapapeles"
        def mostrar_mensaje_copiado():
            # Crear la ventana del mensaje
            mensaje = tk.Toplevel(self.master)
            mensaje.title("Mensaje Copiado")

            # Obtener las dimensiones de la ventana principal
            ventana_width = self.master.winfo_width()
            ventana_height = self.master.winfo_height()

            # Obtener las dimensiones del mensaje
            mensaje_width = 300
            mensaje_height = 50

            # Calcular la posición para centrar el mensaje
            position_top = self.master.winfo_rooty() + (ventana_height // 2) - (mensaje_height // 2)
            position_left = self.master.winfo_rootx() + (ventana_width // 2) - (mensaje_width // 2)

            # Hacer la ventana pequeña, sin bordes y transparente
            mensaje.geometry(f"{mensaje_width}x{mensaje_height}+{position_left}+{position_top}")
            mensaje.overrideredirect(True)  # Eliminar los bordes de la ventana
            mensaje.config(bg="black")  # Fondo negro semitransparente
            mensaje.attributes("-alpha", 0.7)  # Hacerla semi-transparente

            # Etiqueta con el mensaje
            label = tk.Label(mensaje, text="Copiado al portapapeles", fg="white", font=("Arial", 16, "bold"), bg="black")
            label.pack(expand=True)

            # Cerrar el mensaje después de 2 segundos
            mensaje.after(2000, mensaje.destroy)  # 2000 ms = 2 segundos

        # Asociar el evento de clic en la fila
        tree.bind("<ButtonRelease-1>", copiar_fila)

        def mostrar_categorias():
            all_data = traer_todas_las_categorias()
            return all_data


        def mostrar_todas_las_categorias(s = mostrar_categorias()): # cambiar por funcion que traiga todos los datos
            # Limpiar la tabla para mostrar los productos
            for item in tree.get_children():
                tree.delete(item)
            # Configurar el tag para texto en rojo
            # Insertar todos los productos en la tabla
            for i in s:
                tree.insert("", "end", values=("", ""))
                tree.insert("", "end", values=(i[0], i[1]))

        
        # Mostrar todos los productos inmediatamente cuando se abre el Entry    
        mostrar_todas_las_categorias()



    def mostrar_id_inicio(self, username):
        # Simular la obtención del ID del usuario
        id_usuario = obtener_id_usuario(username)  # Método que debes implementar

         # Mostrar mensaje de bienvenida como un título en la parte superior
        self.bienvenida = tk.Label(self.master, text="Bienvenido!", font=("Segoe UI", 50))
        self.bienvenida.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Etiqueta transparente para mostrar el ID
        self.id_label = tk.Label(
            self.master,
            text=f"ID usuario: {id_usuario}",
            font=("Segoe UI", 30, "bold"),
            bg="black",
            fg="white",
            relief="flat", bd=3, padx=15
        )
        self.id_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


        # Configurar opacidad simulada y desaparecer después de 3 segundos
        self.bienvenida.after(10000, self.bienvenida.destroy)
        self.id_label.after(5000, self.id_label.destroy)

    def cambiar_pestana_usuario(self, event):
        pestaña_actual = self.notebook.index(self.notebook.select())
        if pestaña_actual == 0:  # Pestaña de Buscar Datos
            self.mostrar_buscar_datos()
        elif pestaña_actual == 1:  # Pestaña de Administración
            self.mostrar_administracion()

    def cambiar_pestana_administrador(self, event):
        pestaña_actual = self.notebook.index(self.notebook.select())
        if pestaña_actual == 0 and hasattr(self, 'datos'):
            self.mostrar_datos()
        elif pestaña_actual == 0 or pestaña_actual == 1:  # Asegurar que Buscar Datos funciona
            self.mostrar_buscar_datos()
        elif pestaña_actual == 1 or pestaña_actual == 2:  # Asegurar que Administración funciona
            self.mostrar_administracion()

    def mostrar_datos(self):
        self.datos.mostrar()

    def mostrar_buscar_datos(self):
        self.buscar_datos.mostrar()

    def mostrar_administracion(self):
        self.administracion.mostrar()

    def cargar_notas(self):
        try:
            with open("notas.txt", "r") as file:
                notas = file.read()
                self.administracion.text_anotador.insert(tk.END, notas)
        except FileNotFoundError:
            pass

    def guardar_notas(self):
        if hasattr(self.administracion, 'text_anotador'):
            with open("notas.txt", "w") as file:
                notas = self.administracion.text_anotador.get(1.0, tk.END)
                file.write(notas)

    def guardar_notas_y_cerrar(self):
        self.guardar_notas()
        self.master.destroy()




#Crear la ventana principal
root = tk.Tk()
app = Minimarket(root, "mariano", True)
root.mainloop()
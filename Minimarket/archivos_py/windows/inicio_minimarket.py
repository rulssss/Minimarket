from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QComboBox, QTableWidget, QLabel, QDoubleSpinBox, QTableWidgetItem, QApplication
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QFont, QIntValidator
from archivos_py.ui.minimarket import Ui_MainWindow
from archivos_py.threads.db_thread_minimarket import *


# ------------ VARIABLES DE CACHE GLOBALES ------------
categorias_cache = None
proveedores_cache = None
productos_cache = None


productos_por_id_cache = None
productos_por_nombre_cache = None
proveedores_por_nombre_cache = None
proveedores_por_telefono_cache = None
categorias_por_nombre_cache = None


# -----------------------------------------------------

#$  SEGUIR CON VISUALIZACION DE PROVEEDORES
class DatosTab:
    def __init__(self, ui):
        self.ui = ui
        self.button19_connected = False

        global usuario_activo

        #crear arreglo con threads abiertos
        self.threads = []

        # se crean variables globales de uso para actualizar datos
        self.actualizar_variables_globales_de_uso(0, self.inicializar_ui_con_datos) 

    def inicializar_ui_con_datos(self):
        #agregar productos
        self.ventana_agregar_productos()


        #borrar productos
        self.ventana_borrar_productos()

        # editar productos
        self.edit_product_by_id()

        # visualizar productos
        self.visualizar_datos()

        #-----------------------

        # agregar proveedores

        self.agregar_proveedor()

        # borrar proveedores
        self.borrar_proveedor()

        # editar proveedores
        self.editar_proveedor()

        # visualizar proveedores
        self.visualizar_proveedores()

        #-----------------------
        


    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()

    # funciones para corroborar si es decimal o entero
    def is_decimal(self, value):
            try:
                float(value)
                return True
            except ValueError:
                return False

    def is_digit(self, value):
            try:
                int(value)
                return True
            except ValueError:
                return False
            
            
    def actualizar_variables_globales_de_uso(self, r, callback=None):
        global categorias , proveedores, productos
     
        global categorias_cache, proveedores_cache, productos_cache
        global productos_por_id_cache, productos_por_nombre_cache
        global proveedores_por_nombre_cache, proveedores_por_telefono_cache
        global categorias_por_nombre_cache

            # Si ya hay cache, úsalo y llama al callback
        if r == 1 and categorias_cache is not None:
            categorias = categorias_cache
            if callback:
                callback()
            return
        if r == 2 and proveedores_cache is not None:
            proveedores = proveedores_cache
            if callback:
                callback()
            return
        if r == 3 and productos_cache is not None:
            productos = productos_cache
            if callback:
                callback()
            return

        if r == 0:
            self._datos_cargados = {"categorias": False, "proveedores": False, "productos": False}

            def check_all_loaded():
                if all(self._datos_cargados.values()):
                    if callback:
                        callback()
           
            # Obtener todas las categorías y asignarlas a la variable global 'categorias'
            self.categorias_thread = CategoriasThread()
            def on_categorias_obtenidas(cats):
                global categorias, categorias_por_nombre_cache
                categorias = cats
                categorias_por_nombre_cache = {c[0].strip().lower(): c for c in categorias}
                self._datos_cargados["categorias"] = True
                check_all_loaded()
                
                print(f"Categorías obtenidas: {categorias}")  # Para verificar que las categorías se actualizan correctamente
            self.categorias_thread.categorias_obtenidas.connect(on_categorias_obtenidas)
            self.start_thread(self.categorias_thread)
        
            # Obtener todos los proveedores y asignarlos a la variable global 'proveedores'
            self.proveedores_thread = ProveedoresThread()
            def on_proveedores_obtenidos(provs):
                global proveedores, proveedores_por_nombre_cache, proveedores_por_telefono_cache
                proveedores = provs
                proveedores_por_nombre_cache = {p[0].strip().lower(): p for p in proveedores}
                proveedores_por_telefono_cache = {str(p[1]).strip(): p for p in proveedores}
                self._datos_cargados["proveedores"] = True
                check_all_loaded()
                print(f"Proveedores obtenidos: {proveedores}")  # Para verificar que los proveedores se actualizan correctamente
            self.proveedores_thread.proveedores_obtenidos.connect(on_proveedores_obtenidos)
            self.start_thread(self.proveedores_thread)
        
            # Obtener todos los productos y asignarlos a la variable global 'productos'
            self.productos_thread = TraerTodosLosProductosThread()
            def on_productos_obtenidos(productos_obtenidos):
                global productos, productos_por_id_cache, productos_por_nombre_cache
                productos = productos_obtenidos
                productos_por_id_cache = {str(p[0]): p for p in productos}
                productos_por_nombre_cache = {p[1].strip().lower(): p for p in productos}
                self._datos_cargados["productos"] = True
                check_all_loaded()
                print(f"Productos obtenidos: {productos}")  # Para verificar que los productos se actualizan correctamente
            self.productos_thread.resultado.connect(on_productos_obtenidos)
            self.start_thread(self.productos_thread)

            
        else:
            if r == 1:
                # Obtener todas las categorías y asignarlas a la variable global 'categorias'
                self.categorias_thread = CategoriasThread()
                def on_categorias_obtenidas(cats):
                    global categorias, categorias_cache, categorias_por_nombre_cache
                    categorias = cats
                    categorias_cache = cats
                    categorias_por_nombre_cache = {c[0].strip().lower(): c for c in categorias}
                    print(f"Categorías obtenidas: {categorias}")  # Para verificar que las categorías se actualizan correctamente
                    if callback:
                        callback()
                self.categorias_thread.categorias_obtenidas.connect(on_categorias_obtenidas)
                self.start_thread(self.categorias_thread)
            elif r == 2:
                # Obtener todos los proveedores y asignarlos a la variable global 'proveedores'
                self.proveedores_thread = ProveedoresThread()
                def on_proveedores_obtenidos(provs):
                    global proveedores, proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
                    proveedores = provs
                    proveedores_cache = provs
                    proveedores_por_nombre_cache = {p[0].strip().lower(): p for p in proveedores}
                    proveedores_por_telefono_cache = {str(p[1]).strip(): p for p in proveedores}
                    print(f"Proveedores obtenidos: {proveedores}")  # Para verificar que los proveedores se actualizan correctamente
                    if callback:
                        callback()
                self.proveedores_thread.proveedores_obtenidos.connect(on_proveedores_obtenidos)
                self.start_thread(self.proveedores_thread)
            elif r == 3:
                # Obtener todos los productos y asignarlos a la variable global 'productos'
                self.productos_thread = TraerTodosLosProductosThread()
                def on_productos_obtenidos(productos_obtenidos):
                    global productos, productos_cache, productos_por_id_cache, productos_por_nombre_cache
                    productos = productos_obtenidos
                    productos_cache = productos_obtenidos
                    productos_por_id_cache = {str(p[0]): p for p in productos}
                    productos_por_nombre_cache = {p[1].strip().lower(): p for p in productos}
                    print(f"Productos obtenidos: {productos}")  # Para verificar que los productos se actualizan correctamente
                    if callback:
                        callback()
                self.productos_thread.resultado.connect(on_productos_obtenidos)
                self.start_thread(self.productos_thread)

    def limpiar_cache():
        global categorias_cache, proveedores_cache, productos_cache, productos_por_id_cache, productos_por_nombre_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache, categorias_por_nombre_cache
        categorias_cache = None
        proveedores_cache = None
        productos_cache = None
        productos_por_id_cache = None
        productos_por_nombre_cache = None
        proveedores_por_nombre_cache = None
        proveedores_por_telefono_cache = None
        categorias_por_nombre_cache = None

        
        
#################
#################


    #AGREGAR PRODUCTOS

    def ventana_agregar_productos(self):
        #BOTONES de la ventana agregar productos

        button19 = self.ui.frame_5.findChild(QPushButton, "pushButton_19")
        if button19:
            if not self.button19_connected:
                button19.setStyleSheet("background-color: rgb(168, 225, 255)")
                button19.clicked.connect(self.validate_and_process_inputs)
                button19.setShortcut(Qt.Key_Return)
                self.button19_connected = True
           
            
        button20 = self.ui.frame_5.findChild(QPushButton, "pushButton_20")
        if button20:            
            button20.clicked.connect(self.clear_inputs_agregar_productos)


        #configurar categorias y proveedores disponibles
        self.categorias()
        self.proveedores()

        #labels de agregar productos

        label_70 = self.ui.frame_5.findChild(QLabel, "label_70")
        if label_70:
            if label_70.text() != "Agregando":
                label_70.setStyleSheet("color: transparent")

        label_71 = self.ui.frame_5.findChild(QLabel, "label_71")
        if label_71:
            if label_71.text() != "producto...":
                label_71.setStyleSheet("color: transparent")

    #actualiza las categorias del combobox de la ventana agregar productos
    def categorias(self):
        input_categoria = self.ui.frame_5.findChild(QComboBox, "comboBox_5")
        input_categoria.clear()
        #se importa variable global categorias
        global categorias
        
        for i in categorias:
            input_categoria.addItem(f"{i[0]}")

    #actualiza los proveedores del combobox de la ventana agregar productos
    def proveedores(self):
        input_proveedor = self.ui.frame_5.findChild(QComboBox, "comboBox_6")
        input_proveedor.clear()
        #se importa varable global proveedores
        global proveedores
     
        for i in proveedores:
            input_proveedor.addItem(f"{i[0]}")

    def clear_inputs_agregar_productos(self):
        input_id = self.ui.frame_5.findChild(QLineEdit, "lineEdit_7")
        if input_id:
            input_id.clear()
            input_id.setFocus()

        input_nombre = self.ui.frame_5.findChild(QLineEdit, "lineEdit_6")
        if input_nombre:
            input_nombre.clear()

        input_precio_compra = self.ui.frame_5.findChild(QLineEdit, "lineEdit_5")
        if input_precio_compra:
            input_precio_compra.clear()

        input_precio_venta = self.ui.frame_5.findChild(QLineEdit, "lineEdit_4")
        if input_precio_venta:
            input_precio_venta.clear()

        input_stock = self.ui.frame_5.findChild(QLineEdit, "lineEdit_3")
        if input_stock:
            input_stock.clear()

        input_stock_ideal = self.ui.frame_5.findChild(QLineEdit, "lineEdit_8")
        if input_stock_ideal:
            input_stock_ideal.clear()

        input_categoria = self.ui.frame_5.findChild(QComboBox, "comboBox_5")
        if input_categoria:
            input_categoria.setCurrentIndex(0)

        input_proveedor = self.ui.frame_5.findChild(QComboBox, "comboBox_6")
        if input_proveedor:
            input_proveedor.setCurrentIndex(0)

    def validate_and_process_inputs(self):  
        global usuario_activo, productos_cache
        button19 = self.ui.frame_5.findChild(QPushButton, "pushButton_19")
        button20 = self.ui.frame_5.findChild(QPushButton, "pushButton_20")

        if button19:
            button19.setEnabled(False)
        if button20:
            button20.setEnabled(False)

        # lineEditS
        input_id = self.ui.frame_5.findChild(QLineEdit, "lineEdit_7")
        input_nombre = self.ui.frame_5.findChild(QLineEdit, "lineEdit_6")
        input_precio_compra = self.ui.frame_5.findChild(QLineEdit, "lineEdit_5")
        input_precio_venta = self.ui.frame_5.findChild(QLineEdit, "lineEdit_4")
        input_stock = self.ui.frame_5.findChild(QLineEdit, "lineEdit_3")
        input_stock_ideal = self.ui.frame_5.findChild(QLineEdit, "lineEdit_8")
        input_categoria = self.ui.frame_5.findChild(QComboBox, "comboBox_5")
        input_proveedor = self.ui.frame_5.findChild(QComboBox, "comboBox_6")

        input_id_value = input_id.text().strip() if input_id else ""
        input_nombre_value = input_nombre.text().strip() if input_nombre else ""
        input_precio_compra_value = input_precio_compra.text().strip() if input_precio_compra else ""
        input_precio_venta_value = input_precio_venta.text().strip() if input_precio_venta else ""
        input_stock_value = input_stock.text().strip() if input_stock else ""
        input_stock_ideal_value = input_stock_ideal.text().strip() if input_stock_ideal else ""
        input_categoria_value = input_categoria.currentText() if input_categoria else ""
        input_proveedor_value = input_proveedor.currentText() if input_proveedor else ""

        # Verificar si el ID o el nombre ya existen en el cache
        # Usar diccionarios para verificar existencia
        existe_id = productos_por_id_cache and input_id_value in productos_por_id_cache
        existe_nombre = productos_por_nombre_cache and input_nombre_value.lower() in productos_por_nombre_cache

        label_70 = self.ui.frame_5.findChild(QLabel, "label_70")
        label_71 = self.ui.frame_5.findChild(QLabel, "label_71")

        if existe_id or existe_nombre:
            if button19:
                button19.setEnabled(True)
            if button20:
                button20.setEnabled(True)

            if label_70 and label_71:
                label_70.setText("Está intentando cargar")
                label_71.setText("un producto existente")
                label_70.setStyleSheet("color: red; font-weight: bold")
                label_71.setStyleSheet("color: red; font-weight: bold")
            return

        if self.is_digit(input_id_value) and input_nombre_value and self.is_decimal(input_precio_compra_value) and self.is_decimal(input_precio_venta_value) and self.is_decimal(input_stock_value) and self.is_decimal(input_stock_ideal_value):
            if label_70 and label_71:
                label_70.setText("Agregando")
                label_71.setText("producto...")
                label_70.setStyleSheet("color: green; font-weight: bold")
                label_71.setStyleSheet("color: green; font-weight: bold")

            # Lanzar el thread para agregar producto
            self.agregar_thread = AgregarProductoThread(
                input_id_value, input_nombre_value, input_precio_compra_value, input_precio_venta_value,
                input_stock_value, input_stock_ideal_value, input_categoria_value, input_proveedor_value
            )
            self.agregar_thread.producto_agregado.connect(
                lambda exito: self.on_producto_agregado(exito, input_id_value, usuario_activo, input_id)
            )
            self.start_thread(self.agregar_thread)
        else:
            if button19:
                button19.setEnabled(True)
            if button20:
                button20.setEnabled(True)
            
            if label_70 and label_71:
                label_70.setText("Por favor, complete todos")
                label_71.setText("los campos correctamente")
                label_70.setStyleSheet("color: red; font-weight: bold")
                label_71.setStyleSheet("color: red; font-weight: bold")

            # Focus en el campo incorrecto
            if not self.is_digit(input_id_value):
                if input_id:
                    input_id.setFocus()
            elif not input_nombre_value:
                if input_nombre:
                    input_nombre.setFocus()
            elif not self.is_decimal(input_precio_compra_value):
                if input_precio_compra:
                    input_precio_compra.setFocus()
            elif not self.is_decimal(input_precio_venta_value):
                if input_precio_venta:
                    input_precio_venta.setFocus()
            elif not self.is_decimal(input_stock_value):
                if input_stock:
                    input_stock.setFocus()
            elif not self.is_decimal(input_stock_ideal_value):
                if input_stock_ideal:
                    input_stock_ideal.setFocus()


    # En tu clase DatosTab:
    def on_producto_agregado(self, exito, input_id_value, usuario_activo, input_id):
        label_70 = self.ui.frame_5.findChild(QLabel, "label_70")
        label_71 = self.ui.frame_5.findChild(QLabel, "label_71")
        button19 = self.ui.frame_5.findChild(QPushButton, "pushButton_19")
        button20 = self.ui.frame_5.findChild(QPushButton, "pushButton_20")

        if exito:
            if button19:
                button19.setEnabled(True)
            if button20:
                button20.setEnabled(True)

            self.clear_inputs_agregar_productos()
            if label_70 and label_71:
                label_70.setText("Producto cargado")
                label_71.setText("con éxito!")
                label_70.setStyleSheet("color: green; font-weight: bold")
                label_71.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_70.setStyleSheet("color: transparent"))
                QTimer.singleShot(6000, lambda: label_71.setStyleSheet("color: transparent"))
            
            # Usar hilo para cargar el movimiento
            self.movimiento_thread = MovimientoProductoThread(input_id_value, usuario_activo)
            self.start_thread(self.movimiento_thread)
    
            # Limpiar solo el cache de productos antes de actualizar
            global productos_cache, productos_por_id_cache
            productos_cache = None
            productos_por_id_cache = None
    
            self.actualizar_variables_globales_de_uso(3, self.populate_table_with_products)
            combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
            if combobox_id:
                self.populate_combobox_with_ids(combobox_id)
            if input_id:
                input_id.setFocus()
                QTimer.singleShot(2000, lambda: input_id.setFocus())
        else:

            self.clear_inputs_agregar_productos()

            label_70.setText("Esta intentando cargar")
            label_71.setText("un producto existente")
            label_70.setStyleSheet("color: green; font-weight: bold")
            label_71.setStyleSheet("color: green; font-weight: bold")

            if button19:
                button19.setEnabled(True)
            if button20:
                button20.setEnabled(True)

#################
#################

    #BORRAR PRODUCTOS

    def ventana_borrar_productos(self):
        # obtener datos de qline edit
        button21 = self.ui.frame_6.findChild(QPushButton, "pushButton_21")
        if button21:
            button21.setStyleSheet("background-color: red; padding: 5px;")
            button21.clicked.connect(self.delete_product)


        #labels de borrar productos

        label_72 = self.ui.frame_6.findChild(QLabel, "label_72")
        if label_72:
            if label_72.text() != "Producto no encontrado":
                label_72.setStyleSheet("color: transparent")


    #funcion para borrar
    def delete_product(self):
        global usuario_activo, productos_por_id_cache, productos_por_nombre_cache
        label_72 = self.ui.frame_6.findChild(QLabel, "label_72")

        button21 = self.ui.frame_6.findChild(QPushButton, "pushButton_21")
        if button21:
            button21.setEnabled(False)
            
        input_nombre_o_id = self.ui.frame_6.findChild(QLineEdit, "lineEdit_2")
        input_nombre_o_id_value = input_nombre_o_id.text().strip()
        if not input_nombre_o_id_value:
            if label_72:
                label_72.setText("Complete el campo")
                label_72.setStyleSheet("color: red; font-weight: bold")
            if button21:
                button21.setEnabled(True)
            input_nombre_o_id.setFocus()
            return

        self._borrar_id = None
        self._borrar_nombre = None
        self._borrar_valor = input_nombre_o_id_value

        # Buscar en cache usando diccionarios
        if input_nombre_o_id_value.isdigit():
            # Buscar por ID
            producto = productos_por_id_cache.get(input_nombre_o_id_value) if productos_por_id_cache else None
            if producto:
                self._borrar_id = int(input_nombre_o_id_value)
                self._borrar_nombre = producto[1]
                self._on_nombre_obtenido(self._borrar_nombre)
            else:
                if button21:
                    button21.setEnabled(True)
                if label_72:
                    label_72.setText("Producto no encontrado")
                    label_72.setStyleSheet("color: red; font-weight: bold")
                input_nombre_o_id.setFocus()
        else:
            # Buscar por nombre
            producto = productos_por_nombre_cache.get(input_nombre_o_id_value.lower()) if productos_por_nombre_cache else None
            if producto:
                self._borrar_id = producto[0]
                self._borrar_nombre = producto[1]
                self._on_nombre_obtenido(self._borrar_nombre)
            else:
                if button21:
                    button21.setEnabled(True)
                if label_72:
                    label_72.setText("Producto no encontrado")
                    label_72.setStyleSheet("color: red; font-weight: bold")
                input_nombre_o_id.setFocus()
        
            

    def _on_id_obtenido_nombre_ya_disponible(self, id_producto):
        self._borrar_id = id_producto
        # Ya tenemos el nombre, así que seguimos directo al borrado
        self._on_nombre_obtenido(self._borrar_nombre)

    def _on_nombre_obtenido(self, nombre_producto):
        label_72 = self.ui.frame_6.findChild(QLabel, "label_72")
        if label_72:
            label_72.setText("Borrando producto...")
            label_72.setStyleSheet("color: green; font-weight: bold")
            
        self._borrar_nombre = nombre_producto
        # Cuando tenemos ambos datos, lanzar el hilo de borrado
        self.borrar_thread = BorrarProductoThread(self._borrar_valor)
        self.borrar_thread.resultado.connect(self._on_borrado_result)
        self.start_thread(self.borrar_thread)

    def _on_borrado_result(self, exito):
        if exito:
            # Lanzar hilo de movimiento
            self.movimiento_thread = MovimientoProductoBorrarThread(self._borrar_id, self._borrar_nombre, usuario_activo)
            self.movimiento_thread.movimiento_borrado.connect(self.on_producto_borrado)
            self.start_thread(self.movimiento_thread)
        else:
            print("algo ocurrio que no se pudo borrar el producto")
            
    def on_producto_borrado(self):
        label_72 = self.ui.frame_6.findChild(QLabel, "label_72")
        self.clear_inputs_borrar_productos()
        if label_72:
            label_72.setText("Producto borrado con éxito")
            label_72.setStyleSheet("color: green; font-weight: bold")
            QTimer.singleShot(6000, lambda: label_72.setStyleSheet("color: transparent"))

        input_nombre_o_id = self.ui.frame_6.findChild(QLineEdit, "lineEdit_2")
        if input_nombre_o_id:
            QTimer.singleShot(2000, lambda: input_nombre_o_id.setFocus())

        button21 = self.ui.frame_6.findChild(QPushButton, "pushButton_21")
        if button21:
            button21.setEnabled(True)   

        #se actualizan otras aprtes del programa
        # Limpiar solo el cache de productos antes de actualizar
        global productos_cache, productos_por_id_cache
        productos_cache = None
        productos_por_id_cache = None

        # Actualizar productos y refrescar la tabla y combobox cuando termine
        self.actualizar_variables_globales_de_uso(3, lambda: (
            self.populate_table_with_products(),
            self.populate_combobox_with_ids(self.ui.frame_7.findChild(QComboBox, "comboBox_3"))
        ))

        combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
        if combobox_id:
            self.populate_combobox_with_ids(combobox_id)

        # funcion para limpiar despues de borrar  
    def clear_inputs_borrar_productos(self):
        input_nombre = self.ui.frame_6.findChild(QLineEdit, "lineEdit_2")
        if input_nombre:
            input_nombre.clear()
            input_nombre.setFocus()

#################
#################                

    #EDITAR PRODUCTOS

    def edit_product_by_id(self):
        
        global producto_selecc
        combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
        

        if combobox_id:
            combobox_id.setEditable(True)
            combobox_id.setInsertPolicy(QComboBox.NoInsert)
            combobox_id.setCompleter(None)
            # Solo permitir números
            combobox_id.setValidator(QIntValidator())
            # Filtrar IDs mientras se escribe
            combobox_id.lineEdit().textEdited.connect(lambda text: self.filter_combobox_ids(combobox_id, text))
            # Ejecutar load_product_data cada vez que cambia el texto del QLineEdit
            combobox_id.lineEdit().textChanged.connect(lambda _: self.load_product_data())
            self.populate_combobox_with_ids(combobox_id)
            combobox_id.setFocus()
            combobox_id.lineEdit().selectAll()

        boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
        if boton_editar:
                boton_editar.setEnabled(True)
                boton_editar.setStyleSheet("background-color: rgb(255, 202, 96)")
                boton_editar.setShortcut(Qt.Key_Return)
                boton_editar.clicked.connect(lambda: self.verifica_datos_iguales(producto_selecc if producto_selecc is not None else None))

        boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")
        if boton_cancelar:
            boton_cancelar.clicked.connect(self.boton_cancelar)

        # Labels
        label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
        label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
        if label_73 and label_74:
            label_74.setStyleSheet("color: transparent")
            label_73.setStyleSheet("color: transparent")

        # edicion de frame para aumentar precios

        combobox_19 = self.ui.frame_55.findChild(QComboBox, "comboBox_19")
        if combobox_19:
            if combobox_19.count() == 0:
                combobox_19.addItem("Categoría")
                combobox_19.addItem("Proveedor")

            combobox_19.currentIndexChanged.connect(self.update_combobox_20)

        # corre la funcion por si no hay nada en el combobox 20
        combobox_20 = self.ui.frame_55.findChild(QComboBox, "comboBox_20")
        if combobox_20:
            if combobox_20.count() == 0:
                self.update_combobox_20()
        
        doublespinbox = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox")
        if doublespinbox:
            doublespinbox.valueChanged.connect(self.update_spinbox_value)

        pushbutton_49 = self.ui.frame_55.findChild(QPushButton, "pushButton_49")
        if pushbutton_49:
            pushbutton_49.setEnabled(True)
            pushbutton_49.clicked.connect(self.update_product_prices)


    def update_spinbox_value(self):
        doublespinbox = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox")
        doublespinbox_2 = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox_2")
        doublespinbox_value = doublespinbox.value()

        if doublespinbox_2:
            doublespinbox_2.setValue(doublespinbox_value)

    def update_combobox_20(self):
        combobox_19 = self.ui.frame_55.findChild(QComboBox, "comboBox_19")
        combobox_20 = self.ui.frame_55.findChild(QComboBox, "comboBox_20")
        if combobox_19 and combobox_20:
            combobox_20.clear()
            if combobox_19.currentText() == "Categoría":
                self.populate_combobox_with_categorias(combobox_20)
            elif combobox_19.currentText() == "Proveedor":
                self.populate_combobox_with_proveedores(combobox_20)


    def clear_doublespinbox_values(self):
        doublespinbox = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox")
        doublespinbox_2 = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox_2")
        if doublespinbox:
            doublespinbox.setValue(0.00)
        if doublespinbox_2:
            doublespinbox_2.setValue(0.00)

    def update_product_prices(self):
        global usuario_activo

        pushbutton_49 = self.ui.frame_55.findChild(QPushButton, "pushButton_49")
        if pushbutton_49:
            pushbutton_49.setEnabled(False)

        boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
        if boton_editar:
            boton_editar.setEnabled(False)
        boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")
        if boton_cancelar:
            boton_cancelar.setEnabled(False)
            

        doublespinbox = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox")
        doublespinbox_2 = self.ui.frame_55.findChild(QDoubleSpinBox, "doubleSpinBox_2")
        combobox_19 = self.ui.frame_55.findChild(QComboBox, "comboBox_19")
        combobox_20 = self.ui.frame_55.findChild(QComboBox, "comboBox_20")

        doublespinbox_value = doublespinbox.value()
        doublespinbox_2_value = doublespinbox_2.value()
        combobox_19_value = combobox_19.currentText()
        combobox_20_value = combobox_20.currentText()

        if combobox_19_value == "Categoría":
            self.aumentar_thread = AumentarPreciosCategoriaThread(doublespinbox_value, doublespinbox_2_value, combobox_20_value)
            s = True
        else:
            self.aumentar_thread = AumentarPreciosProveedorThread(doublespinbox_value, doublespinbox_2_value, combobox_20_value)
            s = False

        def on_aumento_finalizado():
            pushbutton_49 = self.ui.frame_55.findChild(QPushButton, "pushButton_49")
            boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
            boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")

            if doublespinbox_value != 0.00 or doublespinbox_2_value != 0.00:
                global productos_cache
                # Limpiar solo el cache de productos antes de actualizar
                productos_cache = None
                # Actualizar productos y refrescar la tabla y combobox cuando termine
                self.actualizar_variables_globales_de_uso(3, lambda: (
                    self.populate_table_with_products(),
                ))
                
                self.movimiento_thread = MovimientoAumentoPreciosThread(combobox_20_value, usuario_activo, s)
                self.movimiento_thread.finished.connect(lambda: (self.clear_doublespinbox_values(), self.load_product_data(), pushbutton_49.setEnabled(True), boton_editar.setEnabled(True), boton_cancelar.setEnabled(True)))
                self.start_thread(self.movimiento_thread)

            else:
                if pushbutton_49:
                    pushbutton_49.setEnabled(True)
                if boton_editar:
                    boton_editar.setEnabled(True)
                if boton_cancelar:
                    boton_cancelar.setEnabled(True)
                

        self.aumentar_thread.finished.connect(on_aumento_finalizado)
        self.aumentar_thread.start()

    def load_product_data(self):
        global productos, productos_cache, productos_por_id_cache, producto_selecc
        combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
        if combobox_id:
            selected_id = combobox_id.currentText()
            if selected_id and selected_id.isdigit():
                # Si el cache está vacío, actualizalo primero
                if productos_cache is None or productos_por_id_cache is None:
                    self.actualizar_variables_globales_de_uso(3, lambda: self.load_product_data())
                    return
                # Buscar el producto usando el diccionario (más rápido)
                producto = productos_por_id_cache.get(selected_id)
                self._on_producto_por_id_obtenido(producto, selected_id, combobox_id)
            else:
                # Limpiar todos los campos si el producto no existe
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").clear()
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").clear()
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").clear()
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").clear()
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").clear()
                combobox_categorias = self.ui.frame_7.findChild(QComboBox, "comboBox_4")
                if combobox_categorias:
                    combobox_categorias.setCurrentIndex(-1)
                combobox_proveedores = self.ui.frame_7.findChild(QComboBox, "comboBox_7")
                if combobox_proveedores:
                    combobox_proveedores.setCurrentIndex(-1)


    def _on_producto_por_id_obtenido(self, producto, selected_id, combobox_id):
        global producto_selecc
        producto_selecc = producto
        if producto and selected_id == str(producto[0]):
            
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").setText(producto[1])
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").setText(str(producto[2]))
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").setText(str(producto[3]))
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").setText(str(producto[4]))
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").setText(str(producto[5]))

            # Actualizar los combobox de categoría y proveedor
            combobox_categorias = self.ui.frame_7.findChild(QComboBox, "comboBox_4")
            if combobox_categorias:
                self.populate_combobox_with_categorias(combobox_categorias)
                combobox_categorias.setCurrentText(producto[6])
            combobox_proveedores = self.ui.frame_7.findChild(QComboBox, "comboBox_7")
            if combobox_proveedores:
                self.populate_combobox_with_proveedores(combobox_proveedores)
                combobox_proveedores.setCurrentText(producto[7])

            combobox_id.setFocus()
            combobox_id.lineEdit().selectAll()
        else:
            # Limpiar todos los campos si el producto no existe
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").clear()
            combobox_categorias = self.ui.frame_7.findChild(QComboBox, "comboBox_4")
            if combobox_categorias:
                combobox_categorias.setCurrentIndex(-1)
            combobox_proveedores = self.ui.frame_7.findChild(QComboBox, "comboBox_7")
            if combobox_proveedores:
                combobox_proveedores.setCurrentIndex(-1)

            label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
            label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
            if label_73 and label_74:
                label_73.setText("Seleccione o escriba")
                label_73.setStyleSheet("color: red; font-weight: bold")
                label_74.setText("un ID válido")
                label_74.setStyleSheet("color: red; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_73.setStyleSheet("color: transparent"))
                QTimer.singleShot(6000, lambda: label_74.setStyleSheet("color: transparent"))

    def boton_cancelar(self):
        self.load_product_data()

    def edit_product(self, id, nombre_prod, precio_compra, precio_venta, stock, stock_ideal, categoria, proveedor):
        
        self.actualizar_thread = ActualizarProductoThread(
            id, nombre_prod, precio_compra, precio_venta, stock, stock_ideal, categoria, proveedor
        )
        self.actualizar_thread.finished.connect(self.on_producto_actualizado)
        self.start_thread(self.actualizar_thread)

        # Usar hilo para cargar movimiento editado
        self.movimiento_editado_thread = MovimientoProductoEditadoThread(id, usuario_activo)
        self.movimiento_editado_thread.start()

    def on_producto_actualizado(self):
        label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
        label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
        if label_73 and label_74:
            label_73.setText("Producto actualizado")
            label_73.setStyleSheet("color: green; font-weight: bold")
            label_74.setText("con éxito")
            label_74.setStyleSheet("color: green; font-weight: bold")
            QTimer.singleShot(6000, lambda: label_73.setStyleSheet("color: transparent"))
            QTimer.singleShot(6000, lambda: label_74.setStyleSheet("color: transparent"))
            

        # Limpiar el cache de productos antes de actualizar
        global productos_cache, productos_por_id_cache
        productos_cache = None
        productos_por_id_cache = None

        # Actualizar productos y refrescar la tabla y combobox cuando termine
        self.actualizar_variables_globales_de_uso(3, lambda: (
            self.populate_table_with_products(),
            self.populate_combobox_with_ids(self.ui.frame_7.findChild(QComboBox, "comboBox_3")),
            self.load_product_data()
        ))

        combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
        if combobox_id:
            combobox_id.setFocus()
            combobox_id.lineEdit().selectAll()

        boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
        if boton_editar:
            boton_editar.setEnabled(True)

        boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")
        if boton_cancelar:
            boton_cancelar.setEnabled(True)

        pushbutton_49 = self.ui.frame_55.findChild(QPushButton, "pushButton_49")
        if pushbutton_49:
            pushbutton_49.setEnabled(True)

     


    def verifica_datos_iguales(self, producto):
        global usuario_activo

        if producto:
            if (self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").text() == producto[1] and
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").text() == str(producto[2]) and
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").text() == str(producto[3]) and
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").text() == str(producto[4]) and
                self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").text() == str(producto[5]) and
                self.ui.frame_7.findChild(QComboBox, "comboBox_4").currentText() == producto[6] and
                self.ui.frame_7.findChild(QComboBox, "comboBox_7").currentText() == producto[7]):

                label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
                label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
                if label_73 and label_74:
                    label_73.setText("Por favor, edite")
                    label_73.setStyleSheet("color: red; font-weight: bold")
                    label_74.setText("los campos")
                    label_74.setStyleSheet("color: red; font-weight: bold")
                    

            elif not (self.is_decimal(self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").text()) and
                self.is_decimal(self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").text()) and
                self.is_decimal(self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").text()) and
                self.is_decimal(self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").text())):
                label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
                label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
                
                if label_73 and label_74:
                    label_73.setText("Por favor, ingrese")
                    label_73.setStyleSheet("color: red; font-weight: bold")
                    label_74.setText("valores válidos")
                    label_74.setStyleSheet("color: red; font-weight: bold")
                   
            
            else:
                label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
                label_74 = self.ui.frame_7.findChild(QLabel, "label_74")

                boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
                if boton_editar:
                    boton_editar.setEnabled(False)
                boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")
                if boton_cancelar:
                    boton_cancelar.setEnabled(False)

                pushbutton_49 = self.ui.frame_55.findChild(QPushButton, "pushButton_49")
                if pushbutton_49:
                    pushbutton_49.setEnabled(False)
                
                    
                if label_73 and label_74:
                    label_73.setText("Actualizando")
                    label_74.setText("producto...")
                    label_73.setStyleSheet("color: green; font-weight: bold")
                    label_74.setStyleSheet("color: green; font-weight: bold")
                
                self.edit_product(
                    producto_selecc[0],
                    self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").text().strip(),
                    self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").text().strip(),
                    self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").text().strip(),
                    self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").text().strip(),
                    self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").text().strip(),
                    self.ui.frame_7.findChild(QComboBox, "comboBox_4").currentText(),
                    self.ui.frame_7.findChild(QComboBox, "comboBox_7").currentText()
                )
    
        else:
            boton_editar = self.ui.frame_7.findChild(QPushButton, "pushButton_23")
            if boton_editar:
                boton_editar.setEnabled(True)
            boton_cancelar = self.ui.frame_7.findChild(QPushButton, "pushButton_24")
            if boton_cancelar:
                boton_cancelar.setEnabled(True)
            # Limpiar todos los campos si el producto no existe
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_9").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_10").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_11").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_12").clear()
            self.ui.frame_7.findChild(QLineEdit, "lineEdit_13").clear()
            combobox_categorias = self.ui.frame_7.findChild(QComboBox, "comboBox_4")
            if combobox_categorias:
                combobox_categorias.setCurrentIndex(-1)
            combobox_proveedores = self.ui.frame_7.findChild(QComboBox, "comboBox_7")
            if combobox_proveedores:
                combobox_proveedores.setCurrentIndex(-1)
    
            label_73 = self.ui.frame_7.findChild(QLabel, "label_73")
            label_74 = self.ui.frame_7.findChild(QLabel, "label_74")
            if label_73 and label_74:
                label_73.setText("Seleccione o escriba")
                label_73.setStyleSheet("color: red; font-weight: bold")
                label_74.setText("un ID válido")
                label_74.setStyleSheet("color: red; font-weight: bold")
                

    
    # funciones para actualizado de la seccion de agregar, borrar, visualizar y editar productos

    def populate_combobox_with_ids(self, combobox):
        combobox.clear()
        global productos
        
        ids = [str(producto[0]) for producto in productos]
        combobox.addItems(ids)
        combobox.setMaxVisibleItems(3)

    def filter_combobox_ids(self, combobox, text):
        global productos
        ids = [str(producto[0]) for producto in productos if text in str(producto[0])]
        combobox.clear()
        for item in ids:
            combobox.addItem(item)
        combobox.setCurrentText(text)
        
    
    def filter_combobox_categorias(self, combobox, text):
        global categorias
        nombres_categorias = [categoria[0] for categoria in categorias if self.texto.lower() in categoria[0].lower()]
        combobox.clear()
        for item in nombres_categorias:
            combobox.addItem(item)
        combobox.setCurrentText(text)

    def populate_combobox_with_categorias(self, combobox):
        combobox.clear()
        global categorias
        for categoria in categorias:
            combobox.addItem(categoria[0])
        
        
    def populate_combobox_with_proveedores(self, combobox):
        global proveedores
        combobox.clear()
        for proveedor in proveedores:
            combobox.addItem(proveedor[0])



################
################

    # Visualizacion de productos

    def visualizar_datos(self):
        self.populate_combobox_frame_2()
        self.populate_table_with_products()

        # Conectar el QLineEdit para filtrar productos
        line_edit_1 = self.ui.frame_4.findChild(QLineEdit, "lineEdit1")
        if line_edit_1:
            line_edit_1.textChanged.connect(self.filter_products)
      

        comboboxselecc = self.ui.frame_3.findChild(QComboBox, "comboBox")
        if comboboxselecc:
            comboboxselecc.currentIndexChanged.connect(self.update_combobox_2)
            comboboxselecc.currentIndexChanged.connect(self.filter_products)
            self.update_combobox_2()

        # Conectar el QComboBox_2 para filtrar productos
        combobox_2 = self.ui.frame_3.findChild(QComboBox, "comboBox_2")
        if combobox_2:
            combobox_2.currentIndexChanged.connect(self.filter_products)
            

    def update_combobox_2(self):
        comboboxselecc = self.ui.frame_3.findChild(QComboBox, "comboBox")
        if comboboxselecc:
            combobox_value = comboboxselecc.currentText()
            if combobox_value == "Proveedor":
                self.populate_combobox_proveedores()
            elif combobox_value == "Categoría":
                self.populate_combobox_categorias()
    
    def populate_combobox_frame_2(self):
        combobox = self.ui.frame_3.findChild(QComboBox, "comboBox")
        if combobox:
            combobox.clear()
            combobox.addItem("")
            combobox.addItem("Proveedor")
            combobox.addItem("Categoría")

    
    def populate_combobox_proveedores(self):
        combobox = self.ui.frame_3.findChild(QComboBox, "comboBox_2")
        if combobox:
            global proveedores
            combobox.clear()
            combobox.addItem("")
            for proveedor in proveedores:
                combobox.addItem(proveedor[0])
            

    def populate_combobox_categorias(self):
        combobox = self.ui.frame_3.findChild(QComboBox, "comboBox_2")
        if combobox:
            global categorias
            combobox.clear()
            combobox.addItem("")
            for categoria in categorias:
                combobox.addItem(categoria[0])

    def populate_table_with_products(self):
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if table_widget:
            global productos

            if len(productos) == 0:
                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                table_widget.setRowCount(len(productos))
                table_widget.setColumnCount(8)
                table_widget.setHorizontalHeaderLabels([
                    "ID", "Nombre", "Precio Compra", "Precio Venta", "Stock",
                    "Stock Ideal", "Categoría", "Proveedor"
                ])
                header = table_widget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 16, QFont.Bold))
                for row, producto in enumerate(productos):
                    for col, value in enumerate(producto):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))
                        item.setTextAlignment(Qt.AlignCenter)
                        if col == 4 and float(producto[4]) < float(producto[5]):
                            item.setForeground(Qt.red)
                        table_widget.setItem(row, col, item)

    def filter_products(self):
        line_edit = self.ui.frame_4.findChild(QLineEdit, "lineEdit1")
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        combobox = self.ui.frame_3.findChild(QComboBox, "comboBox")
        combobox_2 = self.ui.frame_3.findChild(QComboBox, "comboBox_2")

        if line_edit and table_widget and combobox and combobox_2:
            filter_text = line_edit.text().lower()
            combobox_value = combobox.currentText()
            combobox_2_value = combobox_2.currentText()

            global productos
        
            filtered_productos = []
            for producto in productos:
                if filter_text in producto[1].lower() or filter_text in str(producto[0]).lower():
                    if combobox_value == "Proveedor" and combobox_2_value:
                        if combobox_2_value == producto[7]:
                            filtered_productos.append(producto)
                    elif combobox_value == "Categoría" and combobox_2_value:
                        if combobox_2_value == producto[6]:
                            filtered_productos.append(producto)
                    elif combobox_value == "":
                        filtered_productos.append(producto)
            if len(filtered_productos) == 0:
                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                table_widget.setRowCount(len(filtered_productos))
                table_widget.setColumnCount(8)
                table_widget.setHorizontalHeaderLabels([
                    "ID", "Nombre", "Precio Compra", "Precio Venta", "Stock", "Stock Ideal", "Categoría", "Proveedor"
                ])
                for row, producto in enumerate(filtered_productos):
                    for col, value in enumerate(producto):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))
                        item.setTextAlignment(Qt.AlignCenter)
                        if col == 4 and float(producto[4]) < float(producto[5]):
                            item.setForeground(Qt.red)
                        table_widget.setItem(row, col, item)


    # Función para copiar una columna al portapapeles
    def copy_column_to_clipboard(self, column_index):
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if table_widget:
            column_data = []
            for row in range(table_widget.rowCount()):
                item = table_widget.item(row, column_index)
                if item:
                    column_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\n".join(column_data))
            self.show_copied_message("Columna copiada al portapapeles")

    # Función para copiar una fila al portapapeles
    def copy_row_to_clipboard(self, row_index):
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

    def copy_entire_table_to_clipboard(self):
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if not table_widget:
            return
        row_count = table_widget.rowCount()
        col_count = table_widget.columnCount()
        # Copiar encabezados
        headers = [table_widget.horizontalHeaderItem(col).text() for col in range(col_count)]
        data = ['\t'.join(headers)]
        # Copiar filas
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = table_widget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append('\t'.join(row_data))
        # Copiar al portapapeles
        clipboard = QApplication.clipboard()
        clipboard.setText('\n'.join(data))
        self.show_copied_message("Tabla copiada al portapapeles")

    # Función para mostrar el mensaje de copiado
    def show_copied_message(self, message):
        copied_label = QLabel(message, self.ui.centralwidget)
        copied_label.setStyleSheet("""
            QLabel {
            background-color: rgba(0, 0, 0, 150);
            color: white;
            font-size: 16pt;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            }
        """)
        copied_label.setAlignment(Qt.AlignCenter)
        copied_label.setFixedSize(350, 50)

        # Centrar el QLabel en la pantalla
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - copied_label.width()) // 2
        y = (screen_geometry.height() - copied_label.height()) // 2
        copied_label.move(x, y)
        copied_label.show()

        # Ocultar el QLabel después de 2 segundos
        QTimer.singleShot(2000, copied_label.hide)


################
################

    # Agregar Proveedor

    def agregar_proveedor(self):


        button_26 = self.ui.frame_10.findChild(QPushButton, "pushButton_26")
        if button_26:
            button_26.setStyleSheet("background-color: rgb(168, 225, 255)")
            button_26.setShortcut(Qt.Key_Return)
            button_26.clicked.connect(self.validate_and_process_inputs_proveedores)

        button_25 = self.ui.frame_10.findChild(QPushButton, "pushButton_25")
        if button_25:
            button_25.clicked.connect(self.clear_inputs_agregar_proveedores)
        

        label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
        if label_75:
            label_75.setStyleSheet("color: transparent")

        label_76 = self.ui.frame_10.findChild(QLabel, "label_76")
        if label_76:
            label_76.setStyleSheet("color: transparent")
    
    def clear_inputs_agregar_proveedores(self):
        lineEdit_14 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_14")
        lineEdit_15 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_15")
        lineEdit_17 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_17")

        if lineEdit_14 and lineEdit_15 and lineEdit_17:            
            lineEdit_14.clear()
            lineEdit_15.clear()
            lineEdit_17.clear()
            lineEdit_14.setFocus()

    def validate_and_process_inputs_proveedores(self):
        global usuario_activo, proveedores_por_nombre_cache, proveedores_por_telefono_cache

        lineEdit_14 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_14")  # Nombre
        lineEdit_15 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_15")  # Teléfono
        lineEdit_17 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_17")  # Dirección

        button_26 = self.ui.frame_10.findChild(QPushButton, "pushButton_26")
        button_25 = self.ui.frame_10.findChild(QPushButton, "pushButton_25")
        if button_26:
            button_26.setEnabled(False)
        if button_25:
            button_25.setEnabled(False)

        if lineEdit_14 and lineEdit_15 and lineEdit_17:
            lineEdit_14_value = lineEdit_14.text().strip()
            lineEdit_15_value = lineEdit_15.text().strip()
            lineEdit_17_value = lineEdit_17.text().strip()

            # Verificar si el proveedor ya existe por nombre o teléfono usando diccionarios
            existe_nombre = proveedores_por_nombre_cache and lineEdit_14_value.lower() in proveedores_por_nombre_cache
            existe_telefono = proveedores_por_telefono_cache and lineEdit_15_value in proveedores_por_telefono_cache

            if existe_nombre or existe_telefono:
                label_75 = self.ui.frame_10.findChild(QLabel, "label_76")
                if button_25:
                    button_25.setEnabled(True)
                if button_26:
                    button_26.setEnabled(True)

                if label_75:
                    label_75.setText("Está intentando cargar un")
                    label_75.setStyleSheet("color: red; font-weight: bold")
                    label_76 = self.ui.frame_10.findChild(QLabel, "label_75")
                    label_76.setText("proveedor o número existente")
                    label_76.setStyleSheet("color: red; font-weight: bold")
                    
                return
            else:
                if lineEdit_14_value and lineEdit_15_value.isdigit():
                    label_75 = self.ui.frame_10.findChild(QLabel, "label_76")
                    label_75.setText("Cargando")
                    label_75.setStyleSheet("color: green; font-weight: bold")
                    label_76 = self.ui.frame_10.findChild(QLabel, "label_75")
                    label_76.setText("proveedor...")
                    label_76.setStyleSheet("color: green; font-weight: bold")
                    self.proveedor_thread = ProveedorThread(lineEdit_14_value, lineEdit_15_value, lineEdit_17_value)
                    self.proveedor_thread.proveedor_cargado.connect(lambda exito: self.on_proveedor_cargado(exito, lineEdit_14_value))
                    self.proveedor_thread.start()
                else:
                    if button_25:
                        button_25.setEnabled(True)
                    if button_26:
                        button_26.setEnabled(True)

                    label_75 = self.ui.frame_10.findChild(QLabel, "label_76")
                    if label_75:
                        label_75.setText("Por favor, complete todos")
                        label_75.setStyleSheet("color: red; font-weight: bold")
                        label_76 = self.ui.frame_10.findChild(QLabel, "label_75")
                        label_76.setText("los campos correctamente")
                        label_76.setStyleSheet("color: red; font-weight: bold")

                    if not lineEdit_14_value:
                        lineEdit_14.setFocus()
                    elif not lineEdit_15_value.isdigit():
                        lineEdit_15.setFocus()
    

    def on_proveedor_cargado(self, exito, nombre_proveedor):
        global usuario_activo
        if exito:
            self.movimiento_proveedor_thread = MovimientoProveedorThread(nombre_proveedor, usuario_activo)
            self.movimiento_proveedor_thread.start()
            #limpia inputs
            self.clear_inputs_agregar_proveedores()

            button_26 = self.ui.frame_10.findChild(QPushButton, "pushButton_26")
            button_25 = self.ui.frame_10.findChild(QPushButton, "pushButton_25")
            if button_26:
                button_26.setEnabled(True)
            if button_25:
                button_25.setEnabled(True)

            label_76 = self.ui.frame_10.findChild(QLabel, "label_76")
            label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
            if label_76 and label_75:
                label_76.setText("Proveedor cargado")
                label_76.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_76.setStyleSheet("color: transparent"))
                label_75.setText("con éxito")
                label_75.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_75.setStyleSheet("color: transparent"))

            # actualiza proveedores
            global proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
            proveedores_cache = None
            proveedores_por_nombre_cache = None
            proveedores_por_telefono_cache = None
            self.actualizar_variables_globales_de_uso(2, lambda: (
                self.populate_combobox_with_proveedores(self.ui.frame_7.findChild(QComboBox, "comboBox_7")),
                self.populate_table_with_proveedores(),
                self.proveedores()
            ))
            
            
        else:
            print("se genero un error de tipeo al cargar el proveedor")


################
################

    #Borrar proveedor

    def borrar_proveedor(self):

        button_34 = self.ui.frame_12.findChild(QPushButton, "pushButton_34")
        if button_34:
            button_34.setStyleSheet("background-color: red; padding: 5px;")
            button_34.clicked.connect(self.delete_proveedor)


        label_77 = self.ui.frame_12.findChild(QLabel, "label_77")
        if label_77:
            label_77.setStyleSheet("color: transparent")

        label_82 = self.ui.frame_42.findChild(QLabel, "label_82")
        if label_82:
            label_82.setStyleSheet("font-size: 16pt;")
            label_82.setText("¡Advertencia!\nSi borra un proveedor, los productos asociados a él se borrarán también")
            label_82.setAlignment(Qt.AlignCenter)

    def delete_proveedor(self):
        global usuario_activo, proveedores_por_nombre_cache

        button_34 = self.ui.frame_12.findChild(QPushButton, "pushButton_34")
        if button_34:
            button_34.setEnabled(False)

        input_nombre = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")
        input_nombre_value = input_nombre.text().strip() if input_nombre else ""

        label_77 = self.ui.frame_12.findChild(QLabel, "label_77")
        lineEdit_20 = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")

        # Caso especial: Proveedor1
        if input_nombre_value == "Proveedor1":
            if lineEdit_20:
                lineEdit_20.clear()
            if label_77:
                label_77.setText("No se puede borrar el Proveedor1")
                label_77.setStyleSheet("color: red; font-weight: bold")
                
            if input_nombre:
                input_nombre.setFocus()

            if button_34:
                button_34.setEnabled(True)
            return
        
        if input_nombre_value == "":
            if lineEdit_20:
                lineEdit_20.clear()
            if label_77:
                label_77.setText("Por favor, complete el campo")
                label_77.setStyleSheet("color: red; font-weight: bold")
                
            if input_nombre:
                input_nombre.setFocus()

            if button_34:
                button_34.setEnabled(True)
            return

        # Verificar en cache si existe el proveedor
        existe_en_cache = proveedores_por_nombre_cache and input_nombre_value.lower() in proveedores_por_nombre_cache
        
        if existe_en_cache:

            if label_77:
                label_77.setText("Borrando Proveedor...")
                label_77.setStyleSheet("color: green; font-weight: bold")
                

            # Buscar en la base (puede tener lógica extra)
            self.buscar_prov_thread = BuscarProveedorThread(input_nombre_value)
            def on_busqueda_finalizada(bandera):

                if bandera:
                    # Traer ID en hilo
                    self.traer_id_thread = TraerIdProveedorThread(input_nombre_value)
                    def on_id_obtenido(id_proveedor):
                        # Cargar movimiento en hilo
                        self.movimiento_borrado_thread = MovimientoProveedorBorradoThread(input_nombre_value, id_proveedor, usuario_activo)
                        self.movimiento_borrado_thread.start()

                        # actualizar cache, tablas y comboboxes
                        global proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
                        proveedores_cache = None
                        proveedores_por_nombre_cache = None
                        proveedores_por_telefono_cache = None

                        self.actualizar_variables_globales_de_uso(2, lambda: (
                            self.populate_combobox_with_proveedores(self.ui.frame_7.findChild(QComboBox, "comboBox_7")),
                            self.populate_table_with_proveedores(),
                            self.populate_combobox_proveedores(),
                            self.proveedores()
                        ))

                         # Limpiar input y mostrar mensaje
                        lineEdit_20 = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")
                        if lineEdit_20:
                            lineEdit_20.clear()
                        label_77 = self.ui.frame_12.findChild(QLabel, "label_77")
                        if label_77:
                            label_77.setText("Proveedor borrado con éxito")
                            label_77.setStyleSheet("color: green; font-weight: bold")
                            QTimer.singleShot(6000, lambda: label_77.setStyleSheet("color: transparent"))
                        
                        button_34 = self.ui.frame_12.findChild(QPushButton, "pushButton_34")
                        if button_34:
                            button_34.setEnabled(True)
                    self.traer_id_thread.resultado.connect(on_id_obtenido)
                    self.traer_id_thread.start()


                else:
                    print("No se encontró el proveedor en la base de datos")
                        
                if input_nombre:
                    input_nombre.setFocus()
            self.buscar_prov_thread.resultado.connect(on_busqueda_finalizada)
            self.buscar_prov_thread.start()
        else:
            if button_34:
                button_34.setEnabled(True)
            # No existe en cache
            lineEdit_20 = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")
            if lineEdit_20:
                lineEdit_20.clear()
            label_77 = self.ui.frame_12.findChild(QLabel, "label_77")
            if label_77:
                label_77.setText("Proveedor no encontrado")
                label_77.setStyleSheet("color: red; font-weight: bold")
                
            if input_nombre:
                input_nombre.setFocus()

################
################
    # editar proveedor
    
    def editar_proveedor(self):
        combobox_nombre = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if combobox_nombre:
            combobox_nombre.setEditable(True)
            combobox_nombre.setInsertPolicy(QComboBox.NoInsert)
            combobox_nombre.setCompleter(None)
            combobox_nombre.lineEdit().textEdited.connect(lambda text: self.filter_combobox_proveedores_todo_su_contenido(combobox_nombre, text))
            combobox_nombre.lineEdit().textChanged.connect(self.load_proveedor_data)
            self.populate_combobox_with_proveedores(combobox_nombre)
            combobox_nombre.setFocus()
            combobox_nombre.lineEdit().selectAll()

        button_37 = self.ui.frame_13.findChild(QPushButton, "pushButton_37")
        if button_37:
            button_37.setStyleSheet("background-color: rgb(255, 202, 96)")
            button_37.setShortcut(Qt.Key_Return)
            button_37.clicked.connect(self.update_proveedor)

        button_38 = self.ui.frame_13.findChild(QPushButton, "pushButton_38")
        if button_38:
            button_38.clicked.connect(self.cancel_edit_proveedor)
            

        label_78 = self.ui.frame_13.findChild(QLabel, "label_78")
        if label_78:
            label_78.setStyleSheet("color: transparent")
        label_79 = self.ui.frame_13.findChild(QLabel, "label_79")
        if label_79:
            label_79.setStyleSheet("color: transparent")

    def cancel_edit_proveedor(self):
        combobox_nombre = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if combobox_nombre:
            combobox_nombre.setFocus()
        self.load_proveedor_data()

    def update_proveedor(self):
        global usuario_activo, proveedor_selecc

        button_37 = self.ui.frame_13.findChild(QPushButton, "pushButton_37")
        if button_37:
            button_37.setEnabled(False)
        button_38 = self.ui.frame_13.findChild(QPushButton, "pushButton_38")
        if button_38:
            button_38.setEnabled(False)

        combobox_nombre = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        lineEdit_28 = self.ui.frame_13.findChild(QLineEdit, "lineEdit_28")
        lineEdit_26 = self.ui.frame_13.findChild(QLineEdit, "lineEdit_26")
        comboBox_value = combobox_nombre.currentText()
        lineEdit_28_value = lineEdit_28.text().strip()
        lineEdit_26_value = lineEdit_26.text().strip()

        label_78 = self.ui.frame_13.findChild(QLabel, "label_78")
        label_79 = self.ui.frame_13.findChild(QLabel, "label_79")

        if comboBox_value and lineEdit_28_value.isdigit():
            if (lineEdit_28_value != str(proveedor_selecc[0][1]) or lineEdit_26_value != str(proveedor_selecc[0][2])) and comboBox_value == proveedor_selecc[0][0]:
                if label_78 and label_79:
                            label_78.setText("Actualizando")
                            label_78.setStyleSheet("color: green; font-weight: bold")
                            label_79.setText("proveedor...")
                            label_79.setStyleSheet("color: green; font-weight: bold")

                self.actualizar_prov_thread = ActualizarProveedorThread(comboBox_value, lineEdit_28_value, lineEdit_26_value)
                def on_actualizado(exito):
                    label_78 = self.ui.frame_13.findChild(QLabel, "label_78")
                    label_79 = self.ui.frame_13.findChild(QLabel, "label_79")
                    button_38 = self.ui.frame_13.findChild(QPushButton, "pushButton_38")
                    button_37 = self.ui.frame_13.findChild(QPushButton, "pushButton_37")

                    if exito:
                        self.movimiento_editado_thread = MovimientoProveedorEditadoThread(comboBox_value, usuario_activo)
                        self.movimiento_editado_thread.start()

                        if label_78 and label_79:
                            label_78.setText("Proveedor actualizado")
                            label_78.setStyleSheet("color: green; font-weight: bold")
                            label_79.setText("con éxito")
                            label_79.setStyleSheet("color: green; font-weight: bold")
                            QTimer.singleShot(6000, lambda: label_78.setStyleSheet("color: transparent"))
                            QTimer.singleShot(6000, lambda: label_79.setStyleSheet("color: transparent"))
                        

                        #limpiar cache de proveedores
                        global proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
                        proveedores_cache = None
                        proveedores_por_nombre_cache = None
                        proveedores_por_telefono_cache = None

                        #actualizar cache tablas y comboboxes
                        self.actualizar_variables_globales_de_uso(2, lambda: (
                            self.populate_combobox_with_proveedores(self.ui.frame_7.findChild(QComboBox, "comboBox_7")),
                            self.populate_table_with_proveedores(),
                            self.populate_combobox_proveedores(),
                            self.proveedores()
                        ))
                        self.clear_inputs_editar_proveedores()

                        if button_37:
                            button_37.setEnabled(True)
                        if button_38:
                            button_38.setEnabled(True)
                        
                    else:
                        print("se genero un error al actualizar el proveedor")
                            
                self.actualizar_prov_thread.resultado.connect(on_actualizado)
                self.actualizar_prov_thread.start()
            else:

                if button_37:
                    button_37.setEnabled(True)
                if button_38:
                    button_38.setEnabled(True)

                if label_78 and label_79:
                    label_78.setText("Por favor, edite")
                    label_78.setStyleSheet("color: red; font-weight: bold")
                    label_79.setText("los campos")
                    label_79.setStyleSheet("color: red; font-weight: bold")
        else:
            if button_37:
                button_37.setEnabled(True)
            if button_38:
                button_38.setEnabled(True)

            if label_78 and label_79:
                label_78.setText("Por favor, complete todos")
                label_78.setStyleSheet("color: red; font-weight: bold")
                label_79.setText("los campos correctamente")
                label_79.setStyleSheet("color: red; font-weight: bold")
                
            if not comboBox_value:
                combobox_nombre.setFocus()
            elif not lineEdit_28_value.isdigit():
                lineEdit_28.setFocus()

    def clear_inputs_editar_proveedores(self):
        lineEdit_28 = self.ui.frame_13.findChild(QLineEdit, "lineEdit_28")
        lineEdit_26 = self.ui.frame_13.findChild(QLineEdit, "lineEdit_26")
        comboBox_11 = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if lineEdit_28 and lineEdit_26:
            lineEdit_28.clear()
            lineEdit_26.clear()
            comboBox_11.clear()
            comboBox_11.setFocus()

    def filter_combobox_proveedores_todo_su_contenido(self, combobox, text):
        global proveedores

        combobox.clear()
        for proveedor in proveedores:
            combobox.addItem(proveedor[0])  # Solo el nombre
        combobox.setCurrentText(text)

    def load_proveedor_data(self):
        global proveedores_por_nombre_cache, proveedor_selecc

        label_78 = self.ui.frame_13.findChild(QLabel, "label_78")
        label_79 = self.ui.frame_13.findChild(QLabel, "label_79")
        combobox_nombre = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if combobox_nombre and (combobox_nombre.currentText() != ""):
            selected_nombre = combobox_nombre.lineEdit().text().strip()
            if selected_nombre and proveedores_por_nombre_cache and selected_nombre.lower() in proveedores_por_nombre_cache:
                proveedor_selecc = [proveedores_por_nombre_cache[selected_nombre.lower()]]
                if label_78 and label_79:
                    label_78.setText("Proveedor")
                    label_78.setStyleSheet("color: green; font-weight: bold")
                    label_79.setText("existente")
                    label_79.setStyleSheet("color: green; font-weight: bold")
                    
                self.ui.frame_13.findChild(QComboBox, "comboBox_11").setCurrentText(proveedor_selecc[0][0])
                self.ui.frame_13.findChild(QLineEdit, "lineEdit_28").setText(str(proveedor_selecc[0][1]))
                self.ui.frame_13.findChild(QLineEdit, "lineEdit_26").setText(str(proveedor_selecc[0][2]))
            else:
                try:
                    self.ui.frame_13.findChild(QLineEdit, "comboBox_11").clear()    
                    self.ui.frame_13.findChild(QLineEdit, "lineEdit_28").clear()
                    self.ui.frame_13.findChild(QLineEdit, "lineEdit_26").clear()
                except:
                    if label_78 and label_79:
                        label_78.setText("Seleccione o escriba")
                        label_78.setStyleSheet("color: red; font-weight: bold")
                        label_79.setText("un proveedor válido")
                        label_79.setStyleSheet("color: red; font-weight: bold")


################
################

    # visualizar proveedores

    def visualizar_proveedores(self):

        
        self.populate_table_with_proveedores()

        # Conectar el QLineEdit para filtrar productos
        line_edit = self.ui.frame_18.findChild(QLineEdit, "lineEdit_27")
        if line_edit:
            line_edit.textChanged.connect(self.filter_proveedores)

    def populate_table_with_proveedores(self):
        global proveedores
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
        if table_widget:
            table_widget.setRowCount(len(proveedores))
            table_widget.setColumnCount(3)
            table_widget.setHorizontalHeaderLabels(["Nombre", "Teléfono", "Email"])
            header = table_widget.horizontalHeader()
            header.setFont(QFont("Segoe UI", 16, QFont.Bold))
            for row, proveedor in enumerate(proveedores):
                for col, value in enumerate(proveedor[:3]):  # Solo nombre, teléfono, email
                    item = QTableWidgetItem(str(value))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(row, col, item)

    def filter_proveedores(self):
        global proveedores
        line_edit = self.ui.frame_16.findChild(QLineEdit, "lineEdit_27")
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")

        if line_edit and table_widget:
            filter_text = line_edit.text().lower()

            filtered_proveedores = []
            for proveedor in proveedores:
                if filter_text in proveedor[0].lower() or filter_text in str(proveedor[1]).lower():
                    filtered_proveedores.append(proveedor)

            # Si no se encuentran proveedores, mostrar un mensaje en la tabla
            if len(filtered_proveedores) == 0:
                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron proveedores")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                # Si hay proveedores, llenar la tabla con los datos filtrados
                table_widget.setRowCount(len(filtered_proveedores))
                table_widget.setColumnCount(3)  # Solo nombre, teléfono, email
                table_widget.setHorizontalHeaderLabels(["Nombre", "Teléfono", "Email"])
                for row, proveedor in enumerate(filtered_proveedores):
                    for col, value in enumerate(proveedor[:3]):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))
                        item.setTextAlignment(Qt.AlignCenter)
                        table_widget.setItem(row, col, item)
    
    
    # Función para copiar una fila al portapapeles
    def copy_row_to_clipboard_proveedores(self, row_index):
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

    def copy_entire_table_to_clipboard_proveedores(self):
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
        if not table_widget:
            return
        row_count = table_widget.rowCount()
        col_count = table_widget.columnCount()
        # Copiar encabezados
        headers = [table_widget.horizontalHeaderItem(col).text() for col in range(col_count)]
        data = ['\t'.join(headers)]
        # Copiar filas
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = table_widget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append('\t'.join(row_data))
        # Copiar al portapapeles
        clipboard = QApplication.clipboard()
        clipboard.setText('\n'.join(data))
        self.show_copied_message("Tabla copiada al portapapeles")



################
################





class BuscarDatosTab:
    def __init__(self, ui):
        self.ui = ui

class AdministracionTab:
    def __init__(self, ui, buscar_datos_tab, datos_tab):
        self.ui = ui

    def open_facturero_ventas(self):
        pass

    def open_facturero_compras(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self, usuario, account):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.save_timer = QTimer()  # Inicializar el temporizador
        self.save_timer.setSingleShot(True)  # Asegurarse de que solo se ejecute una vez por evento
        self.usuario = usuario # trae el usuario que inciio sesion
        self.account = account # trae el tipo de cuenta que tiene el usuario
        self.setMinimumSize(1180, 800)

        global usuario_activo
        usuario_activo = self.usuario # se inicializa la variable global usuario para que sea la misma que la del mainwindow
        
        # Establece el icono y el título de la ventana principal
        self.setWindowIcon(QIcon("C:/Users/mariano/Desktop/proyectos/minimarketclass(Pyside)/archivos_py/resources/r.ico"))
        self.setWindowTitle("rls")  

        # Cambia las tab si es usuario
        tab_widget = self.ui.tabWidget
        if tab_widget:
            if account == "Administrador":
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_1), "Datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_3), "Buscar datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab), "Administración")
            else:
                tab_widget.setTabVisible(tab_widget.indexOf(self.ui.tab_1), False)
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_3), "Buscar datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab), "Administración")

        # Crear instancias de las clases de las pestañas
        self.buscar_datos_tab = BuscarDatosTab(self.ui)
        self.datos_tab = DatosTab(self.ui)
        self.administracion_tab = AdministracionTab(self.ui, self.buscar_datos_tab,  self.datos_tab)  # Inicialización de administracion_tab

        #establece inicio rls
        stacked_widget = self.ui.stackedWidget
        if stacked_widget:
            stacked_widget.setCurrentIndex(2)  # Establece la página que se debe ver primero

        # Conectar botones 
        self.connect_buttons(stacked_widget)

    
    # Muestra la página correspondiente en el stacked widget
    def connect_button(self, button_name, stacked_widget, page_index, extra_action=None):
        button = self.findChild(QPushButton, button_name)
        if button:  
            button.clicked.connect(lambda: self.show_page(stacked_widget, page_index))
            if extra_action:
                button.clicked.connect(extra_action)

    #mostrar la página en el stacked widget
    def show_page(self, stacked_widget, page_index):
        stacked_widget.setCurrentIndex(page_index)

    #conectar botones a pestañas
    def connect_buttons(self, stacked_widget):
        # VENTANA DE DATOS

        # Botón visualizar productos
        button = self.findChild(QPushButton, "pushButton")
        if button:
            button.setStyleSheet("background-color: rgb(226, 245, 255)")
            button.clicked.connect(self.change_table_headers_color_visualizar_productos)
            self.connect_button("pushButton", stacked_widget, 0, lambda: self.focus_visualziar_prod())
            

        self.connect_button("pushButton_5", stacked_widget, 9, lambda: self.focus_visualizar_prov())
        self.connect_button("pushButton_4", stacked_widget, 3, lambda: self.focus_borrar_prod())
        self.connect_button("pushButton_2", stacked_widget, 4, lambda: self.focus_editar_prod())

        # Botón visualizar proveedores
        button5 = self.findChild(QPushButton, "pushButton_5")
        if button5:
            button5.setStyleSheet("background-color: rgb(226, 245, 255)")

        # Agregar productos
        self.connect_button("pushButton_3", stacked_widget, 5, lambda: self.focus_agregar_prod())
     

        self.connect_button("pushButton_8", stacked_widget, 6,  lambda: self.focus_agregar_proveedor())
        self.connect_button("pushButton_7", stacked_widget, 7, lambda: self.focus_borrar_proveedor())
        self.connect_button("pushButton_6", stacked_widget, 8,  lambda: self.focus_editar_proveedor())
        self.connect_button("pushButton_9", stacked_widget, 1,  lambda: self.focus_agregar_categoria())
        self.connect_button("pushButton_10", stacked_widget, 10, lambda: self.focus_borrar_categoria())

        # Visualizar categorías
        button11 = self.findChild(QPushButton, "pushButton_11")
        if button11:
            button11.setStyleSheet("background-color: rgb(226, 245, 255)")
            self.connect_button("pushButton_11", stacked_widget, 11,  lambda: self.focus_visualizar_categorias())

        # Botón borrar datos
        button12 = self.findChild(QPushButton, "pushButton_12")
        if button12:
            button12.setStyleSheet("background-color: red")
            self.connect_button("pushButton_12", stacked_widget, 12)

        #agregar usuario
        button_14 = self.findChild(QPushButton, "pushButton_14")
        if button_14:
            self.connect_button("pushButton_14", stacked_widget, 16, lambda: self.focus_agregar_usuario())

        # editar usuario
        button_18 = self.findChild(QPushButton, "pushButton_18")
        if button_18:
            self.connect_button("pushButton_18", stacked_widget, 17, lambda: self.focus_nombre_usuario())
        
        #borrar usuario
        button_22 = self.findChild(QPushButton, "pushButton_22")
        if button_22:
            self.connect_button("pushButton_22", stacked_widget, 18, lambda : self.focus_borrar_usuario())

        # VENTANA BUSCAR DATOS

        self.connect_button("pushButton_15", stacked_widget, 13)
        self.connect_button("pushButton_13", stacked_widget, 14)
        self.connect_button("pushButton_48", stacked_widget, 19)
        push_button_48 = self.findChild(QPushButton, "pushButton_48")
        if push_button_48:
            push_button_48.setIcon(QIcon("C:/Users/mariano/Desktop/proyectos/minimarketclass(Pyside)/archivos_py/resources/eye_visible_hide_hidden_show_icon_145988.png"))

 
        # VENTANA ADMINISTRACION

        # Botón facturero ventas
        button16 = self.findChild(QPushButton, "pushButton_16")
        if button16:
            button16.setStyleSheet("background-color: rgb(198, 255, 202)")
            self.connect_button("pushButton_16", stacked_widget, 15, self.administracion_tab.open_facturero_ventas)
            button16.clicked.connect(self.change_table_headers_color_ventas)

        # Botón facturero compras
        button17 = self.findChild(QPushButton, "pushButton_17")
        if button17:
            button17.setStyleSheet("background-color: rgb(255, 230, 107)")
            self.connect_button("pushButton_17", stacked_widget, 15, self.administracion_tab.open_facturero_compras)
            button17.clicked.connect(self.change_table_headers_color_compras)

    #####FOCUS A LOS CAMPOS PRINCIPALES PARA ESCRIBIR APENAS SE ABRE LA FUNCION DESEADA

    def focus_agregar_prod(self):
         # Buscar el line_edit_7 en el frame correspondiente
        line_edit_7 = self.ui.frame_5.findChild(QLineEdit, "lineEdit_7")
        if line_edit_7:
            line_edit_7.setFocus()  # Establecer el foco

    def focus_borrar_prod(self):
         # Buscar el line_edit_7 en el frame correspondiente
        line_edit_2 = self.ui.frame_6.findChild(QLineEdit, "lineEdit_2")
        if line_edit_2:
            line_edit_2.setFocus()  # Establecer el foco

    def focus_editar_prod(self):
        combobox_id = self.ui.frame_7.findChild(QComboBox, "comboBox_3")
        if combobox_id:
            combobox_id.setFocus()

    def focus_visualziar_prod(self):
        line_edit1 = self.ui.frame_2.findChild(QLineEdit, "lineEdit1")
        if line_edit1:
            line_edit1.setFocus()

    def focus_agregar_proveedor(self):
        line_edit_14 = self.ui.frame_10.findChild(QLineEdit, "lineEdit_14")
        if line_edit_14:
            line_edit_14.setFocus()

    def focus_borrar_proveedor(self):
        lineEdit_20 = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")
        if lineEdit_20:
            lineEdit_20.setFocus()

    def focus_editar_proveedor(self):
        combobox_11 = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if combobox_11:
            combobox_11.setFocus()
            

    def focus_visualizar_prov(self):
        line_edit_27 = self.ui.frame_16.findChild(QLineEdit, "lineEdit_27")
        if line_edit_27:
            line_edit_27.setFocus()


    def focus_agregar_categoria(self):
        lineedit_16 = self.ui.frame_17.findChild(QLineEdit, "lineEdit_16")
        if lineedit_16:
            lineedit_16.setFocus()

    def focus_borrar_categoria(self):
        line_edit_21 = self.ui.frame_20.findChild(QLineEdit, "lineEdit_21")
        if line_edit_21:
            line_edit_21.setFocus()

    def focus_visualizar_categorias(self):
        lineEdit_19 = self.ui.frame_26.findChild(QLineEdit, "lineEdit_19")
        if lineEdit_19:
            lineEdit_19.setFocus()

    def focus_nombre_usuario(self):
        combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
        if combobox_16:
            combobox_16.setFocus()

    def focus_agregar_usuario(self):
        line_edit_23 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_23")
        if line_edit_23:
            line_edit_23.setFocus()

    def focus_borrar_usuario(self):
        line_edit_29 = self.ui.frame_47.findChild(QLineEdit, "lineEdit_29")
        if line_edit_29:
            line_edit_29.setFocus()

    
    #####    

    def change_table_headers_color_visualizar_categorias(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_3")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
            }
            """)

            
    def change_table_headers_color_visualizar_proveedores(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_2")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
            }
            """)

    def change_table_headers_color_visualizar_productos(self):
        table_widget = self.findChild(QTableWidget, "tableWidget")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
            }
            """)
        

    def change_table_headers_color_ventas(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_4")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(198, 255, 202);
                color: black;
            }
            """)

    def change_table_headers_color_compras(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_4")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(255, 230, 107);
                color: black;
            }
            """)
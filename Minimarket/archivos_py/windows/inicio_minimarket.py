from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QDialog, QVBoxLayout, QComboBox, QTableWidget, QLabel, QDoubleSpinBox, QTableWidgetItem, QApplication, QAbstractButton, QMessageBox, QCheckBox, QDateEdit, QTextEdit, QWidget
from PySide6.QtCore import QTimer, Qt, QDate
from PySide6.QtGui import QIcon, QFont, QIntValidator
from archivos_py.ui.minimarket import Ui_MainWindow
from archivos_py.ui.ventana_facturero_ventas import Ui_Form_ventas as Ui_VentanaFactureroVentas
from archivos_py.ui.ventana_agregar_metodo_de_pago import Ui_Form_agregar_mp as Ui_Dialog
from archivos_py.ui.ventana_borrar_metodo_de_pago import Ui_Form_borrar_mp as Ui_Dialog2
from archivos_py.ui.ventana_facturero_compras  import Ui_Form_compras as Ui_VentanaFactureroCompras
from archivos_py.threads.db_thread_minimarket import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from datetime import datetime, timedelta
import copy
import pytz 
from archivos_py.db.sesiones import SessionManager
from uuid import uuid4

# ------------ VARIABLES DE CACHE GLOBALES ------------
categorias_cache = None
proveedores_cache = None
productos_cache = None
usuarios_cache = None
metodos_pago_cache = None


productos_cache_temporal = None
productos_por_id_cache = None
productos_por_nombre_cache = None
proveedores_por_nombre_cache = None
proveedores_por_telefono_cache = None
categorias_por_nombre_cache = None
usuarios_por_nombre_cache = None
metodos_pago_por_id_cache = None


# -----------------------------------------------------

# 
class DatosTab:
    def __init__(self, ui):
        self.ui = ui
        self.button19_connected = False
        self.button34_connected = False
        self.button_agregar = False
        self.delete_data = False

        global usuario_activo

        #crear arreglo con threads abiertos
        self.threads = []

        self.mp_verificados = False

        if not self.mp_verificados:
            self.verificar_mp_thread = VerificarYAgregarMPThread()
            def on_mp_verificado():
    
                self.mp_verificados = True
            self.verificar_mp_thread.finished.connect(on_mp_verificado)
            self.start_thread(self.verificar_mp_thread)

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
        
        # Conectar eventos de doble clic para copiar al portapapeles
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if table_widget:
            corner_button = table_widget.findChild(QAbstractButton)

            corner_button.clicked.connect(self.copy_entire_table_to_clipboard)
            table_widget.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard)
            table_widget.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard)
            table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

        #-----------------------

        # agregar proveedores

        self.agregar_proveedor()

        # borrar proveedores
        self.borrar_proveedor()

        # editar proveedores
        self.editar_proveedor()

        # visualizar proveedores
        self.visualizar_proveedores()

        # Conectar eventos de doble clic
        table_widget2 = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
        if table_widget2:
            corner_button2 = table_widget2.findChild(QAbstractButton)

            corner_button2.clicked.connect(self.copy_entire_table_to_clipboard_proveedores)
            table_widget2.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard_proveedores)
            table_widget2.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard_proveedores)
            table_widget2.setEditTriggers(QTableWidget.NoEditTriggers)

        #-----------------------

        # agregar categorias
        self.agregar_categoria()

        # borrar categorias
        self.borrar_categoria()

        # visualizar categorias
        self.visualizar_categorias()

        # Conectar eventos de doble clic
        table_widget3 = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")
        if table_widget3:
            corner_button3 = table_widget3.findChild(QAbstractButton)

            corner_button3.clicked.connect(self.copy_entire_table_to_clipboard_categorias)
            table_widget3.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard_categorias)
            table_widget3.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard_categorias)
            table_widget3.setEditTriggers(QTableWidget.NoEditTriggers)

        # ----------------------

        # funcion de admin de usuarios
        
        self.agregar_usuario()

        self.editar_usuario()

        self.borrar_usuario()

        # ----------------------

        # mostrar usuario
        global usuario_activo
        self.mostrar_usuario_activo(usuario_activo)

        # ----------------------


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
        global categorias , proveedores, productos, usuarios, metodos_pago
     
        global categorias_cache, proveedores_cache, productos_cache
        global productos_por_id_cache, productos_por_nombre_cache
        global proveedores_por_nombre_cache, proveedores_por_telefono_cache
        global categorias_por_nombre_cache, usuarios_por_nombre_cache, metodos_pago_por_id_cache, metodos_pago_cache
        global anios_obtenidos
        
        self.anios_thread = TraerAnios()
        def on_anios_obtenidos(anios):
            global anios_obtenidos
            anio_actual = datetime.now().year
            # Asegurarse de que el año actual esté presente
            if anio_actual not in anios:
                anios.append(anio_actual)
            anios = sorted(set(anios))  # Opcional: ordena y elimina duplicados
            anios_obtenidos = anios

        self.anios_thread.resultado.connect(on_anios_obtenidos)
        self.start_thread(self.anios_thread)


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
        if r == 4 and usuarios_cache is not None:
            usuarios = usuarios_cache
            if callback:
                callback()
            return

        if r == 5 and metodos_pago_cache is not None:
            metodos_pago = metodos_pago_cache
            if callback:
                callback()  
            return


        if r == 0:
            self._datos_cargados = {"categorias": False, "proveedores": False, "productos": False, "usuarios": False, "metodos_pago": False}

            def check_all_loaded():
                if all(self._datos_cargados.values()):
                    if callback:
                        callback()

            # obetener todos los metodos de pago al iniciar
            self.metodos_pago_thread = TraerMetodosPagoYSuIdThread()
            def on_metodos_obtenidos(metodos):
                global metodos_pago_cache, metodos_pago_por_id_cache
                
                metodos_pago_cache = metodos
                metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos}
                self._datos_cargados["metodos_pago"] = True
                check_all_loaded()
                

            self.metodos_pago_thread.resultado.connect(on_metodos_obtenidos)
            self.start_thread(self.metodos_pago_thread)
           
            # Obtener todas las categorías y asignarlas a la variable global 'categorias'
            self.categorias_thread = CategoriasThread()
            def on_categorias_obtenidas(cats):
                global categorias, categorias_por_nombre_cache
                categorias = cats
                categorias_por_nombre_cache = {c[1].strip().lower(): c for c in categorias}
                self._datos_cargados["categorias"] = True
                check_all_loaded()
                
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
                
            self.productos_thread.resultado.connect(on_productos_obtenidos)
            self.start_thread(self.productos_thread)

            # obtener todos los usuarios
            self.usuarios_thread = TraerTodosLosUsuariosThread()
            def on_usuarios_obtenidos(usuarios_obtenidos):
                global usuarios, usuarios_por_nombre_cache
                usuarios = usuarios_obtenidos
                usuarios_por_nombre_cache = {u[1].strip(): u for u in usuarios}
                self._datos_cargados["usuarios"] = True
                check_all_loaded()
                
            self.usuarios_thread.resultado.connect(on_usuarios_obtenidos)
            self.start_thread(self.usuarios_thread)

        else:
            if r == 1:
                # Obtener todas las categorías y asignarlas a la variable global 'categorias'
                self.categorias_thread = CategoriasThread()
                def on_categorias_obtenidas(cats):
                    global categorias, categorias_cache, categorias_por_nombre_cache
                    categorias = cats
                    categorias_cache = cats
                    categorias_por_nombre_cache = {c[1].strip().lower(): c for c in categorias}
                
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
                
                    if callback:
                        callback()
                self.productos_thread.resultado.connect(on_productos_obtenidos)
                self.start_thread(self.productos_thread)
            elif r == 4:
                 # obtener todos los usuarios
                self.usuarios_thread = TraerTodosLosUsuariosThread()
                def on_usuarios_obtenidos(usuarios_obtenidos):
                    global usuarios, usuarios_por_nombre_cache
                    usuarios = usuarios_obtenidos
                    usuarios_por_nombre_cache = {u[1].strip(): u for u in usuarios}
                    
                    if callback:
                        callback()
                self.usuarios_thread.resultado.connect(on_usuarios_obtenidos)
                self.start_thread(self.usuarios_thread)

            elif r == 5:
                # Obtener todos los métodos de pago y asignarlos a la variable global 'metodos_pago'
                self.metodos_pago_thread = TraerTodosLosMetodosPagoThread()
                def on_metodos_pago_obtenidos(metodos_obtenidos):
                    global metodos_pago, metodos_pago_cache, metodos_pago_por_id_cache
                    metodos_pago = metodos_obtenidos
                    metodos_pago_cache = metodos_obtenidos
                    metodos_pago_por_id_cache = {str(m[0]): m for m in metodos_pago}
                    
                    if callback:
                        callback()
                self.metodos_pago_thread.resultado.connect(on_metodos_pago_obtenidos)
                self.start_thread(self.metodos_pago_thread)

        #################
        #################


    # AGREGAR PRODUCTOS

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
            input_categoria.addItem(f"{i[1]}")

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


    def on_producto_agregado(self, exito, input_id_value, usuario_activo, input_id):
        label_70 = self.ui.frame_5.findChild(QLabel, "label_70")
        label_71 = self.ui.frame_5.findChild(QLabel, "label_71")
        button19 = self.ui.frame_5.findChild(QPushButton, "pushButton_19")
        button20 = self.ui.frame_5.findChild(QPushButton, "pushButton_20")

        if exito:
            
            # Usar hilo para cargar el movimiento
            self.movimiento_thread = MovimientoProductoThread(input_id_value, usuario_activo)
            self.start_thread(self.movimiento_thread)
    
            # Limpiar solo el cache de productos antes de actualizar
            global productos_cache, productos_por_id_cache
            productos_cache = None
            productos_por_id_cache = None
    
            self.actualizar_variables_globales_de_uso(3, lambda: (
                self.populate_table_with_products(),
                self.populate_combobox_with_ids(self.ui.frame_7.findChild(QComboBox, "comboBox_3"))
            ))

            if input_id:
                input_id.setFocus()
                QTimer.singleShot(2000, lambda: input_id.setFocus())

            #actualizar combobox id de editar productos

            self.clear_inputs_agregar_productos()
                
            if label_70 and label_71:
                label_70.setText("Producto cargado")
                label_71.setText("con éxito!")
                label_70.setStyleSheet("color: green; font-weight: bold")
                label_71.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_70.setStyleSheet("color: transparent"))
                QTimer.singleShot(6000, lambda: label_71.setStyleSheet("color: transparent"))

            if button19:
                button19.setEnabled(True)
            if button20:
                button20.setEnabled(True)

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

                if self.show_delete_product_warning(self._borrar_nombre):
                    self._on_nombre_obtenido(self._borrar_nombre)
                else:
                    if button21:
                        button21.setEnabled(True)
                    if label_72:
                        label_72.setText("Operación cancelada")
                        label_72.setStyleSheet("color: blue; font-weight: bold")
                    input_nombre_o_id.setFocus()
                return
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
                if self.show_delete_product_warning(self._borrar_nombre):
                    self._on_nombre_obtenido(self._borrar_nombre)
                else:
                    if button21:
                        button21.setEnabled(True)
                    if label_72:
                        label_72.setText("Operación cancelada")
                        label_72.setStyleSheet("color: blue; font-weight: bold")
                    input_nombre_o_id.setFocus()
                return
            
            else:
                if button21:
                    button21.setEnabled(True)
                if label_72:
                    label_72.setText("Producto no encontrado")
                    label_72.setStyleSheet("color: red; font-weight: bold")
                input_nombre_o_id.setFocus()


    def show_delete_product_warning(self, nombre_producto):
        msg = QMessageBox(self.ui.frame_6)
        msg.setWindowTitle("ADVERTENCIA!")
        msg.setIcon(QMessageBox.Warning)
        msg.setText(
            f"ADVERTENCIA!\n\n"
            f"Recomendación:\nUsted está a punto de borrar \"{nombre_producto}\".\n\n"
            "Si su petición de borrado es porque no va a usar más este producto, se recomienda NO borrarlo y simplemente setearlo sin categoría y sin proveedor/Proveedor1.\n\n"
            "Cada producto está ligado a su venta y compra, por lo que se verá afectado el historial de compras y ventas si usted lo quita."
        )
        msg.setStyleSheet("""
            QMessageBox {
                font-size: 18pt;
            }
            QLabel {
                font-size: 18pt;
                
            }
        """)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        # Personalizar los textos de los botones
        yes_button = msg.button(QMessageBox.Yes)
        no_button = msg.button(QMessageBox.No)
        if yes_button:
            yes_button.setText("Sí")
        if no_button:
            no_button.setText("No")
        respuesta = msg.exec()
        return respuesta == QMessageBox.Yes

    def _on_id_obtenido_nombre_ya_disponible(self, id_producto):
        self._borrar_id = id_producto
        # Ya tenemos el nombre, así que seguimos directo al borrado
        self._on_nombre_obtenido(self._borrar_nombre)

    def _on_nombre_obtenido(self, nombre_producto):
        if getattr(self, "_borrar_producto", False):
            return  # Ya está en proceso, no ejecutar de nuevo
        self._borrar_producto = True

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
            self._borrar_producto = False
            # Lanzar hilo de movimiento
            self.movimiento_thread = MovimientoProductoBorrarThread(self._borrar_id, self._borrar_nombre, usuario_activo)
            self.movimiento_thread.movimiento_borrado.connect(self.on_producto_borrado)
            self.start_thread(self.movimiento_thread)
        else:
            print("algo ocurrio que no se pudo borrar el producto")
            
    def on_producto_borrado(self):
          

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
                self.movimiento_thread.finished.connect(lambda: (self.load_product_data(), self.clear_doublespinbox_values(), pushbutton_49.setEnabled(True), boton_editar.setEnabled(True), boton_cancelar.setEnabled(True)))
                self.start_thread(self.movimiento_thread)

            else:
                if pushbutton_49:
                    pushbutton_49.setEnabled(True)
                if boton_editar:
                    boton_editar.setEnabled(True)
                if boton_cancelar:
                    boton_cancelar.setEnabled(True)
                

        self.aumentar_thread.finished.connect(on_aumento_finalizado)
        self.start_thread(self.aumentar_thread)

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
        self.movimiento_producto_editado_thread = MovimientoProductoEditadoThread(id, usuario_activo)
        self.start_thread(self.movimiento_producto_editado_thread)

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
            #self.populate_combobox_with_ids(self.ui.frame_7.findChild(QComboBox, "comboBox_3")),
            self.load_product_data(),
            self.populate_table_with_categorias(),
            self.populate_table_with_proveedores()
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
        nombres_categorias = [categoria[1] for categoria in categorias if self.texto.lower() in categoria[0].lower()]
        combobox.clear()
        for item in nombres_categorias:
            combobox.addItem(item)
        combobox.setCurrentText(text)

    def populate_combobox_with_categorias(self, combobox):
        combobox.clear()
        global categorias
        for categoria in categorias:
            combobox.addItem(categoria[1])
        
        
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
                combobox.addItem(categoria[1])

    def populate_table_with_products(self):
        table_widget = self.ui.frame_tabla_productos.findChild(QTableWidget, "tableWidget")
        if table_widget:
            global productos

            cantidad_productos = len(productos)

            if cantidad_productos == 0:
                label_121 = self.ui.frame_59.findChild(QLabel, "label_121")
                if label_121:
                    label_121.clear()
                    label_121.setText(f"0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_121 = self.ui.frame_59.findChild(QLabel, "label_121")
                if label_121:
                    label_121.clear()
                    label_121.setText(f"{cantidad_productos}")

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
                        combobox_2.clear()
                        filtered_productos.append(producto)

            cantidad_productos = len(filtered_productos)
            if cantidad_productos == 0:
                label_121 = self.ui.frame_59.findChild(QLabel, "label_121")
                if label_121:
                    label_121.clear()
                    label_121.setText(f"0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_121 = self.ui.frame_59.findChild(QLabel, "label_121")
                if label_121:
                    label_121.clear()
                    label_121.setText(f"{cantidad_productos}")

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
            if not self.button_agregar:
                self.button_agregar = True
                button_26.clicked.connect(self.validate_and_process_inputs_proveedores)

        button_25 = self.ui.frame_10.findChild(QPushButton, "pushButton_25")
        if button_25:
            button_25.clicked.connect(self.clear_inputs_agregar_proveedores)
        
        label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
        if label_75:
            label_75.setStyleSheet("color: transparent")

    
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
                label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
                if button_25:
                    button_25.setEnabled(True)
                if button_26:
                    button_26.setEnabled(True)

                if label_75:
                    label_75.setText("Está intentando cargar un proveedor o número existente")
                    label_75.setStyleSheet("color: red; font-weight: bold")
                     
                return
            else:
                if lineEdit_14_value and lineEdit_15_value.isdigit():
                    label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
                    label_75.setStyleSheet("color: green; font-weight: bold")
                    label_75.setText("Cargando Proveedor...")
                   
                    
                    self.proveedor_thread = ProveedorThread(lineEdit_14_value, lineEdit_15_value, lineEdit_17_value)
                    self.proveedor_thread.proveedor_cargado.connect(lambda exito: self.on_proveedor_cargado(exito, lineEdit_14_value))
                    self.start_thread(self.proveedor_thread)
                else:
                    if button_25:
                        button_25.setEnabled(True)
                    if button_26:
                        button_26.setEnabled(True)

                    label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
                    if label_75:
                        label_75.setStyleSheet("color: red; font-weight: bold")
                        label_75.setText("Por favor, complete todos los campos correctamente")
                        
                        
                    if not lineEdit_14_value:
                        lineEdit_14.setFocus()
                    elif not lineEdit_15_value.isdigit():
                        lineEdit_15.setFocus()
    

    def on_proveedor_cargado(self, exito, nombre_proveedor):
        global usuario_activo
        if exito:
            self.movimiento_proveedor_thread = MovimientoProveedorThread(nombre_proveedor, usuario_activo)
            self.start_thread(self.movimiento_proveedor_thread)
            #limpia inputs
            self.clear_inputs_agregar_proveedores()

            # actualiza proveedores
            global proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
            proveedores_cache = None
            proveedores_por_nombre_cache = None
            proveedores_por_telefono_cache = None
            self.actualizar_variables_globales_de_uso(2, lambda: (self.populate_combobox_with_proveedores(self.ui.frame_13.findChild(QComboBox, "comboBox_11")),
                self.populate_combobox_with_proveedores(self.ui.frame_7.findChild(QComboBox, "comboBox_7")),
                self.populate_table_with_proveedores(),
                self.proveedores()
            ))

            button_26 = self.ui.frame_10.findChild(QPushButton, "pushButton_26")
            button_25 = self.ui.frame_10.findChild(QPushButton, "pushButton_25")
            if button_26:
                button_26.setEnabled(True)
            if button_25:
                button_25.setEnabled(True)
                
            label_75 = self.ui.frame_10.findChild(QLabel, "label_75")
            if label_75:
                label_75.setText("Proveedor cargado con éxito")
                label_75.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_75.setStyleSheet("color: transparent"))

            
        else:
            print("se genero un error de tipeo al cargar el proveedor")


################
################

    #Borrar proveedor

    def borrar_proveedor(self):

        button_34 = self.ui.frame_12.findChild(QPushButton, "pushButton_34")
        if button_34:
            button_34.setStyleSheet("background-color: red; padding: 5px;")
            if not self.button34_connected:
                self.button34_connected = True
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
                lineEdit_20.selectAll()
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
                lineEdit_20.selectAll()
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
    
            # 1. Traer el ID primero
            def on_id_obtenido(id_proveedor):
                if id_proveedor:
                    # 2. Buscar en la base (puede tener lógica extra)
                    self.buscar_prov_thread = BuscarProveedorThread(input_nombre_value)
                    def on_busqueda_finalizada(bandera):
                        if bandera:
                            # 3. Cargar movimiento en hilo SOLO cuando ya tenemos el id_proveedor
                            self.movimiento_borrado_thread = MovimientoProveedorBorradoThread(input_nombre_value, id_proveedor, usuario_activo)
                            self.start_thread(self.movimiento_borrado_thread)
    
                            # actualizar cache, tablas y comboboxes
                            global proveedores_cache, proveedores_por_nombre_cache, proveedores_por_telefono_cache
                            proveedores_cache = None
                            proveedores_por_nombre_cache = None
                            proveedores_por_telefono_cache = None
    
                            self.actualizar_variables_globales_de_uso(2, lambda: (self.populate_combobox_with_proveedores(self.ui.frame_13.findChild(QComboBox, "comboBox_11")),
                                self.populate_combobox_with_proveedores(self.ui.frame_7.findChild(QComboBox, "comboBox_7")),
                                self.populate_table_with_proveedores(),
                                self.populate_combobox_proveedores(),
                                self.proveedores()
                            ))

                            global productos_cache, productos_por_id_cache, productos_por_nombre_cache
                            productos_cache = None
                            productos_por_id_cache = None
                            productos_por_nombre_cache = None

                            self.actualizar_variables_globales_de_uso(3, lambda: (
                                self.populate_table_with_products(),
                                
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
                        else:
                            print("No se encontró el proveedor en la base de datos")
                        if input_nombre:
                            input_nombre.setFocus()
                    self.buscar_prov_thread.resultado.connect(on_busqueda_finalizada)
                    self.start_thread(self.buscar_prov_thread)
                else:
                    # Si no se encontró el ID válido
                    if label_77:
                        label_77.setText("No se encontró el proveedor")
                        label_77.setStyleSheet("color: red; font-weight: bold")
                    if button_34:
                        button_34.setEnabled(True)
                    if input_nombre:
                        input_nombre.setFocus()
    
            self.traer_id_thread = TraerIdProveedorThread(input_nombre_value)
            self.traer_id_thread.resultado.connect(on_id_obtenido)
            self.start_thread(self.traer_id_thread)
        else:
            if button_34:
                button_34.setEnabled(True)
            # No existe en cache
            lineEdit_20 = self.ui.frame_12.findChild(QLineEdit, "lineEdit_20")
            if lineEdit_20:
                lineEdit_20.selectAll()
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
            
        label_76 = self.ui.frame_13.findChild(QLabel, "label_76")
        if label_76:
            label_76.setStyleSheet("color: transparent")

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

        label_76 = self.ui.frame_13.findChild(QLabel, "label_76")

        if comboBox_value and lineEdit_28_value.isdigit():
            if (lineEdit_28_value != str(proveedor_selecc[0][1]) or lineEdit_26_value != str(proveedor_selecc[0][2])) and comboBox_value == proveedor_selecc[0][0]:
                if label_76:
                    label_76.setStyleSheet("color: green; font-weight: bold")
                    label_76.setText("Actualizando")

                self.actualizar_prov_thread = ActualizarProveedorThread(comboBox_value, lineEdit_28_value, lineEdit_26_value)
                def on_actualizado(exito):
                    button_38 = self.ui.frame_13.findChild(QPushButton, "pushButton_38")
                    button_37 = self.ui.frame_13.findChild(QPushButton, "pushButton_37")

                    if exito:
                        self.movimiento_proveedor_editado_thread = MovimientoProveedorEditadoThread(comboBox_value, usuario_activo)
                        self.start_thread(self.movimiento_proveedor_editado_thread)

                        if label_76:
                            label_76.setStyleSheet("color: green; font-weight: bold")
                            label_76.setText("Proveedor actualizado con éxito")
                            QTimer.singleShot(6000, lambda: label_76.setStyleSheet("color: transparent"))
                        
                        if button_37 and button_38:
                            button_37.setEnabled(True)
                            button_38.setEnabled(True)

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
                            self.proveedores(),
                            self.load_proveedor_data()
                        ))

                        if button_37:
                            button_37.setEnabled(True)
                        if button_38:
                            button_38.setEnabled(True)
                        
                    else:
                        print("se genero un error al actualizar el proveedor")
                            
                self.actualizar_prov_thread.resultado.connect(on_actualizado)
                self.start_thread(self.actualizar_prov_thread)
            else:

                if button_37:
                    button_37.setEnabled(True)
                if button_38:
                    button_38.setEnabled(True)

                if label_76:
                    label_76.setText("No se realizaron cambios")
                    label_76.setStyleSheet("color: red; font-weight: bold")
                    QTimer.singleShot(6000, lambda: label_76.setStyleSheet("color: transparent"))
        else:
            if button_37:
                button_37.setEnabled(True)
            if button_38:
                button_38.setEnabled(True)

            if label_76:
                label_76.setStyleSheet("color: red; font-weight: bold")
                label_76.setText("Por favor, complete todos los campos correctamente")
                
                
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

        label_76 = self.ui.frame_13.findChild(QLabel, "label_76")
        
        combobox_nombre = self.ui.frame_13.findChild(QComboBox, "comboBox_11")
        if combobox_nombre and (combobox_nombre.currentText() != ""):
            selected_nombre = combobox_nombre.lineEdit().text().strip()
            if selected_nombre and proveedores_por_nombre_cache and selected_nombre.lower() in proveedores_por_nombre_cache:
                proveedor_selecc = [proveedores_por_nombre_cache[selected_nombre.lower()]]
                if label_76:
                    label_76.setStyleSheet("color: transparent")
                    label_76.setText("Proveedor existente")
                    
                self.ui.frame_13.findChild(QComboBox, "comboBox_11").setCurrentText(proveedor_selecc[0][0])
                self.ui.frame_13.findChild(QLineEdit, "lineEdit_28").setText(str(proveedor_selecc[0][1]))
                self.ui.frame_13.findChild(QLineEdit, "lineEdit_26").setText(str(proveedor_selecc[0][2]))
            else:
                try:
                    self.ui.frame_13.findChild(QLineEdit, "comboBox_11").clear()    
                    self.ui.frame_13.findChild(QLineEdit, "lineEdit_28").clear()
                    self.ui.frame_13.findChild(QLineEdit, "lineEdit_26").clear()
                except:
                    if label_76:
                        label_76.setStyleSheet("color: red; font-weight: bold")
                        label_76.setText("Seleccione o escriba un proveedor existente")
                        


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
        global proveedores, productos
        cantidad_proveedores = len(proveedores)

        label_124 = self.ui.frame_61.findChild(QLabel, "label_124")
        if label_124:
            label_124.clear()
            label_124.setText(f"{cantidad_proveedores}")

        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
        if table_widget:
            table_widget.setRowCount(len(proveedores))
            table_widget.setColumnCount(4)
            table_widget.setHorizontalHeaderLabels(["Nombre", "Teléfono", "Email", "Productos"])
            header = table_widget.horizontalHeader()
            header.setFont(QFont("Segoe UI", 16, QFont.Bold))
            for row, proveedor in enumerate(proveedores):
                for col, value in enumerate(proveedor[:3]):  # Solo nombre, teléfono, email
                    item = QTableWidgetItem(str(value))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(row, col, item)
                
                # Contar productos para este proveedor
                nombre_proveedor = proveedor[0]
                cantidad_productos = 0
                if productos:
                    for producto in productos:
                        if len(producto) > 7 and str(producto[7]) == nombre_proveedor:
                            cantidad_productos += 1
                
                # Agregar la cantidad de productos en la columna 3
                item_productos = QTableWidgetItem(str(cantidad_productos))
                item_productos.setFont(QFont("Segoe UI", 12))
                item_productos.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, 3, item_productos)

    def filter_proveedores(self):
        global proveedores, productos
        line_edit = self.ui.frame_16.findChild(QLineEdit, "lineEdit_27")
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")


        if line_edit and table_widget:
            filter_text = line_edit.text().lower()

            filtered_proveedores = []
            for proveedor in proveedores:
                if filter_text in proveedor[0].lower() or filter_text in str(proveedor[1]).lower():
                    filtered_proveedores.append(proveedor)

            cantidad_proveedores = len(filtered_proveedores)

            # Si no se encuentran proveedores, mostrar un mensaje en la tabla
            if cantidad_proveedores == 0:
                label_124 = self.ui.frame_61.findChild(QLabel, "label_124")
                if label_124:
                    label_124.clear()
                    label_124.setText(f"0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron proveedores")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_124 = self.ui.frame_61.findChild(QLabel, "label_124")
                if label_124:
                    label_124.clear()
                    label_124.setText(f"{cantidad_proveedores}")

                # Si hay proveedores, llenar la tabla con los datos filtrados
                table_widget.setRowCount(len(filtered_proveedores))
                table_widget.setColumnCount(4)  # Nombre, teléfono, email, productos
                table_widget.setHorizontalHeaderLabels(["Nombre", "Teléfono", "Email", "Productos"])
                for row, proveedor in enumerate(filtered_proveedores):
                    for col, value in enumerate(proveedor[:3]):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))
                        item.setTextAlignment(Qt.AlignCenter)
                        table_widget.setItem(row, col, item)
                    
                    # Contar productos para este proveedor filtrado
                    nombre_proveedor = proveedor[0]
                    cantidad_productos = 0
                    if productos:
                        for producto in productos:
                            if len(producto) > 7 and str(producto[7]) == nombre_proveedor:
                                cantidad_productos += 1
                    
                    # Agregar la cantidad de productos en la columna 3
                    item_productos = QTableWidgetItem(str(cantidad_productos))
                    item_productos.setFont(QFont("Segoe ui", 12))
                    item_productos.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(row, 3, item_productos)
    
    # Función para copiar una columna al portapapeles
    def copy_column_to_clipboard_proveedores(self, column_index):
        table_widget = self.ui.frame_tabla_productos_2.findChild(QTableWidget, "tableWidget_2")
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

    # agregar categoria

    def agregar_categoria(self):
        push_button_27 = self.ui.frame_17.findChild(QPushButton, "pushButton_27")
        if push_button_27:
            push_button_27.setStyleSheet("background-color: rgb(168, 225, 255)")
            push_button_27.setShortcut(Qt.Key_Return)
            push_button_27.clicked.connect(self.validate_and_process_inputs_categorias)

        push_button_28 = self.ui.frame_17.findChild(QPushButton, "pushButton_28")
        if push_button_28:
            push_button_28.clicked.connect(self.clear_inputs_agregar_categorias)

        #labels 
        label_80 = self.ui.frame_17.findChild(QLabel, "label_80")
        if label_80:
            label_80.setStyleSheet("color: transparent")

    def validate_and_process_inputs_categorias(self):
        if getattr(self, "_categoria_en_proceso", False):
            return  # Ya está en proceso, no ejecutar de nuevo
        self._categoria_en_proceso = True

        global usuario_activo

        lineEdit_16 = self.ui.frame_17.findChild(QLineEdit, "lineEdit_16")
        if lineEdit_16:
            lineEdit_16_value = lineEdit_16.text().strip()
        else:
            lineEdit_16_value = ""

        label_80 = self.ui.frame_17.findChild(QLabel, "label_80")

        if lineEdit_16_value:

            push_button_27 = self.ui.frame_17.findChild(QPushButton, "pushButton_27")
            push_button_28 = self.ui.frame_17.findChild(QPushButton, "pushButton_28")
            if push_button_27:
                push_button_27.setEnabled(False)

            if push_button_28:
                push_button_28.setEnabled(False)

            if label_80:
            
                label_80.setStyleSheet("color: green; font-weight: bold")

            self.cargar_categoria_thread = CargarCategoriaThread(lineEdit_16_value)
            def on_categoria_cargada(exito):

                if exito:
                    self._categoria_en_proceso = False

                    self.clear_inputs_agregar_categorias()
                    if label_80:
                        label_80.setText("Categoría cargada con exito")
                        label_80.setStyleSheet("color: green; font-weight: bold")
                        QTimer.singleShot(6000, lambda: label_80.setStyleSheet("color: transparent"))

                    # Hilo para cargar movimiento
                    self.movimiento_categoria_thread = MovimientoAgregarCategoriaThread(lineEdit_16_value, usuario_activo)
                    self.start_thread(self.movimiento_categoria_thread)

                    # actualziar variables globales de uso
                    global categorias_cache, categorias_por_nombre_cache
                    categorias_cache = None
                    categorias_por_nombre_cache = None

                    self.actualizar_variables_globales_de_uso(1, lambda: (
                        self.populate_combobox_with_categorias(self.ui.frame_7.findChild(QComboBox, "comboBox_4")),
                        self.populate_table_with_categorias(),
                        self.populate_combobox_categorias(),
                        self.categorias()
                    ))

                    push_button_27 = self.ui.frame_17.findChild(QPushButton, "pushButton_27")
                    push_button_28 = self.ui.frame_17.findChild(QPushButton, "pushButton_28")
                    if push_button_27:
                        push_button_27.setEnabled(True)

                    if push_button_28:
                        push_button_28.setEnabled(True)
                else:
                    self._categoria_en_proceso = False

                    push_button_27 = self.ui.frame_17.findChild(QPushButton, "pushButton_27")
                    push_button_28 = self.ui.frame_17.findChild(QPushButton, "pushButton_28")

                    if label_80:
                        label_80.setText("Esta intentando cargar una categoría existente")
                        label_80.setStyleSheet("color: red; font-weight: bold")
                    if push_button_27:
                        push_button_27.setEnabled(True)
                    if push_button_28:
                        push_button_28.setEnabled(True)

                    lineEdit_16 = self.ui.frame_17.findChild(QLineEdit, "lineEdit_16")
                    if lineEdit_16:
                        lineEdit_16.selectAll()
                        lineEdit_16.setFocus()
                        
            self.cargar_categoria_thread.resultado.connect(on_categoria_cargada)
            self.start_thread(self.cargar_categoria_thread)
        else:
            if label_80:
                label_80.setText("Por favor, complete el campo")
                label_80.setStyleSheet("color: red; font-weight: bold")
                
            if lineEdit_16:
                lineEdit_16.setFocus()


    def clear_inputs_agregar_categorias(self):
        lineEdit_16 = self.ui.frame_17.findChild(QLineEdit, "lineEdit_16")
        if lineEdit_16:
            lineEdit_16.clear()
            lineEdit_16.selectAll()


################
################

    # borrar categoria

    def borrar_categoria(self):
        lineEdit_21 = self.ui.frame_20.findChild(QLineEdit, "lineEdit_21")
        if lineEdit_21:
            lineEdit_21.setFocus()

        push_button_36 = self.ui.frame_20.findChild(QPushButton, "pushButton_36")
        if push_button_36:
            push_button_36.setStyleSheet("background-color: red; padding: 5px;")
            push_button_36.clicked.connect(self.delete_categoria)

        label_81 = self.ui.frame_20.findChild(QLabel, "label_81")
        if label_81:
            label_81.setStyleSheet("color: transparent")

    def delete_categoria(self):
        if getattr(self, "_borrar_categoria_en_proceso", False):
            return  # Ya está en proceso, no ejecutar de nuevo
        self._borrar_categoria_en_proceso = True

        global usuario_activo, categorias_por_nombre_cache
    
        lineEdit_21 = self.ui.frame_20.findChild(QLineEdit, "lineEdit_21")
        if lineEdit_21:
            lineEdit_21_value = lineEdit_21.text().strip()
        else:
            lineEdit_21_value = ""

        if lineEdit_21_value == "":
            if lineEdit_21:
                lineEdit_21.selectAll()
            label_81 = self.ui.frame_20.findChild(QLabel, "label_81")
            if label_81:
                label_81.setText("Por favor, complete el campo")
                label_81.setStyleSheet("color: red; font-weight: bold")
            return
    
        # Verificar existencia en el cache
        existe_categoria = categorias_por_nombre_cache and lineEdit_21_value.lower() in categorias_por_nombre_cache
        if existe_categoria:
            id_categoria = categorias_por_nombre_cache[lineEdit_21_value.lower()][0]
        else:
            id_categoria = None
    
        label_81 = self.ui.frame_20.findChild(QLabel, "label_81")
    
        if lineEdit_21_value != "Sin categoría":
            if id_categoria is None:
                if label_81:
                    label_81.setText("Categoría no encontrada")
                    label_81.setStyleSheet("color: red; font-weight: bold")
                if lineEdit_21:
                    lineEdit_21.selectAll()
                    lineEdit_21.setFocus()

                return
            
            
            push_button_36 = self.ui.frame_20.findChild(QPushButton, "pushButton_36")
            if push_button_36:
                push_button_36.setEnabled(False)
            
            if label_81:
                label_81.setText("Borrando categoría...")
                label_81.setStyleSheet("color: green; font-weight: bold")

            # Buscar la categoría en un hilo
            self.buscar_categoria_thread = BuscarCategoriaThread(lineEdit_21_value)
            def on_busqueda_finalizada(existe):
                if existe:
                    self._borrar_categoria_en_proceso = False
                
                    # Cargar movimiento en hilo
                    self.movimiento_categoria_thread = MovimientoCategoriaBorradaThread(lineEdit_21_value, id_categoria, usuario_activo)
                    self.start_thread(self.movimiento_categoria_thread)
    
                    # Limpiar cache de categorías
                    global categorias_cache, categorias_por_nombre_cache, categorias_por_id_cache
                    categorias_cache = None
                    categorias_por_nombre_cache = None
                    categorias_por_id_cache = None
                    # Actualizar cache, tablas y comboboxes
                    self.actualizar_variables_globales_de_uso(1, lambda: (
                        self.populate_combobox_with_categorias(self.ui.frame_7.findChild(QComboBox, "comboBox_4")),
                        self.populate_table_with_categorias(),
                        self.populate_combobox_categorias(),
                        self.categorias()
                    ))

                    global productos_cache, productos_por_nombre_cache, productos_por_id_cache
                    productos_cache = None
                    productos_por_nombre_cache = None
                    productos_por_id_cache = None
                    self.actualizar_variables_globales_de_uso(3, lambda: (
                        self.populate_table_with_products(),
                        
                    ))

                    lineEdit_21.clear()
                    if label_81:
                        label_81.setText("Categoría borrada con éxito")
                        label_81.setStyleSheet("color: green; font-weight: bold")
                        QTimer.singleShot(6000, lambda: label_81.setStyleSheet("color: transparent"))


                    push_button_36 = self.ui.frame_20.findChild(QPushButton, "pushButton_36")
                    if push_button_36:
                        push_button_36.setEnabled(True)

                else: 
                    self._borrar_categoria_en_proceso = False
                    print("No se encontró la categoría en la base de datos")

            self.buscar_categoria_thread.resultado.connect(on_busqueda_finalizada)
            self.start_thread(self.buscar_categoria_thread)

            lineEdit_21 = self.ui.frame_20.findChild(QLineEdit, "lineEdit_21")
            if lineEdit_21:
                lineEdit_21.clear()
                lineEdit_21.setFocus()
                QTimer.singleShot(2000, lambda: lineEdit_21.setFocus())
        else:
            lineEdit_21.clear()
            if label_81:
                label_81.setText("No se puede borrar la categoría 'Sin categoría'")
                label_81.setStyleSheet("color: red; font-weight: bold")
                

################
################

    # editar categoria


################
################

    # visualizar categorias
    def visualizar_categorias(self):
        self.populate_table_with_categorias()

        # Conectar el QLineEdit para filtrar productos
        line_edit = self.ui.frame_26.findChild(QLineEdit, "lineEdit_19")
        if line_edit:
            line_edit.textChanged.connect(self.filter_categorias)

    def populate_table_with_categorias(self):
        global categorias, productos
        cantidad_categorias = len(categorias)

        label_127 = self.ui.frame_62.findChild(QLabel, "label_127")
        if label_127:
            label_127.clear()
            label_127.setText(f"{cantidad_categorias}")

        table_widget = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")
        if table_widget:
            table_widget.setRowCount(len(categorias))
            table_widget.setColumnCount(2)
            table_widget.setHorizontalHeaderLabels(["Nombre", "Productos"])
            header = table_widget.horizontalHeader()
            header.setFont(QFont("Segoe UI", 16, QFont.Bold))
            for row, categoria in enumerate(categorias):
                # Agregar solo el nombre de la categoría en la primera columna
                item = QTableWidgetItem(str(categoria[1]))  # categoria[1] es el nombre
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, 0, item)
                
                # Contar productos para esta categoría
                nombre_categoria = categoria[1]
                cantidad_productos = 0
                if productos:
                    for producto in productos:
                        if len(producto) > 6 and str(producto[6]) == nombre_categoria:
                            cantidad_productos += 1
                
                # Agregar la cantidad de productos en la columna 1
                item_productos = QTableWidgetItem(str(cantidad_productos))
                item_productos.setFont(QFont("Segoe ui", 12))
                item_productos.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, 1, item_productos)

    def filter_categorias(self):
        global categorias, productos
        line_edit = self.ui.frame_26.findChild(QLineEdit, "lineEdit_19")
        table_widget = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")

        if line_edit and table_widget:
            filter_text = line_edit.text().lower()

            filtered_categorias = []
            for categoria in categorias:
                if filter_text in categoria[1].lower() or filter_text in str(categoria[0]).lower():
                    filtered_categorias.append(categoria)

            cantidad_categorias = len(filtered_categorias)

            # Si no se encuentran categorías, mostrar un mensaje en la tabla
            if len(filtered_categorias) == 0:
                label_127 = self.ui.frame_62.findChild(QLabel, "label_127")
                if label_127:
                    label_127.clear()
                    label_127.setText(f"0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron categorías")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_127 = self.ui.frame_62.findChild(QLabel, "label_127")
                if label_127:
                    label_127.clear()
                    label_127.setText(f"{cantidad_categorias}")

                # Si hay categorías, llenar la tabla con los datos filtrados
                table_widget.setRowCount(len(filtered_categorias))
                table_widget.setColumnCount(2)  # Nombre y Productos
                table_widget.setHorizontalHeaderLabels(["Nombre", "Productos"])
                for row, categoria in enumerate(filtered_categorias):
                    # Agregar solo el nombre de la categoría en la primera columna
                    item = QTableWidgetItem(str(categoria[1]))  # categoria[1] es el nombre
                    item.setFont(QFont("Segoe ui", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(row, 0, item)
                    
                    # Contar productos para esta categoría filtrada
                    nombre_categoria = categoria[1]
                    cantidad_productos = 0
                    if productos:
                        for producto in productos:
                            if len(producto) > 6 and str(producto[6]) == nombre_categoria:
                                cantidad_productos += 1
                    
                    # Agregar la cantidad de productos en la columna 1
                    item_productos = QTableWidgetItem(str(cantidad_productos))
                    item_productos.setFont(QFont("Segoe ui", 12))
                    item_productos.setTextAlignment(Qt.AlignCenter)
                    table_widget.setItem(row, 1, item_productos)

    # Función para copiar una columna al portapapeles
    def copy_column_to_clipboard_categorias(self, column_index):
        table_widget = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")
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
    def copy_row_to_clipboard_categorias(self, row_index):
        table_widget = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")
        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

    def copy_entire_table_to_clipboard_categorias(self):
        table_widget = self.ui.frame_tabla_productos_3.findChild(QTableWidget, "tableWidget_3")
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

    # funciones del usuario 

    # agregar usuario 

    def agregar_usuario(self):
        if getattr(self, "_usuario_en_proceso", False):
            return
        self._usuario_en_proceso = True

        combobox_14 = self.ui.frame_29.findChild(QComboBox, "comboBox_14")
        line_edit_24 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_24")
        push_button_39 = self.ui.frame_29.findChild(QPushButton, "pushButton_39")
        label_90 = self.ui.frame_29.findChild(QLabel, "label_90")
        label_96 = self.ui.frame_29.findChild(QLabel, "label_96")
        push_button_31 = self.ui.frame_29.findChild(QPushButton, "pushButton_31")
        push_button_32 = self.ui.frame_29.findChild(QPushButton, "pushButton_32")


        if combobox_14:
            combobox_14.clear()
            combobox_14.addItem("Administrador")
            combobox_14.addItem("Usuario")

        if line_edit_24:
            line_edit_24.setEchoMode(QLineEdit.Password)
        
        if push_button_39:
            push_button_39.setFocusPolicy(Qt.NoFocus)
            push_button_39.setIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\eye_visible_hide_hidden_show_icon_145988.png"))
            push_button_39.clicked.connect(self.setear_lineedit_avisual_agregar)

        if label_90:
            label_90.setStyleSheet("color: transparent")

        if label_96:
            label_96.setStyleSheet("color: transparent")

        if push_button_31:
            push_button_31.setFocusPolicy(Qt.NoFocus)
            push_button_31.setStyleSheet("background-color: rgb(168, 225, 255)")
            push_button_31.setShortcut(Qt.Key_Return)
            push_button_31.clicked.connect(self.validar_agregar_usuario)

        if push_button_32:
            push_button_32.setFocusPolicy(Qt.NoFocus)
            push_button_32.clicked.connect(self.clear_inputs_agregar_usuario)


    def validar_agregar_usuario(self):
        global usuario_activo

        combobox_14 = self.ui.frame_29.findChild(QComboBox, "comboBox_14")
        line_edit_23 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_23")
        line_edit_24 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_24")
        line_edit = self.ui.frame_29.findChild(QLineEdit, "lineEdit")
        label_90 = self.ui.frame_29.findChild(QLabel, "label_90")
        label_96 = self.ui.frame_29.findChild(QLabel, "label_96")
        value_combobox_14 = combobox_14.currentText()
        value_line_edit_23 = line_edit_23.text().strip()
        value_line_edit_24 = line_edit_24.text().strip()
        value_line_edit = line_edit.text().strip()
        push_button_31 = self.ui.frame_29.findChild(QPushButton, "pushButton_31")
        push_button_32 = self.ui.frame_29.findChild(QPushButton, "pushButton_32")

        if value_combobox_14 and value_line_edit_23 and value_line_edit_24:
            if len(value_line_edit_24) >= 8:
                # verificar si el email es valido
                if "@gmail" in value_line_edit or "@hotmail" in value_line_edit or "@outlook" in value_line_edit:

                    # verificar si el usuario ya existe
                    if value_line_edit_23 in [usuario[1] for usuario in usuarios]:
                        label_90.setText("El usuario")
                        label_90.setStyleSheet("color: red; font-weight: bold")
                        label_96.setText("ya existe")
                        label_96.setStyleSheet("color: red; font-weight: bold")
                        line_edit_23.setFocus()
                        line_edit_23.selectAll()
                        return
                    # verificcar si el email ya existe

                    if value_line_edit.lower() in [usuario[2].lower() for usuario in usuarios]:
                        label_90.setText("El email ya esta en uso")
                        label_90.setStyleSheet("color: red; font-weight: bold")
                        label_96.setText("por otro usuario")
                        label_96.setStyleSheet("color: red; font-weight: bold")
                        line_edit.setFocus()
                        line_edit.selectAll()
                        return

                    if push_button_31:
                        push_button_31.setEnabled(False)
                    if push_button_32:
                        push_button_32.setEnabled(False)

                    if label_90 and label_96:
                        label_90.setText("Cargando")
                        label_96.setText("usuario...")
                        label_96.setStyleSheet("color: green; font-weight: bold")
                        label_90.setStyleSheet("color: green; font-weight: bold")

                    self.registro_thread = AgregarRegistroUsuarioThread(value_combobox_14, value_line_edit_23, value_line_edit_24, value_line_edit)
                    def on_registro_finalizado(exito):
                        if exito:
                            #controla para que no s eejecute dos veces
                            self._usuario_en_proceso = False

                            label_90 = self.ui.frame_29.findChild(QLabel, "label_90")
                            label_96 = self.ui.frame_29.findChild(QLabel, "label_96")

                            self.movimiento_thread = CargarMovimientoAgregarUsuarioThread(value_line_edit_23, usuario_activo)
                            self.start_thread(self.movimiento_thread)
                            self.clear_inputs_agregar_usuario()
                            combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
                            self.populate_combobox_with_names(combobox_16)

                            global usuarios_cache, usuarios_por_nombre_cache
                            usuarios_cache = None
                            usuarios_por_nombre_cache = None
                            self.actualizar_variables_globales_de_uso(4, lambda: (
                                self.populate_combobox_with_names(self.ui.frame_45.findChild(QComboBox, "comboBox_16"))
                            ))

                            
                            # Actualizar cache de usuarios
                            global usuarios
                            usuarios = None
                            
                            self.actualizar_variables_globales_de_uso(1, lambda: (
                                self.populate_combobox_with_names(self.ui.frame_45.findChild(QComboBox, "comboBox_16")),
                            ))

                            label_90.setText("Usuario agregado")
                            label_96.setText("con éxito")
                            label_96.setStyleSheet("color: green; font-weight: bold")
                            label_90.setStyleSheet("color: green; font-weight: bold")
                            QTimer.singleShot(6000, lambda: label_96.setStyleSheet("color: transparent"))
                            QTimer.singleShot(6000, lambda: label_90.setStyleSheet("color: transparent"))

                            push_button_31 = self.ui.frame_29.findChild(QPushButton, "pushButton_31")
                            push_button_32 = self.ui.frame_29.findChild(QPushButton, "pushButton_32")
                            if push_button_31:
                                push_button_31.setEnabled(True)
                            if push_button_32:
                                push_button_32.setEnabled(True)


                        else:
                           self._usuario_en_proceso = False
                           print("no se pudo cargar el usuario")
                    self.registro_thread.resultado.connect(on_registro_finalizado)
                    self.start_thread(self.registro_thread)
                else:
                    self._usuario_en_proceso = False

                    label_90.setText("Complete correctamente")
                    label_96.setText("el email")
                    label_96.setStyleSheet("color: red; font-weight: bold")
                    label_90.setStyleSheet("color: red; font-weight: bold")
                    line_edit.setFocus()
                    line_edit.selectAll()

            else :
                self._usuario_en_proceso = False

                label_90.setText("La contraseña debe tener")
                label_96.setText("al menos 8 caracteres")
                label_96.setStyleSheet("color: red; font-weight: bold")
                label_90.setStyleSheet("color: red; font-weight: bold")
        else:
            self._usuario_en_proceso = False
            label_90.setText("Por favor, complete todos")
            label_96.setText("los campos correctamente")
            label_96.setStyleSheet("color: red; font-weight: bold")
            label_90.setStyleSheet("color: red; font-weight: bold")

    def clear_inputs_agregar_usuario(self):
        line_edit_23 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_23")
        line_edit_24 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_24")
        line_edit = self.ui.frame_29.findChild(QLineEdit, "lineEdit")
        combobox_14 = self.ui.frame_29.findChild(QComboBox, "comboBox_14")
        if line_edit_23 and line_edit_24 and line_edit:
            line_edit_23.clear()
            line_edit_24.clear()
            line_edit.clear()
            combobox_14.setCurrentIndex(0)
            line_edit_23.setFocus()

    def setear_lineedit_avisual_agregar(self):
        
        line_edit_24 = self.ui.frame_29.findChild(QLineEdit, "lineEdit_24")
        if line_edit_24:
            if line_edit_24.echoMode() == QLineEdit.Password:
                line_edit_24.setEchoMode(QLineEdit.Normal)
            else:
                line_edit_24.setEchoMode(QLineEdit.Password)

    def setear_lineedit_avisual_editar(self):
        line_edit_25 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_25")
        if line_edit_25:
            if line_edit_25.echoMode() == QLineEdit.Password:
                line_edit_25.setEchoMode(QLineEdit.Normal)
            else:
                line_edit_25.setEchoMode(QLineEdit.Password)


################
################

    # editar usuario

    def editar_usuario(self):
        label_98 = self.ui.frame_45.findChild(QLabel, "label_98")
        label_93 = self.ui.frame_45.findChild(QLabel, "label_93")
        combobox_15 = self.ui.frame_45.findChild(QComboBox, "comboBox_15")
        combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
        push_button_33 = self.ui.frame_45.findChild(QPushButton, "pushButton_33")
        push_button_35 = self.ui.frame_45.findChild(QPushButton, "pushButton_35")
        push_button_41 = self.ui.frame_45.findChild(QPushButton, "pushButton_41")
        line_edit_25 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_25")

        if combobox_15:
            combobox_15.clear()
            combobox_15.addItem("Administrador")
            combobox_15.addItem("Usuario")
        
        if combobox_16:
            combobox_16.setEditable(False)  # Deshabilitar la edición
            combobox_16.setInsertPolicy(QComboBox.NoInsert)  # Evitar inserciones
            combobox_16.currentIndexChanged.connect(self.load_user_data)  # Conectar al cambio de índice
            self.populate_combobox_with_names(combobox_16)  # Llenar el combobox con los nombres de usuarios
            
        if push_button_41:
            push_button_41.setFocusPolicy(Qt.NoFocus)
            push_button_41.setIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\eye_visible_hide_hidden_show_icon_145988.png"))
            push_button_41.clicked.connect(self.setear_lineedit_avisual_editar)

        if label_98:
            label_98.setStyleSheet("color: transparent")

        if label_93:
            label_93.setStyleSheet("color: transparent")

        if push_button_33:
            push_button_33.setFocusPolicy(Qt.NoFocus)
            push_button_33.setStyleSheet("background-color: rgb(255, 202, 96)")
            push_button_33.setShortcut(Qt.Key_Return)
            push_button_33.clicked.connect(lambda: self.validar_datos_iguales_usuario(usuario_selecc if usuario_selecc is not None else None))

        if push_button_35:
            push_button_35.setFocusPolicy(Qt.NoFocus)
            push_button_35.clicked.connect(self.clear_inputs_editar_usuario)

        if line_edit_25:
            line_edit_25.setEchoMode(QLineEdit.Password)

    def load_user_data(self):
        global usuario_selecc, usuarios_por_nombre_cache

        combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
        if combobox_16:
            nombre = combobox_16.currentText()
            if nombre and usuarios_por_nombre_cache and nombre in usuarios_por_nombre_cache:
                usuario = usuarios_por_nombre_cache[nombre]
                usuario_selecc = [usuario]  # Para mantener el formato de lista

                if usuario and nombre == str(usuario[1]):
                    if usuario[3]:  # admin (bool)
                        self.ui.frame_45.findChild(QComboBox, "comboBox_15").setCurrentIndex(0)
                    else:
                        self.ui.frame_45.findChild(QComboBox, "comboBox_15").setCurrentIndex(1)
                    self.ui.frame_45.findChild(QComboBox, "comboBox_16").setCurrentText(str(usuario[1]))
                    self.ui.frame_45.findChild(QLineEdit, "lineEdit_25").setText(str(usuario[4]))  # email
                    self.ui.frame_45.findChild(QLineEdit, "lineEdit_22").setText(str(usuario[2]))  # contraseña vacía o buscar aparte

    def populate_combobox_with_names(self, combobox):
        global usuarios_por_nombre_cache
        combobox.clear()
        if usuarios_por_nombre_cache:
            nombres = sorted(usuarios_por_nombre_cache.keys())
            combobox.addItems(nombres)
            combobox.setMaxVisibleItems(4)
        

    def clear_inputs_editar_usuario(self):
        self.load_user_data()

    def validar_datos_iguales_usuario(self, usuario_selecc):
        push_button_33 = self.ui.frame_45.findChild(QPushButton, "pushButton_33")
        push_button_35 = self.ui.frame_45.findChild(QPushButton, "pushButton_35")

        if push_button_33:
            push_button_33.setEnabled(False)
        if push_button_35:
            push_button_35.setEnabled(False)

        label_93 = self.ui.frame_45.findChild(QLabel, "label_93")
        label_98 = self.ui.frame_45.findChild(QLabel, "label_98")

        if usuario_selecc:
            combobox_15 = self.ui.frame_45.findChild(QComboBox, "comboBox_15")
            line_edit_25 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_25")  # contraseña
            line_edit_22 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_22")  # email

            value_line_edit_25 = line_edit_25.text().strip()  # contraseña
            value_combobox_15 = combobox_15.currentText()
            value_combobox_15 = True if value_combobox_15 == "Administrador" else False
            
            # Comparar admin y contraseña Y email
            if usuario_selecc[0][3] == value_combobox_15 and str(usuario_selecc[0][4]) == str(value_line_edit_25) and str(usuario_selecc[0][2]).strip() == line_edit_22.text().strip():
                label_93.setText("Porfavor, edite")
                label_98.setText("los campos")
                label_98.setStyleSheet("color: red; font-weight: bold")
                label_93.setStyleSheet("color: red; font-weight: bold")
            else:
                self.validar_editar_usuario()

    def validar_editar_usuario(self):
        global usuario_selecc, usuario_activo, usuarios

        push_button_33 = self.ui.frame_45.findChild(QPushButton, "pushButton_33")
        push_button_35 = self.ui.frame_45.findChild(QPushButton, "pushButton_35")

        combobox_15 = self.ui.frame_45.findChild(QComboBox, "comboBox_15")
        line_edit_25 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_25")  # mail
        line_edit_22 = self.ui.frame_45.findChild(QLineEdit, "lineEdit_22")  # contraseña
        value_line_edit_22 = line_edit_22.text().strip()  # contraseña
        value_combobox_15 = combobox_15.currentText()
        value_line_edit_25 = line_edit_25.text().strip()  # mail
        label_93 = self.ui.frame_45.findChild(QLabel, "label_93")
        label_98 = self.ui.frame_45.findChild(QLabel, "label_98")
        combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
        value_combobox_16 = combobox_16.currentText().strip()

        # Validar que la contraseña tenga al menos 8 caracteres
        if len(value_line_edit_25) <= 8:
            label_93.setText("La contraseña debe tener")
            label_98.setText("al menos 8 caracteres")
            label_98.setStyleSheet("color: red; font-weight: bold")
            label_93.setStyleSheet("color: red; font-weight: bold")
            line_edit_25.setFocus()
            line_edit_25.selectAll()
            return

        # Validar si el email ya existe en otro usuario (excepto el usuario actual)
        if any(u[2].strip().lower() == value_line_edit_22.lower() and u[0] != usuario_selecc[0][0] for u in usuarios):
            label_93.setText("El email ya está en uso")
            label_98.setText("por otro usuario")
            label_98.setStyleSheet("color: red; font-weight: bold")
            label_93.setStyleSheet("color: red; font-weight: bold")
            line_edit_22.setFocus()
            line_edit_22.selectAll()
            return

        if label_93 and label_98:
            label_93.setText("Actualizando")
            label_98.setText("usuario...")
            label_98.setStyleSheet("color: green; font-weight: bold")
            label_93.setStyleSheet("color: green; font-weight: bold")

        self.actualizar_usuario_thread = ActualizarUsuarioThread(
            usuario_selecc[0][0], value_combobox_15, value_line_edit_25, value_line_edit_22
        )
        def on_actualizado(s):
            if s:
                self.movimiento_thread = CargarMovimientoEditarUsuarioThread(
                    usuario_selecc[0][0], value_combobox_16, usuario_activo
                )
                self.start_thread(self.movimiento_thread)
                QTimer.singleShot(0, lambda: QTimer().stop())
        
                global usuarios_cache
                usuarios_cache = None
                combobox_16 = self.ui.frame_45.findChild(QComboBox, "comboBox_16")
                self.actualizar_variables_globales_de_uso(4, lambda: (
                    self.populate_combobox_with_names(combobox_16)
                ))

                label_93.setText("Usuario")
                label_98.setText("actualizado")
                label_98.setStyleSheet("color: green; font-weight: bold")
                label_93.setStyleSheet("color: green; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_93.setStyleSheet("color: transparent"))
                QTimer.singleShot(6000, lambda: label_98.setStyleSheet("color: transparent"))

                if push_button_33:
                    push_button_33.setEnabled(True)
                if push_button_35:
                    push_button_35.setEnabled(True)

            else:
                if push_button_33:
                    push_button_33.setEnabled(True)
                if push_button_35:
                    push_button_35.setEnabled(True)
                    
                print("no se pudo actualizar el usuario")
                
        self.actualizar_usuario_thread.resultado.connect(on_actualizado)
        self.start_thread(self.actualizar_usuario_thread)



################
################

    # Borrar usuario

    def borrar_usuario(self):
        label_95 = self.ui.frame_47.findChild(QLabel, "label_95")
        push_buttton_40 = self.ui.frame_47.findChild(QPushButton, "pushButton_40")
        label_100 = self.ui.stackedWidget.findChild(QLabel, "label_100")

        if label_100:
            label_100.setAlignment(Qt.AlignCenter)
            label_100.setText("ADVERTENCIA!\n"
            "Si borra un usuario con ventas y compras realizadas tambien seran borradas.")

        if label_95:
            label_95.setStyleSheet("color: transparent")

        if push_buttton_40:
            push_buttton_40.setStyleSheet("background-color: red; padding: 5px;")
            push_buttton_40.clicked.connect(self.delete_usuario)

    def delete_usuario(self):
        global usuarios  # Asegúrate de tener la variable global usuarios cargada

        line_edit_29 = self.ui.frame_47.findChild(QLineEdit, "lineEdit_29")
        label_95 = self.ui.frame_47.findChild(QLabel, "label_95")
        value_line_edit_29 = line_edit_29.text().strip()

        if value_line_edit_29 == "":
            label_95.setText("Complete el campo")
            label_95.setStyleSheet("color: red; font-weight: bold")
            line_edit_29.setFocus()
            return

        if str(usuario_activo) == str(value_line_edit_29):
            label_95.setText("No se puede borrar el usuario activo")
            label_95.setStyleSheet("color: red; font-weight: bold")
            QTimer.singleShot(6000, lambda: label_95.setStyleSheet("color: transparent"))
            line_edit_29.clear()
            line_edit_29.setFocus()
            return

        # Buscar el id_usuario en la variable global usuarios (lista de tuplas)
        id_usuario = None
        if usuarios:
            for u in usuarios:
                # u[1] es el nombre, u[0] es el id_usuario
                if str(u[1]).strip() == value_line_edit_29:
                    id_usuario = u[0]
                    break

        if id_usuario is not None:
            push_buttton_40 = self.ui.frame_47.findChild(QPushButton, "pushButton_40")
            if push_buttton_40:
                push_buttton_40.setEnabled(False)

            label_95.setText("Borrando usuario...")
            label_95.setStyleSheet("color: green; font-weight: bold")

            # Hilo para borrar el usuario
            self.borrar_usuario_thread = BorrarUsuarioThread(value_line_edit_29)
            def on_usuario_borrado(exito):
                if exito:
                    # Hilo para cargar el movimiento de usuario borrado
                    self.movimiento_usuario_borrado_thread = MovimientoUsuarioBorradoThread(value_line_edit_29, id_usuario, usuario_activo)
                    self.start_thread(self.movimiento_usuario_borrado_thread)

                    global usuarios_cache, usuarios_por_nombre_cache
                    usuarios_cache = None
                    usuarios_por_nombre_cache = None
                    self.actualizar_variables_globales_de_uso(4, lambda: (
                        self.populate_combobox_with_names(self.ui.frame_45.findChild(QComboBox, "comboBox_16"))
                    ))

                    label_95.setText("Usuario borrado con éxito")
                    label_95.setStyleSheet("color: green; font-weight: bold")
                    QTimer.singleShot(6000, lambda: label_95.setStyleSheet("color: transparent"))

                    line_edit_29.clear()
                    line_edit_29.setFocus()

                    if push_buttton_40:
                        push_buttton_40.setEnabled(True)
                else:
                    print("Error al borrar el usuario")

            self.borrar_usuario_thread.resultado.connect(on_usuario_borrado)
            self.start_thread(self.borrar_usuario_thread)
        else:
            label_95.setText("Usuario no encontrado")
            label_95.setStyleSheet("color: red; font-weight: bold")
            
            push_buttton_40 = self.ui.frame_47.findChild(QPushButton, "pushButton_40")
            if push_buttton_40:
                push_buttton_40.setEnabled(True)

            line_edit_29 = self.ui.frame_47.findChild(QLineEdit, "lineEdit_29")
            if line_edit_29:
                line_edit_29.selectAll()
                line_edit_29.setFocus()

            

 
################
################

    # funcion para mostrar nombre del usuario activo

    def mostrar_usuario_activo(self, usuario):
        label_31 = self.ui.frame_9.findChild(QLabel, "label_31")
        if label_31:
            label_31.setText(usuario)

        label_69 = self.ui.frame_39.findChild(QLabel, "label_69")
        if label_69:
            label_69.setText(usuario)    

################
################

class BuscarDatosTab:
    def __init__(self, ui, datos_tab):
        self.ui = ui
        self.datos_tab = datos_tab
        #crear arreglo con threads abiertos
        self.threads = []

        self.check_open = False

        # Al principio de tu clase BuscarDatosTab (o donde corresponda)
        self.timer_dia = QTimer()
        self.timer_dia.setSingleShot(True)
        self.timer_dia.timeout.connect(self.enviar_a_setear_tables)

        # se crean variables globales de uso para actualizar datos, 
        self.datos_tab.actualizar_variables_globales_de_uso(0, self.inicializar_ui_con_datos)

    def inicializar_ui_con_datos(self):
        self.boton_mov()
        self.boton_arqueo()
        self.boton_estadisticas()

    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()


################
################
    # Movimientos

    def traer_metodo_pago_cache(self, id_metodo):
        """Obtener método de pago desde cache local"""
        global metodos_pago_por_id_cache

        if metodos_pago_por_id_cache and str(id_metodo) in metodos_pago_por_id_cache:
            return metodos_pago_por_id_cache[str(id_metodo)]
        return "Método desconocido"

    def boton_mov(self):
        push_button_48 = self.ui.tab_3.findChild(QPushButton, "pushButton_48")
        if push_button_48:
            push_button_48.clicked.connect(self.movimientos)

    def movimientos(self):
        # Iniciar combobox y tabla
        combobox_17 = self.ui.frame_53.findChild(QComboBox, "comboBox_17")
        combobox_18 = self.ui.frame_54.findChild(QComboBox, "comboBox_18")
        date_edit = self.ui.frame_54.findChild(QDateEdit, "dateEdit_3")

        if combobox_18:
            combobox_18.setVisible(False)

        if date_edit:
            date_edit.setDisplayFormat("dd MM yyyy")
            date_edit.setDate(QDate.currentDate())  # Establecer la fecha actual como predeterminada
        
         # Conectar eventos de doble clic
        table_widget = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
        if table_widget:
            corner_button = table_widget.findChild(QAbstractButton)
            table_widget.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard)
            table_widget.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard)
            corner_button.clicked.connect(self.copy_entire_table_to_clipboard)

        # Bandera para evitar ejecución en la primera inicialización
        self._combobox_17_initialized = getattr(self, "_combobox_17_initialized", False)

        if combobox_17:
            if combobox_17.count() == 0:
                combobox_17.addItem("Fecha")
                combobox_17.addItem("Usuario")
                combobox_17.addItem("Acción")
            else:
                combobox_17.setCurrentIndex(0)  # Reiniciar a "Fecha" si ya tiene elementos

            # Conectar el evento de cambio de texto al método
            if not self._combobox_17_initialized:
                combobox_17.currentTextChanged.connect(self.setear_combobox_18)
                self._combobox_17_initialized = True  # Marcar como inicializado
                
        # Inicializar la tabla con todos los movimientos
        self.setear_combobox_18()

    def setear_combobox_18(self):
        combobox_17 = self.ui.frame_53.findChild(QComboBox, "comboBox_17")
        combobox_18 = self.ui.frame_54.findChild(QComboBox, "comboBox_18")
        date_edit = self.ui.frame_54.findChild(QDateEdit, "dateEdit_3")

        if combobox_17 and combobox_18 and date_edit:
            if combobox_17.currentText() == "Usuario":
                combobox_18.setVisible(True)
                date_edit.setDate(QDate())  
                date_edit.setHidden(True)
                self.populate_combobox_with_names(combobox_18)
                self.filtro(combobox_17, combobox_18)
                combobox_18.currentTextChanged.connect(lambda: self.filtro(combobox_17, combobox_18))

            elif combobox_17.currentText() == "Fecha":
                combobox_18.setVisible(False)
                date_edit.setHidden(False)
                date_edit.setStyleSheet("font-weight: bold;")
                date_edit.setDate(QDate.currentDate())  # Establecer la fecha actual como predeterminada
                self.filtro(combobox_17, combobox_18)
                date_edit.dateChanged.connect(lambda: self.filtro(combobox_17, combobox_18))
                

            elif combobox_17.currentText() == "Acción":
                combobox_18.setVisible(True)
                date_edit.setDate(QDate())  
                date_edit.setHidden(True)
                self.populate_combobox_acciones(combobox_18)
                self.filtro(combobox_17, combobox_18)
                combobox_18.currentTextChanged.connect(lambda: self.filtro(combobox_17, combobox_18))
    
    def populate_combobox_acciones(self, combobox):
        combobox.clear()
        acciones = ["Agregar", "Borrar", "Editar", "Venta", "Compra", "Login"]
        combobox.addItems(acciones)

    def populate_combobox_with_names(self, combobox):
        global usuarios_por_nombre_cache
        combobox.clear()
        if usuarios_por_nombre_cache:
            nombres = sorted(usuarios_por_nombre_cache.keys())
            combobox.addItems(nombres)

    def filtro(self, combobox_17, combobox_18):
        date_edit = self.ui.frame_54.findChild(QDateEdit, "dateEdit_3")
        filtro = combobox_17.currentText()
        global movimientos

        if filtro == "Usuario" and combobox_18:
            usuario_seleccionado = combobox_18.currentText()
            if usuario_seleccionado:
                self.mov_thread = MovimientosPorUsuarioThread(usuario_seleccionado)
                self.mov_thread.resultado.connect(self._on_movimientos_obtenidos)
                self.start_thread(self.mov_thread)

        elif filtro == "Fecha" and date_edit:
            fecha_qdate = date_edit.date()
            fecha_seleccionada = f"{fecha_qdate.year()}-{fecha_qdate.month():02d}-{fecha_qdate.day():02d}"
            self.mov_thread = MovimientosPorFechaThread(fecha_seleccionada)
            self.mov_thread.resultado.connect(self._on_movimientos_obtenidos)
            self.start_thread(self.mov_thread)

        elif filtro == "Acción" and combobox_18:
            
            accion_seleccionada = combobox_18.currentText()

            if accion_seleccionada:
                self.mov_thread = MovimientosPorAccionThread(accion_seleccionada)
                self.mov_thread.resultado.connect(self._on_movimientos_obtenidos)
                self.start_thread(self.mov_thread)

    def _on_movimientos_obtenidos(self, movimientos_obtenidos):
        global movimientos
        movimientos = movimientos_obtenidos
        self.setear_tabla_movimientos()


    def setear_tabla_movimientos(self):
        global movimientos

        table = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
        
        if table:

            table.clearContents()  # Limpiar el contenido de la tabla
            table.setRowCount(0)  # Reiniciar el número de filas
            table.setEditTriggers(QTableWidget.NoEditTriggers)  # Deshabilitar edición
        

            # Configurar las filas de la tabla
            if len(movimientos) == 0:
             # Si no hay movimientos, mostrar un mensaje
                table.setColumnCount(1)
                table.setHorizontalHeaderLabels(["Mensaje"])
                table.setRowCount(1)
                item = QTableWidgetItem("No hay movimientos")
                item.setFont(QFont("Segoe UI", 12, QFont.Bold))
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(0, 0, item)
                
            else:
                table.setColumnCount(6)
                table.setHorizontalHeaderLabels(["Usuario", "Fecha", "Hora", "Acción", "Entidad Afectada", "Descripción"])
                table.setRowCount(len(movimientos))
            
                for row, movimiento in enumerate(movimientos):
                    # Si es la primera columna (ID del usuario), obtener el nombre del usuario
                    nombre_usuario = ""
                    if usuarios:
                        for u in usuarios:
                            if str(u[0]) == str(movimiento[0]):
                                nombre_usuario = u[1]
                                break
                    item = QTableWidgetItem(str(nombre_usuario))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 0, item)
            
                    # Fecha
                    fecha_str = movimiento[1]
                    # Quitar la zona horaria si existe
                    fecha_str_sin_tz = fecha_str.split('+')[0].strip()
                    fecha_dt = datetime.strptime(fecha_str_sin_tz, "%Y-%m-%dT%H:%M:%S.%f")
                    fecha_formateada = fecha_dt.strftime("%d-%m-%Y")
                    item = QTableWidgetItem(fecha_formateada)
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 1, item)
            
                    # Hora
                    local_tz = pytz.timezone('America/Argentina/Buenos_Aires')
                    fecha_dt_utc = fecha_dt.replace(tzinfo=pytz.UTC)
                    hora_local = fecha_dt_utc.astimezone(local_tz)
                    hora_formateada = hora_local.strftime("%I:%M %p")
                    item = QTableWidgetItem(hora_formateada)
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 2, item)
            
                    # Acción (posición 2 en movimiento)
                    item = QTableWidgetItem(str(movimiento[2]))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 3, item)
            
                    # Entidad Afectada (posición 3 en movimiento)
                    item = QTableWidgetItem(str(movimiento[3]))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 4, item)
            
                    # Descripción (posición 4 en movimiento)
                    item = QTableWidgetItem(str(movimiento[4]))
                    item.setFont(QFont("Segoe UI", 12))
                    item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(row, 5, item)

    def copy_entire_table_to_clipboard(self):
        table_widget = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
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


    # Función para copiar una columna al portapapeles
    def copy_column_to_clipboard(self, column_index):
        table_widget = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
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
        table_widget = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

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

    # cortes y arqueo

    def boton_arqueo(self):
        push_button_15 = self.ui.tab_3.findChild(QPushButton, "pushButton_15")
        if push_button_15:
            push_button_15.clicked.connect(self.inicializar_comboboxes_y_boton)

         # Conectar eventos de doble clic
        table_widget_6 = self.ui.frame_27.findChild(QTableWidget, "tableWidget_6")
        if table_widget_6:
            corner_button_6 = table_widget_6.findChild(QAbstractButton)

            table_widget_6.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard_ventas)
            table_widget_6.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard_ventas)
            corner_button_6.clicked.connect(self.copy_entire_table_to_clipboard_ventas)

        table_widget_7 = self.ui.frame_23.findChild(QTableWidget, "tableWidget_7")
        if table_widget_7:
            corner_button_7 = table_widget_7.findChild(QAbstractButton)
            table_widget_7.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard_compras)
            table_widget_7.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard_compras)
            corner_button_7.clicked.connect(self.copy_entire_table_to_clipboard_compras)
    

    def inicializar_comboboxes_y_boton(self):
        # Obtener los QComboBox
        combobox_10_dia = self.ui.frame_32.findChild(QComboBox, "comboBox_10")
        combobox_9_mes = self.ui.frame_32.findChild(QComboBox, "comboBox_9")
        combobox_8_anio = self.ui.frame_32.findChild(QComboBox, "comboBox_8")
        combobox_12 = self.ui.frame_31.findChild(QComboBox, "comboBox_12")
        combobox_13 = self.ui.frame_31.findChild(QComboBox, "comboBox_13")
        push_button_47 = self.ui.frame_31.findChild(QPushButton, "pushButton_47")

        # Obtener la fecha actual
        hoy = datetime.now()
        anio_actual = hoy.year
        mes_actual = hoy.month
        dia_actual = hoy.day
    
        # Inicializar ComboBox de días
        if combobox_10_dia:
            combobox_10_dia.setStyleSheet("background-color: rgb(226, 245, 255);")
            combobox_10_dia.setMaxVisibleItems(5)  # Mostrar un máximo de 5 elementos visibles
            self.actualizar_dias_combobox(combobox_10_dia, mes_actual, anio_actual)
            combobox_10_dia.setCurrentText(str(dia_actual))
            
            # En la inicialización del combobox de días:
            combobox_10_dia.currentTextChanged.connect(lambda: self.timer_dia.start(2000))
    
        # Inicializar ComboBox de meses
        if combobox_9_mes:
            combobox_9_mes.clear()  # Limpiar el combobox antes de agregar elementos
            combobox_9_mes.setStyleSheet("background-color: rgb(226, 245, 255);")
            combobox_9_mes.addItems(["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"])
            combobox_9_mes.setCurrentIndex(mes_actual)  # Los índices comienzan en 0
            
            # En la inicialización del combobox:
            combobox_9_mes.currentTextChanged.connect(lambda: self.timer_dia.start(2000))
    
        # Inicializar ComboBox de años
        if combobox_8_anio:
            global anios_obtenidos
            
            combobox_8_anio.setStyleSheet("background-color: rgb(226, 245, 255);")
            combobox_8_anio.clear()
            combobox_8_anio.addItems([str(anio) for anio in anios_obtenidos])
            combobox_8_anio.setCurrentText(str(anio_actual))
            
            # En la inicialización del combobox :
            combobox_8_anio.currentTextChanged.connect(lambda: self.timer_dia.start(2000))

        if combobox_8_anio != "":
            if combobox_9_mes and combobox_8_anio and combobox_10_dia:
                combobox_9_mes.currentIndexChanged.connect(
                    lambda: self.actualizar_dias_combobox(
                        combobox_10_dia,
                        combobox_9_mes.currentIndex() + 1,
                        int(combobox_8_anio.currentText()) if combobox_8_anio.currentText().isdigit() else 0
                    )
                )
                combobox_8_anio.currentTextChanged.connect(
                    lambda: self.actualizar_dias_combobox(
                        combobox_10_dia,
                        combobox_9_mes.currentIndex() + 1,
                        int(combobox_8_anio.currentText()) if combobox_8_anio.currentText().isdigit() else 0
                    )
                )


        # Inicializar ComboBox de métodos de pago o usuarios solo si esta vacio
        if combobox_12:
            combobox_12.clear()
            if combobox_12.count() == 0:
                combobox_12.addItem("")
                combobox_12.addItem("Metodo de Pago")
                combobox_12.addItem("Usuario")
                combobox_12.addItem("Categoría")

            # Conectar el evento de cambio de texto para actualizar el combobox_13
            combobox_12.currentTextChanged.connect(lambda: self.actualizar_combobox_13(combobox_12, combobox_13))
            
        
        if combobox_13:
            # Conectar el evento de cambio de texto para actualizar los datos
            # En la inicialización del combobox:
            combobox_13.currentTextChanged.connect(lambda: self.timer_dia.start(2000))  

        if push_button_47:
            if not self.check_open:
                self.check_open = True
                push_button_47.clicked.connect(self.hacer_corte)

          # *** CARGAR DATOS DE HOY AUTOMÁTICAMENTE ***
        # Usar QTimer para asegurar que todos los comboboxes estén configurados
        QTimer.singleShot(100, self.enviar_a_setear_tables)


    def traer_nom_producto(self, id_producto):
        global productos_por_id_cache
        if productos_por_id_cache and str(id_producto) in productos_por_id_cache:
            return productos_por_id_cache[str(id_producto)][1]
        return ""
    
    def traer_usuario(self, id_usuario):
        global usuarios_por_nombre_cache
        if usuarios_por_nombre_cache:
            for usuario in usuarios_por_nombre_cache.values():
                if str(usuario[0]) == str(id_usuario):
                    return usuario[1]
        return ""
    
    def obtener_metodo_pago_id(self, nombre_metodo, callback):
        # Usar el cache global si está disponible
        global metodos_pago_por_id_cache
       
        if metodos_pago_por_id_cache:
            # Buscar el ID por el nombre en el cache
            for id_metodo, nombre in metodos_pago_por_id_cache.items():
                if nombre == nombre_metodo:
                    
                    callback(int(id_metodo))
                    return

    def obtener_metodo_pago(self, id_metodo, callback):
        self.metodo_pago_thread = TraerMetodoPagoThread(id_metodo)
        self.metodo_pago_thread.resultado.connect(callback)
        self.start_thread(self.metodo_pago_thread)

    def obtener_datos_ventas(self, id_metodo_o_usuario, fecha, verif, callback):
        self.ventas_thread = TraerDatosVentasMetodoUsuarioThread(id_metodo_o_usuario, fecha, verif)
        self.ventas_thread.resultado.connect(callback)
        self.start_thread(self.ventas_thread)

    def obtener_datos_compras(self, id_metodo_o_usuario, fecha, verif, callback):
        self.compras_thread = TraerDatosComprasMetodoUsuarioThread(id_metodo_o_usuario, fecha, verif)
        self.compras_thread.resultado.connect(callback)
        self.start_thread(self.compras_thread)
    
    def obtener_datos_arqueo_ventas_fecha(self, fecha, callback):
        self.arqueo_ventas_thread = TraerDatosArqueoVentasFechaThread(fecha)
        self.arqueo_ventas_thread.resultado.connect(callback)
        self.start_thread(self.arqueo_ventas_thread)

    def obtener_datos_arqueo_compras_fecha(self, fecha, callback):
        self.arqueo_compras_thread = TraerDatosArqueoComprasFechaThread(fecha)
        self.arqueo_compras_thread.resultado.connect(callback)
        self.start_thread(self.arqueo_compras_thread)

    
    def enviar_a_setear_tables(self):
        # Obtener elementos UI una sola vez
        push_button_47 = self.ui.frame_31.findChild(QPushButton, "pushButton_47")
        if push_button_47:
            push_button_47.setEnabled(False)

        combobox_10_dia = self.ui.frame_32.findChild(QComboBox, "comboBox_10")
        combobox_9_mes = self.ui.frame_32.findChild(QComboBox, "comboBox_9")
        combobox_8_anio = self.ui.frame_32.findChild(QComboBox, "comboBox_8")
        combobox_12 = self.ui.frame_31.findChild(QComboBox, "comboBox_12")
        combobox_13 = self.ui.frame_31.findChild(QComboBox, "comboBox_13")
        tablewidget_compras = self.ui.frame_23.findChild(QTableWidget, "tableWidget_7")
        tablewidget_ventas = self.ui.frame_27.findChild(QTableWidget, "tableWidget_6")
        label_58 = self.ui.frame_31.findChild(QLabel, "label_58")
        label_47 = self.ui.frame_30.findChild(QLabel, "label_47")

        # Obtener valores una sola vez
        valor_combobox_12 = combobox_12.currentText()
        valor_combobox_13 = combobox_13.currentText()
        valor_combobox_10_dia = combobox_10_dia.currentText()
        valor_combobox_9_mes = combobox_9_mes.currentText()
        valor_combobox_8_anio = combobox_8_anio.currentText()

        # Configurar tablewidgets
        self._configurar_tablewidgets(tablewidget_compras, tablewidget_ventas)

        # Configurar labels
        if label_58:
            label_58.setStyleSheet("color: green; font-weight: bold")
            label_58.setText("$0.00")  # Inicializar
        if label_47:
            label_47.setStyleSheet("color: rgb(230, 180, 80); font-weight: bold")
            label_47.setText("$0.00")  # Inicializar

        if not valor_combobox_8_anio:
            return

        # Construir fecha
        fecha = self._construir_fecha(valor_combobox_8_anio, valor_combobox_9_mes, valor_combobox_10_dia, combobox_9_mes)

        # Verificar cache de métodos de pago
        if not self._verificar_cache_metodos_pago():
            QTimer.singleShot(500, self.enviar_a_setear_tables)
            return

        # Procesar según el tipo de filtro
        if valor_combobox_12 == "Metodo de Pago" and valor_combobox_13:
            self._procesar_por_metodo_pago(valor_combobox_13, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47)
        elif valor_combobox_12 == "Usuario" and valor_combobox_13:
            self._procesar_por_usuario(valor_combobox_13, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47)
        elif valor_combobox_12 == "Categoría" and valor_combobox_13:
            self._procesar_por_categoria(valor_combobox_13, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47)
        else:
            self._procesar_arqueo(fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47)

    def _configurar_tablewidgets(self, tablewidget_compras, tablewidget_ventas):
        """Configurar headers para ambos tablewidgets"""
        headers = ["Usuario", "Fecha", "Hora", "Método de Pago", "Producto", "Cantidad", "Precio Unitario"]

        for widget in [tablewidget_compras, tablewidget_ventas]:
            if widget:
                # Limpiar tabla primero
                widget.clear()
                widget.setColumnCount(7)
                widget.setHorizontalHeaderLabels(headers)
                widget.setEditTriggers(QTableWidget.NoEditTriggers)
                header = widget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 12, QFont.Bold))

    def _construir_fecha(self, anio, mes, dia, combobox_mes):
        """Construir string de fecha según los parámetros seleccionados"""
        if not mes and not dia:
            return anio
        elif mes and not dia:
            return f"{anio}-{combobox_mes.currentIndex()}"
        elif mes and dia:
            return f"{anio}-{combobox_mes.currentIndex()}-{dia}"
        return None

    def _verificar_cache_metodos_pago(self):
        """Verificar si el cache de métodos de pago está disponible"""
        global metodos_pago_por_id_cache

        if metodos_pago_por_id_cache is None:
            # Cargar cache si no existe
            self.metodos_pago_thread = TraerTodosLosMetodosPagoThread()

            def on_metodos_obtenidos(metodos):
                global metodos_pago_por_id_cache
                metodos_pago_por_id_cache = {str(metodo[0]): metodo[1] for metodo in metodos}

            self.metodos_pago_thread.resultado.connect(on_metodos_obtenidos)
            self.start_thread(self.metodos_pago_thread)
            return False

        return True
    
    def _procesar_datos_optimizado(self, datos, es_ventas, tablewidget, label_total):
        """Procesar datos de ventas o compras usando cache de métodos de pago"""
        if not tablewidget:
            return
    
        # Inicializa resultados_arqueo si no existe
        if not hasattr(self, "resultados_arqueo") or not isinstance(self.resultados_arqueo, dict):
            self.resultados_arqueo = {
                "ventas_totales": 0,
                "numero_de_ventas": 0,
                "ventas_por_metodo": {},
                "ganancias_por_metodo": {},
                "ganancias_totales": 0,
                "compras_totales": 0,
                "numero_de_compras": 0
            }
    
        # Si no hay datos, mostrar mensaje y resetear solo la parte correspondiente
        if not datos:
            tablewidget.setRowCount(1)
            tablewidget.setColumnCount(1)
            tablewidget.setHorizontalHeaderLabels(["Mensaje"])
            header = tablewidget.horizontalHeader()
            header.setFont(QFont("Segoe UI", 12, QFont.Bold))
            item = QTableWidgetItem("No se encontraron registros")
            item.setFont(QFont("Segoe UI", 12))
            item.setTextAlignment(Qt.AlignCenter)
            tablewidget.setItem(0, 0, item)
            if label_total:
                label_total.setText("$0.00")
            if es_ventas:
                self.resultados_arqueo["ventas_totales"] = 0
                self.resultados_arqueo["numero_de_ventas"] = 0
                self.resultados_arqueo["ventas_por_metodo"] = {}
                self.resultados_arqueo["ganancias_por_metodo"] = {}
                self.resultados_arqueo["ganancias_totales"] = 0
            else:
                self.resultados_arqueo["compras_totales"] = 0
                self.resultados_arqueo["numero_de_compras"] = 0
            return
    
        tablewidget.setRowCount(len(datos))
        tablewidget.setColumnCount(7)
        headers = ["Usuario", "Fecha", "Hora", "Método de Pago", "Producto", "Cantidad", "Precio Unitario"]
        tablewidget.setHorizontalHeaderLabels(headers)
        header = tablewidget.horizontalHeader()
        header.setFont(QFont("Segoe UI", 12, QFont.Bold))
    
        total = 0
        ventas_por_metodo = {}
        ganancias_por_metodo = {}
    
        for row, dato in enumerate(datos):
            usuario = self.traer_usuario(dato[0])
            fecha_str = dato[1]
            
            fecha_str_sin_tz = fecha_str.split('+')[0].strip()
            try:
                fecha_dt = datetime.strptime(fecha_str_sin_tz, "%Y-%m-%dT%H:%M:%S.%f")
            except ValueError:
                fecha_dt = datetime.strptime(fecha_str_sin_tz, "%Y-%m-%dT%H:%M:%S")
            fecha_separada = fecha_dt.strftime("%d-%m-%Y")
            
            local_tz = pytz.timezone('America/Argentina/Buenos_Aires')
            fecha_dt_utc = fecha_dt.replace(tzinfo=pytz.UTC)
            hora_local = fecha_dt_utc.astimezone(local_tz)
            hora_separada = hora_local.strftime("%I:%M %p")
    
            metodo_pago = self.traer_metodo_pago_cache(dato[2])
            producto = self.traer_nom_producto(dato[3])
            cantidad = dato[4]
            precio_unitario = dato[5]
            total += precio_unitario * cantidad
    
            # Calcular ganancia solo para ventas (precio_venta - precio_compra)
            if es_ventas:
                costo_unitario = dato[6] if len(dato) > 6 else 0
                ganancia = (precio_unitario - costo_unitario) * cantidad
                ventas_por_metodo.setdefault(metodo_pago, 0)
                ventas_por_metodo[metodo_pago] += precio_unitario * cantidad
                ganancias_por_metodo.setdefault(metodo_pago, 0)
                ganancias_por_metodo[metodo_pago] += ganancia
            else:
                ventas_por_metodo.setdefault(metodo_pago, 0)
                ventas_por_metodo[metodo_pago] += precio_unitario * cantidad
    
            items = [usuario, fecha_separada, hora_separada, metodo_pago, producto, str(cantidad), f"${precio_unitario}"]
            for col, item_text in enumerate(items):
                item = QTableWidgetItem(str(item_text))
                item.setFont(QFont("Segoe UI", 10))
                item.setTextAlignment(Qt.AlignCenter)
                tablewidget.setItem(row, col, item)
    
        if label_total:
            label_total.setText(f"${total:.2f}")
    
        # Guardar resultados globales para el corte (solo la parte correspondiente)
        if es_ventas:
            self.resultados_arqueo["ventas_totales"] = total
            self.resultados_arqueo["numero_de_ventas"] = len(datos)
            self.resultados_arqueo["ventas_por_metodo"] = ventas_por_metodo
            self.resultados_arqueo["ganancias_por_metodo"] = ganancias_por_metodo
            self.resultados_arqueo["ganancias_totales"] = sum(ganancias_por_metodo.values())
        else:
            self.resultados_arqueo["compras_totales"] = total
            self.resultados_arqueo["numero_de_compras"] = len(datos)

        push_button_47 = self.ui.frame_31.findChild(QPushButton, "pushButton_47")
        if push_button_47:
            push_button_47.setEnabled(True)

    def _procesar_por_metodo_pago(self, metodo_pago_nombre, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47):
        """Procesar datos filtrados por método de pago"""
        resultados = {}
        def on_metodo_pago_id_obtenido(metodo_pago_id):
            resultados.clear()  # Limpiar resultados previos
            def on_ventas_obtenidas(datos_ventas):
                self._procesar_datos_optimizado(datos_ventas, True, tablewidget_ventas, label_58)

            def on_compras_obtenidas(datos_compras):
                self._procesar_datos_optimizado(datos_compras, False, tablewidget_compras, label_47)

            self.obtener_datos_ventas(metodo_pago_id, fecha, "id_metodo", on_ventas_obtenidas)
            self.obtener_datos_compras(metodo_pago_id, fecha, "id_metodo", on_compras_obtenidas)

        self.obtener_metodo_pago_id(metodo_pago_nombre, on_metodo_pago_id_obtenido)

    def _procesar_por_usuario(self, usuario_nombre, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47):
        """Procesar datos filtrados por usuario"""
        global usuarios_por_nombre_cache

        usuario_id = None
        if usuarios_por_nombre_cache and usuario_nombre in usuarios_por_nombre_cache:
            usuario_id = usuarios_por_nombre_cache[usuario_nombre][0]

        if not usuario_id:
            return

        def on_ventas_obtenidas(datos_ventas):
            self._procesar_datos_optimizado(datos_ventas, True, tablewidget_ventas, label_58)

        def on_compras_obtenidas(datos_compras):
            self._procesar_datos_optimizado(datos_compras, False, tablewidget_compras, label_47)

        self.obtener_datos_ventas(usuario_id, fecha, "id_usuario", on_ventas_obtenidas)
        self.obtener_datos_compras(usuario_id, fecha, "id_usuario", on_compras_obtenidas)

    def _procesar_por_categoria(self, nombre_categoria, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47):
        """Procesar datos filtrados por categoría"""
        global categorias_por_nombre_cache

        categoria_id = None
        if categorias_por_nombre_cache and nombre_categoria in categorias_por_nombre_cache:
            categoria_id = categorias_por_nombre_cache[nombre_categoria][0]

        if not categoria_id:
            return

        def on_ventas_obtenidas(datos_ventas):
            self._procesar_datos_optimizado(datos_ventas, True, tablewidget_ventas, label_58)

        def on_compras_obtenidas(datos_compras):
            self._procesar_datos_optimizado(datos_compras, False, tablewidget_compras, label_47)

        self.obtener_datos_ventas(categoria_id, fecha, "id_categoria", on_ventas_obtenidas)
        self.obtener_datos_compras(categoria_id, fecha, "id_categoria", on_compras_obtenidas)

    def _procesar_arqueo(self, fecha, tablewidget_ventas, tablewidget_compras, label_58, label_47):
        """Procesar datos de arqueo (sin filtros específicos)"""
        def on_ventas_arqueo_obtenidas(datos_ventas):
            self._procesar_datos_optimizado(datos_ventas, True, tablewidget_ventas, label_58)

        def on_compras_arqueo_obtenidas(datos_compras):
            self._procesar_datos_optimizado(datos_compras, False, tablewidget_compras, label_47)

        self.obtener_datos_arqueo_ventas_fecha(fecha, on_ventas_arqueo_obtenidas)
        self.obtener_datos_arqueo_compras_fecha(fecha, on_compras_arqueo_obtenidas)

    def traer_metodo_pago_cache(self, id_metodo):
        """Obtener método de pago desde cache local"""
        global metodos_pago_por_id_cache

        if metodos_pago_por_id_cache and str(id_metodo) in metodos_pago_por_id_cache:
            return metodos_pago_por_id_cache[str(id_metodo)]
        return "Método desconocido"
    
    def actualizar_combobox_13(self, combobox_12, combobox_13):
        combobox_13.clear()

        if combobox_12.currentText() == "Metodo de Pago":
            global metodos_pago_cache, metodos_pago_por_id_cache
            combobox_13.addItems(sorted(metodos_pago_por_id_cache.values()))

        elif combobox_12.currentText() == "Usuario":
            # Usar el cache global de usuarios
            global usuarios_por_nombre_cache
            if usuarios_por_nombre_cache:
                nombres = sorted(usuarios_por_nombre_cache.keys())
                combobox_13.addItems(nombres)

        elif combobox_12.currentText() == "Categoría":
            # Usar el cache global de categorías
            global categorias_por_nombre_cache
            if categorias_por_nombre_cache:
                nombres = sorted(categorias_por_nombre_cache.keys())
                combobox_13.addItems(nombres)

        else:
            combobox_13.addItem("")

    def actualizar_dias_combobox(self, combobox_10_dia, mes, anio):
        # Determinar el número de días en el mes
        if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 días
            dias = 31
        elif mes in [4, 6, 9, 11]:  # Meses con 30 días
            dias = 30
        else:  # Febrero
            # Año bisiesto: divisible por 4 y (no divisible por 100 o divisible por 400)
            dias = 29 if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)) else 28
    
        # Actualizar los días en el ComboBox
        combobox_10_dia.clear()
        combobox_10_dia.addItem("")  # Agregar un elemento vacío como primera opción
        combobox_10_dia.addItems([str(dia) for dia in range(1, dias + 1)])


    def hacer_corte(self):
        import tempfile
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        import webbrowser

        self.corte_id = uuid4()  # Generar un ID único para el corte actual

        combobox_12 = self.ui.frame_31.findChild(QComboBox, "comboBox_12")
        combobox_13 = self.ui.frame_31.findChild(QComboBox, "comboBox_13")
        filtro_tipo = combobox_12.currentText() if combobox_12 else ""
        filtro_valor = combobox_13.currentText() if combobox_13 else ""

        combobox_10_dia = self.ui.frame_32.findChild(QComboBox, "comboBox_10")
        combobox_9_mes = self.ui.frame_32.findChild(QComboBox, "comboBox_9")
        combobox_8_anio = self.ui.frame_32.findChild(QComboBox, "comboBox_8")

        dia = combobox_10_dia.currentText()
        mes = combobox_9_mes.currentIndex()
        if mes == 0:
            mes = None
        anio = combobox_8_anio.currentText()

        # Usar los datos ya procesados en la pantalla
        resultados = getattr(self, "resultados_arqueo", {})

        # Validar que hay datos suficientes
        if not resultados or "ventas_totales" not in resultados or "compras_totales" not in resultados:
            print("No hay datos suficientes para el corte. Realiza el arqueo primero.")
            return

        ventas_totales = resultados.get('ventas_totales', 0)
        ganancias_totales = resultados.get('ganancias_totales', 0)
        compras_totales = resultados.get('compras_totales', 0)
        numero_de_compras = resultados.get('numero_de_compras', 0)
        ventas_por_metodo = resultados.get('ventas_por_metodo', {})
        numero_de_ventas = resultados.get('numero_de_ventas', 0)

        filtro_texto = ""
        if filtro_tipo == "Metodo de Pago" and filtro_valor:
            filtro_texto = f"Filtrado por Método de Pago: {filtro_valor}"
        elif filtro_tipo == "Usuario" and filtro_valor:
            filtro_texto = f"Filtrado por Usuario: {filtro_valor}"
        elif filtro_tipo == "Categoría" and filtro_valor:
            filtro_texto = f"Filtrado por Categoría: {filtro_valor}"

        if dia and mes and anio:
            titulo_corte = f"Corte del Día {dia}/{int(mes):02d}/{anio}"
        elif mes and anio:
            titulo_corte = f"Corte del Mes {int(mes):02d}/{anio}"
        else:
            titulo_corte = f"Corte del Año {anio}"

        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        hora_actual = datetime.now().strftime("%I:%M %p")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
            ruta_pdf = temp_pdf.name

        c = canvas.Canvas(ruta_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(200, 750, titulo_corte)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, 730, f"Fecha de corte realizado: {fecha_actual}")
        c.drawString(50, 715, f"Hora de corte realizado: {hora_actual}")

        if filtro_texto:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(50, 700, filtro_texto)
            y_base = 685
        else:
            y_base = 700

        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y_base, f"Ventas Totales: ${ventas_totales:.2f}")
        c.drawString(300, y_base, f"Ganancias: ${ganancias_totales:.2f}")

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y_base - 30, "Ventas:")
        c.setFont("Helvetica", 10)
        y_pos = y_base - 45
        c.drawString(70, y_pos, f"Número de Ventas: {numero_de_ventas}")
        y_pos -= 15

        # Mostrar ventas por método de pago (sin ganancia)
        for metodo, total in ventas_por_metodo.items():
            metodo_pago_nombre = str(metodo)
            global metodos_pago_por_id_cache
            if metodos_pago_por_id_cache and str(metodo) in metodos_pago_por_id_cache:
                metodo_pago_nombre = metodos_pago_por_id_cache[str(metodo)]
            c.drawString(70, y_pos, f"{metodo_pago_nombre}: ${total:.2f}")
            y_pos -= 15

        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y_pos - 20, "Compras:")
        c.setFont("Helvetica", 10)
        y_pos -= 35
        c.drawString(70, y_pos, f"Total Compras: ${compras_totales:.2f}")
        c.drawString(70, y_pos - 15, f"Número de Compras: {numero_de_compras}")

        c.setFont("Helvetica-Oblique", 8)
        c.drawString(50, 50, "Generado automáticamente por el sistema rls.")

        c.setTitle(f"Corte - {fecha_actual}")  # Título del PDF

        c.save()
        webbrowser.open(f"file://{ruta_pdf}")
        


    # Función para copiar una columna al portapapeles
    
    def copy_entire_table_to_clipboard_ventas(self):
        table_widget = self.ui.frame_27.findChild(QTableWidget, "tableWidget_6")
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

    def copy_column_to_clipboard_ventas(self, column_index):

        # Intentar encontrar tableWidget_6 primero (ventas)
        table_widget = self.ui.frame_27.findChild(QTableWidget, "tableWidget_6")
        
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
    def copy_row_to_clipboard_ventas(self, row_index):
        # Intentar encontrar tableWidget_6 primero (ventas)
        table_widget = self.ui.frame_27.findChild(QTableWidget, "tableWidget_6")

        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

    def copy_entire_table_to_clipboard_compras(self):
        table_widget = self.ui.frame_23.findChild(QTableWidget, "tableWidget_7")
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

    def copy_column_to_clipboard_compras(self, column_index):

        # Intentar encontrar tableWidget_7 primero (compras)
        table_widget = self.ui.frame_23.findChild(QTableWidget, "tableWidget_7")

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
    def copy_row_to_clipboard_compras(self, row_index):
        # Intentar encontrar tableWidget_7 primero (compras)
        table_widget = self.ui.frame_23.findChild(QTableWidget, "tableWidget_7")

        if table_widget:
            row_data = []
            for col in range(table_widget.columnCount()):
                item = table_widget.item(row_index, col)
                if item:
                    row_data.append(item.text())
            clipboard = QApplication.clipboard()
            clipboard.setText("\t".join(row_data))
            self.show_copied_message("Fila copiada al portapapeles")

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

    # estadisticas

    def boton_estadisticas(self):
        push_button_13 = self.ui.tab_3.findChild(QPushButton, "pushButton_13")
        if push_button_13:
            push_button_13.clicked.connect(self.mostrar_estadisticas)

    def mostrar_estadisticas(self):
        label_101  = self.ui.stackedWidget.findChild(QLabel, "label_101")
        label_108 = self.ui.stackedWidget.findChild(QLabel, "label_108")
        label_109 = self.ui.stackedWidget.findChild(QLabel, "label_109")
        label_110 = self.ui.stackedWidget.findChild(QLabel, "label_110")
        label_111 = self.ui.stackedWidget.findChild(QLabel, "label_111")
        semana_actual = self.ui.stackedWidget.findChild(QPushButton, "pushButton_46")
        mes_anteriror = self.ui.stackedWidget.findChild(QPushButton, "pushButton_45")
        mes_actual = self.ui.stackedWidget.findChild(QPushButton, "pushButton_44")
        ano_actual = self.ui.stackedWidget.findChild(QPushButton, "pushButton_43")

        if label_101:
            label_101.setText(f"Ventas")

        if label_108:
            label_108.setText("$0.00")

        if label_109:
            label_109.setText("0")

        if label_110:
            label_110.setText("$0.00")

        if label_111:
            label_111.setText("$0.00")

        
        # acciones  

        if ano_actual:
            ano_actual.clicked.connect(self.mostrar_estadisticas_ano_actual)

        if mes_actual:
            mes_actual.clicked.connect(self.mostrar_estadisticas_mes_actual)

        if mes_anteriror:
            mes_anteriror.clicked.connect(self.mostrar_estadisticas_mes_anterior)

        if semana_actual:
            semana_actual.clicked.connect(self.mostrar_estadisticas_semana_actual)

        # Limpiar el gráfico en el widget
        parent_widget = self.ui.stackedWidget.findChild(QWidget, "widget")
        if parent_widget:
            layout = parent_widget.layout()
            if layout:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

        # Limpiar el gráfico en el widget_2
        widget_2 = self.ui.stackedWidget.findChild(QWidget, "widget_2")
        if widget_2:
            layout = widget_2.layout()
            if layout:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

    def mostrar_estadisticas_ano_actual(self):
        label_102 = self.ui.stackedWidget.findChild(QLabel, "label_102")
        label_103 = self.ui.stackedWidget.findChild(QLabel, "label_103")
        date_edit1 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit")
        date_edit2 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit_2")
        label_101  = self.ui.stackedWidget.findChild(QLabel, "label_101")
        label_108 = self.ui.stackedWidget.findChild(QLabel, "label_108")
        label_109 = self.ui.stackedWidget.findChild(QLabel, "label_109")
        label_110 = self.ui.stackedWidget.findChild(QLabel, "label_110")
        label_111 = self.ui.stackedWidget.findChild(QLabel, "label_111")
        widget_2 = self.ui.stackedWidget.findChild(QWidget, "widget_2")
        parent_widget = self.ui.stackedWidget.findChild(QWidget, "widget")

        ano_actual = datetime.now().year

        if label_102:
            label_102.setStyleSheet("color: transparent")
        if label_103:
            label_103.setStyleSheet("color: transparent")
        if date_edit1:
            date_edit1.setVisible(False)
        if date_edit2:
            date_edit2.setVisible(False)
        if label_101:
            label_101.setText(f"Ventas del Año {ano_actual}")

        # --- Hilos para los labels ---
        resultados = {}

        def check_and_update_labels():
            if len(resultados) == 4:
                if label_108:
                    label_108.setText(f"${resultados['ventas_totales']:.2f}")
                if label_109:
                    label_109.setText(f"{resultados['numero_de_ventas']}")
                if label_110:
                    label_110.setText(f"${resultados['venta_promedio']:.2f}")
                if label_111:
                    label_111.setText(f"${resultados['ganancias_totales']:.2f}")

        self.ventas_totales_ano_thread = TraerVentasTotalesAnoThread(ano_actual)
        self.numero_de_ventas_ano_thread = TraerNumeroDeVentasAnoThread(ano_actual)
        self.venta_promedio_ano_thread = TraerVentaPromedioAnoThread(ano_actual)
        self.ganancias_totales_ano_thread = TraerGananciasTotalesAnoThread(ano_actual)

        self.ventas_totales_ano_thread.resultado.connect(lambda x: (resultados.update({'ventas_totales': x}), check_and_update_labels()))
        self.numero_de_ventas_ano_thread.resultado.connect(lambda x: (resultados.update({'numero_de_ventas': x}), check_and_update_labels()))
        self.venta_promedio_ano_thread.resultado.connect(lambda x: (resultados.update({'venta_promedio': x}), check_and_update_labels()))
        self.ganancias_totales_ano_thread.resultado.connect(lambda x: (resultados.update({'ganancias_totales': x}), check_and_update_labels()))

        self.start_thread(self.ventas_totales_ano_thread)
        self.start_thread(self.numero_de_ventas_ano_thread)
        self.start_thread(self.venta_promedio_ano_thread)
        self.start_thread(self.ganancias_totales_ano_thread)

        # --- Hilos para la gráfica de ventas y ganancias ---
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        graf_resultados = {}

        def check_and_draw_graph():
            if 'ventas' in graf_resultados and 'ganancias' in graf_resultados:
                ventas = graf_resultados['ventas']
                ganancias = graf_resultados['ganancias']
                # Limpiar el layout si ya tiene un gráfico
                layout = parent_widget.layout()
                if layout:
                    while layout.count():
                        child = layout.takeAt(0)
                        if child.widget():
                            old_canvas = child.widget()
                            if isinstance(old_canvas, FigureCanvas):
                                old_canvas.figure.clear()
                                old_canvas.close()
                            old_canvas.deleteLater()
                fig = Figure(figsize=(6, 4))
                ax = fig.add_subplot(111)
                x = range(len(meses))
                ax.bar(x, ventas, width=0.4, label="Ventas", color="#2986CC", align="center")
                ax.bar([i + 0.4 for i in x], ganancias, width=0.4, label="Ganancias", color="lightgreen", align="center")
                ax.set_xticks([i + 0.2 for i in x])
                ax.set_xticklabels(meses, fontname="Segoe UI", fontsize=8)
                ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                ax.set_title("Ventas y Ganancias", fontname="Segoe UI", fontsize=12)
                legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                legend.get_frame().set_alpha(0.8)
                canvas = FigureCanvas(fig)
                if not layout:
                    layout = QVBoxLayout(parent_widget)
                    parent_widget.setLayout(layout)
                layout.addWidget(canvas)

        self.ventas_ano_thread = TraerVentasAnoActualThread(ano_actual, meses)
        self.ganancias_ano_thread = TraerGananciasAnoActualThread(ano_actual, meses)
        self.ventas_ano_thread.resultado.connect(lambda x: (graf_resultados.update({'ventas': x}), check_and_draw_graph()))
        self.ganancias_ano_thread.resultado.connect(lambda x: (graf_resultados.update({'ganancias': x}), check_and_draw_graph()))
        self.start_thread(self.ventas_ano_thread)
        self.start_thread(self.ganancias_ano_thread)

        # --- Hilos para la gráfica de métodos de pago ---
        if widget_2:
            graf2_resultados = {}
            colores = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF5", "#FFC300", "#DAF7A6", "#C70039"]

            def on_metodos_pago_obtenidos(metodos_pago):
                graf2_resultados['metodos_pago'] = metodos_pago
                graf2_resultados['datos_por_metodo'] = {}
                if not metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    ax.text(0.5, 0.5, "No hay métodos de pago disponibles", fontsize=12, ha='center', va='center', transform=ax.transAxes)
                    ax.axis("off")
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)
                else:
                    # Lanzar un hilo por cada método de pago
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        thread = TraerDatosPorMetodoYMesThread(ano_actual, id_metodo, meses)
                        def make_callback(idx, nombre_metodo):
                            return lambda datos: (
                                graf2_resultados['datos_por_metodo'].__setitem__(nombre_metodo, datos),
                                draw_metodos_graph()
                            )
                        thread.resultado.connect(make_callback(i, nombre_metodo))
                        self.start_thread(thread)

            def draw_metodos_graph():
                metodos_pago = graf2_resultados.get('metodos_pago', [])
                datos_por_metodo = graf2_resultados.get('datos_por_metodo', {})
                if len(datos_por_metodo) == len(metodos_pago) and metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = range(len(meses))
                    ancho_barra = 0.8 / len(metodos_pago)
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        datos = datos_por_metodo.get(nombre_metodo, [0]*len(meses))
                        posiciones = [pos + i * ancho_barra for pos in x]
                        ax.bar(posiciones, datos, width=ancho_barra, label=nombre_metodo, color=colores[i % len(colores)], align="center")
                    ax.set_xticks([pos + (ancho_barra * (len(metodos_pago) - 1)) / 2 for pos in x])
                    ax.set_xticklabels(meses, fontname="Segoe UI", fontsize=8, rotation=0)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas por Método de Pago", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)

            self.metodos_pago_y_id_thread = TraerMetodosPagoYSuIdThread()
            self.metodos_pago_y_id_thread.resultado.connect(on_metodos_pago_obtenidos)
            self.start_thread(self.metodos_pago_y_id_thread)

    def mostrar_estadisticas_mes_actual(self):
        label_102 = self.ui.stackedWidget.findChild(QLabel, "label_102")
        label_103 = self.ui.stackedWidget.findChild(QLabel, "label_103")
        date_edit1 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit")
        date_edit2 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit_2")
        label_101 = self.ui.stackedWidget.findChild(QLabel, "label_101")
        label_108 = self.ui.stackedWidget.findChild(QLabel, "label_108")
        label_109 = self.ui.stackedWidget.findChild(QLabel, "label_109")
        label_110 = self.ui.stackedWidget.findChild(QLabel, "label_110")
        label_111 = self.ui.stackedWidget.findChild(QLabel, "label_111")
        widget_2 = self.ui.stackedWidget.findChild(QWidget, "widget_2")
        widget = self.ui.stackedWidget.findChild(QWidget, "widget")

        mes_actual = datetime.now().month
        ano_actual = datetime.now().year

        if label_102:
            label_102.setStyleSheet("color: transparent")
        if label_103:
            label_103.setStyleSheet("color: transparent")
        if date_edit1:
            date_edit1.setVisible(False)
        if date_edit2:
            date_edit2.setVisible(False)
        if label_101:
            label_101.setText(f"Ventas del Mes {mes_actual}")

        # --- Hilos para los labels ---
        resultados = {}

        def check_and_update_labels():
            if len(resultados) == 4:
                if label_108:
                    label_108.setText(f"${resultados['ventas_totales']:.2f}")
                if label_109:
                    label_109.setText(f"{resultados['numero_de_ventas']}")
                if label_110:
                    label_110.setText(f"${resultados['venta_promedio']:.2f}")
                if label_111:
                    label_111.setText(f"${resultados['ganancias_totales']:.2f}")

        self.ventas_totales_mes_thread = TraerVentasTotalesMesThread(ano_actual, mes_actual)
        self.numero_de_ventas_mes_thread = TraerNumeroDeVentasMesThread(ano_actual, mes_actual)
        self.venta_promedio_mes_thread = TraerVentaPromedioMesThread(ano_actual, mes_actual)
        self.ganancias_totales_mes_thread = TraerGananciasTotalesMesThread(ano_actual, mes_actual)

        self.ventas_totales_mes_thread.resultado.connect(lambda x: (resultados.update({'ventas_totales': x}), check_and_update_labels()))
        self.numero_de_ventas_mes_thread.resultado.connect(lambda x: (resultados.update({'numero_de_ventas': x}), check_and_update_labels()))
        self.venta_promedio_mes_thread.resultado.connect(lambda x: (resultados.update({'venta_promedio': x}), check_and_update_labels()))
        self.ganancias_totales_mes_thread.resultado.connect(lambda x: (resultados.update({'ganancias_totales': x}), check_and_update_labels()))

        self.start_thread(self.ventas_totales_mes_thread)
        self.start_thread(self.numero_de_ventas_mes_thread)
        self.start_thread(self.venta_promedio_mes_thread)
        self.start_thread(self.ganancias_totales_mes_thread)

        # --- Hilos para la gráfica de ventas y ganancias del mes actual ---
        if widget:
            graf_resultados = {}

            def check_and_draw_graph():
                if 'ventas' in graf_resultados and 'ganancias' in graf_resultados:
                    ventas = graf_resultados['ventas']
                    ganancias = graf_resultados['ganancias']
                    layout = widget.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))  # Tamaño uniforme
                    ax = fig.add_subplot(111)
                    x = [mes_actual]  # Solo el mes actual
                    ax.bar(x, [ventas], width=0.4, label="Ventas", color="#2986CC", align="center")
                    ax.bar([i + 0.4 for i in x], [ganancias], width=0.4, label="Ganancias", color="lightgreen", align="center")
                    ax.set_xticks([i + 0.2 for i in x])
                    ax.set_xticklabels([mes_actual], fontname="Segoe UI", fontsize=8)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas y Ganancias del Mes Actual", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray", loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget)
                        widget.setLayout(layout)
                    layout.addWidget(canvas)

            self.ventas_mes_thread = TraerVentasTotalesMesThread(ano_actual, mes_actual)
            self.ganancias_mes_thread = TraerGananciasTotalesMesThread(ano_actual, mes_actual)
            self.ventas_mes_thread.resultado.connect(lambda x: (graf_resultados.update({'ventas': x}), check_and_draw_graph()))
            self.ganancias_mes_thread.resultado.connect(lambda x: (graf_resultados.update({'ganancias': x}), check_and_draw_graph()))
            self.start_thread(self.ventas_mes_thread)
            self.start_thread(self.ganancias_mes_thread)

        # --- Hilos para la gráfica de métodos de pago ---
        if widget_2:
            graf2_resultados = {}
            colores = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF5", "#FFC300", "#DAF7A6", "#C70039"]

            def on_metodos_pago_obtenidos(metodos_pago):
                graf2_resultados['metodos_pago'] = metodos_pago
                graf2_resultados['datos_por_metodo'] = {}
                if not metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    ax.text(0.5, 0.5, "No hay métodos de pago disponibles", fontsize=12, ha='center', va='center', transform=ax.transAxes)
                    ax.axis("off")
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)
                else:
                    # Lanzar un hilo por cada método de pago
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        thread = TraerDatosPorMetodoYMesThread(ano_actual, id_metodo, [mes_actual])
                        def make_callback(idx, nombre_metodo):
                            return lambda datos: (
                                graf2_resultados['datos_por_metodo'].__setitem__(nombre_metodo, datos),
                                draw_metodos_graph()
                            )
                        thread.resultado.connect(make_callback(i, nombre_metodo))
                        self.start_thread(thread)

            def draw_metodos_graph():
                metodos_pago = graf2_resultados.get('metodos_pago', [])
                datos_por_metodo = graf2_resultados.get('datos_por_metodo', {})
                if len(datos_por_metodo) == len(metodos_pago) and metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = [mes_actual]
                    ancho_barra = 0.8 / len(metodos_pago)
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        datos = datos_por_metodo.get(nombre_metodo, [0])
                        posiciones = [pos + i * ancho_barra for pos in x]
                        ax.bar(posiciones, datos, width=ancho_barra, label=nombre_metodo, color=colores[i % len(colores)], align="center")
                    ax.set_xticks([pos + (ancho_barra * (len(metodos_pago) - 1)) / 2 for pos in x])
                    ax.set_xticklabels([mes_actual], fontname="Segoe UI", fontsize=8, rotation=0)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas por Método de Pago del Mes Actual", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)

            self.metodos_pago_y_id_thread = TraerMetodosPagoYSuIdThread()
            self.metodos_pago_y_id_thread.resultado.connect(on_metodos_pago_obtenidos)
            self.start_thread(self.metodos_pago_y_id_thread)



    def mostrar_estadisticas_mes_anterior(self):
        label_102 = self.ui.stackedWidget.findChild(QLabel, "label_102")
        label_103 = self.ui.stackedWidget.findChild(QLabel, "label_103")
        date_edit1 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit")
        date_edit2 = self.ui.stackedWidget.findChild(QDateEdit, "dateEdit_2")
        label_101 = self.ui.stackedWidget.findChild(QLabel, "label_101")
        label_108 = self.ui.stackedWidget.findChild(QLabel, "label_108")
        label_109 = self.ui.stackedWidget.findChild(QLabel, "label_109")
        label_110 = self.ui.stackedWidget.findChild(QLabel, "label_110")
        label_111 = self.ui.stackedWidget.findChild(QLabel, "label_111")
        widget_2 = self.ui.stackedWidget.findChild(QWidget, "widget_2")
        widget = self.ui.stackedWidget.findChild(QWidget, "widget")

        mes_anterior = datetime.now().month - 1
        ano_actual = datetime.now().year

        if label_102:
            label_102.setStyleSheet("color: transparent")
        if label_103:
            label_103.setStyleSheet("color: transparent")
        if date_edit1:
            date_edit1.setVisible(False)
        if date_edit2:
            date_edit2.setVisible(False)
        if label_101:
            label_101.setText(f"Ventas del Mes {mes_anterior}")

        # --- Hilos para los labels ---
        resultados = {}

        def check_and_update_labels():
            if len(resultados) == 4:
                if label_108:
                    label_108.setText(f"${resultados['ventas_totales']:.2f}")
                if label_109:
                    label_109.setText(f"{resultados['numero_de_ventas']}")
                if label_110:
                    label_110.setText(f"${resultados['venta_promedio']:.2f}")
                if label_111:
                    label_111.setText(f"${resultados['ganancias_totales']:.2f}")

        self.ventas_totales_mes_thread = TraerVentasTotalesMesThread(ano_actual, mes_anterior)
        self.numero_de_ventas_mes_thread = TraerNumeroDeVentasMesThread(ano_actual, mes_anterior)
        self.venta_promedio_mes_thread = TraerVentaPromedioMesThread(ano_actual, mes_anterior)
        self.ganancias_totales_mes_thread = TraerGananciasTotalesMesThread(ano_actual, mes_anterior)

        self.ventas_totales_mes_thread.resultado.connect(lambda x: (resultados.update({'ventas_totales': x}), check_and_update_labels()))
        self.numero_de_ventas_mes_thread.resultado.connect(lambda x: (resultados.update({'numero_de_ventas': x}), check_and_update_labels()))
        self.venta_promedio_mes_thread.resultado.connect(lambda x: (resultados.update({'venta_promedio': x}), check_and_update_labels()))
        self.ganancias_totales_mes_thread.resultado.connect(lambda x: (resultados.update({'ganancias_totales': x}), check_and_update_labels()))

        self.start_thread(self.ventas_totales_mes_thread)
        self.start_thread(self.numero_de_ventas_mes_thread)
        self.start_thread(self.venta_promedio_mes_thread)
        self.start_thread(self.ganancias_totales_mes_thread)

        # --- Hilos para la gráfica de métodos de pago ---
        if widget_2:
            graf2_resultados = {}
            colores = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF5", "#FFC300", "#DAF7A6", "#C70039"]

            def on_metodos_pago_obtenidos(metodos_pago):
                graf2_resultados['metodos_pago'] = metodos_pago
                graf2_resultados['datos_por_metodo'] = {}
                if not metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    ax.text(0.5, 0.5, "No hay métodos de pago disponibles", fontsize=12, ha='center', va='center', transform=ax.transAxes)
                    ax.axis("off")
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)
                else:
                    # Lanzar un hilo por cada método de pago
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        thread = TraerDatosPorMetodoYMesThread(ano_actual, id_metodo, [mes_anterior])
                        def make_callback(idx, nombre_metodo):
                            return lambda datos: (
                                graf2_resultados['datos_por_metodo'].__setitem__(nombre_metodo, datos),
                                draw_metodos_graph()
                            )
                        thread.resultado.connect(make_callback(i, nombre_metodo))
                        self.start_thread(thread)

            def draw_metodos_graph():
                metodos_pago = graf2_resultados.get('metodos_pago', [])
                datos_por_metodo = graf2_resultados.get('datos_por_metodo', {})
                if len(datos_por_metodo) == len(metodos_pago) and metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = [mes_anterior]
                    ancho_barra = 0.8 / len(metodos_pago)
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        datos = datos_por_metodo.get(nombre_metodo, [0])
                        posiciones = [pos + i * ancho_barra for pos in x]
                        ax.bar(posiciones, datos, width=ancho_barra, label=nombre_metodo, color=colores[i % len(colores)], align="center")
                    ax.set_xticks([pos + (ancho_barra * (len(metodos_pago) - 1)) / 2 for pos in x])
                    ax.set_xticklabels([mes_anterior], fontname="Segoe UI", fontsize=8, rotation=0)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas por Método de Pago del Mes Anterior", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)

            self.metodos_pago_y_id_thread = TraerMetodosPagoYSuIdThread()
            self.metodos_pago_y_id_thread.resultado.connect(on_metodos_pago_obtenidos)
            self.start_thread(self.metodos_pago_y_id_thread)

        # --- Hilos para la gráfica de ventas y ganancias del mes anterior ---
        if widget:
            graf_resultados = {}

            def check_and_draw_graph():
                if 'ventas' in graf_resultados and 'ganancias' in graf_resultados:
                    ventas = graf_resultados['ventas']
                    ganancias = graf_resultados['ganancias']
                    layout = widget.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = [mes_anterior]
                    ax.bar(x, [ventas], width=0.4, label="Ventas", color="#2986CC", align="center")
                    ax.bar([i + 0.4 for i in x], [ganancias], width=0.4, label="Ganancias", color="lightgreen", align="center")
                    ax.set_xticks([i + 0.2 for i in x])
                    ax.set_xticklabels([mes_anterior], fontname="Segoe UI", fontsize=8)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas y Ganancias del Mes Anterior", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget)
                        widget.setLayout(layout)
                    layout.addWidget(canvas)

            self.ventas_mes_thread = TraerVentasTotalesMesThread(ano_actual, mes_anterior)
            self.ganancias_mes_thread = TraerGananciasTotalesMesThread(ano_actual, mes_anterior)
            self.ventas_mes_thread.resultado.connect(lambda x: (graf_resultados.update({'ventas': x}), check_and_draw_graph()))
            self.ganancias_mes_thread.resultado.connect(lambda x: (graf_resultados.update({'ganancias': x}), check_and_draw_graph()))
            self.start_thread(self.ventas_mes_thread)
            self.start_thread(self.ganancias_mes_thread)


    def mostrar_estadisticas_semana_actual(self):
        label_101 = self.ui.stackedWidget.findChild(QLabel, "label_101")
        label_108 = self.ui.stackedWidget.findChild(QLabel, "label_108")
        label_109 = self.ui.stackedWidget.findChild(QLabel, "label_109")
        label_110 = self.ui.stackedWidget.findChild(QLabel, "label_110")
        label_111 = self.ui.stackedWidget.findChild(QLabel, "label_111")
        widget_2 = self.ui.stackedWidget.findChild(QWidget, "widget_2")
        widget = self.ui.stackedWidget.findChild(QWidget, "widget")

        semana_actual = datetime.now().isocalendar()[1]
        ano_actual = datetime.now().year

        if label_101:
            label_101.setText(f"Ventas de la Semana {semana_actual}")

        # --- Hilos para los labels ---
        resultados = {}

        def check_and_update_labels():
            if len(resultados) == 4:
                if label_108:
                    label_108.setText(f"${resultados['ventas_totales']:.2f}")
                if label_109:
                    label_109.setText(f"{resultados['numero_de_ventas']}")
                if label_110:
                    label_110.setText(f"${resultados['venta_promedio']:.2f}")
                if label_111:
                    label_111.setText(f"${resultados['ganancias_totales']:.2f}")

        self.ventas_totales_semana_thread = TraerVentasTotalesSemanaThread(ano_actual, semana_actual)
        self.numero_de_ventas_semana_thread = TraerNumeroDeVentasSemanaThread(ano_actual, semana_actual)
        self.venta_promedio_semana_thread = TraerVentaPromedioSemanaThread(ano_actual, semana_actual)
        self.ganancias_totales_semana_thread = TraerGananciasTotalesSemanaThread(ano_actual, semana_actual)

        self.ventas_totales_semana_thread.resultado.connect(lambda x: (resultados.update({'ventas_totales': x}), check_and_update_labels()))
        self.numero_de_ventas_semana_thread.resultado.connect(lambda x: (resultados.update({'numero_de_ventas': x}), check_and_update_labels()))
        self.venta_promedio_semana_thread.resultado.connect(lambda x: (resultados.update({'venta_promedio': x}), check_and_update_labels()))
        self.ganancias_totales_semana_thread.resultado.connect(lambda x: (resultados.update({'ganancias_totales': x}), check_and_update_labels()))

        self.start_thread(self.ventas_totales_semana_thread)
        self.start_thread(self.numero_de_ventas_semana_thread)
        self.start_thread(self.venta_promedio_semana_thread)
        self.start_thread(self.ganancias_totales_semana_thread)

        # --- Hilos para la gráfica de ventas y ganancias de la semana ---
        if widget:
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
            graf_resultados = {}

            def check_and_draw_graph():
                if 'ventas' in graf_resultados and 'ganancias' in graf_resultados:
                    ventas = graf_resultados['ventas']
                    ganancias = graf_resultados['ganancias']
                    layout = widget.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget(): 
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = range(len(dias_semana))
                    ax.bar(x, ventas, width=0.4, label="Ventas", color="#2986CC", align="center")
                    ax.bar([i + 0.4 for i in x], ganancias, width=0.4, label="Ganancias", color="lightgreen", align="center")
                    ax.set_xticks([i + 0.2 for i in x])
                    ax.set_xticklabels(dias_semana, fontname="Segoe UI", fontsize=8)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas y Ganancias de la Semana Actual", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget)
                        widget.setLayout(layout)
                    layout.addWidget(canvas)

            self.ventas_semana_thread = TraerVentasSemanaActualThread(ano_actual, semana_actual, dias_semana)
            self.ganancias_semana_thread = TraerGananciasSemanaActualThread(ano_actual, semana_actual, dias_semana)
            self.ventas_semana_thread.resultado.connect(lambda x: (graf_resultados.update({'ventas': x}), check_and_draw_graph()))
            self.ganancias_semana_thread.resultado.connect(lambda x: (graf_resultados.update({'ganancias': x}), check_and_draw_graph()))
            self.start_thread(self.ventas_semana_thread)
            self.start_thread(self.ganancias_semana_thread)

        # --- Hilos para la gráfica de métodos de pago de la semana ---
        if widget_2:
            graf2_resultados = {}
            colores = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF", "#33FFF5", "#FFC300", "#DAF7A6", "#C70039"]
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

            def on_metodos_pago_obtenidos(metodos_pago):
                graf2_resultados['metodos_pago'] = metodos_pago
                graf2_resultados['datos_por_metodo'] = {}
                if not metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    ax.text(0.5, 0.5, "No hay métodos de pago disponibles", fontsize=12, ha='center', va='center', transform=ax.transAxes)
                    ax.axis("off")
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)
                else:
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        thread = TraerDatosPorMetodoYDiaSemanaThread(ano_actual, semana_actual, id_metodo, dias_semana)
                        def make_callback(idx, nombre_metodo):
                            return lambda datos: (
                                graf2_resultados['datos_por_metodo'].__setitem__(nombre_metodo, datos),
                                draw_metodos_graph()
                            )
                        thread.resultado.connect(make_callback(i, nombre_metodo))
                        self.start_thread(thread)

            def draw_metodos_graph():
                metodos_pago = graf2_resultados.get('metodos_pago', [])
                datos_por_metodo = graf2_resultados.get('datos_por_metodo', {})
                if len(datos_por_metodo) == len(metodos_pago) and metodos_pago:
                    layout = widget_2.layout()
                    if layout:
                        while layout.count():
                            child = layout.takeAt(0)
                            if child.widget():
                                old_canvas = child.widget()
                                if isinstance(old_canvas, FigureCanvas):
                                    old_canvas.figure.clear()
                                    old_canvas.close()
                                old_canvas.deleteLater()
                    fig = Figure(figsize=(6, 4))
                    ax = fig.add_subplot(111)
                    x = range(len(dias_semana))
                    ancho_barra = 0.8 / len(metodos_pago)
                    for i, metodo in enumerate(metodos_pago):
                        id_metodo = metodo[0]
                        nombre_metodo = metodo[1]
                        datos = datos_por_metodo.get(nombre_metodo, [0]*len(dias_semana))
                        posiciones = [pos + i * ancho_barra for pos in x]
                        ax.bar(posiciones, datos, width=ancho_barra, label=nombre_metodo, color=colores[i % len(colores)], align="center")
                    ax.set_xticks([pos + (ancho_barra * (len(metodos_pago) - 1)) / 2 for pos in x])
                    ax.set_xticklabels(dias_semana, fontname="Segoe UI", fontsize=8, rotation=0)
                    ax.set_ylabel("Monto ($)", fontname="Segoe UI", fontsize=10)
                    ax.set_title("Ventas por Método de Pago de la Semana Actual", fontname="Segoe UI", fontsize=12)
                    legend = ax.legend(prop={"family": "Segoe UI", "size": 8}, frameon=True, facecolor="white", edgecolor="gray",loc="upper right")
                    legend.get_frame().set_alpha(0.8)
                    canvas = FigureCanvas(fig)
                    if not layout:
                        layout = QVBoxLayout(widget_2)
                        widget_2.setLayout(layout)
                    layout.addWidget(canvas)

            self.metodos_pago_y_id_thread = TraerMetodosPagoYSuIdThread()
            self.metodos_pago_y_id_thread.resultado.connect(on_metodos_pago_obtenidos)
            self.start_thread(self.metodos_pago_y_id_thread)
    

    

################
################

class AdministracionTab:
    def __init__(self, ui, buscar_datos_tab, datos_tab):
        self.ui = ui
        self.facturero_ventas_window = None
        self.facturero_compras_window = None
        self.buscar_datos_tab = buscar_datos_tab  # Guarda la referenciaBuscarDatosTab
        self.datos_tab = datos_tab

        #crear arreglo con threads abiertos
        self.threads = []

        # Bandera para controlar que solo se abra un facturero a la vez
        self.facturero_activo = None  # None, "ventas" o "compras"

    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()

    def open_facturero_ventas(self):

        if self.facturero_activo == "compras" and self.facturero_compras_window:
            self.cerrar_facturero_compras()

        if not self.facturero_ventas_window:

            self.facturero_activo = "ventas"

            self.facturero_ventas_window = QDialog(self.ui.centralwidget)  # Set as a child of the main window
            self.facturero_ui = Ui_VentanaFactureroVentas()
            self.facturero_ui.setupUi(self.facturero_ventas_window)
            # Establece el icono y el título de la ventana principal
            self.facturero_ventas_window.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
            self.facturero_ventas_window.setWindowTitle("Facturero Ventas")
            self.facturero_ventas_window.setWindowModality(Qt.NonModal)
            self.facturero_ventas_window.setFixedSize(self.facturero_ventas_window.size())

            # Configuración de botones y etiquetas
            self._customize_facturero_ui(self.facturero_ventas_window, "rgb(198, 255, 202)")

            
            #se inicializa el arreglo de productos seleccionados del facturer ventas
            global productos_seleccionados_facturero_ventas
            productos_seleccionados_facturero_ventas = []

            # se inicializa el arreglo de productos cache temporal
            global productos_cache_temporal, productos_cache
            if productos_cache_temporal == None:
                productos_cache_temporal = copy.deepcopy(productos_cache)  # Copiar el contenido de productos_cache a productos_cache_temporal

            # inicializar la variable donde acumula el total de los prod agregados 
            global total_facturero_ventas
            total_facturero_ventas = 0

            line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
            if line_edit_18:
                line_edit_18.clear()  # Limpiar el QLineEdit al abrir la ventana

             # Inicializar los QLineEdit en blanco y no editables
            self.initialize_lineedits_ventas()

            # Configuración del QComboBox de IDs
            combobox_id = self.facturero_ventas_window.findChild(QComboBox, "comboBox")
            if combobox_id:
                combobox_id.setEditable(True)
                combobox_id.setFocus()
                combobox_id.setMaxVisibleItems(5)
                combobox_id.setInsertPolicy(QComboBox.NoInsert)
                combobox_id.setCompleter(None)

                # Eliminar la lógica que fuerza la apertura del menú desplegable
                combobox_id.lineEdit().textEdited.connect(lambda text: self.filter_combobox_ids(combobox_id, text))
                combobox_id.currentIndexChanged.connect(self.load_facturero_data_ventas)
                self.populate_combobox_with_ids(combobox_id)
                

            
            # Configuración del QComboBox de método de pago
            combobox_metodo_pago = self.facturero_ventas_window.findChild(QComboBox, "comboBox_3")
            if combobox_metodo_pago:
                combobox_metodo_pago.clear()
                combobox_metodo_pago.addItems([metodo for metodo in self.traer_metodos_de_pago()])
                
             # Configuración del botón "Agregar"
            boton_agregar = self.facturero_ventas_window.findChild(QPushButton, "pushButton_2")
            if boton_agregar:
                boton_agregar.setShortcut("Return")  # Conectar el botón al enter
                boton_agregar.clicked.connect(self.agregar_producto_a_tablewidget_ventas)

            label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setStyleSheet("color: transparent")

            #color propio del label12 de ventas
            label_12 = self.facturero_ventas_window.findChild(QLabel, "label_12")
            if label_12:
                label_12.setStyleSheet("color: green; font-weight: bold")

            text_edit = self.facturero_ventas_window.findChild(QTextEdit, "textEdit")
            if text_edit:
                text_edit.setFont(QFont("Segoe UI", 12))  # Set the font to Segoe UI with size 12
                text_edit.setReadOnly(True)
                text_edit.setFocusPolicy(Qt.NoFocus)
                

            push_button_4 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_4")
            if push_button_4:
                push_button_4.clicked.connect(self.cerrar_facturero_venta)
                push_button_4.setFocusPolicy(Qt.NoFocus)
            
            push_button = self.facturero_ventas_window.findChild(QPushButton, "pushButton")
            if push_button:
                push_button.clicked.connect(self.borrar_ultimo_agregado_ventas)
                push_button.setFocusPolicy(Qt.NoFocus)  

            pushbutton_3 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_3")
            if pushbutton_3:
                pushbutton_3.setEnabled(True)  # Deshabilitar el botón al inicio
                pushbutton_3.clicked.connect(self.procesar_factura_ventas)
                pushbutton_3.setFocusPolicy(Qt.NoFocus)

            push_button_5 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_5")
            if push_button_5:
                push_button_5.clicked.connect(self.ventana_agregar_mp_ventas)  # Conectar al método
                push_button_5.setFocusPolicy(Qt.NoFocus)                                 
 
            push_button_6 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_6")
            if push_button_6:
                push_button_6.clicked.connect(self.ventana_borrar_mp_ventas)
                push_button_6.setFocusPolicy(Qt.NoFocus)

            # Limitar el QLineEdit de cantidad a 5 caracteres
            lineedit_cantidad = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_2")
            if lineedit_cantidad:
                lineedit_cantidad.setMaxLength(5)

            qtablewidget = self.facturero_ventas_window.findChild(QTableWidget, "tableWidget")  
            if qtablewidget:
                qtablewidget.setStyleSheet("""
                QHeaderView::section {
                    background-color: rgb(198, 255, 202);
                    color: black;
                }
                """)
                #edicion y agregacion de datos a la table widget
                qtablewidget.setColumnCount(7)
                qtablewidget.setHorizontalHeaderLabels(["Producto", "Precio", "Cantidad", "Categoría", "Proveedor", "MP", "Total"])
                header = qtablewidget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 12))

            
            # Desactivar la cruz de cierre de la ventana
            self.facturero_ventas_window.setWindowFlags(self.facturero_ventas_window.windowFlags() & ~Qt.WindowCloseButtonHint)

            #visualizar productos del facturero
            self.visualizar_productos_facturero()
            
        
        self.facturero_ventas_window.show()

    def ventana_agregar_mp_ventas(self):
        
        # --- 1. Configurar el QDialog como ventana hija de self.facturero_ventas_window ---
        dialogo_agregar_mp = QDialog(self.facturero_ventas_window)  # ¡Ventana hija del facturero!
        dialogo_agregar_mp.setAttribute(Qt.WA_DeleteOnClose)  # Eliminar al cerrar

        # --- 2. Cargar la interfaz ---
        ui_ventana = Ui_Dialog()
        ui_ventana.setupUi(dialogo_agregar_mp)
        dialogo_agregar_mp.setWindowTitle("Agregar Método de Pago")
        dialogo_agregar_mp.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))

        # --- 3. Configurar widgets ---
        lineEdit = dialogo_agregar_mp.findChild(QLineEdit, "lineEdit")
        if lineEdit:
            lineEdit.setFocus()

        pushButton = dialogo_agregar_mp.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.setEnabled(True)  # Habilitar el botón al inicio
            pushButton.clicked.connect(lambda: self.agregar_metodo_de_pago_ventas(dialogo_agregar_mp))
            pushButton.setShortcut("Return")

        label_2 = dialogo_agregar_mp.findChild(QLabel, "label_2")
        if label_2:
            label_2.setStyleSheet("color: transparent")

        # --- 4. Mostrar la ventana ---
        dialogo_agregar_mp.exec()

    def agregar_metodo_de_pago_ventas(self, dialog):
        lineEdit = dialog.findChild(QLineEdit, "lineEdit")
        label_2 = dialog.findChild(QLabel, "label_2")
        combobox_metodo_pago_facturero = self.facturero_ventas_window.findChild(QComboBox, "comboBox_3")
        
        pushButton = dialog.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.setEnabled(False)
        

        if lineEdit:
            lineEdit_value = lineEdit.text()
    
            if lineEdit_value != "":
                lineEdit_value = lineEdit_value.strip()
    
                if not lineEdit_value[0].isupper():
                    lineEdit_value = lineEdit_value[0].upper() + lineEdit_value[1:]
    
                # Usar el hilo para agregar método de pago
                self.agregar_mp_thread = AgregarMPThread(lineEdit_value)
    
                def on_resultado(exito):
                    if exito:
                        #  Hilo para cargar movimiento de agregar método de pago
                        global usuario_activo, metodos_pago_por_id_cache, metodos_pago_cache
                        self.movimiento_agregar_mp_thread = MovimientoAgregarMetodoPagoThread(lineEdit_value, usuario_activo)
                        self.start_thread(self.movimiento_agregar_mp_thread)
    
                        # Actualizar el combobox usando un hilo
                        combobox_metodo_pago_facturero.setEnabled(False)  # Deshabilita el combobox antes de actualizar

                        self.metodos_pago_thread = TraerMetodosPagoYSuIdThread()
                        def on_metodos_obtenidos(metodos):
                            combobox_metodo_pago_facturero.clear()
                            
                            combobox_metodo_pago_facturero.addItems([metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1]])  # Asegúrate de que el método tenga al menos dos elementos
                            combobox_metodo_pago_facturero.setEnabled(True)  # Habilita el combobox cuando termina

                            #actualizar el cache de metodos
                            global metodos_pago_cache, metodos_pago_por_id_cache
                            metodos_pago_cache = metodos
                            metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos if m and len(m) > 1}
                      
                            label_2 = dialog.findChild(QLabel, "label_2")
                            if label_2:
                                label_2.setText("Método de pago agregado")
                                label_2.setStyleSheet("color: green; font-weight: bold")
                                QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))
                                lineEdit.clear()
                                lineEdit.setFocus()

                            pushButton = dialog.findChild(QPushButton, "pushButton")
                            if pushButton:
                                pushButton.setEnabled(True)

                        self.metodos_pago_thread.resultado.connect(on_metodos_obtenidos)
                        self.start_thread(self.metodos_pago_thread)
    
                    else:
                        pushButton = dialog.findChild(QPushButton, "pushButton")
                        if pushButton:
                            pushButton.setEnabled(True)

                        if label_2:
                            label_2.setText("El método de pago ya existe")
                            label_2.setStyleSheet("color: red; font-weight: bold")
                            QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))
    
                self.agregar_mp_thread.resultado.connect(on_resultado)
                self.start_thread(self.agregar_mp_thread)
            else:
                pushButton = dialog.findChild(QPushButton, "pushButton")
                if pushButton:
                    pushButton.setEnabled(True)

                if label_2:
                    label_2.setText("Por favor, complete el campo")
                    label_2.setStyleSheet("color: red; font-weight: bold")
                    QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))
                       
    def ventana_borrar_mp_ventas(self):
        
        # --- 1. Configurar el QDialog como ventana hija de self.facturero_ventas_window ---
        dialogo_borrar_mp = QDialog(self.facturero_ventas_window)  # Ventana hija del facturero
        dialogo_borrar_mp.setAttribute(Qt.WA_DeleteOnClose)  # Eliminar al cerrar

        # --- 2. Cargar la interfaz ---
        ui_ventana = Ui_Dialog2()
        ui_ventana.setupUi(dialogo_borrar_mp)
        dialogo_borrar_mp.setWindowTitle("Borrar Método de Pago")
        dialogo_borrar_mp.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
        global metodos_pago_cache, metodos_pago_por_id_cache

        # --- 3. Configurar widgets ---
        combobox = dialogo_borrar_mp.findChild(QComboBox, "comboBox")
        if combobox:
            combobox.clear()
            metodos_protegidos = {"Efectivo", "Transferencia", "Tarjeta de Crédito", "Tarjeta de Débito"}
            metodos_disponibles = [
                metodo for metodo in self.traer_metodos_de_pago() if metodo not in metodos_protegidos
            ]
            
            combobox.addItems(metodos_disponibles)
            combobox.setFocus()

        label = dialogo_borrar_mp.findChild(QLabel, "label")
        if label:
            label.setText("Método de Pago")

        label_2 = dialogo_borrar_mp.findChild(QLabel, "label_2")
        if label_2:
            label_2.setStyleSheet("color: transparent")

        label_3 = dialogo_borrar_mp.findChild(QLabel, "label_3")
        if label_3:
            label_3.setAlignment(Qt.AlignCenter)   
            label_3.setStyleSheet("font-weight: bold; color: red;")
            label_3.setText("Advertencia!\n Se eliminará lo relacionado al método")
             
        pushButton = dialogo_borrar_mp.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.setEnabled(True)  # Habilitar el botón al inicio
            pushButton.clicked.connect(lambda: self.borrar_metodo_de_pago_ventas(dialogo_borrar_mp))
            pushButton.setShortcut("Return")

        # --- 4. Mostrar la ventana ---
        dialogo_borrar_mp.exec()

    def borrar_metodo_de_pago_ventas(self, dialog):
        combobox_mp = dialog.findChild(QComboBox, "comboBox")
        label_2 = dialog.findChild(QLabel, "label_2")
        combobox_mp_facturero = self.facturero_ventas_window.findChild(QComboBox, "comboBox_3")

        if combobox_mp_facturero:
            combobox_mp_facturero.setEnabled(False)

        pushButton = dialog.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.setEnabled(False) 

        if combobox_mp:
            combobox_value = combobox_mp.currentText()

            if combobox_value != "":
                # ACA - Diálogo de confirmación
                dialogo_confirmacion = QMessageBox(dialog)
                dialogo_confirmacion.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
                dialogo_confirmacion.setWindowTitle("Confirmar eliminación")
                dialogo_confirmacion.setText(f"Está por borrar: \"{combobox_value}\"")
                dialogo_confirmacion.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                dialogo_confirmacion.setDefaultButton(QMessageBox.Cancel)

                # Personalizar el texto de los botones
                boton_aceptar = dialogo_confirmacion.button(QMessageBox.Ok)
                boton_cancelar = dialogo_confirmacion.button(QMessageBox.Cancel)
                if boton_aceptar:
                    boton_aceptar.setText("Aceptar")
                if boton_cancelar:
                    boton_cancelar.setText("Cancelar")

                # Mostrar el diálogo y verificar la respuesta
                respuesta = dialogo_confirmacion.exec()

                if respuesta == QMessageBox.Ok:
                    # Usuario confirmó, proceder con el borrado
                    # Usar el hilo para borrar método de pago
                    if label_2:
                        label_2.setText("Borrando método de pago...")
                        label_2.setStyleSheet("color: green; font-weight: bold")

                    self.borrar_mp_thread = BorrarMPThread(combobox_value)

                    def on_resultado(exito, id_metodo):
                        if exito:
                            #  Hilo para cargar movimiento de borrar método de pago
                            global usuario_activo
                            self.movimiento_borrar_mp_thread = MovimientoBorrarMetodoPagoThread(combobox_value, usuario_activo, id_metodo)
                            self.start_thread(self.movimiento_borrar_mp_thread)
                            
                            # Actualizar comboboxes usando un hilo
                            
                            def actualizar_comboboxes_metodos(metodos):
                                global metodos_pago_cache, metodos_pago_por_id_cache
                                metodos_protegidos = {"Efectivo", "Transferencia", "Tarjeta de Crédito", "Tarjeta de Débito"}
                                combobox_mp.clear()
                                metodos_filtrados = [metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1] and metodo[1] not in metodos_protegidos]
                                combobox_mp.addItems(metodos_filtrados)
                                combobox_mp.setCurrentText("")
                                
                                # combobox faCTURERO
                                combobox_mp_facturero.clear()
                                combobox_mp_facturero.addItems([metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1]])

                                global metodos_pago_cache, metodos_pago_por_id_cache
                                metodos_pago_cache = metodos
                                metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos if m and len(m) > 1}

                                #  Mostrar mensaje final después de cargar el movimiento
                                if label_2:
                                    label_2.setStyleSheet("color: green; font-weight: bold")
                                    label_2.setText("Método de pago eliminado con éxito")
                                    QTimer.singleShot(2000, lambda: label_2.setStyleSheet("color: transparent"))
                                    
                                pushButton = dialog.findChild(QPushButton, "pushButton")
                                if pushButton:
                                    pushButton.setEnabled(True) 
    
                                if combobox_mp_facturero:
                                    combobox_mp_facturero.setEnabled(True)  # Habilitar el combobox después de actualizar

                            self.metodos_pago_thread = TraerMetodosPagoYSuIdThread()
                            self.metodos_pago_thread.resultado.connect(actualizar_comboboxes_metodos)
                            self.start_thread(self.metodos_pago_thread)


                        else:
                            pushButton = dialog.findChild(QPushButton, "pushButton")
                            if pushButton:
                                pushButton.setEnabled(True) 

                            if label_2:
                                label_2.setText("Error al borrar el método de pago")
                                label_2.setStyleSheet("color: red; font-weight: bold")
                                QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))

                    self.borrar_mp_thread.resultado.connect(on_resultado)
                    self.start_thread(self.borrar_mp_thread)
                else:
                    # Usuario canceló, no hacer nada
                    pushButton = dialog.findChild(QPushButton, "pushButton")
                    if pushButton:
                        pushButton.setEnabled(True) 

                    if label_2:
                        label_2.setText("Operación cancelada")
                        label_2.setStyleSheet("color: blue; font-weight: bold")
                        QTimer.singleShot(1500, lambda: label_2.setStyleSheet("color: transparent"))
            else:
                pushButton = dialog.findChild(QPushButton, "pushButton")
                if pushButton:
                    pushButton.setEnabled(True) 

                if label_2:
                    label_2.setStyleSheet("color: red; font-weight: bold")
                    label_2.setText("Por favor, seleccione un método de pago")
                    QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))

    def initialize_lineedits_ventas(self):
        # Inicializar los QLineEdit en blanco y no editables
        lineedit_nombre = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_5")
        lineedit_precio = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit")
        lineedit_cantidad = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_2")
        lineedit_categoria = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_3")
        lineedit_proveedor = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_4")
        

        if lineedit_nombre:
            lineedit_nombre.setText("")
            lineedit_nombre.setReadOnly(True)
            lineedit_nombre.setFocusPolicy(Qt.NoFocus)

        if lineedit_precio:
            lineedit_precio.setText("")
            lineedit_precio.setReadOnly(True)
            lineedit_precio.setFocusPolicy(Qt.NoFocus)

        if lineedit_cantidad:
            lineedit_cantidad.setText("")
            

        if lineedit_categoria:
            lineedit_categoria.setText("")
            lineedit_categoria.setReadOnly(True)
            lineedit_categoria.setFocusPolicy(Qt.NoFocus)

        if lineedit_proveedor:
            lineedit_proveedor.setText("")
            lineedit_proveedor.setReadOnly(True)
            lineedit_proveedor.setFocusPolicy(Qt.NoFocus)

    def populate_combobox_with_ids(self, combobox):
        # Llenar el QComboBox con IDs usando el cache global
        combobox.clear()
        global productos_cache_temporal, productos

        # Si hay cache disponible, usarlo; si no, usar la variable global productos
        if productos_cache_temporal:
            productos_a_usar = productos_cache_temporal
        else:
            productos_a_usar = []

        if productos_a_usar:
            ids = [str(producto[0]) for producto in productos_a_usar]
            combobox.addItems(ids)

    def filter_combobox_ids(self, combobox, text):
        # Filtrar los elementos del QComboBox usando el cache global
        global productos_cache_temporal, productos
        
        # Si hay cache disponible, usarlo
        if productos_cache_temporal:
            productos_a_usar = productos_cache_temporal
        else:
            productos_a_usar = []
        
        if productos_a_usar:
            ids = [str(producto[0]) for producto in productos_a_usar if text.lower() in str(producto[0]).lower()]
            combobox.clear()
            combobox.addItems(ids)
            combobox.setCurrentText(text)

    def cerrar_facturero_venta(self):
        global productos_seleccionados_facturero_ventas, productos_cache_temporal
        
        # volver a productos cache la variable de productos cache temporal(ya que no va a hacerse ningun cambio)
        productos_cache_temporal = copy.deepcopy(productos_cache)

        # Se actualiza la tabla de productos
        self.borrar_lineedit_18()
        self.filter_products_facturero()

    
        self.facturero_ventas_window.close()
        self.facturero_ventas_window = None

        self.facturero_activo = None  # Reiniciar la bandera de facturero activo

    def borrar_lineedit_18(self):
        line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
        if line_edit_18:
            line_edit_18.clear()

    def load_facturero_data_ventas(self):
        # Cargar datos relacionados con el ID seleccionado en el QComboBox
        combobox_id = self.facturero_ventas_window.findChild(QComboBox, "comboBox")
        if combobox_id and combobox_id.currentText().isdigit():
            id_producto = combobox_id.currentText()

            # Usar el cache global de productos por ID
            global productos_por_id_cache
            producto = None

            if productos_por_id_cache and id_producto in productos_por_id_cache:
                producto = productos_por_id_cache[id_producto]

            if producto:
                # Suponiendo que `producto` es una tupla con los datos en este orden:
                # (id, nombre, precio_compra, precio_venta, stock, stock_ideal, categoria, proveedor)
                lineedit_nombre = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_5")
                lineedit_precio = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit")
                lineedit_cantidad = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_2")
                lineedit_categoria = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_3")
                lineedit_proveedor = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_4")

                # Convertir los valores a cadenas antes de asignarlos
                if lineedit_nombre:
                    lineedit_nombre.setText(str(producto[1]))  # Nombre del producto

                if lineedit_precio:
                    lineedit_precio.setText(str(producto[3]))  # Precio de venta

                if lineedit_cantidad:
                    lineedit_cantidad.setText(str(1))  # cantidad

                if lineedit_categoria:
                    lineedit_categoria.setText(str(producto[6]))  # Categoría

                if lineedit_proveedor:
                    lineedit_proveedor.setText(str(producto[7]))  # Proveedor

                # Seleccionar todo el texto del QComboBox para facilitar el borrado
                combobox_id.lineEdit().selectAll()
            else:
                # Si no se encuentra el producto en el cache, limpiar los campos
                self.initialize_lineedits_ventas()
        else:
            # Si no hay un ID válido seleccionado, limpiar los campos
            self.initialize_lineedits_ventas()

    def actualizar_total(self, s):

        if s:
            global total_facturero_ventas
            label_12 = self.facturero_ventas_window.findChild(QLabel, "label_12")
            if label_12:
                label_12.setText(f"${total_facturero_ventas:.2f}")
                label_12.setStyleSheet("color: green; font-weight: bold")
        else:
            global total_facturero_compras
            label_12 = self.facturero_compras_window.findChild(QLabel, "label_12")
            if label_12:
                label_12.setText(f"${total_facturero_compras:.2f}")
                label_12.setStyleSheet("color: rgb(230, 180, 80); font-weight: bold") 
    
    def es_decimal(self, valor):
        try:
            valor = valor.replace(",", ".")
            float(valor)  # Intenta convertir el valor a un número flotante
            return True
        except ValueError:
            return False
    

    def agregar_producto_a_tablewidget_ventas(self):
        global productos_seleccionados_facturero_ventas, productos_por_id_cache, productos_cache_temporal

        combobox_id = self.facturero_ventas_window.findChild(QComboBox, "comboBox")
        combobox_id_value = combobox_id.currentText()
        line_edit_nombre = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_5")
        line_edit_precio = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit")
        line_edit_cantidad = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_2")
        line_edit_categoria = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_3")
        line_edit_proveedor = self.facturero_ventas_window.findChild(QLineEdit, "lineEdit_4")
        combobox_metodo_pago = self.facturero_ventas_window.findChild(QComboBox, "comboBox_3")

        # Usar cache para verificar si el ID existe
        bandera = False
        if combobox_id_value.isdecimal() and productos_por_id_cache and combobox_id_value in productos_por_id_cache:
            bandera = True

        if bandera:
            qtablewidget = self.facturero_ventas_window.findChild(QTableWidget, "tableWidget")  

            # Verificar si hay una cantidad seleccionada
            if line_edit_cantidad:
                if "," in line_edit_cantidad.text():
                    lineEdit_cantidad_value = line_edit_cantidad.text().replace(",", ".")  
                else:
                    lineEdit_cantidad_value = line_edit_cantidad.text()

            if qtablewidget: 
                if (self.es_decimal(lineEdit_cantidad_value) or lineEdit_cantidad_value.isdigit()) and combobox_metodo_pago.currentText() != "":

                    # Crear el producto para agregar
                    producto_a_agregar = [
                        line_edit_nombre.text(),
                        float(line_edit_precio.text()),
                        float(lineEdit_cantidad_value),
                        line_edit_categoria.text(),
                        line_edit_proveedor.text(),
                        combobox_metodo_pago.currentText(),
                        float(line_edit_precio.text()) * float(lineEdit_cantidad_value)
                    ]
                    
                    # controla la cantidad para ver si sigue habiendo stock o no
                    resultado = self.controlar_cantidades2(producto_a_agregar, s=True)
        
                    if resultado:
                        # Agregar a la lista global
                        productos_seleccionados_facturero_ventas.append(producto_a_agregar)
                        #actualizar cantidad en producto
                        self.actualizar_stock_producto(productos_seleccionados_facturero_ventas[-1], s=True)

                         
                        row = qtablewidget.rowCount()
                        qtablewidget.insertRow(row)
                        for column, value in enumerate(productos_seleccionados_facturero_ventas[-1]):
                            item = QTableWidgetItem(str(value))
                            item.setFont(QFont("Segoe UI", 10))
                            qtablewidget.setItem(row, column, item)

                         # Actualizar el QTableWidget
                        self.filter_products_facturero()


                    else:
                        label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
                        if label_9 and combobox_id_value:
                            stock = self.traer_stock_restante(combobox_id_value)
                            label_9.setAlignment(Qt.AlignCenter)
                            label_9.setText(f"Stock restante: {stock}")
                            label_9.setStyleSheet("color: red; font-weight: bold")
                            QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))
                        
                        # Remover el último producto agregado si las cantidades no son válidas
                        #if productos_seleccionados_facturero_ventas:
                        #    productos_seleccionados_facturero_ventas.pop()

                      #agregar total 
                    global total_facturero_ventas
                    #actualiza el total de los productos agregados
                    total_facturero_ventas = sum([producto[-1] for producto in productos_seleccionados_facturero_ventas])
                    self.actualizar_total(s=True)

                else:
                    label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
                    if label_9:
                        label_9.setAlignment(Qt.AlignCenter)
                        label_9.setText("Complete todos los\ncampos correctamente")
                        label_9.setStyleSheet("color: red; font-weight: bold")
                        QTimer.singleShot(2000, lambda: label_9.setStyleSheet("color: transparent"))

        else:
            label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("Seleccione un ID válido")
                label_9.setStyleSheet("color: red; font-weight: bold")
                QTimer.singleShot(2000, lambda: label_9.setStyleSheet("color: transparent"))

        # Seleccionar todo el texto del QComboBox para facilitar el borrado
        combobox_id.setFocus()
        combobox_id.lineEdit().selectAll()


    def traer_stock_restante(self, id):
        # Usar el cache global de productos
        global productos_cache_temporal

        if productos_cache_temporal:
            for producto in productos_cache_temporal:
                if str(producto[0]) == str(id):  # producto[0] es el ID
                    return producto[4]  # producto[4] es el stock

        # Si no se encuentra en nada en cache, devolver 0
        return 0

    def controlar_cantidades2(self, producto_modificado, s):
        nombre = producto_modificado[0]
        cantidad = float(producto_modificado[2])
    
        # Usar el cache global de productos
        global productos_cache_temporal
        
        # Determinar qué cache usar
        cache_a_usar = productos_cache_temporal
        
        if not cache_a_usar:
            return False  # No hay datos en cache
        
        # Buscar el producto en el cache por nombre
        stock_actual = None
        for producto in cache_a_usar:
            if producto[1] == nombre:  # producto[1] es el nombre
                stock_actual = float(producto[4])  # producto[4] es el stock
                break
            
        if stock_actual is None:
            return False  # Producto no encontrado en cache
        
        op = stock_actual - cantidad
        
        if s:  # Si es venta
            if op >= 0 and cantidad > 0:
                return True
            else:
                return False
        else:  # Si es compra
            if cantidad > 0:
                return True
            else:
                return False

    def procesar_factura_ventas(self):
        s = True
        global productos_seleccionados_facturero_ventas, total_facturero_ventas, usuario_activo, productos_cache_temporal, productos_cache

        boton_agregar = self.facturero_ventas_window.findChild(QPushButton, "pushButton_2")
        if boton_agregar:
            boton_agregar.setEnabled(False)

        push_button = self.facturero_ventas_window.findChild(QPushButton, "pushButton")
        if push_button:
            push_button.setEnabled(False)

        pushbutton_3 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_3")
        if pushbutton_3:
            pushbutton_3.setEnabled(False)

        push_button_4 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_4")
        if push_button_4:
            push_button_4.setEnabled(False)

        if productos_seleccionados_facturero_ventas:

            label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("Procesando factura...")
                label_9.setStyleSheet("color: green; font-weight: bold")
            # Usar hilo para agregar a registro
            self.agregar_registro_thread = AgregarARegistroThread(
                productos_seleccionados_facturero_ventas, s, usuario_activo
            )

            def on_registro_agregado(exito):
                if exito:
                    #  ACTUALIZAR DESDE LA BASE DE DATOS, NO DESDE CACHE TEMPORAL
                    global productos_cache, productos_por_id_cache, productos_por_nombre_cache
                    productos_cache = None
                    productos_por_id_cache = None  
                    productos_por_nombre_cache = None
                    # Actualizar el cache desde la base de datos
                    self.datos_tab.actualizar_variables_globales_de_uso(3, lambda: (
                        self.filter_products_facturero(),
                        self.datos_tab.visualizar_datos()
                    ))
                    label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
                    if label_9:
                        label_9.setAlignment(Qt.AlignCenter)
                        label_9.setText("Factura procesada con éxito")
                        label_9.setStyleSheet("color: green; font-weight: bold")
                        QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))
                    pushbutton_3 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_3")
                    if pushbutton_3:
                        pushbutton_3.setEnabled(True)
                    push_button_4 = self.facturero_ventas_window.findChild(QPushButton, "pushButton_4")
                    if push_button_4:
                        push_button_4.setEnabled(True)

                    boton_agregar = self.facturero_ventas_window.findChild(QPushButton, "pushButton_2")
                    if boton_agregar:
                        boton_agregar.setEnabled(True)

                    push_button = self.facturero_ventas_window.findChild(QPushButton, "pushButton")
                    if push_button:
                        push_button.setEnabled(True)
                    # Llamar a inicializar_comboboxes_y_boton de la clase buscar datos
                    self.buscar_datos_tab.enviar_a_setear_tables()


                else:
                    print("Error al agregar a registro")

            self.agregar_registro_thread.resultado.connect(on_registro_agregado)
            self.start_thread(self.agregar_registro_thread)
        else:
            label_9 = self.facturero_ventas_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("No hay productos agregados")
                label_9.setStyleSheet("color: red; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))

            if push_button_4 and pushbutton_3 and push_button and boton_agregar:
                push_button_4.setEnabled(True)
                pushbutton_3.setEnabled(True)
                push_button.setEnabled(True)
                boton_agregar.setEnabled(True)

        qtablewidget = self.facturero_ventas_window.findChild(QTableWidget, "tableWidget")
        if qtablewidget:
            qtablewidget.setRowCount(0)

        total_facturero_ventas = 0
        productos_seleccionados_facturero_ventas = []

        self.actualizar_total(s=True)

        # Limpiar interfaz
        combobox_id = self.facturero_ventas_window.findChild(QComboBox, "comboBox")
        if combobox_id:
            combobox_id.setFocus()
            combobox_id.lineEdit().selectAll()


    def borrar_ultimo_agregado_ventas(self): 
        global productos_seleccionados_facturero_ventas, productos_cache_temporal

        if productos_seleccionados_facturero_ventas:
            
            self.actualizar_stock_producto(productos_seleccionados_facturero_ventas[-1], s=False)  # Actualizar el stock del último producto agregado

            #actualiza tabla de productos
            self.filter_products_facturero()

            self.actualizar_total(s=True)


        # Actualizar la interfaz del facturero
        qtablewidget = self.facturero_ventas_window.findChild(QTableWidget, "tableWidget") 
        if qtablewidget:
            row_count = qtablewidget.rowCount()
            if row_count > 0:
                qtablewidget.removeRow(row_count - 1)  # Remove the last row
                if productos_seleccionados_facturero_ventas:
                    productos_seleccionados_facturero_ventas.pop()
                    # Actualiza el total de los productos agregados
                    total_facturero_ventas = sum([producto[-1] for producto in productos_seleccionados_facturero_ventas])

        # Edita el label del total
        self.actualizar_total(s=True)


    #FUNCION PARA ACTUALIZAR CONSTANTEMENTE la tabla de productos por detras

    def visualizar_productos_facturero(self):
        global productos_cache_temporal
        self.populate_table_with_products_facturero()
        
        # Conectar el QLineEdit para filtrar productos
        line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
        if line_edit_18:
            line_edit_18.setFocus()
            line_edit_18.textChanged.connect(self.filter_products_facturero)
    
    def filter_products_facturero(self):
        
        line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
        table_widget = self.ui.frame_tabla_productos_4.findChild(QTableWidget, "tableWidget_4")

        if line_edit_18 and table_widget:
            filter_text = line_edit_18.text().lower()

            # Configurar la tabla 
            corner_button = table_widget.findChild(QAbstractButton)
            if corner_button:
                corner_button.clicked.connect(self.copy_entire_table_to_clipboard)
            table_widget.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard)
            table_widget.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard)
            table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

            # Usar el cache global de productos
            global productos_cache_temporal

        
            if productos_cache_temporal:
                productos_a_usar = productos_cache_temporal
            else:
                productos_a_usar = []
            

            filtered_productos = []
            for producto in productos_a_usar:
                if filter_text in producto[1].lower() or filter_text in str(producto[0]).lower():
                    filtered_productos.append(producto)

            cantidad = len(filtered_productos) if filtered_productos else 0

            # Si no se encuentran productos, mostrar un mensaje en la tabla
            if cantidad == 0:
                label_123 = self.ui.frame_60.findChild(QLabel, "label_123")
                if label_123:
                    label_123.clear()
                    label_123.setText("0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_123 = self.ui.frame_60.findChild(QLabel, "label_123")
                if label_123:
                    label_123.clear()
                    label_123.setText(f"{cantidad}")

                # Si hay productos, llenar la tabla con los datos filtrados
                table_widget.setRowCount(len(filtered_productos))
                table_widget.setColumnCount(8)
                table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Precio Compra", "Precio Venta", "Stock", "Stock Ideal", "Categoría", "Proveedor"])

                # Configurar el header 
                header = table_widget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 16, QFont.Bold))

                for row, producto in enumerate(filtered_productos):
                    for col, value in enumerate(producto):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))
                        item.setTextAlignment(Qt.AlignCenter)

                        # Aplicar color rojo si el stock es menor al ideal 
                        if col == 4 and float(producto[4]) < float(producto[5]):
                            item.setForeground(Qt.red)

                        table_widget.setItem(row, col, item)

            # NO cambiar el texto del line_edit para mantener el filtro
            # line_edit_18.setText(filter_text)  # Esta línea causaba problemas
            # line_edit_18.setFocus()  # Esta línea también puede interferir

    def populate_table_with_products_facturero(self):
        table_widget = self.ui.frame_tabla_productos_4.findChild(QTableWidget, "tableWidget_4")

        line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
        if table_widget:
            corner_button = table_widget.findChild(QAbstractButton)

            corner_button.clicked.connect(self.copy_entire_table_to_clipboard)
            table_widget.horizontalHeader().sectionDoubleClicked.connect(self.copy_column_to_clipboard)
            table_widget.verticalHeader().sectionDoubleClicked.connect(self.copy_row_to_clipboard)
            table_widget.setEditTriggers(QTableWidget.NoEditTriggers)

            filter_text = line_edit_18.text().lower()

            # Usar el cache global de productos
            global productos_cache

            # Si hay cache disponible, usarlo; si no, usar la variable global productos y CONTROLA SI ES VENTA O COMPRA
            
            if productos_cache:
                productos_a_usar = productos_cache
            else:
                productos_a_usar = []

            cantidad = len(productos_a_usar) if productos_a_usar else 0
            
            # Si no se encuentran productos, mostrar un mensaje en la tabla
            if cantidad == 0:
                label_123 = self.ui.frame_60.findChild(QLabel, "label_123")
                if label_123:
                    label_123.clear()
                    label_123.setText("0")

                table_widget.setRowCount(1)
                table_widget.setColumnCount(1)
                table_widget.setHorizontalHeaderLabels(["Mensaje"])
                item = QTableWidgetItem("No se encontraron productos")
                item.setFont(QFont("Segoe ui", 12))
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(0, 0, item)
            else:
                label_123 = self.ui.frame_60.findChild(QLabel, "label_123")
                if label_123:
                    label_123.clear()
                    label_123.setText(f"{cantidad}")
                    
                # Si hay productos, llenar la tabla con los datos
                table_widget.setRowCount(len(productos_a_usar))
                table_widget.setColumnCount(8)
                table_widget.setHorizontalHeaderLabels(["ID", "Nombre", "Precio Compra", "Precio Venta", "Stock", "Stock Ideal", "Categoría", "Proveedor"])
                header = table_widget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 16, QFont.Bold))  # Set font size to 16 and bold
                for row, producto in enumerate(productos_a_usar):
                    for col, value in enumerate(producto):
                        item = QTableWidgetItem(str(value))
                        item.setFont(QFont("Segoe ui", 12))  # Set the font size to 12pt
                        item.setTextAlignment(Qt.AlignCenter)  # Center align the text
                        if col == 4 and float(producto[4]) < float(producto[5]):  # Check if stock is less than stock ideal
                            item.setForeground(Qt.red)
                        table_widget.setItem(row, col, item)

            line_edit_18.setText(filter_text)
            line_edit_18.setFocus()

    # Función para copiar una columna al portapapeles
    def copy_column_to_clipboard(self, column_index):
        table_widget = self.ui.frame_tabla_productos_4.findChild(QTableWidget, "tableWidget_4")
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
        table_widget = self.ui.frame_tabla_productos_4.findChild(QTableWidget, "tableWidget_4")
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
        table_widget = self.ui.frame_tabla_productos_4.findChild(QTableWidget, "tableWidget_4")
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



    #######################################################################################
    #######################################################################################


    def open_facturero_compras(self):


        if self.facturero_activo == "ventas" and self.facturero_ventas_window:
            self.cerrar_facturero_venta()
            

        if not self.facturero_compras_window:

            self.facturero_activo = "compras"

            self.facturero_compras_window = QDialog(self.ui.centralwidget)
            self.facturero_ui = Ui_VentanaFactureroCompras()
            self.facturero_ui.setupUi(self.facturero_compras_window)
            self.facturero_compras_window.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
            self.facturero_compras_window.setWindowTitle("Facturero Compras")
            self.facturero_compras_window.setWindowModality(Qt.NonModal)
            self.facturero_compras_window.setFixedSize(self.facturero_compras_window.size())

            # Configuración de botones y etiquetas
            self._customize_facturero_ui(self.facturero_compras_window, "rgb(255, 230, 107)")


            #se inicializa el arreglo de productos seleccionados del facturer ventas
            global productos_seleccionados_facturero_compras
            productos_seleccionados_facturero_compras = []

             # se inicializa el arreglo de productos cache temporal
            global productos_cache_temporal, productos_cache
            if productos_cache_temporal == None:
                productos_cache_temporal = copy.deepcopy(productos_cache)

            # inicializar la variable donde acumula el total de los prod agregados 
            global total_facturero_compras
            total_facturero_compras = 0

            line_edit_18 = self.ui.frame_38.findChild(QLineEdit, "lineEdit_18")
            if line_edit_18:
                line_edit_18.clear()  # Limpiar el QLineEdit al abrir la ventana

            # Inicializar los QLineEdit en blanco y no editables
            self.initialize_lineedits_compras()

            # Configuración del QComboBox de IDs
            combobox_id = self.facturero_compras_window.findChild(QComboBox, "comboBox")
            if combobox_id:
                combobox_id.setEditable(True)
                combobox_id.setFocus()
                combobox_id.setMaxVisibleItems(5)
                combobox_id.setInsertPolicy(QComboBox.NoInsert)
                combobox_id.setCompleter(None)


                # Eliminar la lógica que fuerza la apertura del menú desplegable
                combobox_id.lineEdit().textEdited.connect(lambda text: self.filter_combobox_ids(combobox_id, text))
                combobox_id.currentIndexChanged.connect(self.load_facturero_data_compras)
                self.populate_combobox_with_ids(combobox_id)
                

            
            # Configuración del QComboBox de método de pago
            combobox_metodo_pago = self.facturero_compras_window.findChild(QComboBox, "comboBox_3")
            if combobox_metodo_pago:
                combobox_metodo_pago.clear()
                combobox_metodo_pago.addItems([metodo for metodo in self.traer_metodos_de_pago()])
                
                
            
             # Configuración del botón "Agregar"
            boton_agregar = self.facturero_compras_window.findChild(QPushButton, "pushButton_2")
            if boton_agregar:
                boton_agregar.setShortcut("Return")  # Conectar el botón al enter
                boton_agregar.clicked.connect(self.agregar_producto_a_tablewidget_compras)

            label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setStyleSheet("color: transparent")

            #color propio del label12 de compras
            label_12 = self.facturero_compras_window.findChild(QLabel, "label_12")
            if label_12:
                label_12.setStyleSheet("color: rgb(230, 180, 80); font-weight: bold")

            text_edit = self.facturero_compras_window.findChild(QTextEdit, "textEdit")
            if text_edit:
                text_edit.setFont(QFont("Segoe UI", 12))  # Set the font to Segoe UI with size 12
                text_edit.setReadOnly(True)
                text_edit.setFocusPolicy(Qt.NoFocus)
                


            push_button_4 = self.facturero_compras_window.findChild(QPushButton, "pushButton_4")
            if push_button_4:
                push_button_4.clicked.connect(self.cerrar_facturero_compras)
                push_button_4.setFocusPolicy(Qt.NoFocus)
            
            push_button = self.facturero_compras_window.findChild(QPushButton, "pushButton")
            if push_button:
                push_button.clicked.connect(self.borrar_ultimo_agregado_compras)
                push_button.setFocusPolicy(Qt.NoFocus)

            pushbutton_3 = self.facturero_compras_window.findChild(QPushButton, "pushButton_3")
            if pushbutton_3:
                pushbutton_3.clicked.connect(self.procesar_factura_compras)
                pushbutton_3.setFocusPolicy(Qt.NoFocus)


            push_button_5 = self.facturero_compras_window.findChild(QPushButton, "pushButton_7")
            if push_button_5:
                push_button_5.clicked.connect(self.ventana_agregar_mp_compras)  # Conectar al método
                push_button_5.setFocusPolicy(Qt.NoFocus)                                 
 
            push_button_6 = self.facturero_compras_window.findChild(QPushButton, "pushButton_8")
            if push_button_6:
                push_button_6.clicked.connect(self.ventana_borrar_mp_compras)
                push_button_6.setFocusPolicy(Qt.NoFocus)

            # Limitar el QLineEdit de cantidad a 5 caracteres
            lineedit_cantidad = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_2")
            if lineedit_cantidad:
                lineedit_cantidad.setMaxLength(5)

            qtablewidget = self.facturero_compras_window.findChild(QTableWidget, "tableWidget")  
            if qtablewidget:
                qtablewidget.setStyleSheet("""
                QHeaderView::section {
                    background-color: rgb(255, 230, 107);
                    color: black;
                }
                """)
                #edicion y agregacion de datos a la table widget
                qtablewidget.setColumnCount(7)
                qtablewidget.setHorizontalHeaderLabels(["Producto", "Precio", "Cantidad", "Categoría", "Proveedor", "MP", "Total"])
                header = qtablewidget.horizontalHeader()
                header.setFont(QFont("Segoe UI", 12))

            
            # Desactivar la cruz de cierre de la ventana
            self.facturero_compras_window.setWindowFlags(self.facturero_compras_window.windowFlags() & ~Qt.WindowCloseButtonHint)

            # visualizar productos
            self.visualizar_productos_facturero()

        self.facturero_compras_window.show()


    def ventana_agregar_mp_compras(self):
        
        # --- 1. Configurar el QDialog como ventana hija de self.facturero_ventas_window ---
        dialogo_agregar_mp = QDialog(self.facturero_compras_window)  # ¡Ventana hija del facturero!
        dialogo_agregar_mp.setAttribute(Qt.WA_DeleteOnClose)  # Eliminar al cerrar

        # --- 2. Cargar la interfaz ---
        ui_ventana = Ui_Dialog()
        ui_ventana.setupUi(dialogo_agregar_mp)
        dialogo_agregar_mp.setWindowTitle("Agregar Método de Pago")
        dialogo_agregar_mp.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))

        # --- 3. Configurar widgets ---
        lineEdit = dialogo_agregar_mp.findChild(QLineEdit, "lineEdit")
        if lineEdit:
            lineEdit.setFocus()

        pushButton = dialogo_agregar_mp.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.clicked.connect(lambda: self.agregar_metodo_de_pago_compras(dialogo_agregar_mp))
            pushButton.setShortcut("Return")

        label_2 = dialogo_agregar_mp.findChild(QLabel, "label_2")
        if label_2:
            label_2.setStyleSheet("color: transparent")

        # --- 4. Mostrar la ventana ---
        dialogo_agregar_mp.exec()

    def agregar_metodo_de_pago_compras(self, dialog):
        lineEdit = dialog.findChild(QLineEdit, "lineEdit")
        label_2 = dialog.findChild(QLabel, "label_2")
        # Obtener el combobox del facturero principal, no del diálogo
        combobox_metodo_pago_facturero = self.facturero_compras_window.findChild(QComboBox, "comboBox_3")

        if lineEdit:
            lineEdit_value = lineEdit.text()

            if lineEdit_value != "":

                # Remove leading and trailing spaces
                lineEdit_value = lineEdit_value.strip()

                if not lineEdit_value[0].isupper():
                    lineEdit_value = lineEdit_value[0].upper() + lineEdit_value[1:]
                
                # Usar el hilo para agregar método de pago
                self.agregar_mp_thread = AgregarMPThread(lineEdit_value)
    
                def on_resultado(exito):
                    if exito:
                        #  Hilo para cargar movimiento de agregar método de pago
                        global usuario_activo, metodos_pago_por_id_cache, metodos_pago_cache
                        self.movimiento_agregar_mp_thread = MovimientoAgregarMetodoPagoThread(lineEdit_value, usuario_activo)
                        self.start_thread(self.movimiento_agregar_mp_thread)
    
                        # Actualizar el combobox usando un hilo
                        combobox_metodo_pago_facturero.setEnabled(False)  # Deshabilita el combobox antes de actualizar

                        self.metodos_pago_thread = TraerMetodosPagoYSuIdThread()
                        def on_metodos_obtenidos(metodos):
                            combobox_metodo_pago_facturero.clear()
                            
                            combobox_metodo_pago_facturero.addItems([metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1]])  # Asegúrate de que el método tenga al menos dos elementos
                            combobox_metodo_pago_facturero.setEnabled(True)  # Habilita el combobox cuando termina

                            #actualizar el cache de metodos
                            global metodos_pago_cache, metodos_pago_por_id_cache
                            metodos_pago_cache = metodos
                            metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos if m and len(m) > 1}
                      
                            label_2 = dialog.findChild(QLabel, "label_2")
                            if label_2:
                                label_2.setText("Método de pago agregado")
                                label_2.setStyleSheet("color: green; font-weight: bold")
                                QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))
                                lineEdit.clear()
                                lineEdit.setFocus()

                            pushButton = dialog.findChild(QPushButton, "pushButton")
                            if pushButton:
                                pushButton.setEnabled(True)

                        self.metodos_pago_thread.resultado.connect(on_metodos_obtenidos)
                        self.start_thread(self.metodos_pago_thread)
    
                    else:
                        pushButton = dialog.findChild(QPushButton, "pushButton")
                        if pushButton:
                            pushButton.setEnabled(True)

                        if label_2:
                            label_2.setText("El método de pago ya existe")
                            label_2.setStyleSheet("color: red; font-weight: bold")
                            QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))
    
                self.agregar_mp_thread.resultado.connect(on_resultado)
                self.start_thread(self.agregar_mp_thread)
            else:
                pushButton = dialog.findChild(QPushButton, "pushButton")
                if pushButton:
                    pushButton.setEnabled(True)

                if label_2:
                    label_2.setText("Por favor, complete el campo")
                    label_2.setStyleSheet("color: red; font-weight: bold")
                    QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))


    def ventana_borrar_mp_compras(self):
        
        # --- 1. Configurar el QDialog como ventana hija de self.facturero_ventas_window ---
        dialogo_borrar_mp = QDialog(self.facturero_compras_window)  # Ventana hija del facturero
        dialogo_borrar_mp.setAttribute(Qt.WA_DeleteOnClose)  # Eliminar al cerrar

        # --- 2. Cargar la interfaz ---
        ui_ventana = Ui_Dialog2()
        ui_ventana.setupUi(dialogo_borrar_mp)
        dialogo_borrar_mp.setWindowTitle("Borrar Método de Pago")
        dialogo_borrar_mp.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))

       # --- 3. Configurar widgets ---
        combobox = dialogo_borrar_mp.findChild(QComboBox, "comboBox")
        if combobox:
            combobox.clear()
            #  Filtrar métodos de pago para excluir "Efectivo" y "Transferencia"
            metodos_protegidos = {"Efectivo", "Transferencia", "Tarjeta de Crédito", "Tarjeta de Débito"}
            metodos_disponibles = [
                metodo for metodo in self.traer_metodos_de_pago() 
                if metodo not in metodos_protegidos
            ]
            combobox.addItems(metodos_disponibles)
            combobox.setFocus()

        label_2 = dialogo_borrar_mp.findChild(QLabel, "label_2")
        if label_2:
            label_2.setStyleSheet("color: transparent")

        label = dialogo_borrar_mp.findChild(QLabel, "label")
        if label:
            label.setText("Método de Pago")

        label_3 = dialogo_borrar_mp.findChild(QLabel, "label_3")
        if label_3:
            label_3.setAlignment(Qt.AlignCenter)       
            label_3.setStyleSheet("font-weight: bold; color: red;")
            label_3.setText("Advertencia!\n Se eliminará lo relacionado al método")

        pushButton = dialogo_borrar_mp.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.clicked.connect(lambda: self.borrar_metodo_de_pago_compras(dialogo_borrar_mp))
            pushButton.setShortcut("Return")

        # --- 4. Mostrar la ventana ---
        dialogo_borrar_mp.exec()

    def traer_metodos_de_pago(self):
        global metodos_pago_por_id_cache
        if metodos_pago_por_id_cache:
            # Retorna solo los nombres (los valores del diccionario)
            return list(metodos_pago_por_id_cache.values())
        return []

    def borrar_metodo_de_pago_compras(self, dialog):
        combobox_mp = dialog.findChild(QComboBox, "comboBox")
        label_2 = dialog.findChild(QLabel, "label_2")
        combobox_mp_facturero = self.facturero_compras_window.findChild(QComboBox,"comboBox_3")

        pushButton = dialog.findChild(QPushButton, "pushButton")
        if pushButton:
            pushButton.setEnabled(False) 
        
        if combobox_mp:
            combobox_value = combobox_mp.currentText()

            if combobox_value != "":
                # ACA - Diálogo de confirmación
                dialogo_confirmacion = QMessageBox(dialog)
                dialogo_confirmacion.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
                dialogo_confirmacion.setWindowTitle("Confirmar eliminación")
                dialogo_confirmacion.setText(f"Está por borrar: \"{combobox_value}\"")
                dialogo_confirmacion.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                dialogo_confirmacion.setDefaultButton(QMessageBox.Cancel)

                # Personalizar el texto de los botones
                boton_aceptar = dialogo_confirmacion.button(QMessageBox.Ok)
                boton_cancelar = dialogo_confirmacion.button(QMessageBox.Cancel)
                if boton_aceptar:
                    boton_aceptar.setText("Aceptar")
                if boton_cancelar:
                    boton_cancelar.setText("Cancelar")

                # Mostrar el diálogo y verificar la respuesta
                respuesta = dialogo_confirmacion.exec()

                if respuesta == QMessageBox.Ok:
                    # Usuario confirmó, proceder con el borrado
                    # Usar el hilo para borrar método de pago
                    if label_2:
                        label_2.setText("Borrando método de pago...")
                        label_2.setStyleSheet("color: green; font-weight: bold")

                    self.borrar_mp_thread = BorrarMPThread(combobox_value)

                    def on_resultado(exito, id_metodo):
                        if exito:
                            #  Hilo para cargar movimiento de borrar método de pago
                            global usuario_activo
                            self.movimiento_borrar_mp_thread = MovimientoBorrarMetodoPagoThread(combobox_value, usuario_activo, id_metodo)
                            self.start_thread(self.movimiento_borrar_mp_thread)
                            
                            # Actualizar comboboxes usando un hilo
                            
                            def actualizar_comboboxes_metodos(metodos):
                                global metodos_pago_cache, metodos_pago_por_id_cache
                                metodos_protegidos = {"Efectivo", "Transferencia", "Tarjeta de Crédito", "Tarjeta de Débito"}
                                combobox_mp.clear()
                                metodos_filtrados = [metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1] and metodo[1] not in metodos_protegidos]
                                combobox_mp.addItems(metodos_filtrados)
                                combobox_mp.setCurrentText("")
                                
                                # combobox faCTURERO
                                combobox_mp_facturero.clear()
                                combobox_mp_facturero.addItems([metodo[1] for metodo in metodos if metodo and len(metodo) > 1 and metodo[1]])

                                global metodos_pago_cache, metodos_pago_por_id_cache
                                metodos_pago_cache = metodos
                                metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos if m and len(m) > 1}

                                #  Mostrar mensaje final después de cargar el movimiento
                                if label_2:
                                    label_2.setStyleSheet("color: green; font-weight: bold")
                                    label_2.setText("Método de pago eliminado con éxito")
                                    QTimer.singleShot(2000, lambda: label_2.setStyleSheet("color: transparent"))
                                    
                                pushButton = dialog.findChild(QPushButton, "pushButton")
                                if pushButton:
                                    pushButton.setEnabled(True) 
    
                                if combobox_mp_facturero:
                                    combobox_mp_facturero.setEnabled(True)  # Habilitar el combobox después de actualizar

                            self.metodos_pago_thread = TraerMetodosPagoYSuIdThread()
                            self.metodos_pago_thread.resultado.connect(actualizar_comboboxes_metodos)
                            self.start_thread(self.metodos_pago_thread)

                        else:
                            pushButton = dialog.findChild(QPushButton, "pushButton")
                            if pushButton:
                                pushButton.setEnabled(True) 

                            if label_2:
                                label_2.setText("Error al borrar el método de pago")
                                label_2.setStyleSheet("color: red; font-weight: bold")
                                QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))

                    self.borrar_mp_thread.resultado.connect(on_resultado)
                    self.start_thread(self.borrar_mp_thread)
                else:
                    # Usuario canceló, no hacer nada
                    pushButton = dialog.findChild(QPushButton, "pushButton")
                    if pushButton:
                        pushButton.setEnabled(True) 

                    if label_2:
                        label_2.setText("Operación cancelada")
                        label_2.setStyleSheet("color: blue; font-weight: bold")
                        QTimer.singleShot(1500, lambda: label_2.setStyleSheet("color: transparent"))
            else:
                pushButton = dialog.findChild(QPushButton, "pushButton")
                if pushButton:
                    pushButton.setEnabled(True) 

                if label_2:
                    label_2.setStyleSheet("color: red; font-weight: bold")
                    label_2.setText("Por favor, seleccione un método de pago")
                    QTimer.singleShot(1000, lambda: label_2.setStyleSheet("color: transparent"))


    def initialize_lineedits_compras(self):
        # Inicializar los QLineEdit en blanco y no editables
        lineedit_nombre = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_5")
        lineedit_precio = self.facturero_compras_window.findChild(QLineEdit, "lineEdit")
        lineedit_cantidad = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_2")
        lineedit_categoria = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_3")
        lineedit_proveedor = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_4")
        


        if lineedit_nombre:
            lineedit_nombre.setText("")
            lineedit_nombre.setReadOnly(True)
            lineedit_nombre.setFocusPolicy(Qt.NoFocus)

        if lineedit_precio:
            lineedit_precio.setText("")
            lineedit_precio.setReadOnly(True)
            lineedit_precio.setFocusPolicy(Qt.NoFocus)

        if lineedit_cantidad:
            lineedit_cantidad.setText("")
            

        if lineedit_categoria:
            lineedit_categoria.setText("")
            lineedit_categoria.setReadOnly(True)
            lineedit_categoria.setFocusPolicy(Qt.NoFocus)

        if lineedit_proveedor:
            lineedit_proveedor.setText("")
            lineedit_proveedor.setReadOnly(True)
            lineedit_proveedor.setFocusPolicy(Qt.NoFocus)


    def cerrar_facturero_compras(self):
        global productos_seleccionados_facturero_compras, productos_cache_temporal

        productos_cache_temporal = copy.deepcopy(productos_cache)  # Actualizar el cache temporal con el cache global

        # Se actualiza la tabla de productos
        self.borrar_lineedit_18()
        self.filter_products_facturero()

        self.facturero_compras_window.close()
        self.facturero_compras_window = None

        self.facturero_activo = None  # Reiniciar el estado del facturero activo

    def load_facturero_data_compras(self):
        # Cargar datos relacionados con el ID seleccionado en el QComboBox
        combobox_id = self.facturero_compras_window.findChild(QComboBox, "comboBox")
        if combobox_id and combobox_id.currentText().isdigit():
            id_producto = combobox_id.currentText()

            # Usar el cache global de productos por ID
            global productos_por_id_cache
            producto = None

            if productos_por_id_cache and id_producto in productos_por_id_cache:
                producto = productos_por_id_cache[id_producto]
            

            if producto:
                # Suponiendo que `producto` es una tupla con los datos en este orden:
                # (nombre, precio_venta, cantidad, categoria, proveedor)
                lineedit_nombre = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_5")
                lineedit_precio = self.facturero_compras_window.findChild(QLineEdit, "lineEdit")
                lineedit_cantidad = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_2")
                lineedit_categoria = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_3")
                lineedit_proveedor = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_4")
                
                

                # Convertir los valores a cadenas antes de asignarlos
                if lineedit_nombre:
                    lineedit_nombre.setText(str(producto[1]))  # Nombre del producto

                if lineedit_precio:
                    lineedit_precio.setText(str(producto[2]))  # Precio de venta

                if lineedit_cantidad:
                    lineedit_cantidad.setText(str(1)) #cantidad
                    

                if lineedit_categoria:
                    lineedit_categoria.setText(str(producto[6]))  # Categoría

                if lineedit_proveedor:
                    lineedit_proveedor.setText(str(producto[7]))  # Proveedor


            
            # Seleccionar todo el texto del QComboBox para facilitar el borrado
            combobox_id.lineEdit().selectAll()

               
        else:
            # Si no hay un ID válido seleccionado, limpiar los campos

            self.initialize_lineedits_compras()

    def agregar_producto_a_tablewidget_compras(self):

        global productos_seleccionados_facturero_compras, productos_por_id_cache

        combobox_id = self.facturero_compras_window.findChild(QComboBox, "comboBox")
        combobox_id_value = combobox_id.currentText()
        line_edit_nombre = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_5")
        line_edit_precio = self.facturero_compras_window.findChild(QLineEdit, "lineEdit")
        line_edit_cantidad = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_2")
        line_edit_categoria = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_3")
        line_edit_proveedor = self.facturero_compras_window.findChild(QLineEdit, "lineEdit_4")
        combobox_metodo_pago = self.facturero_compras_window.findChild(QComboBox, "comboBox_3")
        
        bandera = False
        if combobox_id_value.isdecimal() and productos_por_id_cache and combobox_id_value in productos_por_id_cache:
            bandera = True

        if bandera:
            
            qtablewidget = self.facturero_compras_window.findChild(QTableWidget, "tableWidget")  
            # Verificar si hay una cantidad seleccionado
            if line_edit_cantidad:
                if "," in line_edit_cantidad.text():
                    lineEdit_cantidad_value  = line_edit_cantidad.text().replace(",", ".")
                else:
                    lineEdit_cantidad_value = line_edit_cantidad.text()
         
            if qtablewidget:
                if (self.es_decimal(lineEdit_cantidad_value)or lineEdit_cantidad_value.isdigit()) and combobox_metodo_pago.currentText() != "":

                    # Crear el producto para agregar
                    producto_a_agregar = [
                        line_edit_nombre.text(),
                        float(line_edit_precio.text()),
                        float(lineEdit_cantidad_value),
                        line_edit_categoria.text(),
                        line_edit_proveedor.text(),
                        combobox_metodo_pago.currentText(),
                        float(line_edit_precio.text()) * float(lineEdit_cantidad_value)
                    ]


                    if int(lineEdit_cantidad_value) < 10000:

                        # Agregar a la lista global
                        productos_seleccionados_facturero_compras.append(producto_a_agregar)
                        #actualizar cantidad en producto
                        self.actualizar_stock_producto(productos_seleccionados_facturero_compras[-1], s=False)

                        # Actualizar el QTableWidget
                        self.filter_products_facturero()
                         
                        row = qtablewidget.rowCount()
                        qtablewidget.insertRow(row)
                        for column, value in enumerate(productos_seleccionados_facturero_compras[-1]):
                            item = QTableWidgetItem(str(value))
                            item.setFont(QFont("Segoe UI", 10))
                            qtablewidget.setItem(row, column, item)


                    else:
                        label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
                        label_9.setAlignment(Qt.AlignCenter)
                        label_9.setText(f"Inserte una cantidad razonable")
                        label_9.setStyleSheet("color: red; font-weight: bold")
                        QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))


                    #agregar total 
                    global total_facturero_compras
                    #actualiza el total de los productos agregados
                    total_facturero_compras = sum([producto[-1] for producto in productos_seleccionados_facturero_compras])

                    #edita el label del total
                    self.actualizar_total(s = False)

                else:
                    label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
                    if label_9:
                        label_9.setAlignment(Qt.AlignCenter)
                        label_9.setText("Complete los campos correctamente")
                        label_9.setStyleSheet("color: red; font-weight: bold")
                        QTimer.singleShot(2000, lambda: label_9.setStyleSheet("color: transparent"))
            
        else:
            label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("Seleccione un ID válido")
                label_9.setStyleSheet("color: red; font-weight: bold")
                QTimer.singleShot(2000, lambda: label_9.setStyleSheet("color: transparent"))

         
        # Seleccionar todo el texto del QComboBox para facilitar el borrado
        combobox_id.setFocus()
        combobox_id.lineEdit().selectAll()


    def procesar_factura_compras(self):
        global productos_seleccionados_facturero_compras, total_facturero_compras, usuario_activo, productos_cache_temporal
        
        s = False

        boton_agregar = self.facturero_compras_window.findChild(QPushButton, "pushButton_2")
        if boton_agregar:
            boton_agregar.setEnabled(False)

        push_button = self.facturero_compras_window.findChild(QPushButton, "pushButton")
        if push_button:
            push_button.setEnabled(False)

        pushbutton_3 = self.facturero_compras_window.findChild(QPushButton, "pushButton_3")
        if pushbutton_3:
            pushbutton_3.setEnabled(False)

        push_button_4 = self.facturero_compras_window.findChild(QPushButton, "pushButton_4")
        if push_button_4:
            push_button_4.setEnabled(False)

        if productos_seleccionados_facturero_compras:

            label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("Procesando factura...")
                label_9.setStyleSheet("color: green; font-weight: bold")
            # Usar hilo para agregar a registro
            self.agregar_registro_thread = AgregarARegistroThread(
                productos_seleccionados_facturero_compras, s, usuario_activo
            )

            def on_registro_agregado(exito):
                if exito:
                            
                    #  ACTUALIZAR DESDE LA BASE DE DATOS, NO DESDE CACHE TEMPORAL
                    global productos_cache, productos_por_id_cache, productos_por_nombre_cache
                    productos_cache = None
                    productos_por_id_cache = None  
                    productos_por_nombre_cache = None

                    # Actualizar el cache desde la base de datos
                    self.datos_tab.actualizar_variables_globales_de_uso(3, lambda: (
                        self.filter_products_facturero(),
                        self.datos_tab.visualizar_datos()
                    ))

                    label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
                    if label_9:
                        label_9.setAlignment(Qt.AlignCenter)
                        label_9.setText("Factura procesada con éxito")
                        label_9.setStyleSheet("color: green; font-weight: bold")
                        QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))

                    pushbutton_3 = self.facturero_compras_window.findChild(QPushButton, "pushButton_3")
                    if pushbutton_3:
                        pushbutton_3.setEnabled(True)

                    push_button_4 = self.facturero_compras_window.findChild(QPushButton, "pushButton_4")
                    if push_button_4:
                        push_button_4.setEnabled(True)

                    boton_agregar = self.facturero_compras_window.findChild(QPushButton, "pushButton_2")
                    if boton_agregar:
                        boton_agregar.setEnabled(True)

                    push_button = self.facturero_compras_window.findChild(QPushButton, "pushButton")
                    if push_button:
                        push_button.setEnabled(True)

                    # Llamar a inicializar_comboboxes_y_boton de la clase buscar datos
                    self.buscar_datos_tab.enviar_a_setear_tables()
                   

                else:
                    print("Error al agregar a registro")

            self.agregar_registro_thread.resultado.connect(on_registro_agregado)
            self.start_thread(self.agregar_registro_thread)
        else:
            label_9 = self.facturero_compras_window.findChild(QLabel, "label_9")
            if label_9:
                label_9.setAlignment(Qt.AlignCenter)
                label_9.setText("No hay productos agregados")
                label_9.setStyleSheet("color: red; font-weight: bold")
                QTimer.singleShot(6000, lambda: label_9.setStyleSheet("color: transparent"))

            if pushbutton_3 and push_button_4 and boton_agregar and push_button:
                pushbutton_3.setEnabled(True)
                push_button_4.setEnabled(True)
                boton_agregar.setEnabled(True)
                push_button.setEnabled(True)

        qtablewidget = self.facturero_compras_window.findChild(QTableWidget, "tableWidget")
        if qtablewidget:
            qtablewidget.setRowCount(0)

        total_facturero_compras = 0
        productos_seleccionados_facturero_compras = []

        self.actualizar_total(s=False)

        # Limpiar interfaz
        combobox_id = self.facturero_compras_window.findChild(QComboBox, "comboBox")
        if combobox_id:
            combobox_id.setFocus()
            combobox_id.lineEdit().selectAll()


    def borrar_ultimo_agregado_compras(self):
        global usuario_activo, productos_seleccionados_facturero_compras, total_facturero_compras, productos_cache_temporal

        if productos_seleccionados_facturero_compras:
            self.actualizar_stock_producto(productos_seleccionados_facturero_compras[-1], s=True)

            #actualiza tabla de productos
            self.filter_products_facturero()

            self.actualizar_total(s=False)

        qtablewidget = self.facturero_compras_window.findChild(QTableWidget, "tableWidget") 
        if qtablewidget:
            row_count = qtablewidget.rowCount()
            if row_count > 0:
                qtablewidget.removeRow(row_count - 1)  # Remove the last row
                if productos_seleccionados_facturero_compras:
                    productos_seleccionados_facturero_compras.pop()
                    # Actualiza el total de los productos agregados
                    total_facturero_compras = sum([producto[-1] for producto in productos_seleccionados_facturero_compras])

        #edita el label del total
        self.actualizar_total(s = False)

    def actualizar_stock_producto(self, producto_modificado, s):
        global productos_cache_temporal, productos_seleccionados_facturero_compras

        # S true venta, S false compra

        if s:  # Si es venta    
                
            if productos_cache_temporal:
            
                nombre_producto = producto_modificado[0]  # Nombre del producto
                cantidad_vendida = float(producto_modificado[2])  # Cantidad vendida
                # Buscar y actualizar el producto en el cache temporal
                for i, producto in enumerate(productos_cache_temporal):
                    if producto[1] == nombre_producto:  # Comparar por nombre (producto[1])
                        # Crear una nueva tupla con el stock actualizado
                        producto_actualizado = list(producto)
                        producto_actualizado[4] = float(float(producto[4]) - cantidad_vendida)  # Restar del stock
                        productos_cache_temporal[i] = tuple(producto_actualizado)
                        break
                
        else:  # Si es compra
            nombre_producto = producto_modificado[0]  # Nombre del producto
            cantidad_comprada = float(producto_modificado[2])  # Cantidad comprada
            # Buscar y actualizar el producto en el cache temporal
            for i, producto in enumerate(productos_cache_temporal):
                if producto[1] == nombre_producto:  # Comparar por nombre (producto[1])
                    # Crear una nueva tupla con el stock actualizado
                    producto_actualizado = list(producto)
                    producto_actualizado[4] = float(producto[4]) + cantidad_comprada  # Sumar al stock
                    productos_cache_temporal[i] = tuple(producto_actualizado)
                    break
          

    def _customize_facturero_ui(self, window, color):
        # Configuración de botones
        button = window.findChild(QPushButton, "pushButton_2")
        if button:
            button.setStyleSheet(f"background-color: {color}")

        button3 = window.findChild(QPushButton, "pushButton_3")
        if button3:
            button3.setStyleSheet("background-color: rgb(200, 200, 200)")

        button2 = window.findChild(QPushButton, "pushButton")
        if button2:
            button2.setStyleSheet("background-color: rgb(255, 127, 127)")

        button4 = window.findChild(QPushButton, "pushButton_4")
        if button4:
            button4.setStyleSheet("background-color: rgb(200, 16, 16)")


class MainWindow(QMainWindow):
    def __init__(self, usuario, account):
        super(MainWindow, self).__init__()
        self.session_manager = SessionManager()
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
        self.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
        self.setWindowTitle("rls")  

        # Mostrar overlay de carga al iniciar
        QTimer.singleShot(0, lambda: self.mostrar_overlay(i=False))
        
        QTimer.singleShot(500, self.inicializar_aplicacion)  # Esperar 500ms antes de inicializar


    def logout(self):
        """Cerrar sesión y volver al login"""
        try:
            # Mostrar diálogo de confirmación ANTES de cerrar sesión
            from PySide6.QtWidgets import QMessageBox
            dialogo_confirmacion = QMessageBox()
            dialogo_confirmacion.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
            dialogo_confirmacion.setWindowTitle("Confirmar Cierre de Sesión")
            dialogo_confirmacion.setText("¿Está seguro de que desea cerrar sesión?")
            dialogo_confirmacion.setInformativeText("La aplicación volverá al login y deberá autenticarse nuevamente.")
            dialogo_confirmacion.setIcon(QMessageBox.Question)
            dialogo_confirmacion.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            dialogo_confirmacion.setDefaultButton(QMessageBox.Cancel)

            # Personalizar el texto de los botones
            boton_aceptar = dialogo_confirmacion.button(QMessageBox.Ok)
            boton_cancelar = dialogo_confirmacion.button(QMessageBox.Cancel)
            if boton_aceptar:
                boton_aceptar.setText("Aceptar")
            if boton_cancelar:
                boton_cancelar.setText("Cancelar")

            # Mostrar el diálogo y verificar la respuesta
            respuesta = dialogo_confirmacion.exec()

            if respuesta == QMessageBox.Ok:
                # Usuario confirmó, proceder con el cierre de sesión
                # Limpiar la sesión
                self.session_manager.clear_session()

                # Mostrar mensaje de confirmación
                msg = QMessageBox()
                msg.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
                msg.setWindowTitle("Sesión Cerrada")
                msg.setText("Has cerrado sesión exitosamente.\nVolviendo al login...")
                msg.setIcon(QMessageBox.Information)
                msg.exec()

                # Cerrar la ventana actual
                self.close()

                # Abrir la ventana de login web
                try:
                    from archivos_py.windows.inicio_login_web import InicioWeb
                    self.login_window = InicioWeb()
                    self.login_window.show()
                except Exception as e:
                    print(f"Error al abrir ventana de login: {e}")
                    # Si hay error, cerrar la aplicación
                    import sys
                    sys.exit()
            else:
                # Usuario canceló, no hacer nada
                print("Cierre de sesión cancelado por el usuario")
                return

        except Exception as e:
            print(f"Error al cerrar sesión: {e}")
            # Mostrar mensaje de error
            from PySide6.QtWidgets import QMessageBox
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
            msg.setWindowTitle("Error")
            msg.setText(f"Error al cerrar sesión: {e}")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()


    def inicializar_aplicacion(self):
        """Inicializar la aplicación después de mostrar el overlay"""

        # Cambia las tab si es usuario
        tab_widget = self.ui.tabWidget
        if tab_widget:
            if self.account == "Administrador":
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_1), "Datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_3), "Buscar datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab), "Administración")
            else:
                tab_widget.setTabVisible(tab_widget.indexOf(self.ui.tab_1), False)
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab_3), "Buscar datos")
                tab_widget.setTabText(tab_widget.indexOf(self.ui.tab), "Administración")

        # Crear instancias de las clases de las pestañas
        self.datos_tab = DatosTab(self.ui)
        self.buscar_datos_tab = BuscarDatosTab(self.ui, self.datos_tab)
        self.administracion_tab = AdministracionTab(self.ui, self.buscar_datos_tab, self.datos_tab)

        # Cerrar factureros al cambiar a la pestaña "Datos"
        tab_widget = self.ui.tabWidget
        if tab_widget:
            def on_tab_changed(index):
                # Cambia el número 0 por el índice real de la pestaña "Datos" si es diferente
                if tab_widget.tabText(index) == "Datos":
                    if self.administracion_tab.facturero_ventas_window:
                        self.administracion_tab.cerrar_facturero_venta()
                    if self.administracion_tab.facturero_compras_window:
                        self.administracion_tab.cerrar_facturero_compras()
            tab_widget.currentChanged.connect(on_tab_changed)

        # Establece inicio rls
        stacked_widget = self.ui.stackedWidget
        if stacked_widget:
            stacked_widget.setCurrentIndex(2)

        # Crear arreglo con threads abiertos
        self.threads = []
        self.guardando_al_cerrar = False

        # Conectar botones 
        self.connect_buttons(stacked_widget)


        self.setear_fechayhora()

        # Edicion de anotador
        self.inicializar_anotador(self.usuario)
        self.anotador(self.usuario)

        # Ocultar el overlay después de 9 segundos
        QTimer.singleShot(9000, self.ocultar_overlay_inicial)


    def ocultar_overlay_inicial(self):
        """Ocultar el overlay de carga inicial"""
        if hasattr(self, 'overlay'):
            self.overlay.hide()



    def start_thread(self, thread):
        self.threads.append(thread)
        thread.finished.connect(lambda: self.threads.remove(thread) if thread in self.threads else None)
        thread.start()

    def inicializar_anotador(self, usuario):
        # Buscar el QTextEdit dentro del tabWidget
        textEdit_3 = self.ui.tabWidget.findChild(QTextEdit, "textEdit_3")
        if textEdit_3:

            # Usar hilo para traer el último texto
            self.traer_texto_thread = TraerUltimoTextoAnotadorThread()

            def on_texto_obtenido(ultimo_texto):
                if ultimo_texto:
                    textEdit_3.setPlainText(ultimo_texto)
                else:
                    # Si no hay texto, establecer texto principal usando hilo
                    self.set_texto_thread = SetTextoAnotadorThread(usuario)

                    def on_texto_establecido(exito):
                        if exito:
                            # Traer el texto nuevamente después de establecerlo
                            self.traer_texto_final_thread = TraerUltimoTextoAnotadorThread()
                            self.traer_texto_final_thread.resultado.connect(
                                lambda texto_final: textEdit_3.setPlainText(texto_final)
                            )
                            self.start_thread(self.traer_texto_final_thread)

                        else:
                            print("Error al establecer texto principal")

                    self.set_texto_thread.resultado.connect(on_texto_establecido)
                    self.start_thread(self.set_texto_thread)

            self.traer_texto_thread.resultado.connect(on_texto_obtenido)
            self.start_thread(self.traer_texto_thread)

    def guardar_en_base_de_datos(self, textEdit, usuario):
        texto = textEdit.toPlainText()

        texto = textEdit.toPlainText()
        try:
            # Crear y ejecutar el hilo de guardado
            self.guardar_cerrar_thread = GuardarAlCerrarThread(texto, usuario)
            self.start_thread(self.guardar_cerrar_thread)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def iniciar_guardado_demorado(self):
        # Reiniciar el temporizador cada vez que cambie el texto
        self.save_timer.stop()
        self.save_timer.start(3000)  # Esperar 3 segundos antes de guardar

    def guardar_y_cerrar(self, event, textEdit, usuario):
        # Si ya está en proceso de cierre, permitir el cierre
        if hasattr(self, '_cerrando') and self._cerrando:
            event.accept()
            return

        #  Rechazar el evento la primera vez para mostrar el overlay
        event.ignore()
        self._cerrando = True  # Marcar que está cerrando

        #  Crear y mostrar el overlay de guardado
        self.mostrar_overlay(i=True)
        

        # Obtener el texto del QTextEdit
        texto = textEdit.toPlainText()

        # Crear y ejecutar el hilo de guardado
        self.guardar_cerrar_thread = GuardarAlCerrarThread(texto, usuario)

        def on_guardado_completado(exito):
            if not exito:
                # Ocultar el overlay si existe en caso de error
                if hasattr(self, 'overlay'):
                    self.overlay.hide()

            # Ocultar el overlay y cerrar después de un breve delay
            QTimer.singleShot(3000, self.cerrar_aplicacion_final)

        self.guardar_cerrar_thread.resultado.connect(on_guardado_completado)
        self.start_thread(self.guardar_cerrar_thread)

    def resizeEvent(self, event):
        """Manejar el redimensionamiento de la ventana"""
        super().resizeEvent(event)
        
        # Si existe el overlay, redimensionarlo para que cubra toda la ventana
        if hasattr(self, 'overlay') and self.overlay.isVisible():
            self.overlay.setGeometry(self.rect())
    
    def mostrar_overlay(self, i):
        """Crear y mostrar el overlay de guardado"""
    
        self.show()
        QApplication.processEvents()
    
        # Crear el overlay que cubre toda la ventana
        self.overlay = QWidget(self)
        self.overlay.setGeometry(self.rect())
        
        self.overlay.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 150);
            }
        """)
    
        # Crear el layout para el overlay
        layout = QVBoxLayout(self.overlay)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes para que ocupe toda la ventana
        if i:
            # Crear el label con el mensaje
            label = QLabel("Guardando anotaciones")
        else:
             # Crear el label con el mensaje
            label = QLabel("Cargando Datos")
    
        label.setStyleSheet("""
                QLabel {
                    color: white;
                    font-size: 24pt;
                    font-weight: bold;
                    font-family: 'Segoe UI';
                    background-color: transparent;
                    padding: 20px;
                }
        """)
        label.setAlignment(Qt.AlignCenter)
    
        # Crear un indicador de carga (puntos animados)
        self.puntos_label = QLabel("...")
        self.puntos_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18pt;
                font-weight: bold;
                font-family: 'Segoe UI';
                background-color: transparent;
            }
        """)
        self.puntos_label.setAlignment(Qt.AlignCenter)
    
        # Agregar los elementos al layout
        layout.addWidget(label)
        layout.addWidget(self.puntos_label)
    
        # Mostrar el overlay
        self.overlay.show()
    
        # Iniciar animación de puntos
        self.animar_puntos()

    def animar_puntos(self):
        """Animar los puntos de carga"""
        if hasattr(self, 'puntos_label'):
            self.puntos_count = getattr(self, 'puntos_count', 0)
            puntos_text = "." * ((self.puntos_count % 3) + 1)
            self.puntos_label.setText(puntos_text)
            self.puntos_count += 1

            # Continuar la animación cada 300ms
            QTimer.singleShot(300, self.animar_puntos)

    def cerrar_aplicacion_final(self):
        """Cerrar la aplicación después de guardar"""
       
        if hasattr(self, 'overlay'):
            self.overlay.hide()

        # Cerrar la aplicación
        self.close()

    def anotador(self, usuario):
        # Buscar el QTextEdit dentro del tabWidget
        textEdit_3 = self.ui.tabWidget.findChild(QTextEdit, "textEdit_3")
        if textEdit_3:

            # Crear un QTimer para retrasar el guardado
            self.save_timer = QTimer()
            self.save_timer.setSingleShot(True)  # Asegurarse de que solo se ejecute una vez por evento
            self.save_timer.timeout.connect(lambda: self.guardar_en_base_de_datos(textEdit_3, usuario))  # Conectar al método de guardado

            # Conectar el evento textChanged al método que inicia el temporizador
            textEdit_3.textChanged.connect(self.iniciar_guardado_demorado)

            # Conectar el evento closeEvent para guardar el texto al cerrar
            self.closeEvent = lambda event: self.guardar_y_cerrar(event, textEdit_3, usuario)

    
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

        #boton de cerrar sesion
        # Si no se encuentra, intentar búsqueda directa
        logout_button = self.findChild(QPushButton, "pushButton_50")
        if logout_button:
            logout_button.clicked.connect(self.logout)
            logout_button.setStyleSheet("background-color: rgb(255, 127, 127); font-weight: bold;")


        # Botón visualizar productos
        button = self.findChild(QPushButton, "pushButton")
        if button:
            button.setStyleSheet("background-color: rgb(226, 245, 255)")
            button.clicked.connect(self.change_table_headers_color_visualizar_productos)
            self.connect_button("pushButton", stacked_widget, 0, lambda: self.focus_visualziar_prod())
            

        self.connect_button("pushButton_4", stacked_widget, 3, lambda: self.focus_borrar_prod())
        self.connect_button("pushButton_2", stacked_widget, 4, lambda: self.focus_editar_prod())

        # Botón visualizar proveedores
        button5 = self.findChild(QPushButton, "pushButton_5")
        if button5:
            button5.setStyleSheet("background-color: rgb(226, 245, 255)")
            button5.clicked.connect(self.change_table_headers_color_visualizar_proveedores)
            self.connect_button("pushButton_5", stacked_widget, 9, lambda: self.focus_visualizar_prov())

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
            button11.clicked.connect(self.change_table_headers_color_visualizar_categorias)
            self.connect_button("pushButton_11", stacked_widget, 11,  lambda: self.focus_visualizar_categorias())

        # Botón borrar datos
        button12 = self.findChild(QPushButton, "pushButton_12")
        if button12:
            button12.setStyleSheet("background-color: red")
            button12.clicked.connect(self.delete_all_data)

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
        botton_15 = self.findChild(QPushButton, "pushButton_15")
        if botton_15:
            self.connect_button("pushButton_15", stacked_widget, 13)
            botton_15.clicked.connect(self.change_table_headers_color_arqueo)

        self.connect_button("pushButton_13", stacked_widget, 14)
        self.connect_button("pushButton_48", stacked_widget, 19)
        push_button_48 = self.findChild(QPushButton, "pushButton_48")
        if push_button_48:
            push_button_48.setIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\eye_visible_hide_hidden_show_icon_145988.png"))
            self.connect_button("pushButton_48", stacked_widget, 19,  lambda: self.change_table_headers_color_visualizar_movimientos())

        # VENTANA ADMINISTRACION

        # Botón facturero ventas
        button16 = self.findChild(QPushButton, "pushButton_16")
        if button16:
            button16.setStyleSheet("background-color: rgb(198, 255, 202)")
            button16.clicked.connect(self.administracion_tab.visualizar_productos_facturero)
            self.connect_button("pushButton_16", stacked_widget, 15, self.administracion_tab.open_facturero_ventas)
            button16.clicked.connect(self.change_table_headers_color_ventas)

        # Botón facturero compras
        button17 = self.findChild(QPushButton, "pushButton_17")
        if button17:
            button17.setStyleSheet("background-color: rgb(255, 230, 107)")
            button17.clicked.connect(self.administracion_tab.visualizar_productos_facturero)
            self.connect_button("pushButton_17", stacked_widget, 15, self.administracion_tab.open_facturero_compras)
            button17.clicked.connect(self.change_table_headers_color_compras)


    # borrar datos:
    def delete_all_data(self):
        global usuario_activo

        borrar_categorias = True
        borrar_ventas_compras = True
        borrar_proveedores = True
        borrar_usuarios = True
        borrar_movimientos = True

        if borrar_categorias and borrar_ventas_compras and borrar_proveedores and borrar_usuarios and borrar_movimientos:
            if self.show_confirmation_dialog():
                # Ejecutar ambos hilos y mostrar mensaje cuando ambos terminen
                self.clear_thread = ClearDataThread(borrar_categorias, borrar_ventas_compras, borrar_proveedores, borrar_usuarios, borrar_movimientos)
                self._clear_done = False  # bandera interna
                def on_clear_finished():
                    if self._clear_done:
                        return
                    self._clear_done = True  # marcar como hecho
                    QMessageBox.information(self.ui.centralwidget, "Datos borrados", "El programa se cerrará.")
                    sys.exit()
                    
                self.clear_thread.finished.connect(on_clear_finished)
                self.start_thread(self.clear_thread)
                self.mov_thread = CargarMovimientosThread(usuario_activo)
                self.start_thread(self.mov_thread)


    def show_confirmation_dialog(self):
        dialog = QMessageBox()
        dialog.setWindowIcon(QIcon(r"C:\Users\mariano\Desktop\proyectos\mnmkt\Minimarket\archivos_py\resources\r.ico"))
        dialog.setWindowTitle("Confirmación")
        dialog.setText("¿Está seguro de que desea borrar TODOS los datos?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setDefaultButton(QMessageBox.No)

        # Cambiar el texto de los botones a español
        yes_button = dialog.button(QMessageBox.Yes)
        no_button = dialog.button(QMessageBox.No)
        if yes_button:
            yes_button.setText("Sí")
        if no_button:
            no_button.setText("No")

        return dialog.exec() == QMessageBox.Yes
    

    def setear_fechayhora(self):
        
        def update_datetime():
            fecha = datetime.now().strftime("%d/%m/%y")  # Formato día/mes/año (últimos 2 dígitos del año)
            hora = datetime.now().strftime("%I:%M %p")

            label_66 = self.findChild(QLabel, "label_66")
            if label_66:
                label_66.setText(fecha)

            label_65 = self.findChild(QLabel, "label_65")
            if label_65:
                label_65.setText(hora)

        # Crear un QTimer para actualizar la fecha y hora en tiempo real
        timer = QTimer(self)
        timer.timeout.connect(update_datetime)
        timer.start(1000)  # Actualizar cada 1 segundo

        # Llamar a la función una vez para inicializar los valores
        update_datetime()


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
                font-family: 'Segoe UI';
                font-size: 16pt;
                font-weight: bold;
            }
            """)

    def change_table_headers_color_visualizar_movimientos(self):
        table = self.ui.frame_52.findChild(QTableWidget, "tableWidget_5")
        # Aplicar estilo mediante stylesheet con el color especificado
        table.setStyleSheet("""
            QHeaderView::section {
                font-size: 20px;
                font-weight: bold;
                font-family: Segoe UI;
                background-color: rgb(243, 66, 66);
                color: black;
            }
            QTableWidget {
                gridline-color: rgb(243, 66, 66);
            }
            
        """)


            
    def change_table_headers_color_visualizar_proveedores(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_2")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
                font-family: 'Segoe UI';
                font-size: 16pt;
                font-weight: bold;
            }
            """)

    def change_table_headers_color_visualizar_productos(self):
        table_widget = self.findChild(QTableWidget, "tableWidget")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
                font-family: 'Segoe UI';
                font-size: 16pt;
                font-weight: bold;
            }
            """)
        

    def change_table_headers_color_ventas(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_4")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(198, 255, 202);
                color: black;
                font-family: 'Segoe UI';
                font-size: 16pt;
                font-weight: bold;
            }
            """)

    def change_table_headers_color_compras(self):
        table_widget = self.findChild(QTableWidget, "tableWidget_4")
        if table_widget:
            table_widget.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(255, 230, 107);
                color: black;
                font-family: 'Segoe UI';
                font-size: 16pt;
                font-weight: bold;
                                       
            }
            """)

    def change_table_headers_color_arqueo(self):
        table_widget_6 = self.findChild(QTableWidget, "tableWidget_6")
        table_widget_7 = self.findChild(QTableWidget, "tableWidget_7")

        if table_widget_6 and table_widget_7:
            table_widget_6.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
                font-family: 'Segoe UI';
                font-size: 12pt;
                font-weight: bold;
            }
            """)
            table_widget_7.setStyleSheet("""
            QHeaderView::section {
                background-color: rgb(226, 245, 255);
                color: black;
                font-family: 'Segoe UI';
                font-size: 12pt;
                font-weight: bold;
            }
            """)
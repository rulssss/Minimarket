from PySide6.QtWidgets import QMainWindow, QPushButton, QLineEdit, QDialog, QVBoxLayout, QComboBox, QTableWidget, QLabel, QDoubleSpinBox, QTableWidgetItem, QApplication, QAbstractButton, QMessageBox, QCheckBox, QDateEdit, QTextEdit, QWidget
from PySide6.QtCore import QTimer, Qt, QDate
from PySide6.QtGui import QIcon, QFont, QIntValidator
from archivos_py.threads.db_thread_minimarket import *


class ProductosManager:
    def __init__(self, ui, id_usuario_perfil, usuario_activo):
        self.ui = ui
        self.id_usuario_perfil = id_usuario_perfil
        self.usuario_activo = usuario_activo
        #self.parent = parent  # Puede ser DatosTab si necesitas acceder a otras funciones

        # Inicialización de botones, variables, etc.
        self.threads = []
        self.editando = False
        self._borrar_producto = False
        self.button19_connected = False
        self.button34_connected = False


        self.inicializar_ui_con_datos()

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


    #######################

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
        global productos_cache, productos_por_nombre_cache
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
            self.agregar_thread = AgregarProductoThread(self.id_usuario_perfil,
                input_id_value, input_nombre_value, input_precio_compra_value, input_precio_venta_value,
                input_stock_value, input_stock_ideal_value, input_categoria_value, input_proveedor_value
            )
            self.agregar_thread.producto_agregado.connect(
                lambda exito: self.on_producto_agregado(exito, input_id_value, self.usuario_activo, input_id)
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
            self.movimiento_thread = MovimientoProductoThread(self.id_usuario_perfil, input_id_value, usuario_activo)
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

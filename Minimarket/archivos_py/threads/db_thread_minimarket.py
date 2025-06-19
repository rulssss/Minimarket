from PySide6.QtCore import QThread, Signal
from archivos_py.db.productos import *




#Agregar productos:

class CategoriasThread(QThread):
    categorias_obtenidas = Signal(list)

    def run(self):
        categorias = traer_categorias()
        if not categorias:
            crear_categuno()
            categorias = traer_categorias()
            
        self.categorias_obtenidas.emit(categorias)

class ProveedoresThread(QThread):
    proveedores_obtenidos = Signal(list)

    def run(self):
        proveedores = traer_proveedor()
        if not proveedores:
            crear_provuno()
            proveedores = traer_proveedor()
        self.proveedores_obtenidos.emit(proveedores)


class AgregarProductoThread(QThread):
    producto_agregado = Signal(bool)  # éxito

    def __init__(self, *args):
        super().__init__()
        self.args = args

    def run(self):
        # Llama a tu función de agregar producto
        exito = cargar_producto(*self.args)
        self.producto_agregado.emit(exito)

class MovimientoProductoThread(QThread):
    movimiento_cargado = Signal()

    def __init__(self, input_id_value, usuario_activo):
        super().__init__()
        self.input_id_value = input_id_value
        self.usuario_activo = usuario_activo

    def run(self):
        cargar_movimiento_producto_agregado(self.input_id_value, self.usuario_activo)
        self.movimiento_cargado.emit()


# Borrar productos: 
# -> se utiliza el de movimientoproductothread tambien

class TraerIdProductoThread(QThread):
    resultado = Signal(int)
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        id_producto = traer_id_producto(self.nombre)
        self.resultado.emit(id_producto)

class TraerNomProductoThread(QThread):
    resultado = Signal(str)
    def __init__(self, id_producto):
        super().__init__()
        self.id_producto = id_producto
    def run(self):
        nombre_producto = traer_nom_producto(self.id_producto)
        self.resultado.emit(nombre_producto)

class BorrarProductoThread(QThread):
    resultado = Signal(bool)
    def __init__(self, valor):
        super().__init__()
        self.valor = valor
    def run(self):
        exito = buscar_producto(self.valor)
        self.resultado.emit(exito)

class MovimientoProductoBorrarThread(QThread):
    movimiento_borrado = Signal()

    def __init__(self, _borrar_id, input_nombre_o_id_value, usuario_activo):
        super().__init__()
        self._borrar_id = _borrar_id
        self.input_nombre_o_id_value = input_nombre_o_id_value
        self.usuario_activo = usuario_activo

    def run(self):
        cargar_movimiento_producto_borrado(self._borrar_id, self.input_nombre_o_id_value, self.usuario_activo)
        self.movimiento_borrado.emit()

# editar productos

class AumentarPreciosCategoriaThread(QThread):
    finished = Signal()
    def __init__(self, valor1, valor2, categoria):
        super().__init__()
        self.valor1 = valor1
        self.valor2 = valor2
        self.categoria = categoria
    def run(self):
        aumentar_precios_categoria(self.valor1, self.valor2, self.categoria)
        self.finished.emit()

class AumentarPreciosProveedorThread(QThread):
    finished = Signal()
    def __init__(self, valor1, valor2, proveedor):
        super().__init__()
        self.valor1 = valor1
        self.valor2 = valor2
        self.proveedor = proveedor
    def run(self):
        aumentar_precios_proveedor(self.valor1, self.valor2, self.proveedor)
        self.finished.emit()

class MovimientoAumentoPreciosThread(QThread):
    finished = Signal()
    def __init__(self, categoria_o_proveedor, usuario, es_categoria):
        super().__init__()
        self.categoria_o_proveedor = categoria_o_proveedor
        self.usuario = usuario
        self.es_categoria = es_categoria
    def run(self):
        cargar_movimiento_aumento_precios(self.categoria_o_proveedor, self.usuario, self.es_categoria)
        self.finished.emit()

class TraerProductoPorIdThread(QThread):
    resultado = Signal(object)
    def __init__(self, id_producto):
        super().__init__()
        self.id_producto = id_producto
    def run(self):
        producto = traer_datosproducto_por_id(self.id_producto)
        self.resultado.emit(producto)

class ActualizarProductoThread(QThread):
    finished = Signal()
    def __init__(self, id, nombre_prod, precio_compra, precio_venta, stock, stock_ideal, categoria, proveedor):
        super().__init__()
        self.id = id
        self.nombre_prod = nombre_prod
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock
        self.stock_ideal = stock_ideal
        self.categoria = categoria
        self.proveedor = proveedor

    def run(self):
        actualizar_producto(
            self.id, self.nombre_prod, self.precio_compra, self.precio_venta,
            self.stock, self.stock_ideal, self.categoria, self.proveedor
        )
        self.finished.emit()

class MovimientoProductoEditadoThread(QThread):
    movimiento_editado = Signal()

    def __init__(self, id_producto, usuario_activo):
        super().__init__()
        self.id_producto = id_producto
        self.usuario_activo = usuario_activo

    def run(self):
        cargar_movimiento_producto_editado(self.id_producto, self.usuario_activo)
        self.movimiento_editado.emit()


# visualizar productos
class TraerTodosLosProductosThread(QThread):
    resultado = Signal(list)
    def run(self):
        productos = traer_todos_los_productos()
        self.resultado.emit(productos)


# agregar proveedor


class ProveedorThread(QThread):
    proveedor_cargado = Signal(bool)
    def __init__(self, nombre, telefono, direccion):
        super().__init__()
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
    def run(self):
        exito = cargar_proveedor(self.nombre, self.telefono, self.direccion)
        self.proveedor_cargado.emit(exito)

class MovimientoProveedorThread(QThread):
    movimiento_cargado = Signal()
    def __init__(self, nombre, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_agregar_proveedor(self.nombre, self.usuario_activo)
        self.movimiento_cargado.emit()


 # borrar proveedor

# Hilo para buscar proveedor en la base
class BuscarProveedorThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        bandera = buscar_proveedor(self.nombre)
        self.resultado.emit(bandera)

# Hilo para traer el ID del proveedor
class TraerIdProveedorThread(QThread):
    resultado = Signal(int)
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        id_prov = traer_id_proveedor(self.nombre)
        self.resultado.emit(id_prov)

# Hilo para cargar movimiento de proveedor borrado
class MovimientoProveedorBorradoThread(QThread):
    def __init__(self, nombre, id_proveedor, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.id_proveedor = id_proveedor
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_proveedor_borrado(self.nombre, self.id_proveedor, self.usuario_activo)

# actualizar proveedor

class ActualizarProveedorThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre, telefono, direccion):
        super().__init__()
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
    def run(self):
        exito = actualizar_proveedor(self.nombre, self.telefono, self.direccion)
        self.resultado.emit(exito)

class MovimientoProveedorEditadoThread(QThread):
    def __init__(self, nombre, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_proveedor_editado(self.nombre, self.usuario_activo)

# agregar categoria

class CargarCategoriaThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_categoria):
        super().__init__()
        self.nombre_categoria = nombre_categoria
    def run(self):
        exito = cargar_categoria(self.nombre_categoria)
        self.resultado.emit(exito)

class MovimientoAgregarCategoriaThread(QThread):
    def __init__(self, nombre_categoria, usuario_activo):
        super().__init__()
        self.nombre_categoria = nombre_categoria
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_agregar_categoria(self.nombre_categoria, self.usuario_activo)

# borrar categoria
class BuscarCategoriaThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_categoria):
        super().__init__()
        self.nombre_categoria = nombre_categoria
    def run(self):
        existe = buscar_categoria(self.nombre_categoria)
        self.resultado.emit(existe)

class MovimientoCategoriaBorradaThread(QThread):
    def __init__(self, nombre_categoria, id_categoria, usuario_activo):
        super().__init__()
        self.nombre_categoria = nombre_categoria
        self.id_categoria = id_categoria
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_categoria_borrada(self.nombre_categoria, self.id_categoria, self.usuario_activo)


# borrar datos

class CargarMovimientosThread(QThread):
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimientos_datos_borrados(self.usuario_activo)

class ClearDataThread(QThread):
    finished = Signal()
    def __init__(self, borrar_categorias, borrar_ventas_compras, borrar_proveedores, borrar_usuarios, borrar_movimientos):
        super().__init__()
        self.borrar_categorias = borrar_categorias
        self.borrar_ventas_compras = borrar_ventas_compras
        self.borrar_proveedores = borrar_proveedores
        self.borrar_usuarios = borrar_usuarios
        self.borrar_movimientos = borrar_movimientos
    def run(self):
        clear_data(self.borrar_categorias, self.borrar_ventas_compras, self.borrar_proveedores, self.borrar_usuarios, self.borrar_movimientos)
        self.finished.emit()


# administrar usuarios

class AgregarRegistroUsuarioThread(QThread):
    resultado = Signal(bool)
    def __init__(self, rol, usuario, password, email):
        super().__init__()
        self.rol = rol
        self.usuario = usuario
        self.password = password
        self.email = email
    def run(self):
        exito = agregar_a_registro_usuario(self.rol, self.usuario, self.password, self.email)
        self.resultado.emit(exito)

class CargarMovimientoAgregarUsuarioThread(QThread):
    def __init__(self, usuario, usuario_activo):
        super().__init__()
        self.usuario = usuario
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_agregar_usuario(self.usuario, self.usuario_activo)

class TraerTodosLosUsuariosThread(QThread):
    resultado = Signal(list)
    def __init__(self):
        super().__init__()
    def run(self):
        usuarios_obtenidos = traer_todos_los_usuarios()  # Debe ser tu función que retorna la lista de usuarios
        self.resultado.emit(usuarios_obtenidos)


# editar usuario

class ActualizarUsuarioThread(QThread):
    resultado = Signal(bool)
    def __init__(self, id_usuario, rol, mail, password):
        super().__init__()
        self.id_usuario = id_usuario
        self.rol = rol
        self.mail = mail
        self.password = password
    def run(self):
        s = actualizar_usuario(self.id_usuario, self.rol, self.mail, self.password)
        self.resultado.emit(s)

class CargarMovimientoEditarUsuarioThread(QThread):
    def __init__(self, id_usuario, nombre_usuario, usuario_activo):
        super().__init__()
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.usuario_activo = usuario_activo
    def run(self):
        cargar_movimiento_editar_usuario(self.id_usuario, self.nombre_usuario, self.usuario_activo)


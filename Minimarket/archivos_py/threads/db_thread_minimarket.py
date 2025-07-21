from PySide6.QtCore import QThread, Signal
import requests

# ventana datos 
API_URL = "https://web-production-aa989.up.railway.app"


#Agregar productos:

class CategoriasThread(QThread):
    categorias_obtenidas = Signal(list)

    def run(self):
        
        try:
            url = f"{API_URL}/api/categorias"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                categorias = data.get("categorias", [])
                self.categorias_obtenidas.emit(categorias)
            else:
                print(f"Error al obtener categorías: {response.text}")
                self.categorias_obtenidas.emit([])
        except Exception as e:
            print(f"Error en CategoriasThread: {e}")
            self.categorias_obtenidas.emit([])


class ProveedoresThread(QThread):
    proveedores_obtenidos = Signal(list)

    def run(self):
        
        try:
            url = f"{API_URL}/api/proveedores"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                proveedores = data.get("proveedores", [])
                self.proveedores_obtenidos.emit(proveedores)
            else:
                print(f"Error al obtener proveedores: {response.text}")
                self.proveedores_obtenidos.emit([])
        except Exception as e:
            print(f"Error en ProveedoresThread: {e}")
            self.proveedores_obtenidos.emit([])

class AgregarProductoThread(QThread):
    producto_agregado = Signal(bool)  # Señal de éxito

    def __init__(
        self,
        id_producto,
        nombre_producto,
        precio_compra_producto,
        precio_venta_producto,
        cantidad_producto,
        stock_ideal,
        categoria_producto,
        proveedor_producto
    ):
        super().__init__()
        self.producto_data = {
            "id_producto": id_producto,
            "nombre_producto": nombre_producto,
            "precio_compra_producto": precio_compra_producto,
            "precio_venta_producto": precio_venta_producto,
            "cantidad_producto": cantidad_producto,
            "stock_ideal": stock_ideal,
            "categoria_producto": categoria_producto,
            "proveedor_producto": proveedor_producto
        }

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/agregar_producto"
            response = requests.post(url, json=self.producto_data)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.producto_agregado.emit(exito)
            else:
                print(f"Error al agregar producto: {response.text}")
                self.producto_agregado.emit(False)
        except Exception as e:
            print(f"Error en AgregarProductoThread: {e}")
            self.producto_agregado.emit(False)
            

class MovimientoProductoThread(QThread):
    movimiento_cargado = Signal()

    def __init__(self, input_id_value, usuario):
        super().__init__()
        self.input_id_value = input_id_value
        self.usuario = usuario

    def run(self):
        
        try:
            url = f"{API_URL}/api/cargar_movimiento_producto_agregado"
            payload = {
                "input_id_value": self.input_id_value,
                "usuario": self.usuario,
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.movimiento_cargado.emit()
            else:
                print(f"Error al cargar movimiento producto: {response.text}")
                self.movimiento_cargado.emit()
        except Exception as e:
            print(f"Error en MovimientoProductoThread: {e}")
            self.movimiento_cargado.emit()




# Borrar productos: 
# -> se utiliza el de movimientoproductothread tambien

class TraerIdProductoThread(QThread):
    resultado = Signal(int)

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_id_producto"
            payload = {"nombre": self.nombre}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                id_producto = data.get("id_producto", -1)
                self.resultado.emit(id_producto)
            else:
                print(f"Error al traer id_producto: {response.text}")
                self.resultado.emit(-1)
        except Exception as e:
            print(f"Error en TraerIdProductoThread: {e}")
            self.resultado.emit(-1)


class TraerNomProductoThread(QThread):
    resultado = Signal(str)
    def __init__(self, id_producto):
        super().__init__()
        self.id_producto = id_producto

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_nom_producto"
            payload = {"id_producto": self.id_producto}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                nombre_producto = data.get("nombre_producto", "")
                self.resultado.emit(nombre_producto)
            else:
                print(f"Error al traer nombre de producto: {response.text}")
                self.resultado.emit("")
        except Exception as e:
            print(f"Error en TraerNomProductoThread: {e}")
            self.resultado.emit("")

class BorrarProductoThread(QThread):
    resultado = Signal(bool)
    def __init__(self, valor):
        super().__init__()
        self.valor = valor
    def run(self):
        
        try:
            url = f"{API_URL}/api/borrar_producto"
            payload = {"valor": self.valor}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al borrar producto: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en BorrarProductoThread: {e}")
            self.resultado.emit(False)


class MovimientoProductoBorrarThread(QThread):
    movimiento_borrado = Signal()

    def __init__(self, _borrar_id, input_nombre_o_id_value, usuario_activo):
        super().__init__()
        self._borrar_id = _borrar_id
        self.input_nombre_o_id_value = input_nombre_o_id_value
        self.usuario_activo = usuario_activo

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_producto_borrado"
            payload = {
                "_borrar_id": self._borrar_id,
                "input_nombre_o_id_value": self.input_nombre_o_id_value,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.movimiento_borrado.emit()
            else:
                print(f"Error al cargar movimiento producto borrado: {response.text}")
                self.movimiento_borrado.emit()
        except Exception as e:
            print(f"Error en MovimientoProductoBorrarThread: {e}")
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
        
        try:
            url = f"{API_URL}/api/aumentar_precios_categoria"
            payload = {
                "valor1": self.valor1,
                "valor2": self.valor2,
                "categoria": self.categoria
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al aumentar precios por categoría: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error en AumentarPreciosCategoriaThread: {e}")
            self.finished.emit()


class AumentarPreciosProveedorThread(QThread):
    finished = Signal()
    def __init__(self, valor1, valor2, proveedor):
        super().__init__()
        self.valor1 = valor1
        self.valor2 = valor2
        self.proveedor = proveedor
    def run(self):
        
        try:
            url = f"{API_URL}/api/aumentar_precios_proveedor"
            payload = {
                "valor1": self.valor1,
                "valor2": self.valor2,
                "proveedor": self.proveedor
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al aumentar precios por proveedor: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error en AumentarPreciosProveedorThread: {e}")
            self.finished.emit()


class MovimientoAumentoPreciosThread(QThread):
    finished = Signal()
    def __init__(self, categoria_o_proveedor, usuario, es_categoria):
        super().__init__()
        self.categoria_o_proveedor = categoria_o_proveedor
        self.usuario = usuario
        self.es_categoria = es_categoria
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_aumento_precios"
            payload = {
                "categoria_o_proveedor": self.categoria_o_proveedor,
                "usuario": self.usuario,
                "es_categoria": self.es_categoria
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al cargar movimiento aumento precios: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error en MovimientoAumentoPreciosThread: {e}")
            self.finished.emit()


class TraerProductoPorIdThread(QThread):
    resultado = Signal(object)
    def __init__(self, id_producto):
        super().__init__()
        self.id_producto = id_producto
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_producto_por_id"
            payload = {"id_producto": self.id_producto}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                producto = data.get("producto", None)
                self.resultado.emit(producto)
            else:
                print(f"Error al traer producto por id: {response.text}")
                self.resultado.emit(None)
        except Exception as e:
            print(f"Error en TraerProductoPorIdThread: {e}")
            self.resultado.emit(None)


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
        
        try:
            url = f"{API_URL}/api/actualizar_producto"
            payload = {
                "id": self.id,
                "nombre_prod": self.nombre_prod,
                "precio_compra": self.precio_compra,
                "precio_venta": self.precio_venta,
                "stock": self.stock,
                "stock_ideal": self.stock_ideal,
                "categoria": self.categoria,
                "proveedor": self.proveedor
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al actualizar producto: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error en ActualizarProductoThread: {e}")
            self.finished.emit()


class MovimientoProductoEditadoThread(QThread):
    movimiento_editado = Signal()

    def __init__(self, id_producto, usuario_activo):
        super().__init__()
        self.id_producto = id_producto
        self.usuario_activo = usuario_activo

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_producto_editado"
            payload = {
                "id_producto": self.id_producto,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.movimiento_editado.emit()
            else:
                print(f"Error al cargar movimiento producto editado: {response.text}")
                self.movimiento_editado.emit()
        except Exception as e:
            print(f"Error en MovimientoProductoEditadoThread: {e}")
            self.movimiento_editado.emit()



# visualizar productos

class TraerTodosLosProductosThread(QThread):
    resultado = Signal(list)
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_todos_los_productos"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                productos = data.get("productos", [])
                self.resultado.emit(productos)
            else:
                print(f"Error al traer todos los productos: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerTodosLosProductosThread: {e}")
            self.resultado.emit([])


# agregar proveedor


class ProveedorThread(QThread):
    proveedor_cargado = Signal(bool)
    def __init__(self, nombre, telefono, direccion):
        super().__init__()
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion if direccion else ""  # Manejo de dirección opcional
    def run(self):
        
        try:
            url = f"{API_URL}/api/agregar_proveedor"
            payload = {
                "nombre": self.nombre,
                "telefono": self.telefono,
                "direccion": self.direccion
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.proveedor_cargado.emit(exito)
            else:
                print(f"Error al agregar proveedor: {response.text}")
                self.proveedor_cargado.emit(False)
        except Exception as e:
            print(f"Error en ProveedorThread: {e}")
            self.proveedor_cargado.emit(False)


class MovimientoProveedorThread(QThread):
    movimiento_cargado = Signal()
    def __init__(self, nombre, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_agregar_proveedor"
            payload = {
                "nombre": self.nombre,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.movimiento_cargado.emit()
            else:
                print(f"Error al cargar movimiento agregar proveedor: {response.text}")
                self.movimiento_cargado.emit()
        except Exception as e:
            print(f"Error en MovimientoProveedorThread: {e}")
            self.movimiento_cargado.emit()

 # borrar proveedor

# Hilo para buscar proveedor en la base

class BuscarProveedorThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        
        try:
            url = f"{API_URL}/api/buscar_proveedor"
            payload = {"nombre": self.nombre}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                bandera = data.get("existe", False)
                self.resultado.emit(bandera)
            else:
                print(f"Error al buscar proveedor: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en BuscarProveedorThread: {e}")
            self.resultado.emit(False)


# Hilo para traer el ID del proveedor

class TraerIdProveedorThread(QThread):
    resultado = Signal(int)
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_id_proveedor"
            payload = {"nombre": self.nombre}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                id_prov = data.get("id_proveedor", -1)
                self.resultado.emit(id_prov)
            else:
                print(f"Error al traer id proveedor: {response.text}")
                self.resultado.emit(-1)
        except Exception as e:
            print(f"Error en TraerIdProveedorThread: {e}")
            self.resultado.emit(-1)

# Hilo para cargar movimiento de proveedor borrado

class MovimientoProveedorBorradoThread(QThread):
    def __init__(self, nombre, id_proveedor, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.id_proveedor = id_proveedor
        self.usuario_activo = usuario_activo

    def run(self):

        try:
            url = f"{API_URL}/api/movimiento_proveedor_borrado"
            payload = {
                "nombre": self.nombre,
                "id_proveedor": self.id_proveedor,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                pass
            else:
                print(f"Error al cargar movimiento proveedor borrado: {response.text}")
        except Exception as e:
            print(f"Error en MovimientoProveedorBorradoThread: {e}")

# actualizar proveedor

class ActualizarProveedorThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre, telefono, direccion):
        super().__init__()
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion if direccion else ""  # Manejo de dirección opcional 
    def run(self):
        
        try:
            url = f"{API_URL}/api/actualizar_proveedor"
            payload = {
                "nombre": self.nombre,
                "telefono": self.telefono,
                "direccion": self.direccion
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al actualizar proveedor: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en ActualizarProveedorThread: {e}")
            self.resultado.emit(False)

class MovimientoProveedorEditadoThread(QThread):
    def __init__(self, nombre, usuario_activo):
        super().__init__()
        self.nombre = nombre
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_proveedor_editado"
            payload = {
                "nombre": self.nombre,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de proveedor editado registrado correctamente.")
            else:
                print(f"Error al cargar movimiento proveedor editado: {response.text}")
        except Exception as e:
            print(f"Error en MovimientoProveedorEditadoThread: {e}")

# agregar categoria

class CargarCategoriaThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_categoria):
        super().__init__()
        self.nombre_categoria = nombre_categoria
    def run(self):
        
        try:
            url = f"{API_URL}/api/agregar_categoria"
            payload = {"nombre_categoria": self.nombre_categoria}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al agregar categoría: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en CargarCategoriaThread: {e}")
            self.resultado.emit(False)

class MovimientoAgregarCategoriaThread(QThread):
    def __init__(self, nombre_categoria, usuario_activo):
        super().__init__()
        self.nombre_categoria = nombre_categoria
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_agregar_categoria"
            payload = {
                "nombre_categoria": self.nombre_categoria,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de agregar categoría registrado correctamente.")
            else:
                print(f"Error al cargar movimiento agregar categoría: {response.text}")
        except Exception as e:
            print(f"Error en MovimientoAgregarCategoriaThread: {e}")

# borrar categoria
class BuscarCategoriaThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_categoria):
        super().__init__()
        self.nombre_categoria = nombre_categoria
    def run(self):
        
        try:
            url = f"{API_URL}/api/buscar_categoria"
            payload = {"nombre_categoria": self.nombre_categoria}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                existe = data.get("existe", False)
                self.resultado.emit(existe)
            else:
                print(f"Error al buscar categoría: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en BuscarCategoriaThread: {e}")
            self.resultado.emit(False)


class MovimientoCategoriaBorradaThread(QThread):
    def __init__(self, nombre_categoria, id_categoria, usuario_activo):
        super().__init__()
        self.nombre_categoria = nombre_categoria
        self.id_categoria = id_categoria
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_categoria_borrada"
            payload = {
                "nombre_categoria": self.nombre_categoria,
                "id_categoria": self.id_categoria,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de categoría borrada registrado correctamente.")
            else:
                print(f"Error al cargar movimiento categoría borrada: {response.text}")
        except Exception as e:
            print(f"Error en MovimientoCategoriaBorradaThread: {e}")

# borrar datos

class CargarMovimientosThread(QThread):
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/cargar_movimientos_datos_borrados"
            payload = {"usuario_activo": self.usuario_activo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimientos de datos borrados cargados correctamente.")
            else:
                print(f"Error al cargar movimientos de datos borrados: {response.text}")
        except Exception as e:
            print(f"Error en CargarMovimientosThread: {e}")

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
        
        try:
            url = f"{API_URL}/api/clear_data"
            payload = {
                "borrar_categorias": self.borrar_categorias,
                "borrar_ventas_compras": self.borrar_ventas_compras,
                "borrar_proveedores": self.borrar_proveedores,
                "borrar_usuarios": self.borrar_usuarios,
                "borrar_movimientos": self.borrar_movimientos
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al borrar datos: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error en ClearDataThread: {e}")
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
        
        try:
            url = f"{API_URL}/api/agregar_registro_usuario"
            payload = {
                "rol": self.rol,
                "usuario": self.usuario,
                "password": self.password,
                "email": self.email
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al agregar usuario: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en AgregarRegistroUsuarioThread: {e}")
            self.resultado.emit(False)


class CargarMovimientoAgregarUsuarioThread(QThread):
    def __init__(self, usuario, usuario_activo):
        super().__init__()
        self.usuario = usuario
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_agregar_usuario"
            payload = {
                "usuario": self.usuario,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de agregar usuario registrado correctamente.")
            else:
                print(f"Error al cargar movimiento agregar usuario: {response.text}")
        except Exception as e:
            print(f"Error en CargarMovimientoAgregarUsuarioThread: {e}")

class TraerTodosLosUsuariosThread(QThread):
    resultado = Signal(list)
    def __init__(self):
        super().__init__()
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_todos_los_usuarios"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                usuarios = data.get("usuarios", [])
                self.resultado.emit(usuarios)
            else:
                print(f"Error al traer todos los usuarios: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerTodosLosUsuariosThread: {e}")
            self.resultado.emit([])

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
        
        try:
            url = f"{API_URL}/api/actualizar_usuario"
            payload = {
                "id_usuario": self.id_usuario,
                "rol": self.rol,
                "mail": self.mail,
                "password": self.password
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al actualizar usuario: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en ActualizarUsuarioThread: {e}")
            self.resultado.emit(False)

class CargarMovimientoEditarUsuarioThread(QThread):
    def __init__(self, id_usuario, nombre_usuario, usuario_activo):
        super().__init__()
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.usuario_activo = usuario_activo
    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_editar_usuario"
            payload = {
                "id_usuario": self.id_usuario,
                "nombre_usuario": self.nombre_usuario,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de edición de usuario registrado correctamente.")
            else:
                print(f"Error al cargar movimiento editar usuario: {response.text}")
        except Exception as e:
            print(f"Error en CargarMovimientoEditarUsuarioThread: {e}")


class TraerIdUsuarioThread(QThread):
    resultado = Signal(object)
    def __init__(self, nombre_usuario):
        super().__init__()
        self.nombre_usuario = nombre_usuario

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_id_usuario"
            payload = {"nombre_usuario": self.nombre_usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                id_usuario = data.get("id_usuario", None)
                self.resultado.emit(id_usuario)
            else:
                print(f"Error al traer id usuario: {response.text}")
                self.resultado.emit(None)
        except Exception as e:
            print(f"Error en TraerIdUsuarioThread: {e}")
            self.resultado.emit(None)

# Hilo para borrar el usuario
class BorrarUsuarioThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_usuario):
        super().__init__()
        self.nombre_usuario = nombre_usuario

    def run(self):
        
        try:
            url = f"{API_URL}/api/borrar_usuario"
            payload = {"nombre_usuario": self.nombre_usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al borrar usuario: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en BorrarUsuarioThread: {e}")
            self.resultado.emit(False)



# Hilo para cargar el movimiento de usuario borrado
class MovimientoUsuarioBorradoThread(QThread):
    finished = Signal(object)
    def __init__(self, nombre_usuario, id_usuario, usuario_activo):
        super().__init__()
        self.nombre_usuario = nombre_usuario
        self.id_usuario = id_usuario
        self.usuario_activo = usuario_activo

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimiento_usuario_borrado"
            payload = {
                "nombre_usuario": self.nombre_usuario,
                "id_usuario": self.id_usuario,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit(True)
            else:
                print(f"Error al cargar movimiento usuario borrado: {response.text}")
                self.finished.emit(False)
        except Exception as e:
            print(f"Error en MovimientoUsuarioBorradoThread: {e}")
            self.finished.emit(False)

######################################
######################################

 # ventana buscar datos


class MovimientosPorUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimientos_por_usuario"
            payload = {"usuario": self.usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                movimientos = data.get("movimientos", [])
                self.resultado.emit(movimientos)
            else:
                print(f"Error al traer movimientos por usuario: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en MovimientosPorUsuarioThread: {e}")
            self.resultado.emit([])


class MovimientosPorFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimientos_por_fecha"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                movimientos = data.get("movimientos", [])
                self.resultado.emit(movimientos)
            else:
                print(f"Error al traer movimientos por fecha: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en MovimientosPorFechaThread: {e}")
            self.resultado.emit([])

class MovimientosPorAccionThread(QThread):
    resultado = Signal(list)
    def __init__(self, accion):
        super().__init__()
        self.accion = accion

    def run(self):
        
        try:
            url = f"{API_URL}/api/movimientos_por_accion"
            payload = {"accion": self.accion}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                movimientos = data.get("movimientos", [])
                self.resultado.emit(movimientos)
            else:
                print(f"Error al traer movimientos por acción: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en MovimientosPorAccionThread: {e}")
            self.resultado.emit([]) 


# corte

class TraerTodosLosMetodosPagoThread(QThread):
    resultado = Signal(list)
    
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_todos_metodos_pago"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                metodos = data.get("metodos_pago", [])
                self.resultado.emit(metodos)
            else:
                print(f"Error al obtener métodos de pago: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error al obtener métodos de pago: {e}")
            self.resultado.emit([])

class TraerMetodoPagoIdThread(QThread):
    resultado = Signal(object)
    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_metodo_pago_id"
            payload = {"nombre_metodo": self.nombre_metodo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                id_metodo = data.get("id_metodo", None)
                self.resultado.emit(id_metodo)
            else:
                print(f"Error al traer id del método de pago: {response.text}")
                self.resultado.emit(None)
        except Exception as e:
            print(f"Error en TraerMetodoPagoIdThread: {e}")
            self.resultado.emit(None)

class TraerDatosVentasMetodoUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, id_metodo_o_usuario, fecha):
        super().__init__()
        self.id_metodo_o_usuario = id_metodo_o_usuario
        self.fecha = fecha

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_datos_ventas_metodo_o_usuario"
            payload = {
                "id_metodo_o_usuario": self.id_metodo_o_usuario,
                "fecha": self.fecha
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos de ventas por método o usuario: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosVentasMetodoUsuarioThread: {e}")
            self.resultado.emit([])

class TraerDatosComprasMetodoUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, id_metodo_o_usuario, fecha):
        super().__init__()
        self.id_metodo_o_usuario = id_metodo_o_usuario
        self.fecha = fecha

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_datos_compras_metodo_o_usuario"
            payload = {
                "id_metodo_o_usuario": self.id_metodo_o_usuario,
                "fecha": self.fecha
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos de compras por método o usuario: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosComprasMetodoUsuarioThread: {e}")
            self.resultado.emit([])

class TraerMetodoPagoThread(QThread):
    resultado = Signal(object)
    def __init__(self, id_metodo):
        super().__init__()
        self.id_metodo = id_metodo

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_metodo_pago"
            payload = {"id_metodo": self.id_metodo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                metodo = data.get("metodo", None)
                self.resultado.emit(metodo)
            else:
                print(f"Error al traer método de pago: {response.text}")
                self.resultado.emit(None)
        except Exception as e:
            print(f"Error en TraerMetodoPagoThread: {e}")
            self.resultado.emit(None)

class TraerDatosArqueoVentasFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_datos_arqueo_ventas_fecha"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos de arqueo ventas por fecha: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosArqueoVentasFechaThread: {e}")
            self.resultado.emit([])

class TraerDatosArqueoComprasFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_datos_arqueo_compras_fecha"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos de arqueo compras por fecha: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosArqueoComprasFechaThread: {e}")
            self.resultado.emit([])

class TraerMetodosDePagoThread(QThread):
    resultado = Signal(list)
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_metodos_de_pago"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                metodos = data.get("metodos_pago", [])
                self.resultado.emit(metodos)
            else:
                print(f"Error al obtener métodos de pago: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerMetodosDePagoThread: {e}")
            self.resultado.emit([])


class TraerVentasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_totales_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales del día: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesDiaThread: {e}")
            self.resultado.emit(0.0)

class TraerGananciasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ganancias_totales_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ganancias totales del día: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerGananciasTotalesDiaThread: {e}")
            self.resultado.emit(0.0)

class TraerComprasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_compras_totales_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer compras totales del día: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerComprasTotalesDiaThread: {e}")
            self.resultado.emit(0.0)

class TraerNumeroDeComprasDiaThread(QThread):
    resultado = Signal(int)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_compras_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de compras del día: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeComprasDiaThread: {e}")
            self.resultado.emit(0)

class TraerVentasPorMetodoDiaThread(QThread):
    resultado = Signal(dict)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_por_metodo_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas_por_metodo = data.get("ventas_por_metodo", {})
                self.resultado.emit(ventas_por_metodo)
            else:
                print(f"Error al traer ventas por método del día: {response.text}")
                self.resultado.emit({})
        except Exception as e:
            print(f"Error en TraerVentasPorMetodoDiaThread: {e}")
            self.resultado.emit({})


class TraerNumeroDeVentasDiaThread(QThread):
    resultado = Signal(int)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_ventas_dia"
            payload = {"fecha": self.fecha}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de ventas del día: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeVentasDiaThread: {e}")
            self.resultado.emit(0)

class TraerVentasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_totales_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales del mes: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesMesThread: {e}")
            self.resultado.emit(0.0)

class TraerGananciasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ganancias_totales_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ganancias totales del mes: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerGananciasTotalesMesThread: {e}")
            self.resultado.emit(0.0)

class TraerComprasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_compras_totales_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer compras totales del mes: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerComprasTotalesMesThread: {e}")
            self.resultado.emit(0.0)

class TraerNumeroDeComprasMesThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_compras_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de compras del mes: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeComprasMesThread: {e}")
            self.resultado.emit(0)

class TraerVentasPorMetodoMesThread(QThread):
    resultado = Signal(dict)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_por_metodo_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas_por_metodo = data.get("ventas_por_metodo", {})
                self.resultado.emit(ventas_por_metodo)
            else:
                print(f"Error al traer ventas por método del mes: {response.text}")
                self.resultado.emit({})
        except Exception as e:
            print(f"Error en TraerVentasPorMetodoMesThread: {e}")
            self.resultado.emit({})

class TraerNumeroDeVentasMesThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_ventas_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("numero_ventas_mes", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de ventas del mes: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeVentasMesThread: {e}")
            self.resultado.emit(0)

class TraerVentasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_totales_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales del año: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesAnoThread: {e}")
            self.resultado.emit(0.0)


class TraerComprasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_compras_totales_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer compras totales del año: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerComprasTotalesAnoThread: {e}")
            self.resultado.emit(0.0)

class TraerNumeroDeComprasAnoThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_compras_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de compras del año: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeComprasAnoThread: {e}")
            self.resultado.emit(0)

class TraerVentasPorMetodoAnoThread(QThread):
    resultado = Signal(dict)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_por_metodo_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas_por_metodo = data.get("ventas_por_metodo", {})
                self.resultado.emit(ventas_por_metodo)
            else:
                print(f"Error al traer ventas por método del año: {response.text}")
                self.resultado.emit({})
        except Exception as e:
            print(f"Error en TraerVentasPorMetodoAnoThread: {e}")
            self.resultado.emit({})

class TraerNumeroDeVentasAnoThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio

    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_numero_de_ventas_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("numero_ventas_ano", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de ventas del año: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeVentasAnoThread: {e}")
            self.resultado.emit(0)


# Estadistias

class TraerVentasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        
        try:
            url = f"{API_URL}/api/traer_ventas_totales_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales del año: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesAnoThread: {e}")
            self.resultado.emit(0.0)

class TraerVentaPromedioAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_venta_promedio_ano_actual"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                promedio = data.get("venta_promedio_ano", 0.0)
                self.resultado.emit(promedio)
            else:
                print(f"Error al traer venta promedio del año: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentaPromedioAnoThread: {e}")
            self.resultado.emit(0.0)

class TraerGananciasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_totales_ano"
            payload = {"anio": self.anio}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ganancias totales del año: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerGananciasTotalesAnoThread: {e}")
            self.resultado.emit(0.0)

class TraerVentasAnoActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, meses):
        super().__init__()
        self.anio = anio
        self.meses = meses
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ventas_ano_actual"
            payload = {"anio": self.anio, "meses": self.meses}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas = data.get("ventas", [])
                self.resultado.emit(ventas)
            else:
                print(f"Error al traer ventas del año actual: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerVentasAnoActualThread: {e}")
            self.resultado.emit([])

class TraerGananciasAnoActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, meses):
        super().__init__()
        self.anio = anio
        self.meses = meses
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_ano_actual"
            payload = {"anio": self.anio, "meses": self.meses}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ganancias = data.get("ganancias", [])
                self.resultado.emit(ganancias)
            else:
                print(f"Error al traer ganancias del año actual: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerGananciasAnoActualThread: {e}")
            self.resultado.emit([])

class TraerMetodosPagoYSuIdThread(QThread):
    resultado = Signal(list)
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_metodos_pago_y_su_id"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                metodos = data.get("metodos", [])
                self.resultado.emit(metodos)
            else:
                print(f"Error al traer métodos de pago y su id: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerMetodosPagoYSuIdThread: {e}")
            self.resultado.emit([])

class TraerDatosPorMetodoYMesThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, id_metodo, meses):
        super().__init__()
        self.anio = anio
        self.id_metodo = id_metodo
        self.meses = meses
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_datos_por_metodo_y_mes"
            payload = {
                "anio": self.anio,
                "id_metodo": self.id_metodo,
                "meses": self.meses
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos por método y mes: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosPorMetodoYMesThread: {e}")
            self.resultado.emit([])

class TraerVentaPromedioMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_venta_promedio_mes"
            payload = {"anio": self.anio, "mes": self.mes}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                promedio = data.get("venta_promedio_mes", 0.0)
                self.resultado.emit(promedio)
            else:
                print(f"Error al traer venta promedio del mes: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentaPromedioMesThread: {e}")
            self.resultado.emit(0.0)


class TraerVentasTotalesSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ventas_totales_semana"
            payload = {"anio": self.anio, "semana": self.semana}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales de la semana: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesSemanaThread: {e}")
            self.resultado.emit(0.0)

class TraerNumeroDeVentasSemanaThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_numero_de_ventas_semana"
            payload = {"anio": self.anio, "semana": self.semana}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de ventas de la semana: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeVentasSemanaThread: {e}")
            self.resultado.emit(0)

class TraerVentaPromedioSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_venta_promedio_semana"
            payload = {"anio": self.anio, "semana": self.semana}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                promedio = data.get("venta_promedio_semana", 0.0)
                self.resultado.emit(promedio)
            else:
                print(f"Error al traer venta promedio de la semana: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentaPromedioSemanaThread: {e}")
            self.resultado.emit(0.0)

class TraerGananciasTotalesSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_totales_semana"
            payload = {"anio": self.anio, "semana": self.semana}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ganancias totales de la semana: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerGananciasTotalesSemanaThread: {e}")
            self.resultado.emit(0.0)

class TraerVentasSemanaActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.dias_semana = dias_semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ventas_semana_actual"
            payload = {
                "anio": self.anio,
                "semana": self.semana,
                "dias_semana": self.dias_semana
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas = data.get("ventas", [])
                self.resultado.emit(ventas)
            else:
                print(f"Error al traer ventas de la semana actual: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerVentasSemanaActualThread: {e}")
            self.resultado.emit([])

class TraerGananciasSemanaActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.dias_semana = dias_semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_semana_actual"
            payload = {
                "anio": self.anio,
                "semana": self.semana,
                "dias_semana": self.dias_semana
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ganancias = data.get("ganancias", [])
                self.resultado.emit(ganancias)
            else:
                print(f"Error al traer ganancias de la semana actual: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerGananciasSemanaActualThread: {e}")
            self.resultado.emit([])

class TraerDatosPorMetodoYDiaSemanaThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, id_metodo, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.id_metodo = id_metodo
        self.dias_semana = dias_semana
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_datos_por_metodo_y_dia_semana"
            payload = {
                "anio": self.anio,
                "semana": self.semana,
                "id_metodo": self.id_metodo,
                "dias_semana": self.dias_semana
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos por método y día de semana: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosPorMetodoYDiaSemanaThread: {e}")
            self.resultado.emit([])



## periodo

class TraerVentasTotalesPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ventas_totales_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ventas totales del periodo: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentasTotalesPeriodoThread: {e}")
            self.resultado.emit(0.0)

class TraerNumeroDeVentasPeriodoThread(QThread):
    resultado = Signal(int)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_numero_de_ventas_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer número de ventas del periodo: {response.text}")
                self.resultado.emit(0)
        except Exception as e:
            print(f"Error en TraerNumeroDeVentasPeriodoThread: {e}")
            self.resultado.emit(0)

class TraerVentaPromedioPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_venta_promedio_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                promedio = data.get("venta_promedio_periodo", 0.0)
                self.resultado.emit(promedio)
            else:
                print(f"Error al traer venta promedio del periodo: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerVentaPromedioPeriodoThread: {e}")
            self.resultado.emit(0.0)

class TraerGananciasTotalesPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_totales_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                total = data.get("total", 0.0)
                self.resultado.emit(total)
            else:
                print(f"Error al traer ganancias totales del periodo: {response.text}")
                self.resultado.emit(0.0)
        except Exception as e:
            print(f"Error en TraerGananciasTotalesPeriodoThread: {e}")
            self.resultado.emit(0.0)

class TraerVentasPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ventas_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ventas = data.get("ventas", [])
                self.resultado.emit(ventas)
            else:
                print(f"Error al traer ventas del periodo: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerVentasPeriodoThread: {e}")
            self.resultado.emit([])

class TraerGananciasPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ganancias_periodo"
            payload = {"periodo1": self.periodo1, "periodo2": self.periodo2}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                ganancias = data.get("ganancias", [])
                self.resultado.emit(ganancias)
            else:
                print(f"Error al traer ganancias del periodo: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerGananciasPeriodoThread: {e}")
            self.resultado.emit([])


class TraerDatosPorMetodoYDiaPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2, id_metodo):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
        self.id_metodo = id_metodo
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_datos_por_metodo_y_dia_periodo"
            payload = {
                "periodo1": self.periodo1,
                "periodo2": self.periodo2,
                "id_metodo": self.id_metodo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                datos = data.get("datos", [])
                self.resultado.emit(datos)
            else:
                print(f"Error al traer datos por método y día del periodo: {response.text}")
                self.resultado.emit([])
        except Exception as e:
            print(f"Error en TraerDatosPorMetodoYDiaPeriodoThread: {e}")
            self.resultado.emit([])

### facturero ventas

class VerificarYAgregarMPThread(QThread):
    finished = Signal()

    def __init__(self):
        super().__init__()

    def run(self):
        import requests
        try:
            url_verificar = f"{API_URL}/api/verificar_existencia_de_mp"
            response = requests.get(url_verificar)
            existe = False
            if response.status_code == 200:
                data = response.json()
                existe = data.get("existe", False)
            else:
                print(f"Error al verificar existencia de MP: {response.text}")

            if not existe:
                url_agregar = f"{API_URL}/api/agregar_mp_default"
                response_agregar = requests.post(url_agregar)
                if response_agregar.status_code != 200:
                    print(f"Error al agregar MP default: {response_agregar.text}")

        except Exception as e:
            print(f"Error en VerificarYAgregarMPThread: {e}")

        self.finished.emit()

class AgregarMPThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/agregar_metodo_pago"
            payload = {"nombre_metodo": self.nombre_metodo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al agregar método de pago: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en AgregarMPThread: {e}")
            self.resultado.emit(False)

class BorrarMPThread(QThread):
    resultado = Signal(bool, int)  # Emite bool e int

    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo

    def run(self):
        import requests
        try:
            # Traer el id del método de pago
            url_id = f"{API_URL}/api/traer_metodo_pago_id"
            payload_id = {"nombre_metodo": self.nombre_metodo}
            response_id = requests.post(url_id, json=payload_id)
            if response_id.status_code == 200:
                data_id = response_id.json()
                id_metodo = data_id.get("id_metodo", 0)
            else:
                print(f"Error al traer id del método de pago: {response_id.text}")
                self.resultado.emit(False, 0)
                return

            # Borrar el método de pago
            url_borrar = f"{API_URL}/api/borrar_metodo_pago"
            payload_borrar = {"nombre_metodo": self.nombre_metodo}
            response_borrar = requests.post(url_borrar, json=payload_borrar)
            if response_borrar.status_code == 200:
                data_borrar = response_borrar.json()
                exito = data_borrar.get("exito", False)
                self.resultado.emit(exito, id_metodo)
            else:
                print(f"Error al borrar método de pago: {response_borrar.text}")
                self.resultado.emit(False, id_metodo)
        except Exception as e:
            print(f"Error en BorrarMPThread: {e}")
            self.resultado.emit(False, 0)


class ActualizarCantidadProductosThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, productos_seleccionados, m, s=False):
        super().__init__()
        self.productos_seleccionados = productos_seleccionados
        self.m = m
        self.s = s
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/actualizar_cantidad_productos"
            payload = {
                "productos_seleccionados": self.productos_seleccionados,
                "m": self.m,
                "s": self.s
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al actualizar cantidad de productos: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en ActualizarCantidadProductosThread: {e}")
            self.resultado.emit(False)

class AgregarARegistroThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, productos_seleccionados, s, usuario_activo):
        super().__init__()
        self.productos_seleccionados = productos_seleccionados
        self.s = s
        self.usuario_activo = usuario_activo
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/agregar_a_registro"
            payload = {
                "productos_seleccionados": self.productos_seleccionados,
                "s": self.s,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al agregar a registro: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en AgregarARegistroThread: {e}")
            self.resultado.emit(False)


class CargarMovimientoVentaThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/cargar_movimiento_venta"
            payload = {"usuario": self.usuario_activo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("resultado", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al cargar movimiento venta: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en CargarMovimientoVentaThread: {e}")
            self.resultado.emit(False)

class CargarMovimientoCompraThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/cargar_movimiento_compra"
            payload = {"usuario": self.usuario_activo}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("resultado", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al cargar movimiento compra: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en CargarMovimientoCompraThread: {e}")
            self.resultado.emit(False)


class MovimientoAgregarMetodoPagoThread(QThread):
    finished = Signal()

    def __init__(self, metodo_pago, usuario_activo):
        super().__init__()
        self.metodo_pago = metodo_pago
        self.usuario_activo = usuario_activo

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/cargar_movimiento_agregar_metodo_pago"
            payload = {
                "metodo_pago": self.metodo_pago,
                "usuario": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al cargar movimiento de agregar método de pago: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error al cargar movimiento de agregar método de pago: {e}")
            self.finished.emit()

class MovimientoBorrarMetodoPagoThread(QThread):
    finished = Signal()

    def __init__(self, metodo_pago, usuario_activo, id):
        super().__init__()
        self.metodo_pago = metodo_pago
        self.usuario_activo = usuario_activo
        self.id = id

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/cargar_movimiento_borrar_metodo_pago"
            payload = {
                "metodo_pago": self.metodo_pago,
                "usuario": self.usuario_activo,
                "id": self.id
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.finished.emit()
            else:
                print(f"Error al cargar movimiento de borrar método de pago: {response.text}")
                self.finished.emit()
        except Exception as e:
            print(f"Error al cargar movimiento de borrar método de pago: {e}")
            self.finished.emit()

# anotador

class TraerUltimoTextoAnotadorThread(QThread):
    resultado = Signal(str)  # Emite el texto obtenido
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_ultimo_texto_anotador"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                ultimo_texto = data.get("ultimo_texto", "")
                self.resultado.emit(ultimo_texto)
            else:
                print(f"Error al traer último texto del anotador: {response.text}")
                self.resultado.emit("")
        except Exception as e:
            print(f"Error al traer último texto del anotador: {e}")
            self.resultado.emit("")

class SetTextoAnotadorThread(QThread):
    resultado = Signal(bool)  # Emite True si se estableció correctamente

    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/set_texto_principal_anotador"
            payload = {"usuario": self.usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al establecer texto principal del anotador: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error al establecer texto principal del anotador: {e}")
            self.resultado.emit(False)

class LimpiarAnotacionesThread(QThread):
    resultado = Signal(bool)  # Emite True si se limpiaron correctamente

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/limpiar_anotaciones"
            response = requests.post(url)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al limpiar anotaciones: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error en hilo al limpiar anotaciones: {e}")
            self.resultado.emit(False)

class GuardarAlCerrarThread(QThread):
    resultado = Signal(bool)  # Señal para indicar si se guardó correctamente

    def __init__(self, texto, usuario):
        super().__init__()
        self.texto = texto
        self.usuario = usuario

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/guardar_texto_anotador"
            payload = {"texto": self.texto, "usuario": self.usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.resultado.emit(exito)
            else:
                print(f"Error al guardar texto del anotador: {response.text}")
                self.resultado.emit(False)
        except Exception as e:
            print(f"Error al guardar: {e}")
            self.resultado.emit(False)


# movimiento inicio de sesion

class MovimientoLoginThread(QThread):
    finished = Signal(bool)
    
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
    
    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/cargar_movimiento_inicio"
            payload = {"usuario": self.usuario}
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                exito = data.get("exito", False)
                self.finished.emit(exito)
            else:
                print(f"Error al cargar movimiento inicio: {response.text}")
                self.finished.emit(False)
        except Exception as e:
            print(f"Error en MovimientoLoginThread: {e}")
            self.finished.emit(False)
from PySide6.QtCore import QThread, Signal


# ventana datos 
API_URL = "https://web-production-aa989.up.railway.app"


#Agregar productos:

class CategoriasThread(QThread):
    categorias_obtenidas = Signal(list)

    def run(self):
        import requests
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
        import requests
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
    producto_agregado = Signal(bool)  # éxito

    def __init__(self, **kwargs):
        super().__init__()
        self.producto_data = kwargs  # Recibe los datos del producto como diccionario

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
        import requests
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

    def __init__(self, nombre, uid):
        super().__init__()
        self.nombre = nombre
        self.uid = uid

    def run(self):
        import requests
        try:
            url = f"{API_URL}/api/traer_id_producto"
            payload = {"nombre": self.nombre, "uid": self.uid}
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        self.direccion = direccion
    def run(self):
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
        try:
            url = f"{API_URL}/api/movimiento_proveedor_borrado"
            payload = {
                "nombre": self.nombre,
                "id_proveedor": self.id_proveedor,
                "usuario_activo": self.usuario_activo
            }
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("Movimiento de proveedor borrado registrado correctamente.")
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
        self.direccion = direccion
    def run(self):
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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
        import requests
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


class TraerIdUsuarioThread(QThread):
    resultado = Signal(object)
    def __init__(self, nombre_usuario):
        super().__init__()
        self.nombre_usuario = nombre_usuario

    def run(self):
        # Simula consulta a la base de datos
        # Reemplaza esto por tu lógica real
        id_usuario = traer_id_usuario(self.nombre_usuario)
        self.resultado.emit(id_usuario)

    

# Hilo para borrar el usuario
class BorrarUsuarioThread(QThread):
    resultado = Signal(bool)
    def __init__(self, nombre_usuario):
        super().__init__()
        self.nombre_usuario = nombre_usuario

    def run(self):
        # Simula borrado en la base de datos
        # Reemplaza esto por tu lógica real
        exito = borrar_usuario(self.nombre_usuario)
        self.resultado.emit(exito)


# Hilo para cargar el movimiento de usuario borrado
class MovimientoUsuarioBorradoThread(QThread):
    finished = Signal(object)
    def __init__(self, nombre_usuario, id_usuario, usuario_activo):
        super().__init__()
        self.nombre_usuario = nombre_usuario
        self.id_usuario = id_usuario
        self.usuario_activo = usuario_activo

    def run(self):
        # Simula registrar el movimiento
        # Reemplaza esto por tu lógica real
        cargar_movimiento_usuario_borrado(self.nombre_usuario, self.id_usuario, self.usuario_activo)
        self.finished.emit(True)



######################################
######################################

 # ventana buscar datos


class MovimientosPorUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def run(self):
        movimientos = traer_movimientos_por_usuario(self.usuario)
        self.resultado.emit(movimientos)

class MovimientosPorFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        movimientos = traer_movimientos_por_fecha(self.fecha)
        self.resultado.emit(movimientos)

class MovimientosPorAccionThread(QThread):
    resultado = Signal(list)
    def __init__(self, accion):
        super().__init__()
        self.accion = accion

    def run(self):
        movimientos = traer_movimientos_por_accion(self.accion)
        self.resultado.emit(movimientos)    


# corte

class TraerTodosLosMetodosPagoThread(QThread):
    resultado = Signal(list)
    
    def run(self):
        try:
            metodos = traer_todos_metodos_pago()
            self.resultado.emit(metodos)
        except Exception as e:
            print(f"Error al obtener métodos de pago: {e}")
            self.resultado.emit([])

class TraerMetodoPagoIdThread(QThread):
    resultado = Signal(object)
    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo

    def run(self):
        id_metodo = traer_metodo_pago_id(self.nombre_metodo)
        self.resultado.emit(id_metodo)

class TraerDatosVentasMetodoUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, id_metodo_o_usuario, fecha):
        super().__init__()
        self.id_metodo_o_usuario = id_metodo_o_usuario
        self.fecha = fecha

    def run(self):
        datos = traer_datos_ventas_metodo_o_usuario(self.id_metodo_o_usuario, self.fecha)
        self.resultado.emit(datos)

class TraerDatosComprasMetodoUsuarioThread(QThread):
    resultado = Signal(list)
    def __init__(self, id_metodo_o_usuario, fecha):
        super().__init__()
        self.id_metodo_o_usuario = id_metodo_o_usuario
        self.fecha = fecha

    def run(self):
        datos = traer_datos_compras_metodo_o_usuario(self.id_metodo_o_usuario, self.fecha)
        self.resultado.emit(datos)

class TraerMetodoPagoThread(QThread):
    resultado = Signal(object)
    def __init__(self, id_metodo):
        super().__init__()
        self.id_metodo = id_metodo

    def run(self):
        metodo = traer_metodo_pago(self.id_metodo)
        self.resultado.emit(metodo)


class TraerDatosArqueoVentasFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        datos = traer_datos_arqueo_ventas_fecha(self.fecha)
        self.resultado.emit(datos)

class TraerDatosArqueoComprasFechaThread(QThread):
    resultado = Signal(list)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha

    def run(self):
        datos = traer_datos_arqueo_compras_fecha(self.fecha)
        self.resultado.emit(datos)

class TraerMetodosDePagoThread(QThread):
    resultado = Signal(list)
    def run(self):
        metodos = traer_metodos_de_pago()
        self.resultado.emit(metodos)


class TraerVentasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        total = traer_ventas_totales_dia(self.fecha)
        self.resultado.emit(total)

class TraerGananciasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        total = traer_ganancias_totales_dia(self.fecha)
        self.resultado.emit(total)

class TraerComprasTotalesDiaThread(QThread):
    resultado = Signal(float)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        total = traer_compras_totales_dia(self.fecha)
        self.resultado.emit(total)

class TraerNumeroDeComprasDiaThread(QThread):
    resultado = Signal(int)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        total = traer_numero_de_compras_dia(self.fecha)
        self.resultado.emit(total)

class TraerVentasPorMetodoDiaThread(QThread):
    resultado = Signal(dict)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        data = traer_ventas_por_metodo_dia(self.fecha)
        self.resultado.emit(data)

class TraerNumeroDeVentasDiaThread(QThread):
    resultado = Signal(int)
    def __init__(self, fecha):
        super().__init__()
        self.fecha = fecha
    def run(self):
        total = traer_numero_de_ventas_dia(self.fecha)
        self.resultado.emit(total)

class TraerVentasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        total = traer_ventas_totales_mes(self.anio, self.mes)
        self.resultado.emit(total)

class TraerGananciasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        total = traer_ganancias_totales_mes(self.anio, self.mes)
        self.resultado.emit(total)

class TraerComprasTotalesMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        total = traer_compras_totales_mes(self.anio, self.mes)
        self.resultado.emit(total)

class TraerNumeroDeComprasMesThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        total = traer_numero_de_compras_mes(self.anio, self.mes)
        self.resultado.emit(total)

class TraerVentasPorMetodoMesThread(QThread):
    resultado = Signal(dict)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        data = traer_ventas_por_metodo_mes(self.anio, self.mes)
        self.resultado.emit(data)

class TraerNumeroDeVentasMesThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        total = traer_numero_de_ventas_mes(self.anio, self.mes)
        self.resultado.emit(total)

class TraerVentasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_ventas_totales_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerGananciasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_ganancias_totales_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerComprasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_compras_totales_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerNumeroDeComprasAnoThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_numero_de_compras_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerVentasPorMetodoAnoThread(QThread):
    resultado = Signal(dict)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        data = traer_ventas_por_metodo_ano(self.anio)
        self.resultado.emit(data)

class TraerNumeroDeVentasAnoThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_numero_de_ventas_ano(self.anio)
        self.resultado.emit(total)


# Estadistias

class TraerVentasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_ventas_totales_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerNumeroDeVentasAnoThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_numero_de_ventas_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerVentaPromedioAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_venta_promedio_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerGananciasTotalesAnoThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio):
        super().__init__()
        self.anio = anio
    def run(self):
        total = traer_ganancias_totales_ano_actual(self.anio)
        self.resultado.emit(total)

class TraerVentasAnoActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, meses):
        super().__init__()
        self.anio = anio
        self.meses = meses
    def run(self):
        ventas = traer_ventas_ano_actual(self.anio, self.meses)
        self.resultado.emit(ventas)

class TraerGananciasAnoActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, meses):
        super().__init__()
        self.anio = anio
        self.meses = meses
    def run(self):
        ganancias = traer_ganancias_ano_actual(self.anio, self.meses)
        self.resultado.emit(ganancias)

class TraerMetodosPagoYSuIdThread(QThread):
    resultado = Signal(list)
    def run(self):
        metodos = traer_metodos_pago_y_su_id()
        self.resultado.emit(metodos)

class TraerDatosPorMetodoYMesThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, id_metodo, meses):
        super().__init__()
        self.anio = anio
        self.id_metodo = id_metodo
        self.meses = meses
    def run(self):
        datos = traer_datos_por_metodo_y_mes(self.anio, self.id_metodo, self.meses)
        self.resultado.emit(datos)

class TraerVentaPromedioMesThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, mes):
        super().__init__()
        self.anio = anio
        self.mes = mes
    def run(self):
        promedio = traer_venta_promedio_mes(self.anio, self.mes)
        self.resultado.emit(promedio)


class TraerVentasTotalesSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        total = traer_ventas_totales_semana(self.anio, self.semana)
        self.resultado.emit(total)

class TraerNumeroDeVentasSemanaThread(QThread):
    resultado = Signal(int)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        total = traer_numero_de_ventas_semana(self.anio, self.semana)
        self.resultado.emit(total)

class TraerVentaPromedioSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        promedio = traer_venta_promedio_semana(self.anio, self.semana)
        self.resultado.emit(promedio)

class TraerGananciasTotalesSemanaThread(QThread):
    resultado = Signal(float)
    def __init__(self, anio, semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
    def run(self):
        total = traer_ganancias_totales_semana(self.anio, self.semana)
        self.resultado.emit(total)

class TraerVentasSemanaActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.dias_semana = dias_semana
    def run(self):
        ventas = traer_ventas_semana_actual(self.anio, self.semana, self.dias_semana)
        self.resultado.emit(ventas)

class TraerGananciasSemanaActualThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.dias_semana = dias_semana
    def run(self):
        ganancias = traer_ganancias_semana_actual(self.anio, self.semana, self.dias_semana)
        self.resultado.emit(ganancias)

class TraerDatosPorMetodoYDiaSemanaThread(QThread):
    resultado = Signal(list)
    def __init__(self, anio, semana, id_metodo, dias_semana):
        super().__init__()
        self.anio = anio
        self.semana = semana
        self.id_metodo = id_metodo
        self.dias_semana = dias_semana
    def run(self):
        datos = traer_datos_por_metodo_y_dia_semana(self.anio, self.semana, self.id_metodo, self.dias_semana)
        self.resultado.emit(datos)



## periodo

class TraerVentasTotalesPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        total = traer_ventas_totales_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(total)

class TraerNumeroDeVentasPeriodoThread(QThread):
    resultado = Signal(int)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        total = traer_numero_de_ventas_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(total)

class TraerVentaPromedioPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        promedio = traer_venta_promedio_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(promedio)

class TraerGananciasTotalesPeriodoThread(QThread):
    resultado = Signal(float)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        total = traer_ganancias_totales_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(total)

class TraerVentasPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        ventas = traer_ventas_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(ventas)

class TraerGananciasPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
    def run(self):
        ganancias = traer_ganancias_periodo(self.periodo1, self.periodo2)
        self.resultado.emit(ganancias)

class TraerMetodosPagoYSuIdThread(QThread):
    resultado = Signal(list)
    def __init__(self):
        super().__init__()
    def run(self):
        metodos = traer_metodos_pago_y_su_id()
        self.resultado.emit(metodos)


class TraerDatosPorMetodoYDiaPeriodoThread(QThread):
    resultado = Signal(list)
    def __init__(self, periodo1, periodo2, id_metodo):
        super().__init__()
        self.periodo1 = periodo1
        self.periodo2 = periodo2
        self.id_metodo = id_metodo
    def run(self):
        datos = traer_datos_por_metodo_y_dia_periodo(self.periodo1, self.periodo2, self.id_metodo)
        self.resultado.emit(datos)

### facturero ventas

class VerificarYAgregarMPThread(QThread):
    finished = Signal()
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        
        if not verificar_existencia_de_mp():
            agregar_mp_default()
        
        self.finished.emit()

class AgregarMPThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo
    
    def run(self):
        exito = agregar_mp_db(self.nombre_metodo)
        self.resultado.emit(exito)

class BorrarMPThread(QThread):
    resultado = Signal(bool, int)  # ✅ Cambiar para emitir bool e int
    
    def __init__(self, nombre_metodo):
        super().__init__()
        self.nombre_metodo = nombre_metodo
        
    def run(self):
        try:
            #  Corregir: usar self.nombre_metodo en lugar de self.metodo_pago
            id_metodo = traer_mp(self.nombre_metodo)
            exito = borrar_mp_db(self.nombre_metodo)
            
            #  Emitir tanto el éxito como el ID
            self.resultado.emit(exito, id_metodo)
        except Exception as e:
            print(f"Error al borrar método de pago: {e}")
            #  En caso de error, emitir False y 0
            self.resultado.emit(False, 0)

class ActualizarCantidadProductosThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, productos_seleccionados, m, s=False):
        super().__init__()
        self.productos_seleccionados = productos_seleccionados
        self.m = m
        self.s = s
    
    def run(self):
        exito = actualizar_cantidad_productos(self.productos_seleccionados, self.m, self.s)
        self.resultado.emit(exito)



class AgregarARegistroThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, productos_seleccionados, s, usuario_activo):
        super().__init__()
        self.productos_seleccionados = productos_seleccionados
        self.s = s
        self.usuario_activo = usuario_activo
    
    def run(self):
        exito = agregar_a_registro(self.productos_seleccionados, self.s, self.usuario_activo)
        self.resultado.emit(exito)

class CargarMovimientoVentaThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    
    def run(self):
        exito = cargar_movimiento_venta(self.usuario_activo)
        self.resultado.emit(exito)

class CargarMovimientoCompraThread(QThread):
    resultado = Signal(bool)
    
    def __init__(self, usuario_activo):
        super().__init__()
        self.usuario_activo = usuario_activo
    
    def run(self):
        exito = cargar_movimiento_compra(self.usuario_activo)
        self.resultado.emit(exito)

class MovimientoAgregarMetodoPagoThread(QThread):
    finished = Signal()

    def __init__(self, metodo_pago, usuario_activo):
        super().__init__()
        self.metodo_pago = metodo_pago
        self.usuario_activo = usuario_activo

    def run(self):
        try:
            # Llamar a la función que registra el movimiento en la base de datos
            cargar_movimiento_agregar_metodo_pago(self.metodo_pago, self.usuario_activo)
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
        try:
            # Llamar a la función que registra el movimiento en la base de datos
            cargar_movimiento_borrar_metodo_pago(self.metodo_pago, self.usuario_activo, self.id)
            self.finished.emit()
        except Exception as e:
            print(f"Error al cargar movimiento de borrar método de pago: {e}")
            self.finished.emit()

# anotador

class TraerUltimoTextoAnotadorThread(QThread):
    resultado = Signal(str)  # Emite el texto obtenido
    
    def run(self):
        try:
            ultimo_texto = traer_ultimo_agregado_anotador()
            if ultimo_texto:
                self.resultado.emit(ultimo_texto)
            else:
                self.resultado.emit("")  # Emite cadena vacía si no hay texto
        except Exception as e:
            print(f"Error al traer último texto del anotador: {e}")
            self.resultado.emit("")  # Emite cadena vacía en caso de error


class SetTextoAnotadorThread(QThread):
    resultado = Signal(bool)  # Emite True si se estableció correctamente
    
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
    
    def run(self):
        try:
            set_text_principal(self.usuario)
            self.resultado.emit(True)
        except Exception as e:
            print(f"Error al establecer texto principal del anotador: {e}")
            self.resultado.emit(False)


class GuardarTextoAnotadorThread(QThread):
    resultado = Signal(bool)  # Emite True si se guardó correctamente
    
    def __init__(self, texto, usuario):
        super().__init__()
        self.texto = texto
        self.usuario = usuario
    
    def run(self):
        try:
            # Aquí iría la función para guardar en BD
            # Ejemplo: guardar_texto_anotador(self.texto, self.usuario)
            self.resultado.emit(True)
        except Exception as e:
            print(f"Error al guardar texto del anotador: {e}")
            self.resultado.emit(False)

class LimpiarAnotacionesThread(QThread):
    resultado = Signal(bool)  # Emite True si se limpiaron correctamente
    
    def run(self):
        try:
            exito = limpiar_anotaciones_automatico()
            self.resultado.emit(exito)
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
        try:
            # Guardar una última vez al cerrar (por si hay cambios sin guardar)
            resultado = guardar_texto_anotador_sincrono(self.texto, self.usuario)

            self.resultado.emit(resultado)

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
        try:
            # Llamar a la función movimiento_inicio
            exito = cargar_movimiento_inicio(self.usuario)
            self.finished.emit(exito)

        except Exception as e:
            self.finished.emit(False)
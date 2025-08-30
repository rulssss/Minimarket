
from archivos_py.threads.db_thread_minimarket import *


class DataCacheManager:
    def __init__(self, id_usuario_perfil):
        self.id_usuario_perfil = id_usuario_perfil

        #variables de uso

        self.categorias_cache = None
        self.proveedores_cache = None
        self.productos_cache = None
        self.usuarios_cache = None
        self.metodos_pago_cache = None
        self.productos_cache_temporal = None
        self.productos_por_id_cache = None
        self.productos_por_nombre_cache = None
        self.proveedores_por_nombre_cache = None
        self.proveedores_por_telefono_cache = None
        self.categorias_por_nombre_cache = None
        self.usuarios_por_nombre_cache = None
        self.metodos_pago_por_id_cache = None


    def actualizar_variables_globales_de_uso(self, r, callback=None):

        global categorias , proveedores, productos, usuarios, metodos_pago, usuarios_cache
     
        global categorias_cache, proveedores_cache, productos_cache
        global productos_por_id_cache, productos_por_nombre_cache
        global proveedores_por_nombre_cache, proveedores_por_telefono_cache
        global categorias_por_nombre_cache, usuarios_por_nombre_cache, metodos_pago_por_id_cache, metodos_pago_cache
        global anios_obtenidos
        
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

            self.anios_thread = TraerAnios(self.id_usuario_perfil)
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
        

            # obetener todos los metodos de pago al iniciar
            self.metodos_pago_thread = TraerMetodosPagoYSuIdThread(self.id_usuario_perfil)
            def on_metodos_obtenidos(metodos):
                global metodos_pago_cache, metodos_pago_por_id_cache
                
                metodos_pago_cache = metodos
                metodos_pago_por_id_cache = {str(m[0]): m[1] for m in metodos}
                self._datos_cargados["metodos_pago"] = True
                check_all_loaded()
                

            self.metodos_pago_thread.resultado.connect(on_metodos_obtenidos)
            self.start_thread(self.metodos_pago_thread)
           
            # Obtener todas las categorías y asignarlas a la variable global 'categorias'
            self.categorias_thread = CategoriasThread(self.id_usuario_perfil)
            def on_categorias_obtenidas(cats):
                global categorias, categorias_por_nombre_cache
                categorias = cats
                categorias_por_nombre_cache = {c[1].strip().lower(): c for c in categorias}
                self._datos_cargados["categorias"] = True
                check_all_loaded()
                
            self.categorias_thread.categorias_obtenidas.connect(on_categorias_obtenidas)
            self.start_thread(self.categorias_thread)
        
            # Obtener todos los proveedores y asignarlos a la variable global 'proveedores'
            self.proveedores_thread = ProveedoresThread(self.id_usuario_perfil)
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
            self.productos_thread = TraerTodosLosProductosThread(self.id_usuario_perfil)
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
            self.usuarios_thread = TraerTodosLosUsuariosThread(self.id_usuario_perfil)
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
                self.categorias_thread = CategoriasThread(self.id_usuario_perfil)
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
                self.proveedores_thread = ProveedoresThread(self.id_usuario_perfil)
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
                self.productos_thread = TraerTodosLosProductosThread(self.id_usuario_perfil)
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
                self.usuarios_thread = TraerTodosLosUsuariosThread(self.id_usuario_perfil)
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
                self.metodos_pago_thread = TraerTodosLosMetodosPagoThread(self.id_usuario_perfil)
                def on_metodos_pago_obtenidos(metodos_obtenidos):
                    global metodos_pago, metodos_pago_cache, metodos_pago_por_id_cache
                    metodos_pago = metodos_obtenidos
                    metodos_pago_cache = metodos_obtenidos
                    metodos_pago_por_id_cache = {str(m[0]): m for m in metodos_pago}
                    
                    if callback:
                        callback()
                self.metodos_pago_thread.resultado.connect(on_metodos_pago_obtenidos)
                self.start_thread(self.metodos_pago_thread)


    def get_categorias_cache(self):
        return self.categorias_cache


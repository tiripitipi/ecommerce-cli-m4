# La clase Catalogo contiene y gestiona todos los productos

from producto import Producto
from excepciones import ProductoNoEncontradoError

class Catalogo:
    """Gestiona la colección de productos del Rincón del Tenis."""

    def __init__(self):
        # Utilizo los mismos productos que en el Modulo 2 y 3 
        self.__productos = [
            Producto(1, "Raqueta Wilson Pro Staff",       "raquetas",   89990),
            Producto(2, "Zapatillas Asics Gel-Dedicate",  "calzado",    49990),
            Producto(3, "Pelotas Babolat x4",             "pelotas",    8990),
            Producto(4, "Overgrip Wilson Pro x3",         "accesorios", 4990),
            Producto(5, "Camiseta Torino Verde Ellesse",  "ropa",       19990),
            Producto(6, "Antivibrador Head Xtra Damp x2", "accesorios", 8990),
        ]

    def listar_productos(self):
        """Retorna la lista completa de productos."""
        return self.__productos

    def buscar_por_id(self, id_producto):
        """Busca un producto por id. Lanza error si no existe."""
        for producto in self.__productos:
            if producto.get_id() == id_producto:
                return producto
        # Si no lo encontré, lanzo mi excepción personalizada
        raise ProductoNoEncontradoError(id_producto)

    def buscar_por_texto(self, texto):
        """Busca productos cuyo nombre o categoría contengan el texto."""
        texto = texto.lower()
        resultados = [
            # para acortar la escritura y que quede mas bonito
            p for p in self.__productos
            if texto in p.get_nombre().lower() or texto in p.get_categoria().lower()
        ]
        return resultados

    def agregar_producto(self, producto):
        """Agrega un nuevo producto al catálogo."""
        self.__productos.append(producto)

    def actualizar_producto(self, id_producto, nombre=None, categoria=None, precio=None):
        """Actualiza los datos de un producto existente."""
        # buscar_por_id ya lanza el error si no existe
        producto = self.buscar_por_id(id_producto)

        if nombre:
            producto.set_nombre(nombre)
        if categoria:
            producto.set_categoria(categoria)
        if precio:
            producto.set_precio(precio)

    def eliminar_producto(self, id_producto):
        """Elimina un producto del catálogo por su id."""
        producto = self.buscar_por_id(id_producto)
        self.__productos.remove(producto)

    def get_siguiente_id(self):
        """Calcula el próximo id disponible."""
        if not self.__productos:
            return 1
        return max(p.get_id() for p in self.__productos) + 1
# Acá defino mis propios tipos de error para la tienda

class ProductoNoEncontradoError(Exception):
    """Se lanza cuando se busca un producto que no existe en el catálogo."""
    
    def __init__(self, id_producto):
        self.id_producto = id_producto
        super().__init__(f"No existe ningún producto con id {id_producto}")


class CantidadInvalidaError(Exception):
    """Se lanza cuando la cantidad ingresada es menor o igual a 0."""
    
    def __init__(self, cantidad):
        self.cantidad = cantidad
        super().__init__(f"La cantidad debe ser mayor a 0, recibí: {cantidad}")
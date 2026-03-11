# Creo la clase Admin que hereda de Usuario 

from usuario import Usuario

class Admin(Usuario):
    """Usuario con permisos para gestionar el catálogo."""

    def __init__(self, nombre):
        # Le paso el rol fijo "ADMIN" a la clase padre
        super().__init__(nombre, "ADMIN")

    def puede_editar_catalogo(self):
        """El admin siempre puede editar el catálogo."""
        return True
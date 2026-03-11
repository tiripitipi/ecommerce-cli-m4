# 🎾 El Rincón del Tenis — Módulo 4

Continuación del ecommerce del Módulo 3, pero ahora re-estructurado usando POO (Programación Orientada a Objetos). Aprendí a separar el código en clases, usar herencia y manejar errores con excepciones personalizadas.

## ¿Cómo ejecutarlo?
python3 main.py (en linux)
py main.py (en Windows)

## ¿Qué puede hacer cada rol?

### ADMIN
1. Listar productos del catálogo
2. Crear un producto nuevo
3. Actualizar un producto existente
4. Eliminar un producto
5. Guardar el catálogo en catalogo.txt

### CLIENTE
1. Ver el catálogo completo
2. Buscar productos por nombre o categoría
3. Agregar productos al carrito
4. Ver el carrito y el total
5. Confirmar la compra (se guarda en ordenes.txt)
6. Vaciar el carrito

## Archivos que genera el programa

- ordenes.txt: se crea automáticamente cuando el cliente confirma una compra
- catalogo.txt: se crea cuando el admin guarda el catálogo

## Estructura

ecommerce-cli-m4/
├── main.py          # desde acá se ejecuta todo
├── tienda.py        # coordina los menús y los roles
├── producto.py      # clase Producto
├── catalogo.py      # clase Catalogo
├── carrito.py       # clase Carrito
├── usuario.py       # clase base Usuario
├── admin.py         # Admin hereda de Usuario
├── cliente.py       # Cliente hereda de Usuario
└── excepciones.py   # mis excepciones personalizadas
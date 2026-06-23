# INVENTARIO DINÁMICO

# TODO 1: Crea una variable 'inventario' que sea una lista vacía.
inventario = []

# TODO 2: Imprime un encabezado.
print("=== Inventario Dinámico ===")

# TODO 3: Agrega tres productos.
inventario.append("Laptop")
inventario.append("Mouse")
inventario.append("Teclado")

print("Inventario actual:", inventario)

# TODO 4: Agrega "Monitor" al inicio de la lista.
inventario.insert(0, "Monitor")

print("Después de insertar Monitor:", inventario)

# TODO 5: Elimina el último elemento.
ultimo = inventario.pop()

print("Se eliminó:", ultimo)
print("Inventario después de pop:", inventario)

# TODO 6: Elimina "Mouse" por nombre.
inventario.remove("Mouse")

print("Inventario después de remove:", inventario)

# TODO 7: Muestra el total de productos restantes.
print("Total de productos:", len(inventario))

# TODO 8: Recorre la lista e imprime cada producto.
for producto in inventario:
    print("- " + producto)
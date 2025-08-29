"""
DICCIONARIOS
Nota: Tené en cuenta que para que cada FUNCIÓN funcione deberá estar indentada correctamente.
De lo contrario no funcionará. Para completar, por favor, quitá la palabra reservada 'pass'.
Nota 2: Conserva los parámetros.
"""

def Crear_diccionario_de_productos():
    #En esta función, deberás crear un diccionario vacío y retornarlo.
    #Nota: Investiga sobre la estructura de un diccionario en este lenguaje.
    pass

def Agregar_producto_al_inventario(inventario: dict, nombre_producto, cantidad):
    #En esta función, se te da un diccionario de inventario.
    #Debes agregar un nuevo producto con su nombre y cantidad como clave y valor.
    #Retorna el diccionario actualizado.
    pass

def Obtener_cantidad_de_producto(inventario: dict, nombre_producto):
    #Dada un diccionario de inventario, retorna la cantidad de un producto específico.
    # Si el producto no existe, retorna 0.
    pass

def Actualizar_stock_de_producto(inventario: dict, nombre_producto, nueva_cantidad):
    #En esta función, actualiza la cantidad de un producto ya existente en el inventario.
    #Retorna el diccionario actualizado.
    #Si el producto no está, simplemente no hagas nada.
    pass

def Eliminar_producto_del_inventario(inventario: dict, nombre_producto):
    #Dada un diccionario de inventario, elimina el producto especificado.
    #Retorna el diccionario modificado.
    #Nota: Investiga sobre la función pop() o la palabra clave del.
    pass

def Contar_productos_en_inventario(inventario: dict):
    #En esta función, retorna la cantidad total de productos (elementos) que hay en el diccionario.
    pass

def Listar_todos_los_productos(inventario: dict):
    #Retorna una lista con todas las claves (nombres de productos) del diccionario.
    #Nota: Investiga el método keys().
    pass

def Obtener_valores_del_inventario(inventario: dict):
    #Retorna una lista con todos los valores (cantidades) del diccionario.
    #Nota: Investiga el método values().
    pass

def Obtener_items_del_inventario(inventario: dict):
    #Retorna una lista de tuplas donde cada tupla contiene un par de clave-valor del diccionario.
    #Por ejemplo: [('manzanas', 10), ('peras', 5)].
    #Nota: Investiga el método items().
    pass

def Unir_dos_inventarios(inventario1: dict, inventario2: dict):
    #En esta función, une dos diccionarios en uno solo. Si hay claves duplicadas,
    #el valor del segundo diccionario debe sobrescribir al del primero.
    #Retorna el nuevo diccionario combinado.
    #Nota: Investiga sobre el método update().
    pass

def Limpiar_inventario(inventario: dict):
    # En esta función, vacía todo el contenido del diccionario y retorna el diccionario vacío.
    # Nota: Investiga sobre el método clear().
    pass

def Verificar_existencia_de_producto(inventario: dict, nombre_producto):
    #En esta función, verifica si un producto existe en el inventario.
    #Retorna True si el producto está, y False en caso contrario.
    #Puedes usar la palabra clave 'in'.
    pass
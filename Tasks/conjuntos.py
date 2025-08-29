"""
CONJUNTOS (SETS)
Nota: Tené en cuenta que para que cada FUNCIÓN funcione deberá estar indentada correctamente.
De lo contrario no funcionará. Para completar, por favor, quitá la palabra reservada 'pass'.
Nota 2: Conserva los parámetros.
"""

def Crear_conjunto_vacio():
    # En esta función, deberás crear un conjunto vacío y retornarlo.
    # Nota: Investigá cómo crear un set vacío en Python (set()).
    pass

def Agregar_elemento(al_conjunto: set, elemento):
    # Agregá un elemento al conjunto recibido y retornalo actualizado.
    # Nota: Investigá el método add().
    pass

def Eliminar_elemento(al_conjunto: set, elemento):
    # Eliminá un elemento del conjunto y retornalo actualizado.
    # Si el elemento no existe, no debe producirse error.
    # Nota: Investigá discard() (no lanza error) y remove() (lanza error si no existe).
    pass

def Verificar_existencia(al_conjunto: set, elemento):
    # Retorná True si el elemento está en el conjunto, False en caso contrario.
    # Podés usar la palabra clave 'in'.
    pass

def Union_de_conjuntos(conjunto1: set, conjunto2: set):
    # Retorná un nuevo conjunto que sea la unión de conjunto1 y conjunto2.
    # Nota: Investigá union() u operador |.
    pass

def Interseccion_de_conjuntos(conjunto1: set, conjunto2: set):
    # Retorná un nuevo conjunto con los elementos en común entre conjunto1 y conjunto2.
    # Nota: Investigá intersection() u operador &.
    pass

def Diferencia_de_conjuntos(conjunto1: set, conjunto2: set):
    # Retorná un nuevo conjunto con los elementos que están en conjunto1 pero no en conjunto2.
    # Nota: Investigá difference() u operador -.
    pass

def Diferencia_simetrica_de_conjuntos(conjunto1: set, conjunto2: set):
    # Retorná un nuevo conjunto con los elementos que están en uno u otro, pero no en ambos.
    # Nota: Investigá symmetric_difference() u operador ^.
    pass

def Contar_elementos(al_conjunto: set):
    # Retorná la cantidad de elementos del conjunto.
    # Nota: Usá len().
    pass

def Limpiar_conjunto(al_conjunto: set):
    # Vacía todo el contenido del conjunto y retornalo vacío.
    # Nota: Investigá clear().
    pass

def Convertir_lista_a_conjunto(lista):
    # Convertí una lista (con posibles duplicados) a un conjunto (sin duplicados) y retornalo.
    # Nota: Usá set(lista).
    pass

def Es_subconjunto(conjunto_hijo: set, conjunto_padre: set):
    # Retorná True si conjunto_hijo es subconjunto de conjunto_padre, False en caso contrario.
    # Nota: Investigá issubset() u operador <=.
    pass

def Es_superconjunto(conjunto_padre: set, conjunto_hijo: set):
    # Retorná True si conjunto_padre es superconjunto de conjunto_hijo, False en caso contrario.
    # Nota: Investigá issuperset() u operador >=.
    pass

def Clonar_conjunto(al_conjunto: set):
    # Retorná una copia superficial (shallow copy) del conjunto.
    # Nota: Investigá copy().
    pass

def Actualizar_conjunto_con_otro(destino: set, fuente: set):
    # Modificá 'destino' agregando los elementos de 'fuente'. Retorná el conjunto actualizado.
    # Nota: Investigá update() u operador |=.
    pass

def Quitar_y_retornar_un_elemento(al_conjunto: set):
    # Quitá y retorná un elemento arbitrario del conjunto.
    # Si está vacío, no debe romper (podés retornar None).
    # Nota: Investigá pop() en sets (no acepta índice).
    pass
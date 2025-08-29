import pytest
from Tasks.listas import (
    Agregar_al_carrito, 
    Agregar_otro_producto_al_carrito, 
    Contar_productos_adentro_del_carrito, 
    Quitar_productos_al_carrito, 
    Numero_esta_en_la_lista, 
    Seleccionar_un_elemento_adentro_del_carrito,
    Unir_dos_listas_de_compras,
    Insertar_producto_en_orden_especifico_de_la_lista,
    Sumar_elememntos_de_una_lista,
    Cantidad_de_elementos,
    Contar_veces_repetidas_de_elemeno,
    Obtener_maximo_valor,
    Obtener_minimo_valor,
    Obtener_indice_de_elemento,
    Quitar_ultimo_elemento,
    Vaciar_lista,
    Ordenar_en_incremento,
    Ordenar_en_disminucion,
    Reversa_de_lista
    )

def test_Agregar_al_carrito_tipoDato():
    assert isinstance(Agregar_al_carrito([], "Agua"), list), "Debe retornar una lista."
    
def test_Agregar_al_carrito_correcto():
    productos = []
    producto = "Agua"
    resultado_esperado = ["Agua"]
    
    lista_final = Agregar_al_carrito(productos, producto)
    assert lista_final == resultado_esperado
    
def test_Agregar_otro_producto_al_carrito_de_compras_tipoDato():
    assert isinstance(Agregar_otro_producto_al_carrito([], "Agua"), list), "Debe retornar una lista."
    
def test_Agregar_otro_producto_al_carrito_de_compras_correcto():
    productos = ["Agua"]
    producto = ["Lechuga"]
    resultado_esperado = ["Agua", "Lechuga"]
    
    lista_final = Agregar_otro_producto_al_carrito(productos, producto)
    assert lista_final == resultado_esperado
    
def test_Contar_productos_adentro_del_carrito_tipoDato():
    assert isinstance(Contar_productos_adentro_del_carrito(["Agua", "Lechuga"]), int), "Debe retornar un número entero."
    
def test_Contar_productos_adentro_del_carrito_correcto():
    assert Contar_productos_adentro_del_carrito(["Agua", "Lechuga"]) == 2
    assert Contar_productos_adentro_del_carrito([]) == 0
    
def test_Quitar_productos_al_carrito_tipoDato():
    assert isinstance(Quitar_productos_al_carrito(["Agua", "Lechuga"]), list), "Debe retornar una lista."
    
def test_Quitar_productos_al_carrito_correcto():
    productos = ["Agua", "Lechuga"]
    resultado_esperado = ["Agua"]
    
    productos_final = Quitar_productos_al_carrito(productos)
    assert productos_final == resultado_esperado
    
def test_Numero_esta_en_la_lista_tipoDato():
    assert isinstance(Numero_esta_en_la_lista([1,2,3,4,5], 5), bool), "Debe retornar un booleano."
    
def test_Numero_esta_en_la_lista_correcto():
    assert Numero_esta_en_la_lista([1,2,3,4], 4) == True
    assert Numero_esta_en_la_lista([1,2,3,4], 5) == False
    
def test_Seleccionar_un_elemento_adentro_del_carrito_correcto():
    assert Seleccionar_un_elemento_adentro_del_carrito(["Agua", "Leche", "Queso", "Manzana"], "Manzana") == "Manzana"
    assert Seleccionar_un_elemento_adentro_del_carrito(["Agua", "Leche", "Queso", "Manzana"], "Durazno") == None
    
def test_unir_dos_listas_de_compras():
    lista_completa = Unir_dos_listas_de_compras(["zanahoria", "papa", "cebolla"], ["pollo", "carne molida"])
    assert lista_completa == ["zanahoria", "papa", "cebolla", "pollo", "carne molida"]
    
def test_insertar_producto_en_orden_especifico_de_la_lista(): 
    nueva_lista = Insertar_producto_en_orden_especifico_de_la_lista(["leche", "pan", "queso", "jamon"], "mantequilla")
    assert nueva_lista == ["leche", "pan", "mantequilla", "queso", "jamon"]
    assert nueva_lista == ["leche","mantequilla", "pan", "queso", "jamon"]
    assert nueva_lista == ["mantequilla","leche", "pan", "queso", "jamon"]
    assert nueva_lista == ["leche", "pan", "queso","mantequilla", "jamon"]
    assert nueva_lista == ["leche", "pan", "queso", "jamon","mantequilla"]
    
def test_sumar_elementos_de_una_lista():
    assert Sumar_elememntos_de_una_lista([1, 2, 3, 4, 5]) == 15
    assert Sumar_elememntos_de_una_lista([10, -5, 0]) == 5
    assert Sumar_elememntos_de_una_lista([]) == 0

def test_cantidad_de_elementos():
    assert Cantidad_de_elementos(["manzana", "banana", "cereza"]) == 3
    assert Cantidad_de_elementos([]) == 0

def test_contar_veces_repetidas_de_elemeno():
    assert Contar_veces_repetidas_de_elemeno([1, 2, 3, 2, 4, 2], 2) == 3
    assert Contar_veces_repetidas_de_elemeno(["a", "b", "a"], "a") == 2
    assert Contar_veces_repetidas_de_elemeno([1, 2, 3], 5) == 0

def test_obtener_maximo_valor():
    assert Obtener_maximo_valor([1, 5, 2, 9, 3]) == 9
    assert Obtener_maximo_valor([-10, -5, -1]) == -1
    with pytest.raises(ValueError):
        Obtener_maximo_valor([])

def test_obtener_minimo_valor():
    assert Obtener_minimo_valor([1, 5, 2, 9, 3]) == 1
    assert Obtener_minimo_valor([-10, -5, -1]) == -10
    with pytest.raises(ValueError):
        Obtener_minimo_valor([])

def test_obtener_indice_de_elemento():
    assert Obtener_indice_de_elemento(["a", "b", "c"], "b") == 1
    assert Obtener_indice_de_elemento([10, 20, 30, 40], 40) == 3
    with pytest.raises(ValueError):
        Obtener_indice_de_elemento([1, 2, 3], 99)
        
def test_quitar_ultimo_elemento():
    assert Quitar_ultimo_elemento(["leche", "pan", "queso"]) == ["leche", "pan"]
    

def test_vaciar_lista(): 
    assert Vaciar_lista(["leche", "pan", "queso"]) == []
    
def test_ordenar_en_incremento():
    assert Ordenar_en_incremento([5, 1, 4, 2]) == [1, 2, 4, 5]
    assert Ordenar_en_incremento(["c", "a", "b"]) == ["a", "b", "c"]

def test_ordenar_en_disminucion():
    assert Ordenar_en_disminucion([5, 1, 4, 2]) == [5, 4, 2, 1]
    assert Ordenar_en_disminucion(["c", "a", "b"]) == ["c", "b", "a"]

def test_reversa_de_lista():
    assert Reversa_de_lista([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert Reversa_de_lista(["a", "b", "c"]) == ["c", "b", "a"]
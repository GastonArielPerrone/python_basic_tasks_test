import pytest
from Tasks.listas import (
    Agregar_al_carrito, 
    Agregar_otro_producto_al_carrito, 
    Contar_productos_adentro_del_carrito, 
    Quitar_productos_al_carrito, 
    Numero_esta_en_la_lista, 
    Seleccionar_un_elemento_adentro_del_carrito
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
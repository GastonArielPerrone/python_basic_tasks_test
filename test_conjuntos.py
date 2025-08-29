import pytest
from Tasks.conjuntos import (
    Crear_conjunto_vacio,
    Agregar_elemento,
    Eliminar_elemento,
    Verificar_existencia,
    Union_de_conjuntos,
    Interseccion_de_conjuntos,
    Diferencia_de_conjuntos,
    Diferencia_simetrica_de_conjuntos,
    Contar_elementos,
    Limpiar_conjunto,
    Convertir_lista_a_conjunto,
    Es_subconjunto,
    Es_superconjunto,
    Clonar_conjunto,
    Actualizar_conjunto_con_otro,
    Quitar_y_retornar_un_elemento,
)

def test_crear_conjunto_vacio():
    conjunto = Crear_conjunto_vacio()
    assert isinstance(conjunto, set)
    assert len(conjunto) == 0

def test_agregar_elemento():
    conjunto = Agregar_elemento(set(), "manzana")
    assert "manzana" in conjunto # type: ignore

def test_eliminar_elemento_existente():
    conjunto = Eliminar_elemento({"manzana", "pera"}, "manzana")
    assert "manzana" not in conjunto # type: ignore

def test_eliminar_elemento_inexistente(): 
    assert Eliminar_elemento({"pera"}, "banana") == {"pera"}

def test_verificar_existencia():
    assert Verificar_existencia({"manzana", "pera"}, "manzana") is True
    assert Verificar_existencia({"manzana", "pera"}, "banana") is False

def test_union_de_conjuntos():
    assert Union_de_conjuntos({"a", "b"}, {"b", "c"}) == {"a", "b", "c"}
    

def test_interseccion_de_conjuntos():
    assert Interseccion_de_conjuntos({"a", "b"}, {"b", "c"}) == {"b"}
     

def test_diferencia_de_conjuntos():
    assert Diferencia_de_conjuntos({"a", "b"}, {"b", "c"}) == {"a"}
     

def test_diferencia_simetrica_de_conjuntos():
    assert Diferencia_simetrica_de_conjuntos({"a", "b"}, {"b", "c"}) == {"a", "c"} 

def test_contar_elementos(): 
    assert Contar_elementos({"a", "b", "c"}) == 3

def test_limpiar_conjunto():
    assert Limpiar_conjunto({"a", "b"}) == {}
    

def test_convertir_lista_a_conjunto():
    assert Convertir_lista_a_conjunto(["a", "a", "b", "c"]) == {"a", "b", "c"}
     

def test_es_subconjunto():
    assert Es_subconjunto({"a", "b"}, {"a", "b", "c"}) is True
    assert Es_subconjunto({"a", "d"}, {"a", "b", "c"}) is False

def test_es_superconjunto():
    assert Es_superconjunto({"a", "b", "c"}, {"a", "b"}) is True
    assert Es_superconjunto({"a", "b"}, {"a", "c"}) is False

def test_clonar_conjunto():
    conjunto = {"a", "b"}
    clon = Clonar_conjunto(conjunto)
    assert clon == conjunto
    assert clon is not conjunto  

def test_actualizar_conjunto_con_otro():
    destino = {"a"}
    fuente = {"b", "c"}
    resultado = Actualizar_conjunto_con_otro(destino, fuente)
    assert resultado == {"a", "b", "c"}

def test_quitar_y_retornar_un_elemento():
    conjunto = {"a", "b"}
    elemento = Quitar_y_retornar_un_elemento(conjunto)
    assert elemento in {"a", "b"}
    assert elemento not in conjunto
   
    assert Quitar_y_retornar_un_elemento(set()) is None

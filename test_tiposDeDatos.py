"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from traitlets import Int, Set
from Tasks.tiposDeDatos import mi_conjunto_de_numeros, mi_nombre, mi_edad, mayorDeEdadONo, mi_pesaje, mi_lista, mi_diccionario, mi_tupla

def test_nombre_tipoDeDato():
    assert isinstance(mi_nombre("Gastón"), str), "Debe devolverse un string."

def test_edad_tipoDeDato():
    assert isinstance(mi_edad(33), int), "Debe devolverse un número entero."

def test_edad_positivo():
    assert mi_edad(33) > 0, "Debe devolverse un número entero positivo." # type: ignore
    
def test_mayorDeEdadONo():
    assert isinstance(mayorDeEdadONo(33), bool), "Debe retornar un valor booleano."
    
def test_pesaje_tipoDeDato():
    assert isinstance(mi_pesaje(87.45), float), "Debe retornar un número decimal."
    
def test_pesaje_positivo():
    assert mi_pesaje(74.34) > 0, "Debe ser un número positivo." # type: ignore
    
def test_lista_correcta():
    assert isinstance(mi_lista(["colchón", 2, True, 25.5]), list), "Deberá retornar una lista."

def test_diccionario_correcto():
    assert isinstance(mi_diccionario({"nombre":"Gastón", "apellido":"Perrone", "colorFavorito":"Celeste", "edad":33}), dict), "Debe retornar dato de tipo diccionario."
    
def test_tupla_correcta():
    assert isinstance(mi_tupla("Gastón", 33, "Masculino",True), tuple), "Deberá retornar una tupla." # type: ignore
    
def test_mi_conjunto_de_numeros_contenido():
    """
    Verifica que la función devuelva el conjunto de números esperado.
    """
    expected_set = {1, 5, 9, 13, 17}
    result = mi_conjunto_de_numeros() # type: ignore
    assert result == expected_set, f"Se esperaba {expected_set}, pero se obtuvo {result}"

def test_mi_conjunto_de_numeros_tipo():
    result = mi_conjunto_de_numeros() # type: ignore
    assert isinstance(result, set), "La función debe devolver un conjunto (set)."

def test_mi_conjunto_de_numeros_elementos_son_enteros():
    result = mi_conjunto_de_numeros() # type: ignore
    assert all(isinstance(x, int) for x in result), "Todos los elementos del conjunto deben ser enteros."
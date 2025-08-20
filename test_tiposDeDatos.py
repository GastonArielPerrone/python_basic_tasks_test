"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from traitlets import Int, Set
from Tasks.tiposDeDatos import mi_conjunto_de_numeros, mi_nombre, mi_edad, mayorDeEdadONo, mi_pesaje, mi_lista, mi_diccionario, mi_tupla, mi_conjunto_de_numeros

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
    
def test_conjunto_tipoDeDatos():
    # Creamos un conjunto de prueba para pasarlo a la función
    conjunto_de_prueba = {1, 2, 3, 4, 5, 6, 7}
    
    # Ahora la función acepta un conjunto de enteros sin problemas
    resultado = mi_conjunto_de_numeros(conjunto_de_prueba) #type:ignore
    
    assert isinstance(resultado, set), "El valor devuelto debe ser de tipo 'set'."
    
    # También podemos verificar que los elementos del conjunto sean enteros.
    for elemento in resultado: #type:ignore
        assert isinstance(elemento, int), "Todos los elementos del conjunto deben ser de tipo 'int'."
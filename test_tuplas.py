import pytest
from Tasks.tuplas import (
    Contar_repetidos,
    Obtener_indice_de_elemento,
    Obtener_tamanio_de_tupla,
    Suma_de_elementos,
    Obtener_mínimo_valor,
    Obtener_maximo_valor,
    Verificar_elemento
)

def test_Contar_repetidos():
    assert Contar_repetidos((1, 2, 2, 3, 4, 2, 5)) == 3

def test_Obtener_indice_de_elemento():
    assert Obtener_indice_de_elemento(('a', 'b', 'c', 'd'), 'c') == 2

def test_Obtener_tamanio_de_tupla():
    assert Obtener_tamanio_de_tupla((10, 20, 30, 40, 50)) == 5

def test_Suma_de_elementos(): 
    assert Suma_de_elementos((1, 2, 3, 4, 5)) == 15

def test_Obtener_mínimo_valor(): 
    assert Obtener_mínimo_valor((100, 20, 50, 5, 80)) == 5

def test_Obtener_maximo_valor():
    assert Obtener_maximo_valor((10, 50, 30, 90, 25)) == 90

def test_Verificar_elemento_presente(): 
    assert Verificar_elemento(('rojo', 'verde', 'azul'), 'verde') is True

def test_Verificar_elemento_ausente():
    assert Verificar_elemento(('rojo', 'verde', 'azul'), 'amarillo') is False
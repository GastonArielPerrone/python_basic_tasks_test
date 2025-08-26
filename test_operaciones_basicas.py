"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.operaciones_basicas import suma, resta, division, multiplicacion, Raiz_cuadrada, Raiz_n_de_base_n

def test_suma():
    assert suma(3, 2) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 5) == -5
    assert resta(-2, -2) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(-9, 3) == -3
    with pytest.raises(ValueError):
        division(5, 0)

def test_multiplicacion():
    assert multiplicacion(4, 5) == 20
    assert multiplicacion(-3, 3) == -9
    assert multiplicacion(0, 100) == 0
    
def test_Raiz_cuadrada():
    assert Raiz_cuadrada(25) == 5.00
    with pytest.raises(ValueError):
        Raiz_cuadrada(-25)

def test_Raiz_n_de_base_n():
    assert Raiz_n_de_base_n(16,2) == 4.00
    assert Raiz_n_de_base_n(81, 4) == 3.00
    assert Raiz_n_de_base_n(1,1) == 1.00
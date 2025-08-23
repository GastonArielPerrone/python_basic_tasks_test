"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.modularidad_potencia import modularidad, potencia

def test_modularidad():
    assert modularidad(5, 2) == 1
    assert modularidad(5, 3) == 2
    assert modularidad(-9, 3) == 0

def test_potenciacion():
    assert potencia(1, 0) == 1
    assert potencia(1, 1) == 1
    assert potencia(2, 2) == 4
    assert potencia(2, 3) == 8
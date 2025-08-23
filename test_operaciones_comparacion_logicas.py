"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.operaciones_comparacion_logicas import Numero_mayor, Numero_menor

def test_Numero_mayor_correcto():
    assert Numero_mayor(4,5) == 5
    
def test_Numero_menor_correcto():
    assert Numero_menor(2,1,4) == 1
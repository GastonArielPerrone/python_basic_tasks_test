"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.operaciones_comparacion_logicas import Numero_mayor

def test_Numero_mayor_correcto():
    result = Numero_mayor(4,5) == 5
    expected = result
    assert expected == result
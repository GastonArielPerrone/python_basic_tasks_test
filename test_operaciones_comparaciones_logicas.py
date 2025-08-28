"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.operaciones_comparaciones_logicas import Numero_mayor, Numero_menor, Validador_de_password, Recuperacion_de_password

def test_Numero_mayor_correcto():
    assert Numero_mayor(4,5) == 5
    
def test_Numero_menor_correcto():
    assert Numero_menor(2,1,4) == 1
    
def test_Validador_de_password_tipoDato():
    assert isinstance(Validador_de_password("G@p18121991", "G@p18121991"), bool), "Debe retornar un booleano."
    
def test_Validador_de_password_correcto():
    assert Validador_de_password("123456789@", "123456789@") == True
    assert Validador_de_password("123456789@", "@123456789") == False
    
def test_Recuperacion_de_password_tipoDato():
    assert isinstance(Recuperacion_de_password("123456789@", "123456789@", "123456789@"), bool), "Debe retorna un booleano."
    
def test_Recuperacion_de_password_correcto():
    assert Recuperacion_de_password("123456789@", "121314151@", "121314151@") == True
    assert Recuperacion_de_password("123456789@", "121314151@", "133314151@") == False
    assert Recuperacion_de_password("123456789@", "123456789@", "123456789@") == False
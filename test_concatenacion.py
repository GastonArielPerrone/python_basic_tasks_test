"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.concatenacion import mi_perfil, patentar

def test_mi_perfil():
    assert isinstance(mi_perfil("Gastón", "Perrone", 33, "Software Develpment"), str), "La función debe devolver una cadena de str."
    
def test_mi_perfil_formato_correcto():
    resultado = mi_perfil("Gastón", "Perrone", 33, "Software Development")
    esperado = "Gastón Perrone 33 Software Development"
    assert resultado == esperado
    
def test_tipoDato_patentar():
    assert isinstance(patentar("AB", 243, "CD"), str), "Debe retornar un String."
    
def test_patente_formato_correcto():
    resultado = patentar("AB", 243, "CD")
    esperado = "AB243CD"
    assert resultado == esperado

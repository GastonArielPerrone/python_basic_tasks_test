"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.conversion_de_palabras import Convertir_todas_las_letras_a_mayusculas, Convertir_primer_caracter_a_Mayuscula, Reemplazar_caracter_de_la_palabra

def test_Convertir_todas_las_letras_a_mayuscula_tipoDato():
    assert isinstance(Convertir_todas_las_letras_a_mayusculas("gastón"), str), "Debe retornar un str."
    
def test_Convertir_todas_las_letras_a_mayuscula_correcto():
    assert Convertir_todas_las_letras_a_mayusculas("gastón") == "GASTÓN"

def test_Convertir_primer_caracter_a_Mayuscula_TipoDato():
    assert isinstance(Convertir_primer_caracter_a_Mayuscula("gastón"), str), "Debe retornar un str."
    
def test_Convertir_primer_caracter_a_Mayuscula_correcto():
    assert Convertir_primer_caracter_a_Mayuscula("gastón") == "Gastón"
    
def test_Reemplazar_caracter_de_la_palabra_tipoDato():
    assert isinstance(Reemplazar_caracter_de_la_palabra("gato","a"), str), "Debe retornar un str."

def test_Reemplazar_caracter_de_la_palabra_correcto():
    assert Reemplazar_caracter_de_la_palabra("gato","o") == "gatO"
    assert Reemplazar_caracter_de_la_palabra("Gastón","e") == "No se encontró dicho caracter."
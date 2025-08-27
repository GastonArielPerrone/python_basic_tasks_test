"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
from unittest import result
import pytest
from Tasks.problemas_matematicos_geometria import Perimetro_de_cuadrado, Area_de_cuadrado, Perimetro_de_rectangulo, Area_de_rectangulo, Perimetro_de_circunferencia, Area_de_circunferencia, Perimetro_de_triangulo, Area_de_triangulo, Perimetro_de_triangulo, Perimetro_de_rombo, Area_de_rombo, Perimetro_de_romboide, Area_de_romboide

def test_perimetro_de_cuadrado_tipoDato():
    assert  isinstance(Perimetro_de_cuadrado(40.3), float), "Debe retornar un valor tipo float."
    
def test_perimetro_de_cuadrado_correcto():
    assert Perimetro_de_cuadrado(4.00) == 16.00
    assert Perimetro_de_cuadrado(25.10) == 100.40
        
def test_area_de_cuadrado_tipoDato():
    assert isinstance(Area_de_cuadrado(4.00, 2.00), float), "Debe retornar un valor tipo float."
    
def test_area_de_cuadrado_correct():
    assert Area_de_cuadrado(4.00, 4.00) == 16.00
    assert Area_de_cuadrado(2.25, 1.15) == 2.5875
    
def test_perimetro_de_rectangulo_tipoDato():
    assert isinstance(Perimetro_de_rectangulo(25.5, 15.00), float), "Debe retornar un valor tipo float."
    
def test_perimetro_de_rectangulo_correcto():
    assert Perimetro_de_rectangulo(4.25, 8.15) == 24.8
    
def test_area_rectangulo_tipoDato():
    assert isinstance(Area_de_rectangulo(25.50, 15.55), float), "Debe retornar un valor tipo float."

def test_area_rectangulo_correcto():
    assert Area_de_rectangulo(4.25, 8.15) == 34.6375
    
def test_perimetro_circunferencia_tipoDato():
    assert isinstance(Perimetro_de_circunferencia(15.35), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("diametro, resultado_esperado", [
(10, 31.42),   
])

def test_perimetro_circunferencia_valores_correctos(diametro, resultado_esperado):
    assert Perimetro_de_circunferencia(diametro) == resultado_esperado
    
def test_area_circunferencia_tipoDato():
    assert isinstance(Area_de_circunferencia(15.35), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("radio, resultado_esperado", [
(5, 86.35),   
])

def test_area_circunferencia_correcto(diametro, resultado_esperado):
    assert Perimetro_de_circunferencia(diametro) == resultado_esperado
    
def test_perimetro_de_triangulo_tipoDato():
    assert isinstance(Perimetro_de_triangulo(2.10, 4.15, 5.64), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("lado1, lado2, lado3, resultado_esperado", [
    (4.10, 5.15, 2.35, 11.60)
])

def test_perimetro_de_triangulo_correcto(lado1, lado2, lado3, resultado_esperado):
    assert Perimetro_de_triangulo(lado1, lado2, lado3) == resultado_esperado
    
def test_area_de_triangulo_tipoDato():
    assert isinstance(Area_de_triangulo(2.14, 5.65), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("base3, altura3, resultado_esperado", [
    (34.25, 5.75, 196.94)
])

def test_area_de_triangulo_correcto(base3, altura3, resultado_esperado):
    assert Area_de_triangulo(base3, altura3) == resultado_esperado
    
def test_perimetro_de_rombo_tipoDato():
    assert  isinstance(Perimetro_de_rombo(40.3), float), "Debe retornar un valor tipo float."

def test_perimetro_de_rombo_correcto():
    assert Perimetro_de_rombo(4.00) == 16.00
    assert Perimetro_de_rombo(25.10) == 100.40
    
def test_area_de_rombo_tipoDato():
    assert isinstance(Area_de_rombo(24.55, 30.65), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("diagonal, Diagonal, resultado_esperado",[
    (24.35, 25.33, 616.78)
])
    
def test_area_de_rombo_correcto(diagonal, Diagonal, resultado_esperado):
    assert Area_de_rombo(diagonal, Diagonal) == resultado_esperado
    
def test_perimetro_romboide_tipoDato():
    assert isinstance(Perimetro_de_romboide(15.15, 20.15), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("lado_May, lado_men, resultado_esperado",[
    (15.00, 20.00, 70.00)
])

def test_perimetro_romboide_correcto(lado_May, lado_men, resultado_esperado):
    assert Perimetro_de_romboide(lado_May, lado_men) == resultado_esperado
    
def test_area_de_romboide_tipoDato():
    assert isinstance(Area_de_romboide(4.25, 5.75), float), "Debe retornar un valor tipo float."
    
@pytest.mark.parametrize("base4, altura4, resultado_esperado",[
    (4.25, 7.15, 30.39)
])

def test_area_de_romboide_correcto(base4, altura4, resultado_esperado):
    assert Area_de_romboide(base4, altura4) == resultado_esperado
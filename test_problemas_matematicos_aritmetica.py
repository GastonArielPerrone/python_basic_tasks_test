"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.problemas_matematicos_aritmetica import promedioDeNotas, promocionoONo, sobrante_de_manzanas, minutos_a_horas_minutos_segundos, peso_a_dolar


def test_promedioDeNotas_calculo_correcto():
    assert promedioDeNotas(7.0, 8.0, 9.0) == 8.0
    assert promedioDeNotas(6.0, 6.0, 6.0) == 6.0
    assert promedioDeNotas(10.0, 10.0, 10.0) == 10.0

def test_promocionoONo_caso_promociona_exito():
    assert promocionoONo(8.5, 8.0, 9.0, 7.5) is True
    assert promocionoONo(7.0, 7.0, 7.0, 7.0) is True

def test_promocionoONo_caso_no_promociona_por_promedio():
    assert promocionoONo(6.99, 8.0, 9.0, 8.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_1():
    assert promocionoONo(8.0, 6.5, 8.0, 9.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_2():
    assert promocionoONo(8.0, 8.0, 6.5, 9.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_3():
    assert promocionoONo(8.0, 8.0, 9.0, 6.5) is False
    
def test_sobrante_de_manzanas_tipoDatoRetorno():
    assert sobrante_de_manzanas(16, 4) == 0, "Los sobrantes deben ser números enteros o cero (nada)."
    
def test_minutos_a_horas_minutos_segundos_tipoDato():
    result = minutos_a_horas_minutos_segundos(60)
    assert isinstance(result, str), "Se esperaba un tipo de dato string."
    
def test_minutos_a_horas_minutos_segundos_correcto():
    result = minutos_a_horas_minutos_segundos(60)
    expected = "01:00:00"
    assert result == expected, "No se logró el resultado esperado."
    
def test_peso_a_dolar_tipoDato():
    assert isinstance(peso_a_dolar(4.00), float), "Debe retornar un resultado decimal."
    
def test_peso_a_dolar_correcto():
    result = peso_a_dolar(4)
    expected = 0.00304
    assert result == expected, "No es lo que se esperaba."
    with pytest.raises(ValueError):
        peso_a_dolar(0)
    with pytest.raises(ValueError):
        peso_a_dolar(-4.5)
"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
from traitlets import Int
from Tasks.problemas_matematicos_aritmetica import promedioDeNotas, promocionoONo, sobrante_de_manzanas


def test_promedioDeNotas_calculo_correcto():
    """Verifica que el promedio de notas se calcule correctamente."""
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
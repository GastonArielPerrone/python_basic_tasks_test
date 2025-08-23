"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
from Tasks.problemas_matematicos_aritmetica import promedioDeNotas


def test_promedioDeNotas_calculo_correcto():
    """Verifica que el promedio de notas se calcule correctamente."""
    assert promedioDeNotas(7.0, 8.0, 9.0) == 8.0
    assert promedioDeNotas(6.0, 6.0, 6.0) == 6.0
    assert promedioDeNotas(10.0, 10.0, 10.0) == 10.0

def test_promocionoONo_si_promociona():
    assert promocionoONo(8.5, 8.0, 9.0, 7.5) is True # type: ignore
    assert promocionoONo(7.0, 7.0, 7.0, 7.0) is True # type: ignore

def test_promocionoONo_no_promociona_por_promedio():
    """Verifica el caso donde el promedio es menor a 7.00."""
    assert promocionoONo(6.99, 8.0, 9.0, 8.0) is False # type: ignore

def test_promocionoONo_no_promociona_por_nota_1():
    """Verifica el caso donde la primera nota es menor a 7.00."""
    assert promocionoONo(8.0, 6.5, 8.0, 9.0) is False # type: ignore

def test_promocionoONo_no_promociona_por_nota_2():
    """Verifica el caso donde la segunda nota es menor a 7.00."""
    assert promocionoONo(8.0, 8.0, 6.5, 9.0) is False # type: ignore

def test_promocionoONo_no_promociona_por_nota_3():
    """Verifica el caso donde la tercera nota es menor a 7.00."""
    assert promocionoONo(8.0, 8.0, 9.0, 6.5) is False # type: ignore
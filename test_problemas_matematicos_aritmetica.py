"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
from Tasks.problemas_matematicos_aritmetica import promedioDeNotas, promocionoONo


def test_promedioDeNotas_calculo_correcto():
    """Verifica que el promedio de notas se calcule correctamente."""
    assert promedioDeNotas(7.0, 8.0, 9.0) == 8.0
    assert promedioDeNotas(6.0, 6.0, 6.0) == 6.0
    assert promedioDeNotas(10.0, 10.0, 10.0) == 10.0

def test_promocionoONo_caso_promociona_exito():
    """Verifica el caso ideal donde el promedio y todas las notas son >= 7.00."""
    assert promocionoONo(8.5, 8.0, 9.0, 7.5) is True
    assert promocionoONo(7.0, 7.0, 7.0, 7.0) is True

def test_promocionoONo_caso_no_promociona_por_promedio():
    """Verifica que el alumno no promocione si el promedio es < 7.00, incluso con buenas notas."""
    assert promocionoONo(6.99, 8.0, 9.0, 8.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_1():
    """Verifica que el alumno no promocione si la primera nota es < 7.00."""
    assert promocionoONo(8.0, 6.5, 8.0, 9.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_2():
    """Verifica que el alumno no promocione si la segunda nota es < 7.00."""
    assert promocionoONo(8.0, 8.0, 6.5, 9.0) is False

def test_promocionoONo_caso_no_promociona_por_nota_3():
    """Verifica que el alumno no promocione si la tercera nota es < 7.00."""
    assert promocionoONo(8.0, 8.0, 9.0, 6.5) is False
"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
from Tasks.problemas_matematicos_aritmetica import promedioDeNotas


def test_promedioDeNotas_calculo_correcto():
    """Verifica que el promedio de notas se calcule correctamente."""
    assert promedioDeNotas(7.0, 8.0, 9.0) == 8.0
    assert promedioDeNotas(6.0, 6.0, 6.0) == 6.0
    assert promedioDeNotas(10.0, 10.0, 10.0) == 10.0

def test_promedio_alias_funcional():
    """Verifica que el alias 'promedio' funcione igual que promedioDeNotas."""
    assert promedio(7.0, 8.0, 9.0) == 8.0 # type: ignore

def test_promocionoONo_tipo_de_dato():
    """Verifica que la función promocionoONo retorne un booleano."""
    assert isinstance(promocionoONo(7.5, 8.0, 7.0, 9.0), bool) # type: ignore

def test_promocionoONo_caso_promociona():
    """Verifica el caso en que el promedio y todas las notas son >= 7.00."""
    assert promocionoONo(8.5, 8.0, 9.0, 8.5) is True # type: ignore

def test_promocionoONo_caso_no_promociona_por_promedio():
    """Verifica el caso donde el promedio es < 7.00."""
    assert promocionoONo(6.99, 8.0, 8.0, 8.0) is False # type: ignore

def test_promocionoONo_caso_no_promociona_por_nota():
    """Verifica el caso donde una de las notas es < 7.00."""
    assert promocionoONo(8.0, 7.0, 6.99, 9.0) is False # type: ignore
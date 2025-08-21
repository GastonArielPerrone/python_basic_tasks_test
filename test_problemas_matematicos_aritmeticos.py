"""
Por favor, no borrar ni modificar este código ya que tu test pasará depende de este.
"""
import pytest
from Tasks.problemas_matematicos_aritmetica import promedio, promocionoONo

def test_promedioDeNotas_tipoDeDato():
    assert isinstance(promedio(7.85, 9.00, 7.00), float), "Debe retornar un número decimal."
    
def test_promedioDeNotas():
    promedio = {7.00, 8.00, 9.00}
    assert isinstance(promedio, float), "Debe resultar un dato decimal."
    with pytest.raises(ValueError, match="Las notas deben ser valores positivos"):
        promedio = {0.00, -4.5, -7.00}
        
def test_promocionoONo_tipoDato():
    assert isinstance(promocionoONo(7.00, 7.00, 8.00, 9.00), bool), "Debe retornar un booleano (true o false)."
    
def test_promocionoONo_error():
    with pytest.raises(ValueError, match= "No pueden haber promedio y notas negativos ni 0."):
        promocionoONo(-3.89, -6.67, 0, -5.00)
import pytest
from Tasks.diccionarios import (
    Crear_diccionario_de_productos,
    Agregar_producto_al_inventario,
    Obtener_cantidad_de_producto,
    Actualizar_stock_de_producto,
    Eliminar_producto_del_inventario,
    Contar_productos_en_inventario,
    Listar_todos_los_productos,
    Obtener_valores_del_inventario,
    Obtener_items_del_inventario,
    Unir_dos_inventarios,
    Limpiar_inventario,
    Verificar_existencia_de_producto
)

def test_crear_diccionario_de_productos():
    inventario = Crear_diccionario_de_productos()
    assert isinstance(inventario, dict)
    assert inventario == {}

def test_agregar_producto_al_inventario():
    inventario = {}
    inventario = Agregar_producto_al_inventario(inventario, "manzanas", 10)
    assert inventario == {"manzanas": 10}

def test_obtener_cantidad_de_producto_existente():
    inventario = {"peras": 5}
    assert Obtener_cantidad_de_producto(inventario, "peras") == 5

def test_obtener_cantidad_de_producto_inexistente():
    inventario = {"peras": 5}
    assert Obtener_cantidad_de_producto(inventario, "manzanas") == 0

def test_actualizar_stock_de_producto_existente():
    inventario = {"peras": 5}
    inventario = Actualizar_stock_de_producto(inventario, "peras", 12)
    assert inventario["peras"] == 12 # type: ignore

def test_actualizar_stock_de_producto_inexistente():
    inventario = {"peras": 5}
    inventario = Actualizar_stock_de_producto(inventario, "manzanas", 8)
    assert inventario == {"peras": 5}  # no cambia nada

def test_eliminar_producto_del_inventario_existente():
    inventario = {"peras": 5, "manzanas": 10}
    inventario = Eliminar_producto_del_inventario(inventario, "peras")
    assert "peras" not in inventario # type: ignore
    assert inventario == {"manzanas": 10}

def test_eliminar_producto_del_inventario_inexistente():
    inventario = {"manzanas": 10}
    inventario = Eliminar_producto_del_inventario(inventario, "peras")
    assert inventario == {"manzanas": 10}  # sin cambios

def test_contar_productos_en_inventario():
    inventario = {"manzanas": 10, "peras": 5}
    assert Contar_productos_en_inventario(inventario) == 2

def test_listar_todos_los_productos():
    inventario = {"manzanas": 10, "peras": 5}
    productos = Listar_todos_los_productos(inventario)
    assert set(productos) == {"manzanas", "peras"} # type: ignore

def test_obtener_valores_del_inventario():
    inventario = {"manzanas": 10, "peras": 5}
    valores = Obtener_valores_del_inventario(inventario)
    assert set(valores) == {10, 5} # type: ignore

def test_obtener_items_del_inventario():
    inventario = {"manzanas": 10, "peras": 5}
    items = Obtener_items_del_inventario(inventario)
    assert ("manzanas", 10) in items # type: ignore
    assert ("peras", 5) in items # type: ignore

def test_unir_dos_inventarios():
    inv1 = {"manzanas": 10, "peras": 5}
    inv2 = {"peras": 8, "naranjas": 4}
    combinado = Unir_dos_inventarios(inv1, inv2)
    assert combinado == {"manzanas": 10, "peras": 8, "naranjas": 4}

def test_limpiar_inventario():
    inventario = {"manzanas": 10, "peras": 5}
    inventario = Limpiar_inventario(inventario)
    assert inventario == {}

def test_verificar_existencia_de_producto_true():
    inventario = {"manzanas": 10}
    assert Verificar_existencia_de_producto(inventario, "manzanas") is True

def test_verificar_existencia_de_producto_false():
    inventario = {"manzanas": 10}
    assert Verificar_existencia_de_producto(inventario, "peras") is False
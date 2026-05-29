from app.tareas import agregar_tarea, contar_tareas


def test_agregar_tarea_valida():
    mis_tareas = []
    resultado = agregar_tarea(mis_tareas, "Estudiar DevOps")
    assert resultado == "Tarea 'Estudiar DevOps' agregada"
    assert len(mis_tareas) == 1


def test_agregar_tarea_vacia():
    mis_tareas = []
    resultado = agregar_tarea(mis_tareas, "")
    assert resultado == "Tarea vacía"
    assert len(mis_tareas) == 0


def test_contar_tareas():
    lista_ejemplo = ["Lavar ropa", "Cocinar"]
    assert contar_tareas(lista_ejemplo) == 2
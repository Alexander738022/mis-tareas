def agregar_tarea(lista, nueva_tarea):
    if nueva_tarea == "":
        return "Tarea vacía"
    lista.append(nueva_tarea)
    return f"Tarea '{nueva_tarea}' agregada"


def contar_tareas(lista):
    return len(lista)
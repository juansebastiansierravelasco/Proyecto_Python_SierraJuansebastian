from validaciones import normalizar_texto
import json


def eliminar_materia(horario):

    nombre = input("Qué materia quieres eliminar: ")
    dia = input("Ingrese el día: ")
    hora = input("Ingrese la hora de inicio: ")
    encontrada = False

    for materia in horario:

        if (
            normalizar_texto(materia["materia"]) == normalizar_texto(nombre)
            and normalizar_texto(materia["dia"]) == normalizar_texto(dia)
            and normalizar_texto(materia["hora_inicio"])==normalizar_texto(hora)
        ):

            horario.remove(materia)
            with open("horario.json", "w", encoding="utf-8") as archivo:
                json.dump(horario,archivo,indent=4,ensure_ascii=False)

            print("Materia eliminada.")

            encontrada = True

            break

    if not encontrada:

        print(
            "No se encontró una materia con ese nombre y ese día."
        )
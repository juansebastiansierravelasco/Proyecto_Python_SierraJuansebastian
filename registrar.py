from validaciones import (
    pedir_hora,
    pedir_hora_final,
    normalizar_texto,
    pedir_dia,
    hay_conflicto_horario
)

import json


def registrar_materia(horario):

    nombre = input("Materia: ")

    dia = pedir_dia()

    hora_inicio = pedir_hora("Hora de inicio: ")

    hora_fin = pedir_hora_final(hora_inicio)

    ubicacion = input("Ubicación: ")

    conflicto = False

    for materia_existente in horario:

        if normalizar_texto(dia) == normalizar_texto(materia_existente["dia"]):

            if hay_conflicto_horario(
                hora_inicio,
                hora_fin,
                materia_existente
            ):

                conflicto = True

                print("Ya existe una materia que se cruza con ese horario.")

                print(
                    "Materia:",
                    materia_existente["materia"]
                )

                print(
                    "Horario:",
                    materia_existente["hora_inicio"],
                    "-",
                    materia_existente["hora_fin"]
                )

                break

    if conflicto:

        print("La materia no se puede registrar.")

    else:

        materia = {
            "materia": nombre,
            "dia": normalizar_texto(dia),
            "hora_inicio": hora_inicio,
            "hora_fin": hora_fin,
            "ubicacion": ubicacion
        }

        horario.append(materia)

        with open("horario.json", "w", encoding="utf-8") as archivo:
            json.dump(horario,archivo,indent=4,ensure_ascii=False)

        print("Materia registrada correctamente.")
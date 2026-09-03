from validaciones import (
    pedir_hora,
    pedir_hora_final,
    normalizar_texto,
    pedir_dia,
    hay_conflicto_horario
)

import json


def modificar_materia(horario):

    nombre = input("Ingrese la materia que quiere modificar: ")

    encontrada = False

    for materia in horario:

        if normalizar_texto(materia["materia"]) == normalizar_texto(nombre):

            encontrada = True

            nuevo_dia = pedir_dia()

            nueva_hora_inicio = pedir_hora(
                "Nueva hora de inicio: "
            )

            nueva_hora_fin = pedir_hora_final(
                nueva_hora_inicio
            )

            nueva_ubicacion = input("Nueva ubicación: ")

            conflicto = False

            for materia_existente in horario:

                # No comparar la materia consigo misma
                if materia_existente == materia:
                    continue

                if (
                    normalizar_texto(nuevo_dia)
                    == normalizar_texto(materia_existente["dia"])
                ):

                    if hay_conflicto_horario(
                        nueva_hora_inicio,
                        nueva_hora_fin,
                        materia_existente
                    ):

                        conflicto = True

                        print(
                            "No se puede modificar la materia."
                        )

                        print(
                            "El nuevo horario se cruza con:"
                        )

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
                break

            materia["dia"] = normalizar_texto(nuevo_dia)
            materia["hora_inicio"] = nueva_hora_inicio
            materia["hora_fin"] = nueva_hora_fin
            materia["ubicacion"] = nueva_ubicacion

            with open("horario.json", "w", encoding="utf-8") as archivo:
                json.dump(horario,archivo,indent=4,ensure_ascii=False)

            print("Materia modificada correctamente.")

            break

    if not encontrada:

        print("No se encontró una materia con ese nombre.")
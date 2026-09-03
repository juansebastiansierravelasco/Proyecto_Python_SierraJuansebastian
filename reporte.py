import json


def generar_reporte(horario):

    dias = [
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado"
    ]

    reporte = {}

    total_materias = 0

    for dia in dias:

        materias_dia = []

        for materia in horario:

            if materia["dia"] == dia:

                materias_dia.append(materia)

        reporte[dia] = materias_dia

        total_materias += len(materias_dia)

    with open("reporte.json", "w", encoding="utf-8") as archivo:
        json.dump(reporte,archivo,indent=4,ensure_ascii=False)

    return reporte, total_materias


def mostrar_reporte(reporte, total_materias):

    print("===================================================")
    print("          REPORTE DEL HORARIO SEMANAL")
    print("===================================================")

    for dia, materias in reporte.items():

        print()
        print(dia.capitalize() + ":")

        if len(materias) == 0:

            print("- Libre")

        else:

            for materia in materias:

                print(
                    "-",
                    materia["materia"],
                    "(" +
                    materia["hora_inicio"] +
                    " - " +
                    materia["hora_fin"] +
                    ")",
                    "en",
                    materia["ubicacion"]
                )

        print(
            "Total",
            dia + ":",
            len(materias),
            "materias"
        )

        print("------------------------------------------")

    print("Total de materias:", total_materias)
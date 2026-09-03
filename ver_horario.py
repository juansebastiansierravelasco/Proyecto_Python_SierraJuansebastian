def ver_horario(horario):
    dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
    encabezado_dias = " | ".join([d.capitalize().ljust(12) for d in dias])
    
    separador = "=" * 105
    print(separador)
    print(f"| {'Hora'.ljust(13)} | {encabezado_dias} |")
    print(separador)

    horas = []
    for materia in horario:
        hora = f"{materia['hora_inicio']} - {materia['hora_fin']}"
        if hora not in horas:
            horas.append(hora)

    horas.sort()

    if not horas:
        print("| No hay materias registradas en el horario.".ljust(104) + "|")
        print(separador)
        return

    for hora in horas:
        fila = []
        for dia in dias:
            materia_encontrada = "Libre"
            for materia in horario:
                horario_materia = f"{materia['hora_inicio']} - {materia['hora_fin']}"
                if materia["dia"] == dia and horario_materia == hora:
                    # Trunca el nombre si supera los 12 caracteres para mantener la tabla fija
                    materia_encontrada = materia["materia"][:12]
                    break
            fila.append(materia_encontrada.ljust(12))

        datos_fila = " | ".join(fila)
        print(f"| {hora.ljust(13)} | {datos_fila} |")
        print("-" * 105)
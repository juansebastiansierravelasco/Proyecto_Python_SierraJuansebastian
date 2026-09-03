def validar_hora(hora):
    try:
        partes = hora.split(":")

        if len(partes) != 2:
            return False

        horas = int(partes[0])
        minutos = int(partes[1])

        if horas < 0 or horas > 23:
            return False

        if minutos < 0 or minutos > 59:
            return False

        return True

    except ValueError:
        return False


def pedir_hora(mensaje):
    while True:
        hora = input(mensaje)

        if validar_hora(hora):
            return hora
        else:
            print("Hora inválida. Use el formato HH:MM.")
            print("Ejemplo: 8:00, 14:30, 18:45")


def validar_hora_final(hora_inicio, hora_fin):
    inicio = hora_inicio.split(":")
    fin = hora_fin.split(":")

    minutos_inicio = int(inicio[0]) * 60 + int(inicio[1])
    minutos_fin = int(fin[0]) * 60 + int(fin[1])

    return minutos_fin > minutos_inicio


def pedir_hora_final(hora_inicio):
    while True:
        hora_fin = input("Hora de fin: ")

        if not validar_hora(hora_fin):
            print("Hora inválida. Use el formato HH:MM.")
            print("Ejemplo: 10:00, 14:30, 18:45")

        elif not validar_hora_final(hora_inicio, hora_fin):
            print("La hora de fin debe ser posterior a la hora de inicio.")

        else:
            return hora_fin


def normalizar_texto(texto):
    texto = texto.lower()

    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        "ü": "u"
    }

    for letra, reemplazo in reemplazos.items():
        texto = texto.replace(letra, reemplazo)

    return texto

def pedir_dia():

    dias_validos = [
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado"
    ]

    while True:

        dia = input("Día: ")

        dia_normalizado = normalizar_texto(dia)

        if dia_normalizado in dias_validos:

            return dia_normalizado

        else:

            print("Día inválido.")
            print("Ingrese uno de estos días:")
            print("Lunes, Martes, Miércoles, Jueves, Viernes o Sábado.")
            
def hay_conflicto_horario(hora_inicio, hora_fin, materia_existente):

    inicio_nuevo = hora_inicio.split(":")
    fin_nuevo = hora_fin.split(":")

    inicio_existente = materia_existente["hora_inicio"].split(":")
    fin_existente = materia_existente["hora_fin"].split(":")

    inicio_nuevo_minutos = int(inicio_nuevo[0]) * 60 + int(inicio_nuevo[1])
    fin_nuevo_minutos = int(fin_nuevo[0]) * 60 + int(fin_nuevo[1])

    inicio_existente_minutos = int(inicio_existente[0]) * 60 + int(inicio_existente[1])
    fin_existente_minutos = int(fin_existente[0]) * 60 + int(fin_existente[1])

    if (
        inicio_nuevo_minutos < fin_existente_minutos
        and fin_nuevo_minutos > inicio_existente_minutos
    ):
        return True

    return False

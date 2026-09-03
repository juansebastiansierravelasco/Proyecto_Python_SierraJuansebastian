import json
from registrar import registrar_materia
from ver_horario import ver_horario
from modificar import modificar_materia
from eliminar import eliminar_materia
from reporte import generar_reporte, mostrar_reporte
try:
    with open("horario.json", "r", encoding="utf-8") as archivo:
        horario = json.load(archivo)
except FileNotFoundError:
    horario = []
except json.JSONDecodeError:

    horario = []
while True:
    print()
    print("==============================================")
    print("          SISTEMA DE HORARIO SEMANAL")
    print("==============================================")
    print("1. Registrar una materia")
    print("2. Ver horario semanal")
    print("3. Modificar una materia o actividad")
    print("4. Eliminar una materia o actividad")
    print("5. Generar reporte del horario")
    print("6. Salir")
    print("==============================================")
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número del 1 al 6.")
        continue
    if opcion == 1:
        registrar_materia(horario)
    elif opcion == 2:
        ver_horario(horario)
    elif opcion == 3:
        modificar_materia(horario)
    elif opcion == 4:
        eliminar_materia(horario)
    elif opcion == 5:
        reporte, total_materias = generar_reporte(horario)
        mostrar_reporte(reporte,total_materias)
    elif opcion == 6:
        print("Programa finalizado.")
        break
    else:

        print("Opción inválida. Seleccione una opción del 1 al 6.")
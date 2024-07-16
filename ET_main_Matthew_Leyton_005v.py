from ET_main_Matthew_Leyton_005v import*

lista_Trabajadores = [
 "Juan Perez",
 "Maria Garcia",
 "Carlos Lopez",
 "Ana Martinez",
 "Pedro Rodriguez",
 "Laura Hernandez",
 "Miguel Sanchez",
 "Isabel Gomez",
 "Francisco Diaz",
 "Elena Fernandez"
]


print("Bienvenido a nuestra aplicacion para la empresa")

while True:
    print("Menu")
    print("1. Asignar sueldos aleatorios")
    print()
    print("2. Clasificar sueldos")
    print()
    print("3. Ver estadisticas")
    print()
    print("4. Reporte de sueldos")
    print()
    print("5. Salir del programa")
    print()
    opcion = input("Ingrese una opcion a elegir: ")
        
    if opcion == '1':
            Asignar_sueldos_aleatorios()
    elif opcion == '2':
            Clasificar_sueldos()
    elif opcion == '3':
            Ver_estadisticas()
    elif opcion == '4':
            Reporte_sueldos()
    elif opcion == '5':
            break
print("Hasta luego, muchas gracias")



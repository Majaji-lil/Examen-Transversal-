import random
import csv
import math


lista_trabajadores = [
    "Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", 
    "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
    "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"
]


sueldos = {}

def Asignar_sueldos_aleatorios():
    global sueldos
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in lista_trabajadores}
    print("Sueldos asignados correctamente.")

def Clasificar_sueldos():
    menores_800k = []
    entre_800k_y_2M = []
    superiores_2M = []
    
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            menores_800k.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2M.append((trabajador, sueldo))
        else:
            superiores_2M.append((trabajador, sueldo))
    
    print("\nSueldos menores a $800,000")
    print("TOTAL:", len(menores_800k))
    for trabajador, sueldo in menores_800k:
        print(f"{trabajador} ${sueldo}")

    print("\nSueldos entre $800,000 y $2,000,000")
    print("TOTAL:", len(entre_800k_y_2M))
    for trabajador, sueldo in entre_800k_y_2M:
        print(f"{trabajador} ${sueldo}")

    print("\nSueldos superiores a $2,000,000")
    print("TOTAL:", len(superiores_2M))
    for trabajador, sueldo in superiores_2M:
        print(f"{trabajador} ${sueldo}")

    print("\ntotal de sueldos: $", sum(sueldo for _, sueldo in sueldos.items()))

def Ver_estadisticas():
    lista_sueldos = list(sueldos.values())
    if lista_sueldos:
        max_sueldo = max(lista_sueldos)
        min_sueldo = min(lista_sueldos)
        promedio_sueldos = sum(lista_sueldos) / len(lista_sueldos)
        

        producto_sueldos = math.prod(lista_sueldos)
        media_geometrica = producto_sueldos ** (1 / len(lista_sueldos))
        
        print(f"\nSueldo mas alto: ${max_sueldo}")
        print(f"Sueldo mas bajo: ${min_sueldo}")
        print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
        print(f"Media geometrica: ${media_geometrica:.2f}")
    else:
        print("No se han asignado sueldos todavía.")
    
    def Reporte_sueldos():
        with open('reporte_sueldos.csv', 'w', newline='') as file:
         writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        
        for trabajador, sueldo_base in sueldos.items():
            descuento_salud = sueldo_base * 0.07
            descuento_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - descuento_salud - descuento_afp
            writer.writerow([trabajador, sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
        
    print("Reporte de sueldos exportado a 'reporte_sueldos.csv'.")


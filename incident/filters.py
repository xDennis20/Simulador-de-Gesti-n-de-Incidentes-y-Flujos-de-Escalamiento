
def filtrar_prioridad(lista_incidentes):
    salir = False
    while not salir:
        print("""Prioridad de incidentes 
        1. Alta
        2. Media
        3. Baja
        4. Volver al menu anterior""")
        try:
            opcion = int(input("Elija una prioridad: "))
        except ValueError:
            print("Valor invalido ingrese un numero entero")
            continue
        if opcion == 1:
            for incidente in lista_incidentes:
                if incidente.prioridad == "alta":
                    print(incidente)
        elif opcion == 2:
            for incidente in lista_incidentes:
                if incidente.prioridad == "media":
                    print(incidente)
        elif opcion == 3:
            for incidente in lista_incidentes:
                if incidente.prioridad == "baja":
                    print(incidente)
        elif opcion == 4:
            salir = True
        else:
            print("Opcion no valida")

def filtrar_estados(lista_incidentes):
    salir = False
    while not salir:
        print("""Estados de incidentes:
        1. Incidentes Pendientes
        2. Incidentes Activos
        3. Incidentes Resueltos
        4. Incidentes Escalables
        5. volver al menu anterior""")
        try:
            opcion = int(input("Elija una opcion: "))
        except ValueError:
            print("Valor invalido ingrese un numero entero")
            continue
        if opcion == 1:
            for incidente in lista_incidentes:
                if incidente.estado == "pendiente":
                    print(incidente)
        elif opcion == 2:
            for incidente in lista_incidentes:
                if incidente.estado == "activo":
                    print(incidente)
        elif opcion == 3:
            for incidente in lista_incidentes:
                if incidente.estado == "resuelto":
                    print(incidente)
        elif opcion == 4:
            for incidente in lista_incidentes:
                if incidente.estado == "escalable":
                    print(incidente)
        elif opcion == 5:
            salir = True
        else:
            print("Opcion no valida")
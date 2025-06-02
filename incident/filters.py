
def filtrar_prioridad(lista_incidentes):
    salir = False
    while not salir:
        print("""Prioridad de incidentes 
        1. Alta
        2. Media
        3. Baja
        4. Volver al menu anterior""")
        opcion = int(input("Elija una prioridad: "))
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

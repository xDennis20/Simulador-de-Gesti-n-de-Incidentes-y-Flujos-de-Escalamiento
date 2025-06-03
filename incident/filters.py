from util.mostrar import mostrar_incidente

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
                    mostrar_incidente(incidente)
        elif opcion == 2:
            for incidente in lista_incidentes:
                if incidente.prioridad == "media":
                    mostrar_incidente(incidente)
        elif opcion == 3:
            for incidente in lista_incidentes:
                if incidente.prioridad == "baja":
                    mostrar_incidente(incidente)
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
                    mostrar_incidente(incidente)
        elif opcion == 2:
            for incidente in lista_incidentes:
                if incidente.estado == "activo":
                    mostrar_incidente(incidente)
        elif opcion == 3:
            for incidente in lista_incidentes:
                if incidente.estado == "resuelto":
                    mostrar_incidente(incidente)
        elif opcion == 4:
            for incidente in lista_incidentes:
                if incidente.estado == "escalable":
                    mostrar_incidente(incidente)
        elif opcion == 5:
            salir = True
        else:
            print("Opcion no valida")

def filtrar_estado_pendiente_activo(lista_incidente):
    lista_filtrada = []
    for incidente in lista_incidente:
        if incidente.estado == "pendiente" or incidente.estado == "activo":
            lista_filtrada.append(incidente)
    if lista_filtrada:
        return lista_filtrada
    else:
        print("No hay incidentes a resolver")
        return None
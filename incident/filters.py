from util.mostrar import mostrar_incidente
import re
from datetime import datetime

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

def buscar_texto(lista_incidentes,texto_a_buscar: str):
    patron = re.compile(rf".*{re.escape(texto_a_buscar)}.*",re.IGNORECASE)
    resultados = [incidente for incidente in lista_incidentes if patron.search(incidente.descripcion)]
    return resultados

def buscar_por_tipo(lista_incidentes, tipo_busqueda):
    patron = re.compile(rf".*{re.escape(tipo_busqueda)}.*", re.IGNORECASE)
    resultados = [incidente for incidente in lista_incidentes if patron.search(incidente.tipo)]
    return resultados

def buscar_por_rango_fechas(lista_incidentes, fecha_inicio_str, fecha_fin_str):
    try:
        formato = "%Y-%m-%d"
        fecha_inicio = datetime.strptime(fecha_inicio_str, formato)
        fecha_fin = datetime.strptime(fecha_fin_str, formato)
    except ValueError:
        print("❌ Formato inválido. Usa el formato YYYY-MM-DD.")
        return []

    resultados = [
        incidente for incidente in lista_incidentes
        if fecha_inicio <= incidente.creado_en <= fecha_fin
    ]
    return resultados

def buscar_por_operador(lista_incidentes, texto_operador):
    patron = re.compile(re.escape(texto_operador), re.IGNORECASE)

    resultados = [
        incidente for incidente in lista_incidentes
        if incidente.asignado and patron.search(incidente.asignado)
    ]
    return resultados
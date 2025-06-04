import json
from collections import deque
from datetime import datetime
from incident.models import Incidentes

def guardar_incidente_json(lista_incidentes: deque, nombre_archivo="incidentes.json"):
    datos = []
    for incidente in lista_incidentes:
        datos.append({
            "id": incidente.id,
            "tipo": incidente.tipo,
            "prioridad": incidente.prioridad,
            "descripcion": incidente.descripcion,
            "fecha_creacion": incidente.fecha_creacion.isoformat(), # Convertir la fecha a String
            "asignado": incidente.asignado,
            "estado": incidente.estado
        })
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

def cargar_incidentes_json(nombre_archivo="incidentes.json"):
    lista = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                incidente = Incidentes(
                    id=item["id"],
                    tipo=item["tipo"],
                    prioridad=item["prioridad"],
                    descripcion=item["descripcion"],
                    fecha_creacion=datetime.fromisoformat(item["fecha_creacion"]),
                    asignado=item["asignado"],
                    estado=item["estado"]
                )
                lista.append(incidente)
    except FileNotFoundError:
        pass  # Si el archivo no existe empieza con lista vacía
    return lista

def guardar_historial_json(historial: list , nombre_archivo="historial.json"):
    datos_historial = []
    for incidente in historial:
        datos_historial.append({
            "id": incidente.id,
            "tipo": incidente.tipo,
            "prioridad": incidente.prioridad,
            "descripcion": incidente.descripcion,
            "fecha_creacion": incidente.fecha_creacion.isoformat(),
            "asignado": incidente.asignado,
            "estado": incidente.estado
        })
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos_historial, archivo, indent=4)

def cargar_historial_json(nombre_archivo="historial.json"):
    lista = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for item in datos:
                incidente = Incidentes(
                    id=item["id"],
                    tipo=item["tipo"],
                    prioridad=item["prioridad"],
                    descripcion=item["descripcion"],
                    fecha_creacion=datetime.fromisoformat(item["fecha_creacion"]),
                    asignado=item["asignado"],
                    estado=item["estado"]
                )
                lista.append(incidente)
    except FileNotFoundError:
        pass
    return lista
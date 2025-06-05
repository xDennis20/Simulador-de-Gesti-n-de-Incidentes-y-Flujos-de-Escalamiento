import json
from collections import deque
from datetime import datetime
from incident.models import Incidentes
from typing import List


def guardar_incidente_json(cola_incidentes: deque, archivo="incidentes.json"):
    datos = []
    for inc in cola_incidentes:
        datos.append({
            "id": inc.id,
            "tipo": inc.tipo,
            "prioridad": inc.prioridad,
            "descripcion": inc.descripcion,
            "fecha_creacion": inc.fecha_creacion.isoformat(),
            "asignado": inc.asignado,
            "estado": inc.estado
        })
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def cargar_incidente_json(archivo="incidentes.json") -> deque:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            incidentes = deque()
            for item in datos:
                inc = Incidentes(
                    id=item["id"],
                    tipo=item["tipo"],
                    prioridad=item["prioridad"],
                    descripcion=item["descripcion"],
                    fecha_creacion=datetime.fromisoformat(item["fecha_creacion"]),
                    asignado=item["asignado"],
                    estado=item["estado"]
                )
                incidentes.append(inc)
            return incidentes
    except FileNotFoundError:
        return deque()


def guardar_historial_json(historial: List[Incidentes], archivo="historial.json"):
    datos = []
    for inc in historial:
        datos.append({
            "id": inc.id,
            "tipo": inc.tipo,
            "prioridad": inc.prioridad,
            "descripcion": inc.descripcion,
            "fecha_creacion": inc.fecha_creacion.isoformat(),
            "asignado": inc.asignado,
            "estado": inc.estado
        })
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)


def cargar_historial_json(archivo="historial.json") -> List[Incidentes]:
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            historial = []
            for item in datos:
                inc = Incidentes(
                    id=item["id"],
                    tipo=item["tipo"],
                    prioridad=item["prioridad"],
                    descripcion=item["descripcion"],
                    fecha_creacion=datetime.fromisoformat(item["fecha_creacion"]),
                    asignado=item["asignado"],
                    estado=item["estado"]
                )
                historial.append(inc)
            return historial
    except FileNotFoundError:
        return []
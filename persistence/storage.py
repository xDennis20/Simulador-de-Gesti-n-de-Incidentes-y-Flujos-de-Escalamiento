import json
from collections import deque
from datetime import datetime
from incident.models import Incidentes
from typing import List


class IncidentStorage:

    @staticmethod
    def _incidente_to_dict(incidente: Incidentes) -> dict:
        """Convierte incidente a diccionario para JSON"""
        return {
            "id": incidente.id,
            "tipo": incidente.tipo,
            "prioridad": incidente.prioridad,
            "descripcion": incidente.descripcion,
            "fecha_creacion": incidente.fecha_creacion.isoformat(),
            "asignado": incidente.asignado,
            "estado": incidente.estado
        }

    @staticmethod
    def _dict_to_incidente(data: dict) -> Incidentes:
        """Convierte diccionario a incidente"""
        return Incidentes(
            id=data["id"],
            tipo=data["tipo"],
            prioridad=data["prioridad"],
            descripcion=data["descripcion"],
            fecha_creacion=datetime.fromisoformat(data["fecha_creacion"]),
            asignado=data["asignado"],
            estado=data["estado"]
        )

    def guardar_incidentes(self, incidentes: deque, archivo="incidentes.json"):
        """Guarda incidentes en JSON"""
        datos = [self._incidente_to_dict(inc) for inc in incidentes]
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar_incidentes(self, archivo="incidentes.json") -> List[Incidentes]:
        """Carga incidentes desde JSON"""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [self._dict_to_incidente(item) for item in datos]
        except FileNotFoundError:
            return []

    def guardar_historial(self, historial: List[Incidentes], archivo="historial.json"):
        """Guarda historial en JSON"""
        datos = [self._incidente_to_dict(inc) for inc in historial]
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def cargar_historial(self, archivo="historial.json") -> List[Incidentes]:
        """Carga historial desde JSON"""
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                return [self._dict_to_incidente(item) for item in datos]
        except FileNotFoundError:
            return []
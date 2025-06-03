import json
from datetime import datetime
from incident.models import Incidentes

def guardar_incidente(lista_incidentes: list, nombre_archivo="persistence/incidentes.json"):
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

def cargar_incidentes_json(nombre_archivo="persistence/incidentes.json"):
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
        pass  # Si el archivo no existe, empezamos con lista vacía
    return lista
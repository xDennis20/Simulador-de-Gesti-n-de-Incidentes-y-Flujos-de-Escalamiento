from incident.models import Incidentes
from cli.interface import InterfazIncidenteServicio
from datetime import datetime

class ServicioIncidente(InterfazIncidenteServicio):
    contador_id = 0
    def __init__(self):
        ServicioIncidente.contador_id +=1
        self.id = ServicioIncidente.contador_id
    def registrar_incidente(self):
        ide = self.id
        tipo = input("Ingrese el tipo de incidente: ").lower().strip()
        prioridad = input("Ingrese la prioridad del incidente ('Alto,Medio,Bajo'): ").lower().strip()
        descripcion = input("Descripcion del incidente: ")
        fecha_creacion = datetime.now()
        asignar_operador = None
        estado = input("Ingrese el estado del incidente: ").lower()
        return Incidentes(ide,tipo,prioridad,descripcion,fecha_creacion,asignar_operador,estado)

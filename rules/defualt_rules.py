from datetime import datetime,timedelta

def regla_escalar(incidente,minutos = 30):
    tiempo_minutos = datetime.now() - incidente.fecha_creacion
    return incidente.estado == "pendiente" and tiempo_minutos >= timedelta(minutos)

def regla_prioridad_alta(incidente):
    return incidente.prioridad == "alta"

def roles_permitidos():
    roles = {
    "infraestructura": {"tecnico", "admin"},
    "seguridad": {"admin"},
    "solicitud": {"tecnico", "soporte"}
    }


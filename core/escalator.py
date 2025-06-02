from datetime import datetime,timedelta

def escalar_incidentes(lista_incidentes):
    for incidente in lista_incidentes:
        tiempo_minutos = datetime.now() - incidente.fecha_creacion
        if incidente.estado == "pendiente" and tiempo_minutos >= timedelta(minutes=30):
            incidente.estado = "escalable"
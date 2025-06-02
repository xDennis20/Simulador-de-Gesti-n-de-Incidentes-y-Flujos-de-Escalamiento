from Excepciones import ValorInvalidoError

def validar_tipo_incidente(tipo: str):
    tipos_validos = ["infraestructura","seguridad","solicitud"]
    if tipo in tipos_validos:
        return tipo
    else:
        raise ValorInvalidoError

def validar_prioridad(prioridad: str):
    prioridades_validas = ["alta","media","baja"]
    if prioridad in prioridades_validas:
        return prioridad
    else:
        raise ValorInvalidoError

def validar_estado_incidente(estado: str):
    estados_validos = ["pendiente","activo","resuelto","escalable"]
    if estado in estados_validos:
        return estado
    else:
        raise ValorInvalidoError
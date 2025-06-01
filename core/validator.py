from Excepciones import ValorInvalidoErrro

def validar_tipo_incidente(tipo):
    tipos_validos = ["infraestructura","seguridad","solicitud"]
    if tipo in tipos_validos:
        return tipo
    else:
        raise ValorInvalidoErrro
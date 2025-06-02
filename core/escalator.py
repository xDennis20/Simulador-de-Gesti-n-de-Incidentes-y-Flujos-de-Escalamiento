from rules.defualt_rules import regla_escalar

def escalar_incidentes(lista_incidentes):
    for incidente in lista_incidentes:
        if regla_escalar(incidente):
            incidente.estado = "escalable"

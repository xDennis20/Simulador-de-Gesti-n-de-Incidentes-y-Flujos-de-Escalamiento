from incident.models import Incidentes
from cli.interface import InterfazIncidenteServicio
from datetime import datetime
from Excepciones import ValorInvalidoError
from util.mostrar import mostrar_incidente
from validator import validar_tipo_incidente,validar_estado_incidente,validar_prioridad
from collections import deque
from rules.defualt_rules import regla_prioridad_alta,roles_permitidos,set_operadores_disponibles
from incident.filters import filtrar_estado_pendiente_activo

class ServicioIncidente(InterfazIncidenteServicio):
    contador_id = 0
    def __init__(self):
        ServicioIncidente.contador_id +=1
        self._id = ServicioIncidente.contador_id

    def registrar_incidente(self):
        def solicitar_dato(mensaje: str, funcion_validador):
            while True:
                entrada = input(mensaje).lower().strip()
                try:
                    return funcion_validador(entrada)
                except ValorInvalidoError:
                    print("Dato inválido. Intenta de nuevo.")

        ide = self._id
        tipo = solicitar_dato("Ingrese el tipo de incidente: ",validar_tipo_incidente)
        prioridad = solicitar_dato("Ingrese la prioridad del incidente: ",validar_prioridad)
        descripcion = input("Descripcion del incidente: ")
        fecha_creacion = datetime.now()
        asignar_operador = None
        estado = solicitar_dato("Ingrese el estado del incidente: ",validar_estado_incidente)
        return Incidentes(ide,tipo,prioridad,descripcion,fecha_creacion,asignar_operador,estado)

class GestorDeIncidentes:
    def __init__(self,servicio_incidente: InterfazIncidenteServicio):
        self.servicio_incidente = servicio_incidente
        self.cola_incidentes = deque([])

    def registrar_incidente(self):
        nuevo_incidente = self.servicio_incidente.registrar_incidente()
        if regla_prioridad_alta(nuevo_incidente): #En esta condicional es para poner primero los incidentes con prioridad alta en la cola
            self.cola_incidentes.appendleft(nuevo_incidente)
        else:
            self.cola_incidentes.append(nuevo_incidente)
        print("Incidente Registrado Correctamente")

    def resolver_incidente(self):
        lista_filtrada = filtrar_estado_pendiente_activo(self.cola_incidentes)
        contador = 0
        salir = False
        for incidente in lista_filtrada:
            contador+=1
            print(f"""\n{contador}. Incidente
            {mostrar_incidente(incidente)}""")
        while not salir:
            try:
                opcion = int(input("Elija un incidente a resolver: "))
            except ValueError:
                print("Coloque un valor entero por favor")
                continue
            if 1 <= opcion <= len(lista_filtrada):
                incidente_obtenido = lista_filtrada[opcion - 1]
                roles = roles_permitidos()
                operador = input("Que operador desea usar?: ").lower().strip()
                if operador in set_operadores_disponibles():
                    if operador in roles.get(incidente_obtenido.tipo, []):
                        incidente_obtenido.estado = "resuelto"
                        incidente_obtenido.asignado = operador
                        salir = True
                else:
                    print("Operador no disponible")
            else:
                print("Opción fuera de rango. Regresando al menú.")
                salir = True

servicio_incidente = ServicioIncidente()
gestor = GestorDeIncidentes(servicio_incidente)
gestor.registrar_incidente()
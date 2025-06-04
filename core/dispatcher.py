from incident.models import Incidentes
from cli.interface import InterfazIncidenteServicio
from datetime import datetime
from Excepciones import ValorInvalidoError
from util.mostrar import mostrar_incidente
from validator import validar_tipo_incidente,validar_estado_incidente,validar_prioridad
from collections import deque
from rules.defualt_rules import regla_prioridad_alta,roles_permitidos,set_operadores_disponibles
from incident.filters import filtrar_estado_pendiente_activo,buscar_texto,buscar_por_tipo,buscar_por_operador,buscar_por_rango_fechas
from persistence.storage import guardar_incidente_json,guardar_historial_json
from escalator import escalar_incidentes

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
        self.historial = []

    def registrar_incidente(self):
        nuevo_incidente = self.servicio_incidente.registrar_incidente()
        if regla_prioridad_alta(nuevo_incidente): #En esta condicional es para poner primero los incidentes con prioridad alta en la cola
            self.cola_incidentes.appendleft(nuevo_incidente)
        else:
            self.cola_incidentes.append(nuevo_incidente)
        print("Incidente Registrado Correctamente")

    def mostrar_incidentes(self):
        lista_mostrar = filtrar_estado_pendiente_activo(self.cola_incidentes)
        if not lista_mostrar:
            print("📭 No hay incidentes pendientes ni activos.")
            return

        print("📋 Lista de incidentes pendientes/en progreso:")
        for incidente in lista_mostrar:
            print(mostrar_incidente(incidente))

    def resolver_incidente(self):
        escalar_incidentes(self.cola_incidentes)
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
                        self.historial.append(incidente_obtenido)
                        guardar_historial_json(self.historial)
                        guardar_incidente_json(self.cola_incidentes)
                        salir = True
                    else:
                        print("Este operador no tiene permiso para ese incidentes")
                else:
                    print("Operador no disponible")
            else:
                print("Opción fuera de rango. Regresando al menú.")
                salir = True

    def asignar_incidente_a_operador(self):
        lista_filtrada = filtrar_estado_pendiente_activo(self.cola_incidentes)
        if not lista_filtrada:
            print("No hay incidentes pendientes para asignar.")
            return

        for idx, incidente in enumerate(lista_filtrada, 1):
            print(f"\n{idx}. Incidente\n{mostrar_incidente(incidente)}")

        try:
            opcion = int(input("Seleccione el incidente a asignar: "))
            if 1 <= opcion <= len(lista_filtrada):
                incidente_seleccionado = lista_filtrada[opcion - 1]
                operador = input("Ingrese el operador: ").lower().strip()
                if operador in set_operadores_disponibles():
                    roles = roles_permitidos()
                    if operador in roles.get(incidente_seleccionado.tipo, []):
                        incidente_seleccionado.asignado = operador
                        print("✅ Incidente asignado correctamente.")
                    else:
                        print("❌ Este operador no tiene permisos para este tipo de incidente.")
                else:
                    print("❌ Operador no disponible.")
            else:
                print("Opción fuera de rango. Regresando al menu")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

    def buscar_incidentes(self):
        while True:
            print(f"""\n Buscar incidentes.
            1. 🔡 Texto
            2. 🚧 Tipo
            3. 🕴 Operador
            4. 📅 Fecha 
            5. Regresar al menu anterior""")
            try:
                opcion = int(input("Elija una opcion: "))
            except ValueError:
                print("Por favor coloque valores enteros")
                continue

            if opcion == 1:
                texto = input("🔍 Ingresa el texto que deseas buscar en las descripciones: ").strip()
                coincidencias = buscar_texto(self.cola_incidentes, texto)

                if coincidencias:
                    for inc in coincidencias:
                        print(mostrar_incidente(inc))  # Usa tu función ya hecha
                else:
                    print("❌ No se encontraron incidentes con ese texto.")

            elif opcion == 2:
                tipo = input("📁 Ingresa el tipo de incidente a buscar (ej. seguridad, red): ").strip()
                coincidencias = buscar_por_tipo(self.cola_incidentes, tipo)

                if coincidencias:
                    for inc in coincidencias:
                        print(mostrar_incidente(inc))
                else:
                    print("❌ No se encontraron incidentes con ese tipo.")

            elif opcion == 3:
                inicio = input("📅 Fecha de inicio (YYYY-MM-DD): ").strip()
                fin = input("📅 Fecha de fin (YYYY-MM-DD): ").strip()

                coincidencias = buscar_por_rango_fechas(self.cola_incidentes, inicio, fin)

                if coincidencias:
                    for inc in coincidencias:
                        print(mostrar_incidente(inc))
                else:
                    print("❌ No se encontraron incidentes en ese rango de fechas.")

            elif opcion == 4:
                texto = input("🔍 Ingresa el nombre o parte del nombre del operador: ").strip()
                coincidencias = buscar_por_operador(self.cola_incidentes, texto)

                if coincidencias:
                    for inc in coincidencias:
                        print(mostrar_incidente(inc))
                else:
                    print("❌ No se encontraron incidentes asignados a ese operador.")

            elif opcion == 5:
                return False
            else:
                print("Opcion no encontrada")
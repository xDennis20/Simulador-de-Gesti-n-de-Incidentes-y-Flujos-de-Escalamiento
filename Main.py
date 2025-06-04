from cli.interface import MenuPrincipal
from core.Excepciones import OpcionInvalidaError
from core.dispatcher import GestorDeIncidentes,ServicioIncidente
from persistence.storage import cargar_incidentes_json, cargar_historial_json,guardar_incidente_json,guardar_historial_json
from collections import deque
from util.mostrar import mostrar_incidente


class MenuControlado:
    def __init__(self,menu: MenuPrincipal):
        self.menu = menu
        cola_cargada = cargar_incidentes_json()
        historial_cargado = cargar_historial_json()
        servicio = ServicioIncidente()
        self.gestor = GestorDeIncidentes(servicio)
        self.gestor.cola_incidentes = deque(cola_cargada)
        self.gestor.historial = historial_cargado

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            try:
                opcion = int(input("Escoja una opcion: "))
                salir = self.procesar_opcion(opcion)
                if salir:
                    print("Guardando y saliendo del sistema")
                    break
            except OpcionInvalidaError:
                print("❌ Opción no válida. Intenta de nuevo.")

    def procesar_opcion(self,opcion: int):
        if opcion == 1:
            self.gestor.registrar_incidente()
        elif opcion == 2:
            print("Aun no impletado la opcion 2")
            return False
        elif opcion == 3:
            self.gestor.asignar_incidente_a_operador()
        elif opcion == 4:
            self.gestor.resolver_incidente()
        elif opcion == 5:
            for i,incidente in enumerate(self.gestor.historial,start=1):
                print(f"\n{i}.")
                print(mostrar_incidente(incidente))
        elif opcion == 6:
            self.gestor.buscar_incidentes()
        elif opcion == 7:
            guardar_incidente_json(self.gestor.cola_incidentes)
            guardar_historial_json(self.gestor.historial)
            return True
        else:
            raise OpcionInvalidaError

prueba = MenuControlado(MenuPrincipal())
prueba.ejecutar()
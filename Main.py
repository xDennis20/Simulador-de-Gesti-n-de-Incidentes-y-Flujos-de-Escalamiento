from cli.interface import MenuPrincipal
from core.Excepciones import OpcionInvalidaError

class MenuControlado:
    def __init__(self,menu: MenuPrincipal):
        self.menu = menu

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

    @staticmethod
    def procesar_opcion(opcion: int):
        if opcion == 1:
            print("Aun no impletado la opcion 1")
            return False #Coloco return False en estas opciones porque en el IDE me sale error xd
        elif opcion == 2:
            print("Aun no impletado la opcion 2")
            return False
        elif opcion == 3:
            print("Aun no impletado la opcion 3")
            return False
        elif opcion == 4:
            print("Aun no impletado la opcion 4")
            return False
        elif opcion == 5:
            print("Aun no impletado la opcion 5")
            return False
        elif opcion == 6:
            return True
        else:
            raise OpcionInvalidaError

prueba = MenuControlado(MenuPrincipal())
prueba.ejecutar()
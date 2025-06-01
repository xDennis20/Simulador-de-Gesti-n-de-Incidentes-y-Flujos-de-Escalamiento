from abc import ABC,abstractmethod
class MenuBase(ABC):
    @abstractmethod
    def mostrar_menu(self):
        pass

class MenuPrincipal(MenuBase):
    def mostrar_menu(self):
        print("\n👨‍‍🚒 Sistema de gestion de incidentes")
        print("1. 📔 Registrar incidente")
        print("2. 🚧 Mostrar incidentes")
        print("3. 👨‍🚒 Asignar incidente a un operador")
        print("4. ✅ Resolver incidente")
        print("5. 📓 Ver historial de incidentes")
        print("6. 📤 Guardar y salir")
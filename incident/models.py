from typing import Optional
from datetime import datetime
from dataclasses import dataclass, replace
from typing import Literal

EstadoIncidente = Literal["pendiente", "activo", "resuelto", "escalable"]
PrioridadIncidente = Literal["alta", "media", "baja"]  # Ajustado a tus validadores
TipoIncidente = Literal["infraestructura", "seguridad", "solicitud"]

@dataclass(frozen=True)
class Incidentes:
    id: int
    tipo: str  #"infraestructura", "seguridad", "solicitud"
    prioridad: str  # "alto", "medio", "bajo"
    descripcion: str
    fecha_creacion: datetime
    asignado: Optional[str]
    estado: str  # "pendiente", "Activo", "resuelto", "escalable"

    def asignar_operador(self, operador: str) -> 'Incidentes':
        """Crea nueva instancia con operador asignado"""
        return replace(self, asignado=operador, estado="activo")

    def resolver(self, operador: str) -> 'Incidentes':
        """Crea nueva instancia resuelta"""
        return replace(self, asignado=operador, estado="resuelto")

    def escalar(self) -> 'Incidentes':
        """Crea nueva instancia escalada"""
        return replace(self, estado="escalable")
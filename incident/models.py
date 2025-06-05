from typing import Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Incidentes:
    id: int
    tipo: str  #"infraestructura", "seguridad", "solicitud"
    prioridad: str  # "alta", "media", "baja"
    descripcion: str
    fecha_creacion: datetime
    asignado: Optional[str]
    estado: str  # "pendiente", "Activo", "resuelto", "escalable"
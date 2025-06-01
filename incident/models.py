from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass(frozen=True)
class Incidentes:
    id: int
    tipo: str  #"infraestructura", "seguridad", "solicitud"
    prioridad: str  # "alto", "medio", "bajo"
    descripcion: str
    fecha_creacion: datetime
    asignado: Optional[str]
    estado: str  # "pendiente", "en_progreso", "resuelto", "escalable"
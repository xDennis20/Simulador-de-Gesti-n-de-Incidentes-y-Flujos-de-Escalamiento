def mostrar_incidente(incidente):
    print(f"""
🔹 ID: {incidente.id}
🔸 Tipo: {incidente.tipo.capitalize()}
⚠️ Prioridad: {incidente.prioridad.capitalize()}
📝 Descripción: {incidente.descripcion}
📅 Fecha de creación: {incidente.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}
👷 Operador asignado: {incidente.operador_asignado or 'No asignado'}
📌 Estado: {incidente.estado.capitalize()}
{"─" * 40}
""")
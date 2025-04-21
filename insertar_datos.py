from app import db, Especialidad, Medico

especialidades = [
    "Medicina interna", "Cardiología", "Cirugía general", "Cirugía neurológica", "Dermatología",
    "Endocrinología", "Gastroenterología", "Ginecoobstetricia", "Cirugía plástica y estética",
    "Cirugía vascular", "Medicina del trabajo", "Cirugía de columna", "Urología", "Reumatología",
    "Otorrinolaringología", "Ortopedia y/o traumatología", "Oftalmología", "Neurología",
    "Neumología", "Nefrología", "Neurocirugía"
]

for nombre in especialidades:
    e = Especialidad(nombre=nombre)
    db.session.add(e)
db.session.commit()

especialidades_bd = Especialidad.query.all()
for e in especialidades_bd:
    medico = Medico(nombre=f"Dr(a). {e.nombre}", especialidad_id=e.id)
    db.session.add(medico)
db.session.commit()

print("✅ Especialidades y médicos insertados correctamente.")

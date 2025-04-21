from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Datos simulados para demostración
especialidades = [
    {'id': 1, 'nombre': 'Cardiologia'},
    {'id': 2, 'nombre': 'Pediatría'},
    {'id': 3, 'nombre': 'Medicina interna'},
    {'id': 4, 'nombre': 'Cirugia general'},
    {'id': 5, 'nombre': 'Dermatologia'},
    {'id': 6, 'nombre': 'Endocrinologia'},
    {'id': 7, 'nombre': 'Gastroenterologia'},
    {'id': 8, 'nombre': 'Ginecoobstetricia'},
    {'id': 9, 'nombre': 'Cirugia plastica y estetica'},
    {'id': 10, 'nombre': 'Cirugia vascular'},
    {'id': 11, 'nombre': 'Medicina del trabajo'},
    {'id': 12, 'nombre': 'Cirugia de columna'},
    {'id': 13, 'nombre': 'Urologia'},
    {'id': 14, 'nombre': 'Reumatologia'},
    {'id': 15, 'nombre': 'Otorrinolaringologia'},
    {'id': 16, 'nombre': 'Ortopedia y/o Traumatologia'},
    {'id': 17, 'nombre': 'Oftalmologia'},
    {'id': 18, 'nombre': 'Neurologia'},
    {'id': 19, 'nombre': 'Neumologia'},
    {'id': 20, 'nombre': 'Nefralogia'},
    {'id': 21, 'nombre': 'Neurocirugia'},
]

medicos = {
    1: [{'id': 1, 'nombre': 'Dr. Juan Pérez'}, {'id': 2, 'nombre': 'Dra. Ana Gómez'}],
    2: [{'id': 2, 'nombre': 'Dr. Carlos Ramírez'}],
    3: [{'id': 3, 'nombre': 'Dra. Laura Méndez'}],
    4: [{'id': 4, 'nombre': 'Dra. L'}],
    5: [{'id': 5, 'nombre': 'Dra. M'}],
    6: [{'id': 6, 'nombre': 'Dra. A'}],

}

# Turnos reservados: ejemplo {'2025-04-08': {1: ['07:00', '07:10']}}
turnos_reservados = {}

@app.route('/')
def index():
    return render_template('index.html', especialidades=especialidades)

@app.route('/medicos/<int:especialidad_id>')
def obtener_medicos(especialidad_id):
    return jsonify(medicos.get(especialidad_id, []))

@app.route('/turnos_ocupados')
def turnos_ocupados():
    medico_id = int(request.args.get('medico_id'))
    fecha = request.args.get('fecha')

    ocupados = turnos_reservados.get(fecha, {}).get(medico_id, [])
    return jsonify(ocupados)

@app.route('/reservar', methods=['POST'])
def reservar_turno():
    datos = request.get_json()
    nombre = datos.get('nombre')
    correo = datos.get('correo')
    fecha = datos.get('fecha')
    hora = datos.get('hora')
    medico_id = int(datos.get('medico_id'))

    # Validaciones básicas
    if not nombre or not correo or not fecha or not hora or not medico_id:
        return jsonify({'error': 'Todos los campos son obligatorios.'})

    # Evitar reservas duplicadas
    if fecha not in turnos_reservados:
        turnos_reservados[fecha] = {}
    if medico_id not in turnos_reservados[fecha]:
        turnos_reservados[fecha][medico_id] = []

    if hora in turnos_reservados[fecha][medico_id]:
        return jsonify({'error': 'Ese turno ya fue reservado. Elija otra hora.'})

    # Guardar el turno
    turnos_reservados[fecha][medico_id].append(hora)

    # Agregar 'am' a la hora (puedes adaptar si más adelante hay horarios pm) ← MODIFICADO
    hora_con_am = f"{hora} am"

    # Confirmación en consola incluyendo fecha y hora ← MODIFICADO
    print(f"Turno reservado para {nombre} el {fecha} a las {hora_con_am}.")

    return jsonify({'mensaje': f'Turno reservado para {nombre} el {fecha} a las {hora_con_am}.'})  # ← MODIFICADO


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



from flask import Blueprint, request, jsonify
from models import db, Consulta, Paciente, Profissional
from datetime import datetime

consultas_bp = Blueprint('consultas', __name__)

@consultas_bp.route('/consultas', methods=['POST'])
def agendar_consulta():
    dados = request.get_json()
    paciente_id = dados.get('paciente_id')
    profissional_id = dados.get('profissional_id')
    data_str = dados.get('data')

    if not paciente_id or not profissional_id or not data_str:
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        data = datetime.strptime(data_str, '%Y-%m-%d %H:%M')
    except ValueError:
        return jsonify({'erro': 'Formato de data inválido. Use YYYY-MM-DD HH:MM'}), 400

    nova_consulta = Consulta(
        paciente_id=paciente_id,
        profissional_id=profissional_id,
        data=data
    )

    db.session.add(nova_consulta)
    db.session.commit()

    return jsonify({'mensagem': 'Consulta agendada com sucesso', 'id': nova_consulta.id}), 201

@consultas_bp.route('/consultas', methods=['GET'])
def listar_consultas():
    consultas = Consulta.query.all()
    resultado = []
    for c in consultas:
        paciente = Paciente.query.get(c.paciente_id)
        profissional = Profissional.query.get(c.profissional_id)
        resultado.append({
            'id': c.id,
            'paciente': {
                'id': paciente.id,
                'nome': paciente.nome,
                'cpf': paciente.cpf
            },
            'profissional': {
                'id': profissional.id,
                'nome': profissional.nome,
                'especialidade': profissional.especialidade
            },
            'data': c.data.strftime('%Y-%m-%d %H:%M')
        })
    return jsonify(resultado)

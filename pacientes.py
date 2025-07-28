from flask import Blueprint, request, jsonify
from models import db, Paciente, HistoricoClinico
from datetime import datetime

routes = Blueprint('routes', __name__)

@routes.route('/pacientes', methods=['GET'])
def listar_pacientes():
    pacientes = Paciente.query.all()
    return jsonify([{
        'id': p.id,
        'nome': p.nome,
        'cpf': p.cpf,
        'data_nascimento': p.data_nascimento.isoformat(),
        'idade': p.idade
    } for p in pacientes])

@routes.route('/pacientes', methods=['POST'])
def criar_paciente():
    dados = request.get_json()
    nome = dados.get('nome')
    cpf = dados.get('cpf')
    data_nascimento_str = dados.get('data_nascimento')  # Espera string no formato 'YYYY-MM-DD'

    if not nome or not cpf or not data_nascimento_str:
        return jsonify({'erro': 'Dados incompletos'}), 400

    try:
        data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'erro': 'Data de nascimento inválida. Use YYYY-MM-DD.'}), 400

    paciente = Paciente(nome=nome, cpf=cpf, data_nascimento=data_nascimento)
    db.session.add(paciente)
    db.session.commit()
    return jsonify({'mensagem': 'Paciente criado', 'id': paciente.id}), 201

@routes.route('/pacientes/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    paciente = Paciente.query.get(id)
    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    dados = request.get_json()
    nome = dados.get('nome')
    cpf = dados.get('cpf')
    data_nascimento_str = dados.get('data_nascimento')

    if nome:
        paciente.nome = nome
    if cpf:
        paciente.cpf = cpf
    if data_nascimento_str:
        try:
            paciente.data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
        except ValueError:
            return jsonify({'erro': 'Data de nascimento inválida. Use YYYY-MM-DD.'}), 400

    db.session.commit()
    return jsonify({'mensagem': 'Paciente atualizado'})

@routes.route('/pacientes/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    paciente = Paciente.query.get(id)
    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    db.session.delete(paciente)
    db.session.commit()
    return jsonify({'mensagem': 'Paciente deletado'})

# --- Nova rota para histórico clínico do paciente ---
@routes.route('/pacientes/<int:paciente_id>/historico', methods=['GET'])
def obter_historico_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)

    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    historico = HistoricoClinico.query.filter_by(paciente_id=paciente_id).all()

    historico_serializado = [
        {
            'id': h.id,
            'descricao': h.descricao,
            'data': h.data.strftime('%Y-%m-%d %H:%M:%S')
        }
        for h in historico
    ]

    return jsonify({
        'paciente_id': paciente.id,
        'nome': paciente.nome,
        'historico': historico_serializado
    }), 200

# --- Nova rota POST para adicionar histórico clínico ---
@routes.route('/pacientes/<int:paciente_id>/historico', methods=['POST'])
def adicionar_historico_paciente(paciente_id):
    paciente = Paciente.query.get(paciente_id)
    if not paciente:
        return jsonify({'erro': 'Paciente não encontrado'}), 404

    dados = request.get_json()
    descricao = dados.get('descricao')

    if not descricao:
        return jsonify({'erro': 'Descrição do histórico é obrigatória'}), 400

    novo_historico = HistoricoClinico(
        paciente_id=paciente_id,
        descricao=descricao
    )
    db.session.add(novo_historico)
    db.session.commit()

    return jsonify({
        'mensagem': 'Histórico clínico adicionado com sucesso',
        'id': novo_historico.id,
        'descricao': novo_historico.descricao,
        'data': novo_historico.data.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

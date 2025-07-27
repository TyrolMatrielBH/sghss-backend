from flask import Blueprint, request, jsonify
from models import db, Profissional

profissionais_bp = Blueprint('profissionais', __name__)

@profissionais_bp.route('/profissionais', methods=['GET'])
def listar_profissionais():
    profissionais = Profissional.query.all()
    resultado = []
    for p in profissionais:
        resultado.append({
            'id': p.id,
            'nome': p.nome,
            'especialidade': p.especialidade
        })
    return jsonify(resultado)

@profissionais_bp.route('/profissionais', methods=['POST'])
def criar_profissional():
    dados = request.get_json()
    nome = dados.get('nome')
    especialidade = dados.get('especialidade')

    if not nome or not especialidade:
        return jsonify({'erro': 'Dados incompletos'}), 400

    profissional = Profissional(nome=nome, especialidade=especialidade)
    db.session.add(profissional)
    db.session.commit()

    return jsonify({'mensagem': 'Profissional criado', 'id': profissional.id}), 201

@profissionais_bp.route('/profissionais/<int:id>', methods=['PUT'])
def atualizar_profissional(id):
    profissional = Profissional.query.get(id)
    if not profissional:
        return jsonify({'erro': 'Profissional não encontrado'}), 404

    dados = request.get_json()
    nome = dados.get('nome')
    especialidade = dados.get('especialidade')

    if nome:
        profissional.nome = nome
    if especialidade:
        profissional.especialidade = especialidade

    db.session.commit()
    return jsonify({'mensagem': 'Profissional atualizado'})

@profissionais_bp.route('/profissionais/<int:id>', methods=['DELETE'])
def deletar_profissional(id):
    profissional = Profissional.query.get(id)
    if not profissional:
        return jsonify({'erro': 'Profissional não encontrado'}), 404

    db.session.delete(profissional)
    db.session.commit()
    return jsonify({'mensagem': 'Profissional deletado'})

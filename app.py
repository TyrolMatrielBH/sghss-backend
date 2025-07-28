from flask import Flask, jsonify
from models import db, Paciente, HistoricoClinico
from config import Config
from routes import routes
from flask_cors import CORS
from consultas import consultas_bp
from profissional import profissionais_bp
from pacientes import routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)
app.register_blueprint(routes)
app.register_blueprint(consultas_bp)
app.register_blueprint(profissionais_bp)


@app.route('/')
def home():
    return 'API VidaPlus funcionando!'

# Rota para obter histórico clínico do paciente
@app.route('/pacientes/<int:paciente_id>/historico', methods=['GET'])
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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

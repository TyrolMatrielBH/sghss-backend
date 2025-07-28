from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14), unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)

    # Relacionamento com histórico clínico
    historico_clinico = db.relationship('HistoricoClinico', backref='paciente', lazy=True)

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

class Profissional(db.Model):
    __tablename__ = 'profissionais'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))

class Consulta(db.Model):
    __tablename__ = 'consultas'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissionais.id'))
    data = db.Column(db.DateTime)

class Leito(db.Model):
    __tablename__ = 'leitos'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10))
    ocupado = db.Column(db.Boolean, default=False)

class HistoricoClinico(db.Model):
    __tablename__ = 'historico_clinico'

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

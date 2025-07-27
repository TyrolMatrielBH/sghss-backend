from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

db = SQLAlchemy()

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(14), unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)

    @property
    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    profissional_id = db.Column(db.Integer, db.ForeignKey('profissional.id'))
    data = db.Column(db.DateTime)  # Alterado para DateTime

class Leito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10))
    ocupado = db.Column(db.Boolean, default=False)

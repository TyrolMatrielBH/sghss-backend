from models import db, Consulta, Paciente, Profissional
from app import app

with app.app_context():
    consultas_inconsistentes = []
    for c in Consulta.query.all():
        paciente = Paciente.query.get(c.paciente_id)
        profissional = Profissional.query.get(c.profissional_id)
        if not paciente or not profissional:
            consultas_inconsistentes.append({
                'consulta_id': c.id,
                'paciente_id': c.paciente_id,
                'profissional_id': c.profissional_id
            })

    print('Consultas inconsistentes:', consultas_inconsistentes)


    for c in Consulta.query.all():
        if not Paciente.query.get(c.paciente_id) or not Profissional.query.get(c.profissional_id):
            db.session.delete(c)
    db.session.commit()
    print('Consultas inconsistentes removidas.')

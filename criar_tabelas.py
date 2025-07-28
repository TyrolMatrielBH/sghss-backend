from app import app  # ou seu arquivo principal, ex: from main import app
from models import db

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")

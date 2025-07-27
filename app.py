from flask import Flask
from models import db
from config import Config
from routes import routes
from flask_cors import CORS
from consultas import consultas_bp
from profissional import profissionais_bp

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


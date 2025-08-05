from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:secret@db:5432/tareas'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.get('/api/tareas')
def listar():
    return jsonify([{'id': t.id, 'texto': t.texto} for t in Tarea.query.all()])

@app.post('/api/tareas')
def crear():
    data = request.get_json()
    tarea = Tarea(texto=data['texto'])
    db.session.add(tarea)
    db.session.commit()
    return jsonify({'id': tarea.id, 'texto': tarea.texto}), 201

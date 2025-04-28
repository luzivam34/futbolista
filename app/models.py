from . import db

class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_jogo = db.Column(db.Date, nullable=False)
    clube_mandante = db.Column(db.String(100), nullable=False)
    gols_mandante = db.Column(db.Integer, nullable=False)
    gols_visitante = db.Column(db.Integer, nullable=False)
    clube_visitante = db.Column(db.String(100), nullable=False)
    campeonato = db.Column(db.String(100), nullable=False)
    local_partida = db.Column(db.String(100), nullable=False)

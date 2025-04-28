from flask import Blueprint, render_template, request, redirect, url_for
from .models import Jogo
from . import db
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    if request.method == 'POST':
        novo_jogo = Jogo(
            data_jogo=datetime.strptime(request.form['data_jogo'], '%Y-%m-%d'),
            clube_mandante=request.form['mandante'],
            gols_mandante=int(request.form['gols_mandante']),
            gols_visitante=int(request.form['gols_visitante']),
            clube_visitante=request.form['visitante'],
            campeonato=request.form['campeonato'],
            local_partida=request.form['local']
        )
        db.session.add(novo_jogo)
        db.session.commit()
        return redirect(url_for('main.index'))

    jogos = Jogo.query.order_by(Jogo.data_jogo.desc()).all()
    return render_template('index.html', jogos=jogos)
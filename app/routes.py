from flask import Blueprint, render_template, request, redirect, url_for
from .models import Jogo
from . import db
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
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


@main.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    jogo = Jogo.query.get_or_404(id)
    if request.method == 'POST':
        jogo.data_jogo = datetime.strptime(request.form['data_jogo'], '%Y-%m-%d')
        jogo.clube_mandante = request.form['mandante']
        jogo.gols_mandante = int(request.form['gols_mandante'])
        jogo.gols_visitante = int(request.form['gols_visitante'])
        jogo.clube_visitante = request.form['visitante']
        jogo.campeonato = request.form['campeonato']
        jogo.local_partida = request.form['local']

        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('editar.html', jogo=jogo)


@main.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    jogo = Jogo.query.get_or_404(id)
    db.session.delete(jogo)
    db.session.commit()
    return redirect(url_for('main.index'))

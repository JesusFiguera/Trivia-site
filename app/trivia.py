from flask import *
from preguntas import tvc,games,food

bp = Blueprint('trivia',__name__)

respuestas = []
participantes = []
@bp.route('/',methods=['POST','GET'])
def index():
    print('Respuestas desde el index',respuestas)
    if request.method == 'POST':
        username = request.form['username']
        return redirect(url_for('trivia.category',username=username))
    return render_template('index.html')


@bp.route('/<username>/')
def category(username):
    respuestas = []
    return render_template('category.html')


@bp.route('/<category>/<int:id>/<respuesta>/')
def trivia(category,id,respuesta):
    if id == 0 and category == "tvc":
        preguntas = tvc[id]
    elif id == 0 and category == "Games":
        preguntas = games[id]
    elif id == 0 and category == "Food":
        preguntas = food[id]

    if id>0 and category == "tvc" and id<4 and category=="tvc":
        preguntas = tvc[id]
        respuestas.append(respuesta)
    if id>0 and category == "Games" and id<4 and category=="Games":
        preguntas = games[id]
        respuestas.append(respuesta)
    if id>0 and category == "Food" and id<4 and category=="Food":
        preguntas = food[id]
        respuestas.append(respuesta)
    if id>=4:
        respuestas.append(respuesta)
        return redirect(url_for('trivia.index'))
    return render_template('trivia.html',pregunta=preguntas,id=id)
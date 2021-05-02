from flask import *
from db import get_db
from user import load_required
from preguntas import food_questions,movie_questions,game_questions
import time
from tiempo import calcular_tiempo
bp = Blueprint('trivia',__name__)



@bp.route('/category',methods=['POST','GET'])
@load_required
def category():
    db,c = get_db()
    c.execute(
        'select * from user where id = %s',(session.get('user_id'),)
    )
    user = c.fetchone()
    return render_template('trivia/category.html')

@bp.route('/<string:category>/trivia',methods=["POST","GET"])
@load_required
def trivia(category):
    questions = []
    answer = []
    correctas = 0
    fin = 0
    if category == "Food":
        questions = food_questions
    elif category == "Movies":
        questions = movie_questions
    elif category == "Games":
        questions = game_questions

    if request.method == "POST":
        answer = request.form
        tiempo = calcular_tiempo(int(request.form["-1"]))
        for i in range(len(answer)-1):
            if answer[str(i)] == "True":
                correctas+=1
        db,c = get_db()
        c.execute(
            'select username from user where id = %s',(session.get('user_id'),)
        )
        username = c.fetchone()
        c.execute(
            'insert into trivia (correctas,user_id,category,username,tiempo) values (%s,%s,%s,%s,%s)',(correctas,session.get('user_id'),category,username["username"],tiempo)
        )
        db.commit()
        return redirect(url_for('user.index'))
    return render_template('trivia/trivia.html',category=category,questions=questions)
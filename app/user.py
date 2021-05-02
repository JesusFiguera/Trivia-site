from flask import *
from db import get_db
import functools

bp = Blueprint('user',__name__)



@bp.route('/',methods=['POST','GET'])
def index():
    session.clear()
    db,c = get_db()
    c.execute(
        'select * from trivia'
    )
    users = c.fetchall()
    if request.method == 'POST':
        username = request.form['username']
        db,c = get_db()
        c.execute(
            'select * from user where username = %s',(username,)
        )
        error = None
        result = c.fetchone()
        if result != None:
            error = 'El usuario ya existe'
        if not username:
            error = 'Debe ingresar un nombre de usuario'
        if error == None:
            c.execute(
                'insert into user (username) values (%s)',(username,)
            )
            db.commit()
            c.execute(
                'select * from user where username = %s',(username,)
            )
            user = c.fetchone()
            session.clear()
            session['user_id'] = user['id'] 
            return redirect(url_for('trivia.category'))
    return render_template('index.html',users=users)

@bp.before_app_request
def load_user():
    user_id = session.get('user_id')
    if user_id == None:
        g.user = None
    else:
        db,c = get_db()
        c.execute(
            'select username from user where id = %s',(user_id,)
        )
        g.user = c.fetchone()

def load_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user == None:
            return redirect(url_for('user.index'))
        return view(**kwargs)
    return wrapped_view

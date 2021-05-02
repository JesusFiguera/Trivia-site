from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='verydifficultstringidontknowhowtomake',
        DATABASE_HOST='Sentinel.mysql.pythonanywhere-services.com',
        DATABASE_USER='Sentinel',
        DATABASE_PASSWORD='70242526e',
        DATABASE='trivia'
    )

    import db
    db.init_app(app)

    import user
    import trivia
    app.register_blueprint(user.bp)
    app.register_blueprint(trivia.bp)
    @app.route('/prueba')
    def prueba():
        return '<h1>Hola mundo</h1>'
    return app

app = create_app()

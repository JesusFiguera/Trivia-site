from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='sdfasj!"$"#%28394712',
        DATABASE_HOST='localhost',
        DATABASE_USER='root',
        DATABASE_PASSWORD='1234',
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

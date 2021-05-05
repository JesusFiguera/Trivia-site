from flask import *

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='Mikey'
    )
    import trivia
    app.register_blueprint(trivia.bp)
    return app
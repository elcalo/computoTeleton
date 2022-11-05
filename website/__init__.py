from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'pelusa1202'

    from .computo import p

    app.register_blueprint(p, url_prefix='/')

    return app
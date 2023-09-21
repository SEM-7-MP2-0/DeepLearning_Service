import os
from middleware.access_token import VerifyAccessToken
from routes import index

def create_app(app, config_file="settings.py"):
    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, config_file)
    app.config.from_pyfile(config_file)
    app.wsgi_app = VerifyAccessToken(app.wsgi_app)
    app.register_blueprint(index, url_prefix="/")
    return app
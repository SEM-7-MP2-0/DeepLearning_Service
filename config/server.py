import os
from middleware.access_token import VerifyAccessToken
from routes import index, detect_faces


def create_app(app, config_file="settings.py"):
    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, config_file)
    app.config.from_pyfile(config_file)
    app.static_folder = "output"
    app.wsgi_app = VerifyAccessToken(app.wsgi_app)
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(detect_faces, url_prefix="/detect_faces")
    app.add_url_rule(
        "/output/<path:filename>", endpoint="output", view_func=app.send_static_file
    )

    return app

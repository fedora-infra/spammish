import os
from logging.config import dictConfig

from flask import Flask
from flask_healthz import healthz
from flask_mod_auth_gssapi import FlaskModAuthGSSAPI
from flask_wtf.csrf import CSRFProtect
from whitenoise import WhiteNoise

from spammish.views import blueprint


# Forms
csrf = CSRFProtect()


def create_app(config=None):
    """See https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/"""

    app = Flask(__name__)

    # Load default configuration
    app.config.from_object("spammish.defaults")

    # Load the optional configuration file
    if "FLASK_CONFIG" in os.environ:
        app.config.from_envvar("FLASK_CONFIG")

    # Load the config passed as argument
    app.config.update(config or {})

    if app.config.get("TEMPLATES_AUTO_RELOAD"):
        app.jinja_env.auto_reload = True

    # Logging
    if app.config.get("LOGGING"):
        dictConfig(app.config["LOGGING"])

    # Extensions
    csrf.init_app(app)
    FlaskModAuthGSSAPI(app)

    # Register views
    app.register_blueprint(blueprint)
    app.register_blueprint(healthz, url_prefix="/healthz")

    # Static files
    app.wsgi_app = WhiteNoise(
        app.wsgi_app, root=f"{app.root_path}/static/", prefix="static/"
    )

    return app

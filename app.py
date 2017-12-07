from flask import Flask

from endpoints import index, api


def create_app(config, debug=False, testing=False):
    app = Flask(__name__, template_folder='dist', static_folder='dist',
                static_url_path='')
    app.config.from_object(config)
    app.debug = debug
    app.testing = testing

    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_blueprints(app):
    app.register_blueprint(index)
    app.register_blueprint(api)


def register_errorhandlers(app):
    """"""
    def render_error(error):
        """Render error template"""
        error_code = getattr(error, 'code', 404)
        # return render_template("{}.html".format(error_code)), error_code
        return 'Sorry, Nothing at this URL.', error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)

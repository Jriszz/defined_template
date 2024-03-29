from flask import Flask,jsonify,make_response
from .extensions import *
from .router import error_bp,argument_bp
from application.utils import CustomFlaskError


def create_app(config_object='application.settings'):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    register_after_request(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    # bcrypt.init_app(app)
    # cache.init_app(app)
    # db.init_app(app)
    # csrf_protect.init_app(app)
    # login_manager.init_app(app)
    # debug_toolbar.init_app(app)
    # migrate.init_app(app, db)
    # CORS(app)
    # sess.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(public.views.blueprint)
    # app.register_blueprint(user.views.blueprint)
    app.register_blueprint(error_bp)
    app.register_blueprint(argument_bp)
    return None


def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(CustomFlaskError)
    def handler_flask_error(error):
        response = jsonify(error.to_dict())
        response.status_code = 200
        return response



def register_shellcontext(app):
    """Register shell context objects."""
    # def shell_context():
    #     """Shell context objects."""
    #     return {
    #         'db': db,
    #         'User': models.User
    #     }
    #
    # app.shell_context_processor(shell_context)
    pass
def register_after_request(app):
    @app.after_request
    def cors(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Method'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        return response

def register_commands(app):
    """Register Click commands."""
    # app.cli.add_command(test)
    # app.cli.add_command(lint)
    # app.cli.add_command(clean)
    # app.cli.add_command(urls)
    # app.cli.add_command(deploy)
    # app.cli.add_command(fake_data)
    pass
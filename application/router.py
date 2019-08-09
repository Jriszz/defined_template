from flask import Blueprint
from application.services import Errors
from application.services.Errors import set_error,index
error_bp = Blueprint(name=Errors, url_prefix='/auth', import_name='__name__')

error_bp.add_url_rule('/set-error',view_func=set_error,methods=['GET'])
error_bp.add_url_rule('/index',view_func=index, methods=['GET'])

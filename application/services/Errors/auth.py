from application.utils import CustomFlaskError
from flask import request
from application.Enums import RespEnum

def set_error():
    if request.method == 'GET':
        raise CustomFlaskError(resp_code=RespEnum.ERR_00000001[0], resp_desc=RespEnum.ERR_00000001[1])

def index():
    return 'hello world!'
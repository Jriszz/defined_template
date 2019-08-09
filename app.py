from flask import Flask, make_response, jsonify

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/index')
def hello_world():
    res= {'resp_code': '9000','resp_desc': '成功'}
    return jsonify(res)

@app.after_request
def after_handler(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
if __name__ == '__main__':
    app.run(debug=True)

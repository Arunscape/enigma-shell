import os
from enigma_engine import code_parse
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/', methods = ['POST'])
def hello():
    req = request.get_json()
#    raise(Exception(req))
    return jsonify(code_parse(req['code']))

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

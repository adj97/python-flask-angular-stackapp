from blueprints.blueprint1 import blueprint1
from model.model1 import model1

from flask import Flask, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

@app.route('/')
@swag_from('docs/home.yml')
def home():
    result = {
        'hello': 'world'
    }

    return jsonify(result)

@app.route('/really/very/long/api/route',methods=['GET'])
def long_route():
    return jsonify({'msg':'I have come from the far away API land'})

if __name__ == '__main__':
    app.run(debug=True)

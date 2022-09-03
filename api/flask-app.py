from blueprints.blueprint1 import blueprint1
from model.model1 import model1

from flask import Flask, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
@swag_from('docs/home.yml')
def home():
    result = {
        'hello': 'world'
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(
    app,
    config={
        'headers': [],
        'specs': [
            {
                'endpoint': 'apispec_1',
                'route': '/apispec_1.json',
                'rule_filter': lambda rule: True, 
                'model_filter': lambda tag: True,
            }
        ],
        'static_url_path': '/flasgger_static',
        'swagger_ui': True,
        'specs_route': '/'
    }
)

from app.controllers import rotas
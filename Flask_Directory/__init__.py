import os
from flask import Flask
from Flask_Directory import json_functions

app = Flask(__name__)

abs_path = os.environ['ABS_PATH']
secret_key_file = json_functions.read_from_file(f'{abs_path}/keys.json')
secret_key = secret_key_file["SECRET_KEY"]

app.config["SECRET_KEY"] = secret_key

from Flask_Directory import routes
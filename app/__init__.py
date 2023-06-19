from flask import Flask
from flask_cors import CORS

# 初始化web应用
app = Flask(__name__, instance_relative_config=True, static_folder="./templates/_app")
CORS(app, resources=r'/*')

app.config['DEBUG'] = True

from app import views

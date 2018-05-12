from flask import Flask
from player_session_service.apis import api

app = Flask(__name__)
api.init_app(app)

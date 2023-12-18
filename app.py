from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.naver import ChineseResource


app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

api = Api(app)

api.add_resource(ChineseResource,'/chinese')


if __name__ == '__main__':
    app.run()

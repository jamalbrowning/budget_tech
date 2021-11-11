import redis
from flask import Flask,request, jsonify
import os

# Init app
def create_app():
  app = Flask(__name__)
  return app

app = create_app()
basedir = os.path.abspath(os.path.dirname(__file__))
cache = redis.Redis(host='redis', port=6379)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET'])
def hello():

    return jsonify({'msg':'hello world'})

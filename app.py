# import redis
from flask import Flask,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.schemas import *
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# cache = redis.Redis(host='redis', port=6379)

#database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)

# budget Item class/model
class BudgetItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String())
  price = db.Column(db.Float)

  def __init__(self, name, description, price):
    self.name = name
    self.description = description
    self.price = price

# Budget Item Schema
class BudgetItemSchema(ma.Schema):
  class Meta:
    fields = ('id','name','description','price')

# init Schema
budget_item_schema = BudgetItemSchema()
budget_items_schema = BudgetItemSchema(many=True, )

@app.route('/', methods=['GET'])
def hello():

    return jsonify({'msg':'hello world'})
    
# create item
@app.route('/item', methods=['POST'])
def add_item():
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']

  new_item = BudgetItem(name, description, price)

  db.session.add(new_item)
  db.session.commit()

  return budget_item_schema.jsonify(new_item)

# get all items
@app.route('/item', methods=['GET'])
def get_items():
  all_items = BudgetItem.query.all()
  result = budget_items_schema.dump(all_items)
  return jsonify(result)

#get single item
@app.route('/item/<id>', methods=['GET'])
def get_item(id):
  item = BudgetItem.query.get(id)
  return budget_item_schema.jsonify(item)

#update item
@app.route('/item/<id>', methods=['PUT'])
def update_item(id):
  item = BudgetItem.query.get(id)
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']

  item.name = name
  item.description = description
  item.price = price

  db.session.commit()

  return budget_item_schema.jsonify(item)

#delete single item
@app.route('/item/<id>', methods=['DELETE'])
def delete_item(id):
  item = BudgetItem.query.get(id)
  db.session.delete(item)
  db.session.commit()
  return budget_item_schema.jsonify(item)
  
if __name__ == '__main__':
  app.run(debug=True)
 
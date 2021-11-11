from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from ..app import app

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
budget_item_schema = BudgetItemSchema(strict=True)
budget_items_schema = BudgetItemSchema(many=True, strict=True)

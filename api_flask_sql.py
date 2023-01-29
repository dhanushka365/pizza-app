from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Myapp(db.Model):
    order_id = db.Column(db.Integer , primary_key=True)
    size = db.Column(db.String(500))
    toppings = db.Column(db.String(500))
    crust = db.Column(db.String(500))

class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('order_id', 'size', 'toppings', 'crust')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/create')
def create():
    db.create_all()
    return 'All tables created'    

if __name__ == '__main__':
    #db.create_all()
    app.run()

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
    size = db.Column(db.String(500), unique=True, nullable=False)
    toppings = db.Column(db.String(500), unique=True, nullable=False)
    crust = db.Column(db.String(500), unique=True, nullable=False)



with app.app_context():
    db.create_all()



class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('order_id', 'size', 'toppings', 'crust')

@app.route('/')
def hello_world():
    return 'Hello World!'   




if __name__ == '__main__':
    #db.create_all()
    app.run(port=5004,debug=True)

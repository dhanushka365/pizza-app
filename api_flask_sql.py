from flask import Flask, jsonify, redirect, request, url_for
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


my_app_schema = MyAppSchema(many=True)

@app.route('/')
def hello_world():
    return 'Hello World!'   


@app.route('/order')
def get_order():
    entries = Myapp.query.all()
    result = my_app_schema.dump(entries)
    return jsonify(result)


@app.route('/order', methods=["POST"])
def post_order():
    req = request.get_json()
    order_id = req["order_id"]
    size = req["size"]
    toppings =req["toppings"]
    crust = req["crust"]
    new_entry = Myapp(order_id=order_id, size=size, toppings=toppings, crust=crust)

    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for("get_order"))

@app.route('/order/<order_id>', methods=["DELETE"])
def delete_order(order_id):
    entry = Myapp.query.get_or_404(order_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for("get_order"))


@app.route('/order/<order_id>', methods=["PUT"])
def update_order(order_id):
    req = request.get_json()
    entry = Myapp.query.get(order_id)
    entry.size =req["size"]
    entry.toppings =req["toppings"]
    entry.crust = req["crust"]
    db.session.add(entry)
    db.session.commit()
    return redirect(url_for("get_order"))

if __name__ == '__main__':
    #db.create_all()
    app.run(port=5004,debug=True)

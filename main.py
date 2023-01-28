from flask import Flask, make_response, render_template,request,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/html')
def get_html():
    return render_template("index.html")


@app.route('/qs')
def get_qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}:{v}" for k,v in req.items())
    return "No query"


order = {
    "order1":{
        "Size":"Small",
        "Toppings":"Cheese",
        "Crust":"Thin Crust"
    }
}


@app.route("/orders")
def get_order():
    response = make_response(jsonify(order),200)
    return response


if __name__ == '__main__':
    app.run(port=5004,debug=True)
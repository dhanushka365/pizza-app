from flask import Flask, make_response, render_template,request,jsonify

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    return 'Hello World!'

@app1.route('/html')
def get_html():
    return render_template("index.html")


@app1.route('/qs')
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


@app1.route("/orders")
def get_order():
    response = make_response(jsonify(order),200)
    return response


if __name__ == '__main__':
    app1.run(port=5004,debug=True)
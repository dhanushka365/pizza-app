from flask import Flask, make_response, render_template,request,jsonify

app = Flask(__name__)

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

'''
Get order details using orderid
'''

@app.route(("/orders/<orderid>"))
def get_order_details(orderid):
    if orderid in order:
        response = make_response(jsonify(order[orderid]),200)
        return response
    return "Order not Found"


@app.route(("/orders/<orderid>/<items>"))
def get_item_details(orderid, items):
    item = order[orderid].get(items)
    if item:
        response = make_response(jsonify(item),200)
        return response
    return "item not Found"    

if __name__ == '__main__':
    app.run(port=5004,debug=True)
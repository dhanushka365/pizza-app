from flask import Flask, make_response, render_template,request,jsonify

app = Flask(__name__)

order = {
    "order1":{
        "Size":"Small",
        "Toppings":"Cheese",
        "Crust":"Thin Crust"
    }
}


@app.route("/orders/")
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



@app.route("/orders/<orderid>", methods=["POST"])
def post_order_details(orderid):#create order
    req = request.get_json()
    if orderid in order:
        response = make_response(jsonify({"error":"Order ID already exist"} ),400)
        return response
    order.update({orderid:req})
    response = make_response(jsonify({"message":"new order created"}), 201)
    return response


@app.route("/orders/<orderid>", methods=["PUT"])
def put_order_details(orderid):#create order
    req = request.get_json()
    if orderid in order:
        order[orderid]=req
        response = make_response(jsonify({"error":"Order Updated"} ),200)
        return response

    order[orderid]=req
    response = make_response(jsonify({"message":"new order created"}), 201)
    return response


@app.route("/orders/<orderid>", methods=["PATCH"])
def patch_order_details(orderid):#create order
    req = request.get_json()
    if orderid in order:
        for k,v in req.items():
            order[orderid][k]=v
        response = make_response(jsonify({"error":"Order Updated"} ),200)
        return response

    order[orderid]=req
    response = make_response(jsonify({"message":"new order created"}), 201)
    return response

@app.route("/orders/<orderid>", methods=["DELETE"])
def delete_order_details(orderid):#delete order
    if orderid in order:
        del order[orderid]
        response = make_response(jsonify({"message":"Order Deleted"} ),204)
        return response
    response = make_response(jsonify({"error":"Order ID already exist"}), 404)
    return response



if __name__ == '__main__':
    app.run(port=5004,debug=True)
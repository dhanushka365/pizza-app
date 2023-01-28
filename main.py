from flask import Flask, render_template,request

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

if __name__ == '__main__':
    app.run(port=5004,debug=True)
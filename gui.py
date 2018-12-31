from flask import Flask,render_template,redirect,request,url_for,jsonify

app = Flask(__name__)

@app.route("/")
def index():
    open_request =['1234-BINANCE-HUOBI-LTC-0.001','4567-KRAKEN-GATEIO-BTC-0.110','8989-BITMEX-HUOBI-ETH-1.200']
    return render_template('gui.html',open_request=open_request)

@app.route("/transfer_data",methods=['POST'])
def transfer_data():
    var = request.json
    print(var)
    return jsonify(result='successfully transferred!')

@app.route("/add_secret",methods=['POST'])
def add_secret():
    var = request.json
    print(var)
    return jsonify(result='successfully added!')

@app.route("/update_secret",methods=['POST'])
def update_secret():
    var = request.json
    print(var)
    return jsonify(result='successfully updated!')

if __name__ == '__main__':
    app.run(debug=True)
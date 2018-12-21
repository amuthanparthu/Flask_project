from flask import Flask,render_template
import MySQLdb
import datetime

app = Flask(__name__)

db = MySQLdb.connect(host = '127.0.0.1',user = 'root',passwd = 'root',db = 'amuthan')

active_cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
open_order_cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
fill_detail_cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

@app.route("/")
def index():
    active_strategies = []
    open_orders = []
    fill_details = []

    active_cursor.execute("SELECT * FROM active_strategies")
    open_order_cursor.execute("SELECT * FROM open_orders")
    fill_detail_cursor.execute("SELECT * FROM fill_details")

    for active_order in active_cursor.fetchall():
        active_strategies.append(active_order)

    for open_order in open_order_cursor.fetchall():
        open_orders.append(open_order)

    for fill_detail in fill_detail_cursor.fetchall():
        fill_details.append(fill_detail)

    return render_template('market_making.html',active_strategies = active_strategies,open_orders = open_orders , fill_details = fill_details, datetime = datetime.datetime.now())

if __name__ == '__main__':
    app.run(debug=True)


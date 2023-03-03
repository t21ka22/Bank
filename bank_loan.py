import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loanlist')
def loanlist():
    # open the connection to the database
    conn = sqlite3.connect('bank_loan.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from loanlist")
    rows = cur.fetchall()
    conn.close()
    return render_template('loanlist.html', rows=rows)

@app.route('/customerinfo')    
def customerinfo():
    # open the connection to the database
    conn = sqlite3.connect('bank_loan.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from customerinfo")
    rows = cur.fetchall()
    conn.close()
    return render_template('customerinfo.html', rows=rows)

@app.route('/customerinfo/<customer_ID>')    
def customerloan(customer_ID):
    # open the connection to the database
    conn = sqlite3.connect('bank_loan.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from customerinfo where customer_ID=?",[customer_ID])
    rows = cur.fetchall()
    conn.close()
    return render_template('customerinfo.html', rows=rows)
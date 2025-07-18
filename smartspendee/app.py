from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-income")
def add_income():
    return "Add monthly income"

@app.route("/add-expense")
def add_expense():
    return "Add or edit expense"

@app.route("/view-expense")
def view_expenses():
    return "List of expenses"

@app.route("/stats")
def view_stats():
    return "Budget statistics"

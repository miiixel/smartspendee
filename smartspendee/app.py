from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-income", methods=['GET', 'POST'])
def add_income():
    if request.method == "POST":
        income = request.form["income"]
        return f"Income of {income} saved!"
    return render_template("add-income.html")

@app.route("/add-expense")
def add_expense():
    return "Add or edit expense"

@app.route("/view-expense")
def view_expenses():
    return "List of expenses"

@app.route("/stats")
def view_stats():
    return "Budget statistics"

from flask import Flask, render_template, request, redirect, url_for
import features as features
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-income", methods=["GET", "POST"])
def addIncome():
    if request.method == "POST":
        income = request.form["income"]
        features.saveIncome(income)
        return '''
        <h3>Income saved!</h3>
        <a href="/">Back to home page</a>
        '''
    return render_template("add-income.html")

@app.route("/add-expense", methods=["GET", "POST"])
def add_expense():
    if request.method == "POST":
        item = request.form["item"]
        amount = request.form["amount"]
        category = request.form["category"]
        features.addExpense(item, amount, category)
        return redirect(url_for("add_expense_confirm"))

    return render_template("add-expense.html")

@app.route("/add-expense/confirm")
def add_expense_confirm():
    return '''
        <h3>Expense saved!</h3>
        <p>Would you like to add another expense?</p>
        <a href="/add-expense">Add another expense</a><br>
        <a href="/">Back to home page</a>
    '''
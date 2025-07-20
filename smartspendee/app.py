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
    return render_template("confirm-expenses.html")

@app.route("/view-expense", methods=["GET"])
def view_expense():
    expenses = features.getExpenses()
    chart_generated = features.generate_pie_chart_by_category()

    if not expenses:
        return "<h3>No expenses recorded yet.</h3><a href='/'>⬅ Back to Home</a>"

    return render_template("view-expense.html", expenses=expenses, chart_url="/static/pie_chart.png")

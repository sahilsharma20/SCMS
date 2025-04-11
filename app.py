from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "smartcanteensecret"

# Dummy menu data
menu_items = [
    {"id": 1, "name": "Veg Sandwich", "price": 40, "image": "images/sandwich.webp"},
    {"id": 2, "name": "White Sauce Pasta", "price": 90, "image": "images/white_sauce_pasta.jpeg"},
]

# Index/Home Page
@app.route('/')
def index():
    return render_template('index.html', menu=menu_items)

# Orders Page (Dynamic by item id)
@app.route('/order/<int:item_id>', methods=['GET', 'POST'])
def order(item_id):
    item = next((item for item in menu_items if item["id"] == item_id), None)
    if not item:
        flash("Item not found", "danger")
        return redirect(url_for('index'))
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        flash(f"Order placed for {quantity} x {item['name']}!", "success")
        return redirect(url_for('index'))
    return render_template('order.html', item=item)

# Feedback Page
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        # You can add logic to store in DB or file
        flash("Thank you for your feedback!", "success")
        return redirect(url_for('index'))
    return render_template('feedback.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Add logic to verify user
        flash("Logged in successfully!", "success")
        return redirect(url_for('index'))
    return render_template('login.html')

# Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Add logic to store user
        flash("Account created successfully!", "success")
        return redirect(url_for('login'))
    return render_template('signup.html')

# Run the App
if __name__ == '__main__':
    app.run(debug=True)

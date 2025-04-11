from flask import render_template, request, redirect, url_for, session, flash
from app import db
from app.models import User, MenuItem, Order, Feedback
from flask import current_app as app
import re

@app.route('/')
def index():
    """Redirect to the login page."""
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        college_id = request.form['college_id'].strip()
        password = request.form['password']

        # Validate college ID format (e.g., 22CS070)
        if not re.match(r'^\d{2}[a-zA-Z]{2}\d{3}$', college_id):
            flash("Invalid College ID format. Use format: 22CS070", "danger")
        else:
            user = User.query.filter_by(college_id=college_id).first()
            if user and user.password == password:  # Ensure correct password matching
                session['user'] = college_id
                flash("Login successful!", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials", "danger")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """Show the dashboard page."""
    if 'user' not in session:
        flash("You must log in first", "warning")
        return redirect(url_for('login'))

    return render_template('dashboard.html', user=session['user'])

@app.route('/menu')
def menu():
    """Display the food menu."""
    items = MenuItem.query.all()
    return render_template('menu.html', menu=items)

@app.route('/order', methods=['POST'])
def order():
    """Handle the food order."""
    if 'user' not in session:
        flash("You must log in first", "warning")
        return redirect(url_for('login'))

    item_id = request.form['item_id']
    
    # Ensure that item_id is valid (added a check here)
    menu_item = MenuItem.query.get(item_id)
    if not menu_item:
        flash("Invalid menu item", "danger")
        return redirect(url_for('menu'))

    # Save order in the database
    new_order = Order(college_id=session['user'], item_id=item_id)
    db.session.add(new_order)
    db.session.commit()

    flash("Order placed successfully!", "success")
    return redirect(url_for('menu'))

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    """Handle the feedback submission."""
    if 'user' not in session:
        flash("You must log in first", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        comment = request.form['comment']
        
        # Save feedback in the database
        fb = Feedback(college_id=session['user'], comment=comment)
        db.session.add(fb)
        db.session.commit()

        flash("Thanks for your feedback!", "success")
        return redirect(url_for('menu'))
    
    return render_template('feedback.html')

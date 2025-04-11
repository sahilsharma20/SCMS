# from flask import Flask, render_template, request, redirect, url_for, flash, session

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Use a secure key in production

# # Home Page
# @app.route('/')
# def home():
#     return render_template('index.html')

# # Login Page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Dummy login validation
#         username = request.form['username']
#         password = request.form['password']
#         if username == "admin" and password == "123":
#             session['user'] = username
#             flash('Login successful!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid credentials', 'danger')
#             return redirect(url_for('login'))
#     return render_template('login.html')

# # Signup Page
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         # You can add code to save user to DB
#         flash('Account created successfully! Please login.', 'success')
#         return redirect(url_for('login'))
#     return render_template('signup.html')

# # Orders Page
# @app.route('/order')
# def order():
#     return render_template('order.html')

# # Feedback Page
# @app.route('/feedback', methods=['GET', 'POST'])
# def feedback():
#     if request.method == 'POST':
#         name = request.form['name']
#         message = request.form['message']
#         # Store feedback in database or file here
#         flash('Thanks for your feedback!', 'info')
#         return redirect(url_for('feedback'))
#     return render_template('feedback.html')

# # Logout
# @app.route('/logout')
# def logout():
#     session.pop('user', None)
#     flash('Logged out successfully.', 'info')
#     return redirect(url_for('home'))

# # Contact Page
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')  # You can create this file

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

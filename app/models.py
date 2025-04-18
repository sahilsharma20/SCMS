from app import db

class User(db.Model):
    """Model representing a user."""
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False, default='Admin@12345')

    # One-to-many relationship with orders
    orders = db.relationship('Order', backref='user', lazy=True)

    # One-to-many relationship with feedback
    feedbacks = db.relationship('Feedback', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.college_id}>'

class MenuItem(db.Model):
    """Model representing a menu item."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<MenuItem {self.name}>'

class Order(db.Model):
    """Model representing an order."""
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.String(20), db.ForeignKey('user.college_id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    status = db.Column(db.String(20), default='Pending')  # Order status: Pending, In Progress, Completed

    def __repr__(self):
        return f'<Order {self.id} by {self.college_id}>'

class Feedback(db.Model):
    """Model representing user feedback."""
    id = db.Column(db.Integer, primary_key=True)
    college_id = db.Column(db.String(20), db.ForeignKey('user.college_id'), nullable=False)
    comment = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=True)  # Optional rating (1 to 5)

    def __repr__(self):
        return f'<Feedback from {self.college_id}>'

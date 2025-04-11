import os
import sys

# Ensure the project root directory is in the Python path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app

# Create the app instance
app = create_app()

# Run the app in debug mode when executed directly
if __name__ == '__main__':
    app.run(debug=True)

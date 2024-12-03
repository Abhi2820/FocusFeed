
import sys
import os
from app import app, db

# Add the current directory to the module search path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Set the template folder path
app.template_folder = r"C:\Users\admin\OneDrive\Desktop\FocusFeed\templates"

# Create tables in the database (if they don't already exist)
with app.app_context():
    db.create_all()

print(f"Using template folder: {app.template_folder}")  # Debug output

# Run the app
app.run(debug=True)


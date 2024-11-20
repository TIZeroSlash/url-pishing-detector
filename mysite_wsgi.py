import sys

# Add your project directory to the sys.path
project_home = u'/home/TIZeroSlash/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Import Flask app but need to call it "application" for WSGI to work
from app import app as application 

# first app is the main folder name
from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
from flask import Flask

app = Flask(__name__)

@app.route('/parser')
def hello_world():
    return 'Hello, World!'
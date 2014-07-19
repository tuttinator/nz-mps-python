from flask import Flask
app = Flask(__name__)

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
        db_session.remove()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

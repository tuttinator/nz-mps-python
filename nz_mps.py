from flask import Flask, jsonify
app = Flask(__name__)
# app.debug = True

from database import db_session
from models.mp import MP

@app.teardown_appcontext
def shutdown_session(exception=None):
        db_session.remove()

@app.route('/mps')
def index():
    mps = [m.as_json() for m in MP.query.all()]
    return jsonify(mps=mps)

@app.route('/mps/<mp_id>')
def show(mp_id):
    mp = MP.query.filter(User.id == mp_id).first().as_json()
    return jsonify(mp=mp)

if __name__ == '__main__':
    app.run()

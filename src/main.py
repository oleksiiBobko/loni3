from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

db.create_all()

@app.route("/", methods =['GET'])
def index():
    return "<h1>Decent.</p>"

@app.route('/items/<id>', methods=['GET'])
def get_item(id):
    item = Item.query.get(id)
    del item.__dict__['_sa_instance_state']
    return jsonify(item.__dict__)

@app.route('/items', methods=['GET'])
def get_items():
    items = []
    for item in db.session.query(Item).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
    body = request.get_json()
    db.session.add(Item(body['title'], body['content']))
    db.session.commit()
    return "item created"

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
    body = request.get_json()
    db.session.query(Item).filter_by(id=id).update(dict(title=body['title'], content=body['content']))
    db.session.commit()
    return "item updated"

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
    db.session.query(Item).filter_by(id=id).delete()
    db.session.commit()
    return "item deleted"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


if __name__ == "__main__":
    app.run(host='127.0.0.1', threaded=True)

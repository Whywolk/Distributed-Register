from flask import jsonify, request, abort
import hashlib

from server_app import app

#TODO Use SQLAlchemy and SQLite
users = []

def find_user(user: dict):
    for cur_user in users:
        if (user['login'] == cur_user['login'] and
            user['password'] == cur_user['password']):
            return True
    return False

@app.route('/users', methods=['GET'])
def get_all():
    return jsonify(users), 200

@app.route('/user', methods=['GET'])
def get():
    if not request.json or not 'password' in request.json:
        abort(400)
    user = {
        'login': request.json['login'],
        'password': request.json['password'].encode('utf-8')
    }
    print(user)
    user['password'] = hashlib.sha256(user['password']).hexdigest()

    if not find_user(user):
        abort(400)
    return jsonify(user), 200

@app.route('/user', methods=['POST'])
def add():
    if not request.json or not 'password' in request.json:
        abort(400)
    user = {
        'login': request.json['login'],
        'password': request.json['password'].encode('utf-8')
    }
    user['password'] = hashlib.sha256(user['password']).hexdigest()
    if find_user(user):
        abort(400)

    users.append(user)
    return jsonify(user), 201

@app.route('/user', methods=['DELETE'])
def delete():
    if not request.json or not 'password' in request.json:
        abort(400)
    user = {
        'login': request.json['login'],
        'password': request.json['password'].encode('utf-8')
    }
    user['password'] = hashlib.sha256(user['password']).hexdigest()
    if not find_user(user):
        abort(400)

    users.remove(user)
    return jsonify(success=True)


from flask import jsonify, request, abort
import hashlib
from server_app import app, db
from server_app.model import User



# def find_user(user: dict):
#     for cur_user in users:
#         if (user['login'] == cur_user['login'] and
#             user['password'] == cur_user['password']):
#             return True
#     return False

@app.route('/users', methods=['GET'])
def get_all():
    users = User.query.all()
    users = [user.to_json() for user in users]
    return jsonify(users), 200

# @app.route('/user', methods=['GET'])
# def get():
#     if not request.json or not 'password' in request.json:
#         abort(400)
#     user = {
#         'login': request.json['login'],
#         'password': request.json['password'].encode('utf-8')
#     }
#     print(user)
#     user['password'] = hashlib.sha256(user['password']).hexdigest()
#
#     if not find_user(user):
#         abort(400)
#     return jsonify(user), 200
#
@app.route('/user', methods=['POST'])
def add():
    if not request.json or not 'password' in request.json:
        abort(400)

    user = User(name=request.json['name'],
                password=hashlib.sha256(request.json['password'].encode('utf-8')).hexdigest())

    # if User.query.filter(user).one():
    #     abort(400)
    db.session.add(user)
    db.session.commit()
    return jsonify(), 201
#
# @app.route('/user', methods=['DELETE'])
# def delete():
#     if not request.json or not 'password' in request.json:
#         abort(400)
#     user = {
#         'login': request.json['login'],
#         'password': request.json['password'].encode('utf-8')
#     }
#     user['password'] = hashlib.sha256(user['password']).hexdigest()
#     if not find_user(user):
#         abort(400)
#
#     users.remove(user)
#     return jsonify(success=True)


from flask import jsonify, request, abort
from server_app import app, db
from server_app.model import User

@app.route('/api/users', methods=['GET'])
def api_get():
    users = User.query.all()
    users = [user.to_json() for user in users]
    return jsonify(users), 200

@app.route('/api/users', methods=['POST'])
def api_add():
    if not request.json or not 'password' in request.json \
                        or not 'name' in request.json\
                        or not 'uid' in request.json:
        abort(400)

    new_uid = 0
    old_uid_list = User.query.order_by(User.uid)
    if not old_uid_list:
        new_uid = old_uid_list.pop().uid + 1

    user = User(name=request.json['name'],
                password=request.json['password'],
                uid=request.json['uid'])

    # Somehow we got the same uid. Oops
    if user.uid == new_uid:
        abort(400)

    # We can't add users with the same name
    nickname = User.query.filter_by(name=user.name).first()
    if nickname is not None:
        abort(400)

    db.session.add(user)
    db.session.commit()

    return jsonify(), 201


@app.route('/api/users', methods=['DELETE'])
def api_delete():
    if not request.json or not 'uid' in request.json \
                        or not 'name' in request.json:
        abort(400)

    # User not found
    user = User.query.filter_by(uid=request.json['uid'], name=request.json['name']).first()
    if user is None:
        abort(400)

    db.session.delete(user)
    db.session.commit()

    return jsonify(), 201


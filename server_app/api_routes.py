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
        print("[DEBUG] request=" + str(request.json))
        abort(400)

    old_uid = 0
    old_uid_list = User.query.order_by(User.uid).all()
    if old_uid_list:
        old_uid = old_uid_list[-1].uid

    user = User(name=request.json['name'],
                password=request.json['password'],
                uid=request.json['uid'])

    # Somehow we got the same uid. Oops
    if user.uid == old_uid:
        print("[DEBUG] Same uids! request.uid=" + str(user.uid) + ", name=" + str(user.name)
              + ", old_uid=" + str(old_uid) + ", old name=" + str(old_uid_list[-1].name) + "oold uid=" +
              str(old_uid_list[-1].uid))
        abort(400)

    # We can't add users with the same name
    nickname = User.query.filter_by(name=user.name).first()
    if nickname is not None:
        print("[DEBUG] Same names! user.name=" + str(user.name))
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


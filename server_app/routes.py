#    This file is a part of Distributed-Register source code
#    Copyright (C) 2021  Authors:   Alex Shirshov <https://github.com/Whywolk>
#                                   w0rest <https://github.com/w0resT>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import jsonify, request, abort
import hashlib
from server_app import app, db, admin_password
from server_app.model import User
from server_app.service import Service


@app.route('/users', methods=['GET'])
def get_all():
    users = User.query.all()
    users = [user.to_json() for user in users]

    # Updating DB information
    another_users_list = Service.get()
    for another_user in another_users_list:
        for user_json in another_user:
            if User.query.filter_by(uid=user_json['uid']).first() is None:
                users.append(user_json)
                user = User(name=user_json['name'],
                            password=user_json['password'],
                            uid=user_json['uid'])
                db.session.add(user)
                db.session.commit()

                print('[ROUTE][GET] New UID added: ' + str(user_json['uid']))

    return jsonify(users), 200


@app.route('/user', methods=['GET'])
def get():
    if not request.json or not 'uid' in request.json:
        abort(400)

    # Updating DB information
    another_users_list = Service.get()
    for another_user in another_users_list:
        for user_json in another_user:
            if User.query.filter_by(uid=user_json['uid']).first() is None:
                user = User(name=user_json['name'],
                            password=user_json['password'],
                            uid=user_json['uid'])
                db.session.add(user)
                db.session.commit()

                print('[ROUTE][GET] New UID added: ' + str(user_json['uid']))

    # User not found
    user = User.query.filter_by(uid=request.json['uid']).first()
    if user is None:
        abort(400)

    return jsonify(user.to_json()), 200


@app.route('/user', methods=['POST'])
def add():
    if not request.json or not 'password' in request.json \
                        or not 'name' in request.json:
        abort(400)

    old_uid = 1
    old_uid_list = User.query.order_by(User.uid).all()
    if old_uid_list:
        old_uid = old_uid_list.pop().uid + 1

    user = User(name=request.json['name'],
                password=hashlib.sha256(request.json['password'].encode('utf-8')).hexdigest(),
                uid=old_uid)

    # We can't add users with the same name
    nickname = User.query.filter_by(name=user.name).first()
    if nickname is not None:
        abort(400)

    db.session.add(user)
    db.session.commit()
    Service.update(user.name, user.password, user.uid)

    return jsonify(), 201


@app.route('/user', methods=['DELETE'])
def delete():
    if not request.json or not 'uid' in request.json \
                        or not 'name' in request.json\
                        or not 'password' in request.json:
        abort(400)

    # Checking user permission for deleting users
    request_pass = hashlib.sha256(request.json['password'].encode('utf-8')).hexdigest()
    for admin_pass in admin_password:
        if request_pass != admin_pass:
            abort(403)

    # Updating DB information
    another_users_list = Service.get()
    for another_user in another_users_list:
        for user_json in another_user:
            if User.query.filter_by(uid=user_json['uid']).first() is None:
                user = User(name=user_json['name'],
                            password=user_json['password'],
                            uid=user_json['uid'])
                db.session.add(user)
                db.session.commit()

                print('[ROUTE][DELETE] New UID added: ' + str(user_json['uid']))

    # User not found
    user = User.query.filter_by(uid=request.json['uid'], name=request.json['name']).first()
    if user is None:
        abort(400)

    db.session.delete(user)
    db.session.commit()
    Service.delete(user.uid, user.name)

    return jsonify(), 201


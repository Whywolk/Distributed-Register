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

from server_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.name}')"

    def to_json(self):
        return {'id': self.id,
                'uid': self.uid,
                'name': self.name,
                'password': self.password}


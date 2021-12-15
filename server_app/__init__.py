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

import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


argc = len(sys.argv) - 1

if argc >= 4:
    if sys.argv[3] == 'db':
        db_name = sys.argv[4] + '.db'
else:
    db_name = 'sv1.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ok'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
db = SQLAlchemy(app)

ports_list = [5000, 5001, 5002]
if argc >= 2:
    ports_list.remove(int(sys.argv[2]))

admin_password = ['8005ad6755726d1289a2655dd52d9c1036563b75487b65973eb370938f1dbd8c']

from server_app import routes
from server_app import api_routes

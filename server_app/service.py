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

import requests
from flask import json
from server_app import ports_list


class Service:
    @staticmethod
    def update(username, password, uid):
        for port in ports_list:
            response = requests.post("http://localhost:" + str(port) + "/api/users",
                                     json={'name': username, 'password': password, 'uid': uid})

            if response.status_code == 201:
                print('[SERVER][POST] Synchronized with another servers')
            else:
                print('[SERVER][POST] Sync error!')

    @staticmethod
    def get():
        response_list = []
        for port in ports_list:
            response = requests.get("http://localhost:" + str(port) + "/api/users")
            if response.status_code == 200:
                print('[SERVER][GET] Synchronized with another servers')
            else:
                print('[SERVER][GET] Sync error!')

            data = json.loads(response.text)
            response_list.append(data)

        return response_list

    @staticmethod
    def delete(uid, username):
        for port in ports_list:
            response = requests.delete("http://localhost:" + str(port) + "/api/users",
                                       json={'uid': uid, 'name': username})

            if response.status_code == 201:
                print('[SERVER][DELETE] Synchronized with another servers')
            else:
                print('[SERVER][DELETE] Sync error!')

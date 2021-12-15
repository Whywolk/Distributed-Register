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

class HttpClient:
    def __init__(self):
        self.response = None

    def get_users(self, port):
        try:
            self.response = requests.get("http://localhost:" + port + "/users")
        except:
            pass

    def get_user(self, port, uid):
        try:
            self.response = requests.get("http://localhost:" + port + "/user",
                                         json={'uid': uid})
        except:
            pass

    def create(self, port, name, password):
        try:
            self.response = requests.post("http://localhost:" + port + "/user",
                                          json={'name': name,
                                                'password': password})
        except:
            pass

    def delete(self ,port, uid, name, password):
        try:
            self.response = requests.delete("http://localhost:" + port + "/user",
                                            json={'uid': uid,
                                                  'name': name,
                                                  'password': password})
        except:
            pass

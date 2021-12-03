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

import sys, requests
from server_app import ports_list

class Service:
    def update(username, password, uid):
        for port in ports_list:
            response = requests.post("http://localhost:" + str(port) + "/api/users",
                                     json={'name': username, 'password': password, 'uid': uid})

            print('[SERVER] Synchronized with another servers')
            #print("[Server]" + str(response.status_code) + response.headers)
            #print("[Server]" + response.text)
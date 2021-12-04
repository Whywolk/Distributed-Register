import requests

class HttpClient:
    def __init__(self):
        self.response = None

    def get_users(self, port):
        self.response = requests.get("http://localhost:" + port + "/users")

    def get_user(self, port, uid):
        self.response = requests.get("http://localhost:" + port + "/user",
                                     json={'uid': uid})

    def create(self, port, name, password):
        self.response = requests.post("http://localhost:" + port + "/user",
                                      json={'name': name, 'password': password})

    def delete(self ,port, uid, name, password):
        self.response = requests.delete("http://localhost:" + port + "/user",
                                       json={'uid': uid,
                                             'name': name,
                                             'password': password})

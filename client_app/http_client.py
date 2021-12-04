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

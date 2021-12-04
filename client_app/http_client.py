import requests

class HttpClient:
    @staticmethod
    def get_users(port):
        response = requests.get("http://localhost:" + port + "/users")
        return response

    @staticmethod
    def get_user(port, uid):
        response = requests.get("http://localhost:" + port + "/user",
                                json={'uid': uid})
        return response

    @staticmethod
    def create(port, name, password):
        response = requests.post("http://localhost:" + port + "/user",
                                 json={'name': name, 'password': password})
        return response

    @staticmethod
    def delete(port, uid, name, password):
        response = requests.delete("http://localhost:" + port + "/user",
                                   json={'uid': uid,
                                         'name': name,
                                         'password': password})
        return response

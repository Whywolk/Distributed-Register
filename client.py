import sys, requests

if __name__ == "__main__":
    response = 0
    if sys.argv[1] == 'get':
        response = requests.get("http://localhost:8082/user",
                                json={'name': sys.argv[2], 'password': sys.argv[3]})
    elif sys.argv[1] == 'post':
        response = requests.post("http://localhost:8082/user",
                                 json={'name': sys.argv[2], 'password': sys.argv[3]})
    elif sys.argv[1] == 'delete':
        response = requests.delete("http://localhost:8082/user",
                                   json={'name': sys.argv[2], 'password': sys.argv[3]})

    print(response.status_code, response.headers)
    print(response.text)
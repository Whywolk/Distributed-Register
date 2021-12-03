import requests
import sys

if __name__ == "__main__":
    response = None
    server_port = 5000
    argc = len(sys.argv) - 1

    try:
        # Requests func
        if sys.argv[1] == 'port':
            if argc >= 2:
                server_port = sys.argv[2]

            if argc >= 3 and sys.argv[3] == 'get':
                # port 500x get all
                if argc == 3:
                    response = requests.get("http://localhost:" + server_port + "/users")

                # port 500x get uid
                elif argc == 4:
                    response = requests.get("http://localhost:" + server_port + "/user",
                                            json={'uid': sys.argv[4]})

            # port 500x post username password
            elif argc >= 5 and sys.argv[3] == 'post':
                response = requests.post("http://localhost:" + server_port + "/user",
                                         json={'name': sys.argv[4], 'password': sys.argv[5]})

            # port 500x delete uid username
            elif argc >= 6 and sys.argv[3] == 'delete':
                response = requests.delete("http://localhost:" + server_port + "/user",
                                           json={'uid': sys.argv[4],
                                                 'name': sys.argv[5],
                                                 'password': sys.argv[6]})
            else:
                print("[Error] Bad arguments bro. Using: port 500x get/post/delete ...")
        else:
            print("[Error] Bad arguments bro. Using: port 500x ...")
    except Exception as error:
        print("[Exception error] " + str(error))


    if response is not None:
        print(response.status_code, response.headers)
        print(response.text)

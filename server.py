import sys
from server_app import app

if __name__ == '__main__':
    if sys.argv[1] == 'port':
        app.run(debug=True, host='localhost', port=sys.argv[2])
    else:
        app.run(debug=True, host='localhost', port=5000)
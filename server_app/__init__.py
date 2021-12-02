from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

if sys.argv[3] == 'db':
    db_name = sys.argv[4] + '.db'
else:
    db_name = 'sv1.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ok'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

ports_list = [5000, 5001, 5003]
ports_list.remove(int(sys.argv[2]))

from server_app import routes

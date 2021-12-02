from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# db_name = sys.argv[1]
db_name = 'sv1.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ok'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

from server_app import routes

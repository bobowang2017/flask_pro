from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print("Hello World")


if __name__ == '__main__':
    manager.run()

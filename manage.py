import sys
from main import app,db
from views import *
from model import *
from flask_script import Manager
manager=Manager(app)
from flask_migrate import MigrateCommand

#migrate
# @manager.command
# def migrate():
#     db.create_all()
manager.add_command("db",MigrateCommand)



# command=sys.argv[1]
# if command == 'runserver':
#     app.run()
# elif command == "migrate":
#     db.create_all()
if __name__ == '__main__':
    manager.run()

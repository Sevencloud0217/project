import sys
from main import app,db
from views import *
from model import *
from flask_script import Manager
manager=Manager(app)

#migrate
@manager.command
def migrate():
    db.create_all()

# command=sys.argv[1]
# if command == 'runserver':
#     app.run()
# elif command == "migrate":
#     db.create_all()
if __name__ == '__main__':
    manager.run()

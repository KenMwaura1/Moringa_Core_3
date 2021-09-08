from app import create_app
from flask_script import Manager, Server

# creating app instance
app = create_app('development')

manager = Manager(app)
server = Server(host='localhost', port=8096)
manager.add_command('server', server)

if __name__ == '__main__':
    manager.run()

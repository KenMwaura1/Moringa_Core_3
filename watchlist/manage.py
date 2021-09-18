from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Role, Review

# creating app instance
app = create_app('development')
manager = Manager(app)
server = Server(host='localhost', port=8190, use_debugger=True, use_reloader=True)
migrate = Migrate(app, db)
manager.add_command('server', server)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """
    function to run the unit tests
    :return: status of the tests run
    """
    import unittest
    test_app = create_app('test')
    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_DATABASE_URI'] = test_app.config['SQLALCHEMY_DATABASE_URI']
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


if __name__ == '__main__':
    manager.run()

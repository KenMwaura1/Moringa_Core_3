from app import create_app
from flask_script import Manager, Server

# creating app instance
app = create_app('development')

manager = Manager(app)
server = Server(host='localhost', port=8096)
manager.add_command('server', server)


@manager.command
def test():
    """
    function to run the unit tests
    :return:
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()

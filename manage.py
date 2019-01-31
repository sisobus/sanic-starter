from manager import Manager
from api.app import create_app

manager = Manager()


@manager.command
def run():
    create_app()


if __name__ == '__main__':
    manager.main()

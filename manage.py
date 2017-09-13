from flask_script import Server, Manager
# from flask_migrate import Migrate, MigrateCommand

from application.app import app
import logging

manager = Manager(app)
# manager.add_command("runserver", Server(host="0.0.0.0", port=5000, ssl_crt='/Users/biao/Documents/myprojects/payment-redis/myselfsigned.cer', ssl_key='/Users/biao/Documents/myprojects/payment-redis/myselfsigned.key'))
# migrations
# manager.add_command('db', MigrateCommand)


# @manager.command
# def create_db():
#     """Creates the db tables."""
#     db.create_all()


if __name__ == '__main__':
    manager.run()
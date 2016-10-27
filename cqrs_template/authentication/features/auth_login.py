from flask import request

from cqrs_template.mediator import Mediator
from cqrs_template.helpers.jsonify import jsonify

from cqrs_template.authentication import authentication
from cqrs_template.authentication.sqlite_context import Session
from cqrs_template.authentication.models.user import User

mediator = Mediator()


@authentication.route('/token', methods=['POST'])
@jsonify
def auth_login():
    json = request.get_json()
    return mediator.signal("auth_login", json)


def handler(message):
    session = Session()

    new_user = User(name=message.name, fullname=message.fullname, password=message.password)

    session.add(new_user)

    session.commit()
    session.close()


mediator.connect("auth_login", handler)


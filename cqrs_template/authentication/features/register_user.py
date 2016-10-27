from flask import request

from cqrs_template.mediator import Mediator
from cqrs_template.helpers.jsonify import jsonify

from cqrs_template.authentication import authentication
from cqrs_template.authentication.sqlite_context import Session
from cqrs_template.authentication.models.user import User

mediator = Mediator()


@authentication.route('/register/<guid>', methods=['POST'])
@jsonify
def register_user(guid):
    json = request.get_json()
    json.guid = guid

    return mediator.signal("register_user", json)


def handler(message):
    session = Session()

    new_user = User(name=message.name, fullname=message.fullname, password=message.password)

    session.add(new_user)

    session.commit()
    session.close()


mediator.connect("register_user", handler)

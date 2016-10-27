from flask import Blueprint

authentication = Blueprint('authentication', __name__)

from .features.auth_login import *
from .features.register_user import *
from datetime import datetime
from graphql_jwt.settings import jwt_settings


def compare_password(password1, password2):
    if password1 == password2:
        return True
    else:
        return False

def jwt_payload(user, context=None):
    jwt_datetime = datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA
    jwt_expires = int(jwt_datetime.timestamp())
    payload = {}
    payload['username'] = str(user.username) # For library compatibility
    payload['id'] = str(user.id)
    payload['email'] = user.email
    payload['exp'] = jwt_expires
    return payload
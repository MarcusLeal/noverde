import os
from datetime import datetime, timedelta
from jwt import encode
from flask import current_app


def create_token(client_id, expiration_time=None):
    if not expiration_time:
        expiration_time = current_app.config['JWT_EXP_DELTA_SECONDS_ECOMMERCE']
    expiration = datetime.utcnow() + timedelta(seconds=expiration_time)
    token = encode({'client_id': client_id,
                    'exp': expiration}, 'secret',
                   algorithm='HS256').decode('utf8')
    return token

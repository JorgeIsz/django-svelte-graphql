import jwt
import datetime

from server.settings import JWT_SECRET_KEY

def get_tokens(pk):
    now = datetime.datetime.utcnow()
    payload = {
        'uid': pk,
        'iat': now
    }

    def generate_token(**kwargs):
        payload['exp'] = now + datetime.timedelta(**kwargs)
        return jwt.encode(payload, key=JWT_SECRET_KEY, algorithm='HS256') 

    access_token = generate_token(minutes=15)
    refresh_token = generate_token(days=365)

    return (access_token, refresh_token)

def get_payload(token):
    return jwt.decode(token, key=JWT_SECRET_KEY, algorithms=['HS256',])

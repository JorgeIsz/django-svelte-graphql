import jwt
import datetime

secret = 'secret'


def get_tokens(pk):
    now = datetime.datetime.utcnow()
    payload = {
        'uid': pk,
        'iat': now
    }

    def generate_token(**kwargs):
        payload['exp'] = now + datetime.timedelta(**kwargs)
        return jwt.encode(payload, key=secret, algorithm='HS256') 

    access_token = generate_token(minutes=15)
    refresh_token = generate_token(days=365)

    return (access_token, refresh_token)

def get_payload(token):
    return jwt.decode(token, key=secret, algorithms=['HS256',])

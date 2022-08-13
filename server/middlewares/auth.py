from api.models import User
from api.tokens import get_payload

def get_user_by_token(token):
    payload = get_payload(token)
    return User.objects.get(pk=payload['uid'])


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.user.is_authenticated:
            try:
                auth_header = request.META.get("HTTP_AUTHORIZATION")
                _, token = auth_header.split()
                request.user = get_user_by_token(token)
            except Exception as e:
                pass
            
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
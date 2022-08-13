import functools


def auth_required(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        user = kwargs["info"].context.request.user
        if user.is_authenticated:
            return func(*args, **kwargs)
        
        raise Exception("Not authenticated")

    return inner                              

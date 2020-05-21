from functools import wraps
from django.contrib import auth
from django.shortcuts import redirect


def graphic_key(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        request = __find_request(*args)
        if 'graphic_key' in request.session and request.session['graphic_key']:
            return view(*args, **kwargs)
        return redirect('accounts:graphic_key')
    return wrapper

# is not decorator
def __find_request(*args):
    for arg in args:
        if type(arg).__name__ == 'WSGIRequest':
            return arg
    return None
from functools import wraps
from django.contrib import auth
from django.shortcuts import redirect
from utils.shortcuts import iredirect


def graphic_key(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        request = __find_request(*args)
        if not request.user.is_authenticated:
            return view(*args, **kwargs)
        if not request.user.gr_key:
            return iredirect('accounts:graphic_key', get={'status': 'new'})
        if 'graphic_key' in request.session:
            if type(request.session['graphic_key']) == str:
                return iredirect('accounts:graphic_key', get={'status': 'confirm'})
            return view(*args, **kwargs)
        return iredirect('accounts:graphic_key')
    return wrapper

# is not decorator
def __find_request(*args):
    for arg in args:
        if type(arg).__name__ == 'WSGIRequest':
            return arg
    return None
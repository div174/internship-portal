from django.shortcuts import redirect
from django.contrib import messages

def superuser_required(view_func):
    """
    Decorator to check if user is a superuser.
    If not logged in, redirect to login.
    If logged in but not a superuser, show error and redirect.
    """
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if not request.user.is_superuser:
            messages.error(request, 'You do not have permission to access the dashboard.')
            return redirect('index')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

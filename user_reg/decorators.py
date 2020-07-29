from django.shortcuts import redirect



def login_checker(function):
    def wrapper(request, *args,**kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return function(request, *args, **kwargs)
    
    return wrapper
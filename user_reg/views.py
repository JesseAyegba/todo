from django.shortcuts import render, redirect
from . forms import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_registration(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, f"Account Successfully created")
            form.save()
            return redirect("login")
            
    form = CreateUserForm()
    context = {
        "form": form,
    }
    return render(request, "user_reg/user_registration.htm", context)

def login_page(request):
    form = UserLoginForm()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")

    context = {
        "form": form,
    }
    return render(request, "user_reg/login.htm", context)

def logout_page(request):
    logout(request)
    return render(request, "user_reg/logout.htm")

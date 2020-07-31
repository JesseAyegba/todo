from django.shortcuts import render, redirect
from . forms import CreateUserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . decorators import login_checker



@login_checker
def user_registration(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, f"Account Successfully created. You can now login")
            form.save()
            return redirect("login")
    else:        
        form = CreateUserForm()

    context = {
        "form": form,
    }
    return render(request, "user_reg/user_registration.htm", context)


@login_checker
def login_page(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
    else: 
        form = UserLoginForm()
    context = {
        "form": form,
    }
    return render(request, "user_reg/login.htm", context)

def logout_page(request):
    logout(request)
    return render(request, "user_reg/logout.htm")

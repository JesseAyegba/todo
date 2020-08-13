from secrets import token_hex

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import Http404

from user_reg.decorators import login_checker
from . models import Todo
from . forms import TodoForm, TodoForm2






@login_checker
def landing(request):
    return render(request, "landing.html")


@login_required(login_url="login")
def home(request):
    form = TodoForm2()
    token = str(token_hex())[0:10]
    items = Todo.objects.filter(user=request.user).order_by("-date_created")
    items_count = Todo.objects.filter(user=request.user).count()
    checker = False
    if items_count >= 2:
        checker = True


    if request.method == "POST":
        form = TodoForm2(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            ins = Todo.objects.create(user=request.user, item=item, ran_id=token, date_created=timezone.now())
            return redirect("home")
    context = {
        "items": items,
        "checker": checker,
        "form": form
    }
    return render(request, "index.html", context)


@login_required(login_url="login")
def delete_item(request, item_id):
    try:
        item = Todo.objects.get(ran_id=item_id)
    except Exception:
        raise Http404("You don't seem to have such item in your record")
    item.delete()
    return redirect("home")


@login_required(login_url="login")
def update_item(request, item_id):
    try:
        todo_item = Todo.objects.get(ran_id=item_id)
    except Exception:
        raise Http404("You don't seem to have such item in your record")
    form = TodoForm(instance=todo_item)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, f"Update Successful")
            return redirect("home")
    context = {
        "form": form
    }
    return render(request, "update.html", context)


@login_required(login_url="login")
def clear_list(request):
    user = request.user
    user_item_set = user.todo_set.all()
    user_item_set.delete()
    return redirect("home")
    
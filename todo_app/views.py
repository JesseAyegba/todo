from django.shortcuts import render, redirect
from . models import Todo
from . forms import TodoForm, TodoForm2
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from user_reg.decorators import login_checker



@login_checker
def landing(request):
    return render(request, "todo_app/landing.htm")


@login_required(login_url="login")
def home(request):
    form = TodoForm2()
    items = Todo.objects.filter(user=request.user).order_by("-date_created")
    items_count = Todo.objects.filter(user=request.user).count()
    checker = False
    if items_count >= 2:
        checker = True


    if request.method == "POST":
        form = TodoForm2(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            ins = Todo.objects.create(user=request.user, item=item, date_created=timezone.now())
            return redirect("home")
    context = {
        "items": items,
        "checker": checker,
        "form": form
    }
    return render(request, "todo_app/index.htm", context)


@login_required(login_url="login")
def delete_item(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    return redirect("home")


@login_required(login_url="login")
def update_item(request, item_id):
    todo_item = Todo.objects.get(id=item_id)
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
    return render(request, "todo_app/update.htm", context)


@login_required(login_url="login")
def clear_list(request):
    user = request.user
    user_item_set = user.todo_set.all()
    user_item_set.delete()
    return redirect("home")
    
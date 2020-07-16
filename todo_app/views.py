from django.shortcuts import render, redirect


def home(request):
    return render(request, "todo_app/index.htm")
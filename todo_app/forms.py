from django import forms
from django.forms import ModelForm
from . models import Todo


class TodoForm(ModelForm):
    item = forms.CharField(max_length=100, label="" ,widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Update Item...",
    }))
    
    class Meta: 
        model = Todo
        fields = ["item"]



class TodoForm2(ModelForm):
    item = forms.CharField(max_length=100, label="" ,widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Add Item...",
    }))
    
    class Meta: 
        model = Todo
        fields = ["item"]

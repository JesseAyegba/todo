from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from . models import Profile



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 4:
            raise ValidationError("Your username is too short")
        else: 
            return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        for instance in User.objects.all():
            if instance.email == email:
                raise ValidationError("This email already exists")

        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        all_users = User.objects.all()


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "picture"]







        


        


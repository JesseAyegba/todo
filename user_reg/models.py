from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    picture = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user} Profile"



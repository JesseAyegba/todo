from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=40, blank=False, null=True)
    ran_id = models.CharField(max_length=50, primary_key=True, default=uuid4())
    date_created = models.DateTimeField("date created", null=True)

    def __str__(self):
        return self.item




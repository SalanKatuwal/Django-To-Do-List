from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.TextField(max_length=500)
    status = models.BooleanField(default=False)

from django.db import models

from User.models import User


# Create your models here.
class History(models.Model):
    content = models.CharField(max_length=1024)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

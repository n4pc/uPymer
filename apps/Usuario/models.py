from django.db import models
from django.contrib.auth.models import User
from apps.Pymes.models import Pyme
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pyme = models.ForeignKey(Pyme, on_delete=models.CASCADE)
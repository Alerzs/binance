from django.db import models
from django.contrib.auth.models import User

class Shart(models.Model):
    arz = models.CharField(max_length=3)
    price = models.IntegerField()
    user = models.ForeignKey(User)



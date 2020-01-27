from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Function(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    function_text = models.CharField(max_length=200)
    interval = models.FloatField()
    step = models.FloatField()
    graph = models.ImageField()
    date = models.DateTimeField()

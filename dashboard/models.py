from django.db import models
from django.contrib.auth.models import User

# Create your models here.

import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
import datetime


def plot_graph(function_id):
    func = Function.objects.get(id=function_id)
    now = func.date
    delta = datetime.timedelta(days=func.interval)
    previous_date = now - delta
    second_posix_date = now.timestamp()
    first_posix_date = previous_date.timestamp()
    step = func.step * 60 * 60
    t = np.arange(first_posix_date, second_posix_date, step)
    y = ne.evaluate(func.function_text)
    plt.plot(t, y)
    plt.show()


class Function(models.Model):
    function_text = models.CharField(max_length=200)
    interval = models.FloatField()
    step = models.FloatField()
    graph = models.ImageField(blank=True)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #plot_graph(self.id)

    def __str__(self):
        return self.function_text

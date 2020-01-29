from django.db import models
from django.contrib.auth.models import User

# Create your models here.

import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
import datetime
import io
from django.core.files.images import ImageFile
from django.utils.html import mark_safe


class Function(models.Model):
    function_text = models.CharField(max_length=200)
    interval = models.IntegerField()
    step = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.function_text

    def plotter(self):
        now = self.date
        delta = datetime.timedelta(days=self.interval)
        previous_date = now - delta
        second_posix_date = now.timestamp()
        first_posix_date = previous_date.timestamp()
        step = self.step * 60 * 60

        t = np.arange(first_posix_date, second_posix_date, step)
        y = ne.evaluate(self.function_text)

        figure = io.BytesIO()
        plt.plot(t, y)
        plt.savefig(figure, format='png')
        content_file = ImageFile(figure)
        self.image.save(f'{now}' + '.png', content_file)
        self.save()
        plt.close()

    def image_tag(self):
        return mark_safe('<img src="%s" width="250" />' % self.image.url)
    image_tag.short_description = 'image'

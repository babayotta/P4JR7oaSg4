from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe


class Function(models.Model):
    function_text = models.CharField(max_length=100)
    interval = models.IntegerField()
    step = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    date = models.DateTimeField(auto_now=True)
    exception_text = models.CharField(blank=True, null=True, max_length=300)

    def __str__(self):
        return f'{self.function_text} - {self.interval} - {self.step}'

    # https://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
    def image_tag(self):
        if self.exception_text:
            return mark_safe('<p>%s</p>' % self.exception_text)
        elif self.image:
            return mark_safe('<img src="%s" width="250" />' % self.image.url)
    image_tag.short_description = 'image'

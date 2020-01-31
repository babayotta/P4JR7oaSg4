from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.


class Function(models.Model):
    function_text = models.CharField(max_length=200)
    interval = models.IntegerField()
    step = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.function_text} - {self.interval} - {self.step}'

    def save(self, generate_image=True, *args, **kwargs):
        super().save(*args, **kwargs)
        if generate_image:
            from .tasks import plotter
            from django.db import transaction
            # https://stackoverflow.com/questions/53901462/where-to-call-a-celery-task-on-model-save
            transaction.on_commit(lambda: plotter.delay(self.id))

    # https://stackoverflow.com/questions/16307307/django-admin-show-image-from-imagefield
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="250" />' % self.image.url)
    image_tag.short_description = 'image'

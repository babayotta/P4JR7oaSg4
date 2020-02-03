import datetime
import io
import numpy as np
import numexpr as ne
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
from celery import shared_task
from .models import Function


@shared_task
def plotter(function_id):
    func = Function.objects.get(id=function_id)
    now = func.date
    delta = datetime.timedelta(days=func.interval)
    previous_date = now - delta
    second_posix_date = now.timestamp()
    first_posix_date = previous_date.timestamp()
    step = func.step * 60 * 60

    t = np.arange(first_posix_date, second_posix_date, step)
    y = ne.evaluate(func.function_text)

    figure = io.BytesIO()
    plt.plot(t, y)
    plt.savefig(figure, format='png')
    content_file = ImageFile(figure)
    func.image.save(f'{now}' + '.png', content_file)
    func.save()
    plt.close()

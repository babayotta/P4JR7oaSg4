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
    try:
        func.image.delete()
        func.exception_text = ''

        now = func.date
        delta = datetime.timedelta(days=func.interval)
        previous_date = now - delta
        second_posix_date = now.timestamp()
        first_posix_date = previous_date.timestamp()
        step = func.step * 60 * 60

        t = np.arange(first_posix_date, second_posix_date, step)
        y = ne.evaluate(func.function_text)

        figure = io.BytesIO()

        plt.figure(figsize=(20, 10))
        plt.title(f'{func.function_text}')
        plt.xlabel('t')
        plt.ylabel('f(t)')
        plt.grid()
        plt.plot(t, y, 'o-')
        plt.savefig(figure, format='png')
        plt.close()

        func.image.save(f'{now}' + '.png', ImageFile(figure))
        func.save()

    except Exception as e:
        func.exception_text = e
        func.save()

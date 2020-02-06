from django.contrib import admin
from django.db import transaction
from .models import Function
from .tasks import plotter


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    exclude = [
        'image',
        'exception_text',
    ]
    readonly_fields = (
        'id',
        'date',
        'image_tag',
    )
    list_display = (
        'id',
        'function_text',
        'image_tag',
        'interval',
        'step',
        'date',
    )

    def response_add(self, request, obj, post_url_continue=None):
        transaction.on_commit(lambda: plot_and_wait(obj.id))
        return super().response_add(request, obj, post_url_continue=None)

    def response_change(self, request, obj):
        transaction.on_commit(lambda: plot_and_wait(obj.id))
        return super().response_change(request, obj)


def plot_and_wait(function_id):
    result = plotter.delay(function_id)
    result.wait(timeout=10, interval=1)

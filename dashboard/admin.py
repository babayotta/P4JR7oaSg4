from django.contrib import admin
from django.db import transaction
from .models import Function
from .tasks import plotter


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    exclude = [
        'image',
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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # https://stackoverflow.com/questions/53901462/where-to-call-a-celery-task-on-model-save
        transaction.on_commit(lambda: plotter.delay(obj.id))


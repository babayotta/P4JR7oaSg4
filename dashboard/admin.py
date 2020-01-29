from django.contrib import admin
from .models import Function

# Register your models here.


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

from django.contrib import admin
from .models import Function

# Register your models here.


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
        'date',
        'image',
    )
    list_display = (
        'id',
        'function_text',
        'image',
        'interval',
        'step',
        'date',
    )

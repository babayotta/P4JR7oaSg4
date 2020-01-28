from django.contrib import admin
from .models import Function

# Register your models here.


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'function_text',
        'graph',
        'interval',
        'step',
        'date',
    )

from django.contrib import admin
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)

class Todo(admin.ModelAdmin):
    list_display = ['content']


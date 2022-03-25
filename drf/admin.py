from django.contrib import admin
from drf.models import Todo


# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Todo, TodoAdmin)

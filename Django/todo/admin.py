from django.contrib import admin
from .models import ToDo

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "desc")

admin.site.register(ToDo, DataAdmin)

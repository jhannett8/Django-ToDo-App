from django.contrib import admin

# Register your models here.
from .models import Task_model


admin.site.register(Task_model)

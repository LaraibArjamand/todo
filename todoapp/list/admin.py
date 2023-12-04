from django.contrib import admin

from .models import List, Task

admin.site.register(Task)
admin.site.register(List)

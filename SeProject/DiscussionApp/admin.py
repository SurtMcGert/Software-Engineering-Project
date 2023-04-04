from django.contrib import admin

from .models import Chat, Discussion

# Register your models here.
admin.site.register(Discussion)
admin.site.register(Chat)
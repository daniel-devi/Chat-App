from django.contrib import admin
from .models import ChatRoom,Message

# Register your models here.
models = [ChatRoom,Message]
admin.site.register(models)
from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import uuid
# Create your models here.
# models.py

class ChatRoom(models.Model):
    name = models.TextField()
    room_id = models.UUIDField(primary_key=True, default=uuid4, editable=True)
    participants = models.ManyToManyField(User, related_name='chat_room')
    date_created = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='creator')
    admins = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, related_name='admins')
    
    def save(self, *args, **kwargs):
        if not self.room_id:
            self.room_id = uuid.uuid4()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'Chat Room : {self.name}-{self.room_id}'

    

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, to_field="username")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.id} to room {self.chatroom.name}'

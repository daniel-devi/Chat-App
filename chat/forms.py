from django.forms import ModelForm
from chat.models import Message,ChatRoom
from django import forms
# Create the form class.
class MessageForm(ModelForm):
   class Meta:
        model = Message
        fields = ['content']
         
         
         
class RoomCreateForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }

class RoomEditForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name', 'participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }
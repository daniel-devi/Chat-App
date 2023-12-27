from django.urls import path
from . import views

# Paths

urlpatterns = [
    path('', views.home, name='home'),
    path('create/chatroom', views.createRoom, name='create_room'),
    path('chat/<uuid:room_id>/', views.chat_room, name='chat_room'),
    path('search/', views.search_view, name='search'),
    path('getMessages/<uuid:room_id>/', views.getMessages, name='getMessages'),
    path('chat/chatbot', views.chatbot, name='chatbot'),
]


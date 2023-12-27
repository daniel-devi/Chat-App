from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.db.models import Q
from django.urls import reverse
from .forms import MessageForm,RoomCreateForm,RoomEditForm
from  django.contrib import messages

# Create your views here.
def home(request):
    chatroom = ChatRoom.objects.all()
    context = {
        'chatrooms':chatroom,
    }
    return render(request, 'chat/home-page.html',context)


def search_view(request):
    name = request.GET.get('name', '')
    instances = ChatRoom.objects.filter(Q(name__icontains=name))
    count = ChatRoom.objects.filter(Q(name__icontains=name)).count()
    context = {
       'instances': instances,
       'query':name,
       'count':count,
       
    }
    return render(request, 'chat/search.html', context)


@login_required
def createRoom(request):
    form = RoomCreateForm
    if request.method == "POST":
        form = RoomCreateForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.admins = request.user
            instance.save()
            messages.success(request, 'Your Group was Created')
            return redirect('home')
        else:
            messages.error(request, 'Error happened')
    else:
        form = RoomCreateForm()

    context = {
        'form':form
    }
    return render(request, 'chat/createform.html', context)



@login_required
def edit_chatroom(request, chatroom_id):
    chatroom= ChatRoom.objects.get(id=chatroom_id)
    if request.method == 'POST':
        form = RoomEditForm(request.POST, instance=chatroom)
        if form.is_valid():
            form.save()
            return redirect('', roomid=chatroom_id)
    else:
        form = RoomEditForm(instance=chatroom)
    return render(request, 'edit_blogpost.html', {'form': form})




@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, room_id=room_id)
    id = room_id
    participants = room.participants
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            room = get_object_or_404(ChatRoom, room_id=room_id)   
            message.chatroom = room
            message.save()
        else:
            messages.error(request, ('Error happened'))
            
    else:
        form = MessageForm()
        
    context = {
        'room': room, 
        'id':id,
        'form':form,
        'members':participants
    }
    return render(request, 'chat/chat_room.html', context)


def getMessages(request, room_id):
    room = get_object_or_404(ChatRoom, room_id=room_id)
    messages = Message.objects.filter(chatroom=room)
    return JsonResponse({"messages":list(messages.values())})


@login_required
def chatbot(request):
    context = {}
    return render(request, 'chat/chatbot.html', context)

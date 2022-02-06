from django.shortcuts import render ,HttpResponse
from django.contrib.auth.models import User
from Main.models import Message
from django.db.models import Q
from Main.views import get_notifications
# Create your views here.

def chats(request,username=None):
    id = request.user.id
    notifications,count = get_notifications(id)
    user = User.objects.get(id=id)
    chat_users = Message.objects.all().filter(Q(sender_id = user) | Q(reciever_id = user))
    user_list = []
    for chat in chat_users:
        if(chat.sender_id != user and chat.sender_id not in user_list):
            user_list.append(chat.sender_id)
        if(chat.reciever_id != user and chat.reciever_id not in user_list):
            user_list.append(chat.reciever_id)
    if username:
        user0 = User.objects.get(username=username)
        sent_messages = Message.objects.all().filter(sender_id = user , reciever_id = user0)
        recieved_messages = Message.objects.all().filter(sender_id = user0 , reciever_id = user)
        chats = []
        for i in sent_messages:
            x = {'sent':i.message}
            chats.append(x)
        for i in recieved_messages:
            x = {'recieved':i.message}
            chats.append(x)
        return render(request,'message.html',{'user0':user0,'user_list':user_list,'chats':chats,'notifications':notifications,'count':count})
    else:
        return render(request,'message.html',{'user_list':user_list,'notifications':notifications,'count':count})
    

def message(request,username):
    user0 = User.objects.get(username=username)
    id= request.user.id
    if request.method == "POST":
        
        usr=User.objects.get(id=id)
        usr2=User.objects.get(username=username)
        message =request.POST['message']
        message1 = Message.objects.create(sender_id=usr,reciever_id=usr2,message=message)
        message1.save()
        return HttpResponse(message)
    else:
        notifications,count=get_notifications(id)
        return render(request,'message.html',{'user0':user0,'notifications':notifications,'count':count})
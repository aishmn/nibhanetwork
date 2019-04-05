from django.shortcuts import render, redirect
from posts.models import Message
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your views here.
def send_message(request):
    if request.method == "POST":
        user = request.user
        sender_profile = Profile.objects.get(user=user)
        message = request.POST.get('message')
        reciever = request.POST.get('reciever')
        print('message')
        print(message)
        try:
            reciever_user = User.objects.get(username = str(reciever))
        except:
            messages.success(request, 'Wrong Username')
            return redirect('user-profile')
        reciever_profile = Profile.objects.get(user=reciever_user)
        try:
            message = Message.objects.get(send_to=reciever_profile)
        except:
            message = Message(send_to = reciever_profile)
        if message:
            message.body = request.POST.get('message')
            message.date = datetime.now()
            message.send_by = sender_profile
            message.save()
            messages.success(request, 'Messages Succesfully Sent')
            return redirect('user-profile')
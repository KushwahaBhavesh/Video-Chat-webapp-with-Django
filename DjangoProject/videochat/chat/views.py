from django.shortcuts import render,redirect
from .models import Chat

# Create your views here.
def index(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        if room:
            get_room = Chat.objects.filter(room_name=room).first()
            if get_room:
                if int(get_room.allowed_users) <= 2:
                    get_room.allowed_users=2
                    get_room.save()
                    return redirect(f'/chat/{room}/')
                else:
                    return render(request,'chat/room_full.html',{'room_name':room})
            else:
                created_room = Chat.objects.create(room_name=room, allowed_users=1)
                if created_room:
                    return redirect(f'/chat/{room}/')
        else:
            return render(request, 'chat/invalid_room.html')
    return render(request,'chat/index.html')

def room(request,room_name):
    return render(request,"chat/room.html", {"room_name": room_name})

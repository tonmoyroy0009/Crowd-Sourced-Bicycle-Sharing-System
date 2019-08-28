from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from cycles.models import Cycle
#from pickcycles.models import Pickcycle

# Create your views here.

def pickcycle(request):
    allcycle = Cycle.objects.all()
    #allpickcycle = Pickcycle.objects.all()
    
    if request.method == 'POST':
        
        message = 'cycle id:' + request.POST['EnterCycleId'] + ', location id:' + request.POST['EnterLocationId'] 
        owner= Cycle.objects.get(id = request.POST['EnterCycleId'] ).OwnerId.email
        send_mail('Pick Cycle',
        message,
        settings.EMAIL_HOST_USER,
        ['mrahman111213@gmail.com',owner],
        fail_silently=False
        )
    return render(request, 'pickcycles/pickcycle.html', {'allcycle':allcycle})



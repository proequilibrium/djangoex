from django.shortcuts import render
from django.http import HttpResponse

from .models import Event
#def index(request):
#    return HttpResponse("Nazdar")

from django.shortcuts import render

def index(request):

    return render(request, 'events/index.html')

def event_listing(request):

    events = Event.objects.all()

    return render(request, 'events/event_listing.html', {'events': events})

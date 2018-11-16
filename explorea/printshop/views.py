from django.shortcuts import render

# Create your views here.
def profile(request):
#    events = Event.objects.all()
    return render(request, 'events/event_listing.html')

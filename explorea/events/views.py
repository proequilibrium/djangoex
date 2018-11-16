from django.shortcuts import render
from django.http import HttpResponse

from .models import Event, EventRun
from .forms import AddEventRunForm, addEventForm
#def index(request):
#    return HttpResponse("Nazdar")

from django.shortcuts import render

def index(request):

    return render(request, 'events/index.html')

def event_listing(request):
    events = Event.objects.all()
    return render(request, 'events/event_listing.html', {'events': events})

def eventrun_listing(request, pk):
    eventRuns = EventRun.objects.filter(event = pk)
    return render(request, 'events/event_run_listing.html', {'eventRuns': eventRuns})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    details = eventrun_set.all().order_by('happens')
    return render(request, 'events/event_detail.html', {'runs': runs})

def my_events(request):
    myEvents = Event.get(host=User.id)
    return render(request,'events/events_detail.html', {'myEvents': events})

def eventrun_add(request):
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = AddEventRunForm(request.POST)

        if form.is_valid():

            er = EventRun(event = event,
                happens = happens,
                seats_available = seats_available,
                price = price)
            er.set_password(password)
            er.save()

            #return redirect('profile')

    form = AddEventForm()
    return render(request, 'events/add_event_run.html', {'form': form} )

def event_update():
    pass

def event_delete():
    pass

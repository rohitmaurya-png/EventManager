from django.shortcuts import render

from apps.event.models import Event

def frontpage(request):
    newest_events = Event.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'newest_events': newest_events})

def contact(request):
    return render(request, 'core/contact.html')
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404

from .models import Coordinator
from apps.event.models import Event

from .forms import EventForm

def become_coordinator(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            coordinator = Coordinator.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'coordinator/become_coordinator.html', {'form': form})

@login_required
def coordinator_admin(request):
    coordinator = request.user.coordinator
    events = coordinator.events.all()
    orders = coordinator.orders.all()

    for order in orders:
        order.coordinator_amount = 0
        order.coordinator_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.coordinator == request.user.coordinator:
                if item.coordinator_paid:
                    order.coordinator_paid_amount += item.get_total_price()
                else:
                    order.coordinator_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'coordinator/coordinator_admin.html', {'coordinator': coordinator, 'events': events, 'orders': orders})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.coordinator = request.user.coordinator
            event.slug = slugify(event.title)
            event.save()

            return redirect('coordinator_admin')
    else:
        form = EventForm()
    
    return render(request, 'coordinator/add_event.html', {'form': form})

@login_required
def edit_coordinator(request):
    coordinator = request.user.coordinator

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            coordinator.created_by.email = email
            coordinator.created_by.save()

            coordinator.name = name
            coordinator.save()

            return redirect('coordinator_admin')
    
    return render(request, 'coordinator/edit_coordinator.html', {'coordinator': coordinator})

def coordinators(request):
    coordinators = Coordinator.objects.all()

    return render(request, 'coordinator/coordinators.html', {'coordinators': coordinators})

def coordinator(request, coordinator_id):
    coordinator = get_object_or_404(Coordinator, pk=coordinator_id)

    return render(request, 'coordinator/coordinator.html', {'coordinator': coordinator})


import random

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddToCartForm
from .models import Category, Event

from apps.cart.cart import Cart

def search(request):
    query = request.GET.get('query', '')
    events = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'event/search.html', {'events': events, 'query': query})

def event(request, category_slug, event_slug):
    cart = Cart(request)

    event = get_object_or_404(Event, category__slug=category_slug, slug=event_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(event_id=event.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'The event was added to the cart')

            return redirect('event', category_slug=category_slug, event_slug=event_slug)
    else:
        form = AddToCartForm()

    similar_events = list(event.category.events.exclude(id=event.id))

    if len(similar_events) >= 4:
        similar_events = random.sample(similar_events, 4)

    return render(request, 'event/event.html', {'form': form, 'event': event, 'similar_events': similar_events})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'event/category.html', {'category': category})
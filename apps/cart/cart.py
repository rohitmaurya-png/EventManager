from django.conf import settings

from apps.event.models import Event

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['event'] = Event.objects.get(pk=p)
        
        for item in self.cart.values():
            item['total_price'] = item['event'].price * item['quantity']

            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def add(self, event_id, quantity=1, update_quantity=False):
        event_id = str(event_id)
        
        if event_id not in self.cart:
            self.cart[event_id] = {'quantity': 1, 'id': event_id}
        
        if update_quantity:
            self.cart[event_id]['quantity'] += int(quantity)

            if self.cart[event_id]['quantity'] == 0:
                self.remove(event_id)
                        
        self.save()
    
    def remove(self, event_id):
        if event_id in self.cart:
            del self.cart[event_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['event'] = Event.objects.get(pk=p)

        return sum(item['quantity'] * item['event'].price for item in self.cart.values())
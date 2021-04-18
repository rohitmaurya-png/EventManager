from django.contrib.auth.models import User
from django.db import models

class Coordinator(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='coordinator', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_balance(self):
        items = self.items.filter(coordinator_paid=False, order__coordinators__in=[self.id])
        return sum((item.event.price * item.quantity) for item in items)
    
    def get_paid_amount(self):
        items = self.items.filter(coordinator_paid=True, order__coordinators__in=[self.id])
        return sum((item.event.price * item.quantity) for item in items)
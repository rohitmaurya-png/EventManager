from django.forms import ModelForm

from apps.event.models import Event

class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['class'] = 'input'
        self.fields['image'].widget.attrs['class'] = 'input'
        self.fields['title'].widget.attrs['class'] = 'input'
        self.fields['description'].widget.attrs['class'] = 'input'
        self.fields['price'].widget.attrs['class'] = 'input'
    class Meta:
        model = Event
        fields = ['category', 'image', 'title', 'description', 'price']
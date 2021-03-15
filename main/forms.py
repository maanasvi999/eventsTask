from django.forms import ModelForm
from .models import EventDetails

class EventsForm(ModelForm):
    class Meta:
        model = EventDetails
        fields = ["event_name", "date", "time", "location", "image"]

from django.db import models
from django.db import connections

class EventDetails(models.Model):
    event_name = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='main/images/')
    is_liked = models.BooleanField(default = False)
    class Meta:
        db_table = 'events_table'
        verbose_name_plural = "Events Details"

    def __str__(self):
        return self.event_name
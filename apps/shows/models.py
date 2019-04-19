from __future__ import unicode_literals
from django.db import models
from apps.log_app.models import User, Event

class EventManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        pass
        return errors

class Event(models.Model):
    name = models.CharField(max_length=45)
    genre = models.CharField(max_length=45)
    date = models.DateField()
    location = models.CharField(max_length=255)
    host = models.ForeignKey(User, related_name="event")
    attendees = models.ManyToManyField(User, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = EventManager()

    def __repr__(self):
        return f"Event: {self.name}"
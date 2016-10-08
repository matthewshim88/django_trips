from __future__ import unicode_literals
from django.db import models
from ..new_login.models import User
import datetime
import time
import re
from django.db import models

class TripManager(models.Manager):
    def validate(self, data):
        errors = []
        bvalid = re.compile(r'^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$')

        if len(data['destination']) < 1:
            errors.append("Please enter a destination")
        if len(data['description']) < 1:
            errors.append("Please enter a description")
        if len(data['travel_date_from']) < 1:
            errors.append("Please enter a start date")
        if len(data['travel_date_to']) < 1:
            errors.append("Please enter a end date")

        destinationcheck = Trips.objects.filter(destination = data['destination'])
        if destinationcheck:
            errors.append("That Trip is already planned!")
        if not bvalid.match(data['travel_date_from']):
            errors.append("Not a valid start date!")
        if not bvalid.match(data['travel_date_to']):
            errors.append("Not a valid end date!")
        if data['travel_date_from'] > data['travel_date_to']:
            errors.append("Start date cannot be after the end date")

        current_date = (time.strftime("%Y-%m-%d"))
        if data['travel_date_from'] < current_date:
            errors.append('Start date must be in the future')

        return errors

    def addTrip(self, data, id):
        response = {}
        errors = self.validate(data)
        user = User.objects.get(id=id)
        if len(errors) > 0:
            response['added'] = False
            response['errors'] = errors
        else:
            trip = Trips.objects.create(destination=data['destination'], description = data['description'], added_by = user, travel_date_from=data['travel_date_from'], travel_date_to=data['travel_date_to'])
            new_trip = Trips.objects.get(id=trip.id)
            new_trip.save()
            response['added'] = True
            response['trip'] = trip
        return response

    def joinTrip(self, trip, id):
        response = {}
        find_trip = Trips.objects.get(id=trip.id)
        find_trip.joined_trip.add(id)
        find_trip.save()
        response['joined'] = True
        response['trip'] = find_trip
        return response

class Trips(models.Model):
    destination = models.CharField(max_length=200)
    description = models.CharField(max_length = 200)
    added_by = models.ForeignKey(User, related_name='added_by')
    joined_trip = models.ManyToManyField(User, related_name='joined_trip')
    travel_date_from = models.DateTimeField()
    travel_date_to = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()

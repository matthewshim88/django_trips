from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from ..new_login.models import User
from .models import Trips, TripManager

# Create your views here.
def index(request):
    this_user = User.objects.get(id = request.session['id'])
    other_trips = Trips.objects.exclude(joined_trip=request.session['id']).order_by('-date_added')
    my_trips = Trips.objects.filter(joined_trip=request.session['id']).order_by('-date_added')

    context={
        'this_user': this_user,
        'my_trips' : my_trips,
        'other_trips' : other_trips
    }
    return render(request, 'django_demo/index.html', context)

def new_plan(request):
    this_user = User.objects.get(id=request.session['id'])
    context = {
        'this_user': this_user
    }
    return render(request, 'django_demo/addTrip.html', context)

def addTrip(request):
    if request.method == 'POST':
        user_id = request.session['id']
        new_trip = Trips.objects.addTrip(request.POST, user_id)
        if new_trip['added']:
            trip = new_trip['trip']
            messages.success(request, "New Trip successfully Added!")
            return redirect(reverse('travel:index'))
        else:
            for error in new_trip['errors']:
                messages.error(request, error)
            return redirect(reverse('travel:newPlan'))

def showTrip(request, id):
    this_trip = Trips.objects.get(id=id)
    other_users = User.objects.filter(joined_trip=id)
    context = {
        'this_trip': this_trip,
        'other_users': other_users
    }
    return render(request, 'django_demo/showtrip.html', context)

def joinTrip(request, id):
    if request.method=='POST':
        get_trip = Trips.objects.get(id=id)
        user_id = request.session['id']
        trip_joined = Trips.objects.joinTrip(get_trip, user_id)

        if trip_joined['joined']:
            messages.success(request, "Trip Joined")
            trip = trip_joined['trip']
    return redirect(reverse('travel:index'))


def logOut(request):
    request.session.clear()
    return redirect(reverse('users:index'))

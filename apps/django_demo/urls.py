from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^logOut$', views.logOut, name='logOut'),
    url(r'^newPlan$', views.new_plan, name='newPlan'),
    url(r'^newTrip$', views.addTrip, name='newTrip'),
    url(r'^showTrip/(?P<id>\d+)$', views.showTrip, name='showTrip'),
    url(r'^join_trip/(?P<id>\d+)$', views.joinTrip, name='join_trip'),
]

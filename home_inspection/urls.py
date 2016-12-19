from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    # /inspection/
    # add new property
    # display all the properties belong to logged user 
    url(r'^$', views.index, name='index'),

    # /inspection/1/delete
    # delete property from index page
    url(r'^(?P<property_id>[0-9]+)/delete$', views.deleteProp, name='deleteProp'),

    # /inspection/1/
    # see rooms inside property
    url(r'^(?P<property_id>[0-9]+)/$', views.room, name='room'),

    # /inspection/1/delete
    # delete property from index page
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)/delete$', views.deleteRoom, name='deleteRoom'),

    # /inspection/1/1
    # see components inside room
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)$', views.component, name='component'),
]
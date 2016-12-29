from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    # /
    # homepage
    # display all the properties belong to logged user 
    url(r'^$', views.index, name='index'),

    ##NEW PAGES TO EDIT
    # /about/
    # website about page
    url(r'^about/$', views.about, name='about'),
    # /agent_rooms/
    # agent walkthrough, room select
    url(r'^agent_rooms/$', views.agent_rooms, name='agent_rooms'),
    # /agents/
    # agent walkthrough, walkthrough home
    url(r'^agents/$', views.agents, name='agents'),
    # /buyers/
    # buyers walkthrough, walkthrough home
    url(r'^buyers/$', views.buyers, name='buyers'),
    # /inspect_rooms/
    # inspector walkthrough - room select
    url(r'^inspect_rooms/$', views.inspect_rooms, name='inspect_rooms'),
    # /inspector/
    # inspector walkthrough - walkthrough home
    url(r'^inspector/$', views.inspector, name='inspector'),
    # /login/
    # login page
    url(r'^login/$', views.login, name='login'),
    # /register/
    # account registration page
    url(r'^register/$', views.register, name='register'),
    # /contact/
    # contact information page
    url(r'^contact/$', views.contact, name='contact'),
    # /reports/
    # saved user reports page
    url(r'^myreports/$', views.reports, name='reports'),
    # /reports/
    # saved user reports page
    url(r'^terms_conditions/$', views.terms, name='terms'),
    # /reports/
    # saved user reports page
    url(r'^technical_articles/$', views.articles, name='articles'),
    ##/end of new pages

    # /dashboard/
    # user home
    # display all the properties belong to logged user 
    url(r'^dashboard/$', views.dashboard, name='dashboard'),

    # /1/delete
    # delete property from index page
    url(r'^(?P<property_id>[0-9]+)/delete$', views.deleteProp, name='deleteProp'),

    # /1/
    # see rooms inside property
    url(r'^(?P<property_id>[0-9]+)/$', views.room, name='room'),

    # /1/delete
    # delete property from index page
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)/delete$', views.deleteRoom, name='deleteRoom'),

    # /1/1
    # see components inside room
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)$', views.component, name='component'),
       
            
]

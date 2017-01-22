from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    # /
    # homepage
    url(r'^$', views.index, name='index'),

    # /about
    url(r'^about/$', views.about, name='about'),

        
    # /login
    url(r'^login/$', views.login, name='login'),
    
    # /register
    url(r'^register/$', views.register, name='register'),
    
    # /contact
    url(r'^contact/$', views.contact, name='contact'),
    
    # /myreports
    url(r'^myreports/$', views.reports, name='reports'),
    
    # /terms_conditions
    url(r'^terms_conditions/$', views.terms, name='terms'),
    
    # /technical_articles
    url(r'^technical_articles/$', views.articles, name='articles'),
    
    # /dashboard
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    
#    # /agents
#    # agent walkthrough, walkthrough home
#    url(r'^agents/$', views.agents, name='agents'),
#    
#    # /agent_rooms
#    # agent walkthrough, room select
#    url(r'^agent_rooms/$', views.agent_rooms, name='agent_rooms'),
#    
#    # /buyers
#    # buyers walkthrough, walkthrough home
#    url(r'^buyers/$', views.buyers, name='buyers'),
#    # /buyers walkthrough, walkthrough home/
#    
#    # /buyer_rooms
#    # buyer walkthrough, room select
#    url(r'^buyer_rooms/$', views.buyer_rooms, name='buyer_rooms'),
#    
#    # /owners
#    # owners walkthrough, walkthrough home
#    url(r'^owners/$', views.owners, name='owners'),
#    
#    # /owner_rooms
#    # owner walkthrough, room select
#    url(r'^owner_rooms/$', views.owner_rooms, name='owner_rooms'),
#    
#    # /inspector
#    # inspector walkthrough - walkthrough home
#    url(r'^inspector/$', views.inspector, name='inspector'),
#    # /owner walkthrough, room select/
#    
    # /inpector_rooms
    # inspector walkthrough - room select
    url(r'^inspector_rooms/$', views.room, name='inspector_rooms'),

    # /inspector_start
    # see rooms inside property
    url(r'^inspector_start/$', views.inspector_start, name='inspector_start'),
    
    # /#
    # see rooms inside property
    url(r'^(?P<property_id>[0-9]+)/$', views.room, name='room'),
    
    # /#/#
    # see components inside room
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)$', views.component, name='component'),
    
    # /#/delete
    # delete property
    url(r'^(?P<property_id>[0-9]+)/delete$', views.deleteProp, name='deleteProp'),
    
    # /#/#/delete
    # delete property
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)/delete$', views.deleteRoom, name='deleteRoom'),
            
]
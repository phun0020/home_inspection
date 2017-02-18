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
    
    # /profile
    url(r'^profile/$', views.profile, name='profile'),
   
    # /inspector_start
    # define new report
    url(r'^inspector_start/$', views.inspector_start, name='inspector_start'),
    
    # /#/delete
    # delete property
    url(r'^dashboard/(?P<property_id>[0-9]+)/delete$', views.deleteProp, name='deleteProp'),
    
    # /#
    # see rooms inside property
    url(r'^(?P<property_id>[0-9]+)/$', views.room, name='room'),
    
    # /#/#/delete
    # delete property
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)/delete$', views.deleteRoom, name='deleteRoom'),
    
    # /#/#
    # see components inside room
    url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)$', views.component, name='component'),
            
]
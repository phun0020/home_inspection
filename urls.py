from django.conf.urls import url
from . import views

app_name = 'inspection'

urlpatterns = [
    # /
    # homepage
    url(r'^$', views.index, name='index'),
    
    ### NAVBAR LINKS ###
        # /login
        url(r'^login/$', views.login, name='login'),
        # /register
        url(r'^register/$', views.register, name='register'),
        # /dashboard
        url(r'^dashboard/$', views.dashboard, name='dashboard'),
    ### /NAVBAR LINKS ###
    
    ### USER PROFILE ###
    # /profile
        url(r'^profile/$', views.profile, name='profile'),
         # /payment Info
        url(r'^payment_info/$', views.paymentInfo, name='paymentInfo'),
         # /account balance
        url(r'^account_balance/$', views.accountBalance, name='accountBalance'),
    ### /USER PROFILE ###
    
    ### REPORT PAGES ###
         # /inspector_start
        # define new report
        url(r'^inspector_start/$', views.inspector_start, name='inspector_start'),
        # /#
        # edit rooms
        url(r'^(?P<property_id>[0-9]+)/$', views.room, name='room'),
        # /#/#
        # edit components 
        url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)$', views.component, name='component'),
        # /#/delete
        # delete property
        url(r'^dashboard/(?P<property_id>[0-9]+)/delete$', views.deleteProp, name='deleteProp'),
        # /#/#/delete
        # delete room
        url(r'^(?P<property_id>[0-9]+)/(?P<room_id>[0-9]+)/delete$', views.deleteRoom, name='deleteRoom'),
    ### /REPORT PAGES ###
    
    ### FOOTER LINKS ###
        # /about
        url(r'^about/$', views.about, name='about'),
        # /contact
        url(r'^contact/$', views.contact, name='contact'),
        # /myreports
        url(r'^myreports/$', views.reports, name='reports'),
        # /technical_articles
        url(r'^technical_articles/$', views.articles, name='articles'),
        # /terms_conditions
        url(r'^terms_conditions/$', views.terms, name='terms'),
    ### /FOOTER LINKS ###
    
]
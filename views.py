from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Inspector, Property, Room, RoomType, BuildingType, PropertyType #Inspector, Owner,
from .forms import PropertyForm, UserForm, PaymentForm
from .service import isXeditableCallRequest, updateWithXeditable
import json



##### HOME region ######
def index(request):
    return render(request, 'index.html')
##### end of HOME region ######



### NAVBAR LINKS ###
## LOGIN
def login(request):
    return render(request, 'inspection/login.html')
## REGISTER
def register(request):
    return render(request, 'inspection/register.html')
## DASHBOARD
def dashboard(request):
    # get all needed data: properties, buildingType, propType
    allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)
    # list of propType and BuildType for Xeditable's source
    propTypeList = [ob.as_json() for ob in PropertyType.objects.all()]
    buildTypeList = [ob.as_json() for ob in BuildingType.objects.all()]
    # forms
    propForm = PropertyForm(prefix="propFrom")
    users = get_list_or_404(Inspector.objects.order_by('-id'))
    # render normal page if doesn't receive any request
    return render(request, 'inspection/dashboard.html', {
        'allProperties' : allProperties,
        'propForm' : propForm,
        'users' : users,
        'propTypeList' : propTypeList,
        'buildTypeList' : buildTypeList
    })
### /NAVBAR LINKS ###



### USER PROFILE ###
## PROFILE
def profile(request):
    users = get_list_or_404(Inspector.objects.order_by('-id'))
    userForm = UserForm(request.POST, prefix="userForm")
    if request.method == 'POST':
        if userForm.is_valid():# and paymentForm.is_valid():              -- PAYMENT FORM NOT VALIDATING
            userForm.save()
            #    paymentForm.save()                                       -- ValueError: The property could not be created because the data didn't validate
        else:
            return HttpResponse('''
            <h1>Something is not right...</h1>
            <p>invalid submit = return alternative http; page not displaying</p><br/>
            <p>?currently not pulling db values so form is blank</p>
            ''')
    # render normal page if doesn't receive any request
    return render(request, 'inspection/profile.html', {
        'users' : users,
        'userForm' : userForm,
        #'paymentForm' : paymentForm,                                     -- COMMENT OUT PAYMENT FORM SO AVIOD ERROR FOR NOW
    })
## PAYMENT_INFO
def paymentInfo(request):
    return render(request, 'inspection/payment_info.html')
## ACCOUNT_BALANCE
def accountBalance(request):
    return render(request, 'inspection/account_balance.html')
## MY_REPORTS 
def reports(request):
    return render(request, 'inspection/user_reports.html')
### /USER PROFILE ###



### REPORT PAGES ###


## INSPECTOR_START 
def inspector_start(request):
    # get all needed data: properties, buildingType, propType
    allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)
    #users = get_object_or_404(Inspector, id = Property.objects.order_by('-id')) # NO INSPECTOR MATCHES QUERY
        
    
    # list of propType and BuildType for Xeditable's source
    propTypeList = [ob.as_json() for ob in PropertyType.objects.all()]
    buildTypeList = [ob.as_json() for ob in BuildingType.objects.all()]

    # form
    propForm = PropertyForm(prefix="propFrom")
    inspectorForm = UserForm(prefix="inspectorForm")

    # Record Form data
    if request.method == 'POST':
        #-----add new property-----
        inspectorForm = UserForm(request.POST, prefix = 'inspectorForm')
        propForm = PropertyForm(request.POST, prefix = 'propFrom')

        if propForm.is_valid():
            propForm.save()

            # update the allProperties, can't use the one above
            allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)
            #property = get_object_or_404(Property, id = property_id)
            
            return render(request, 'inspection/room.html', {
                'allProperties' : allProperties,
                'property' : property
            })

            # or
            # redirect to the room page of created property
            # return HttpResponseRedirect('/inspection/'+ str(prop.id))

        #-----change property attributes-----
        if isXeditableCallRequest(request):
            reqClass = request.POST.get('class')
            # decision depend on params class : inspector or Property
            
            # TODO really need to refactor this xeditable after come back -tam
            
            # TODO limit requirements to username and company - eric
            if(reqClass == 'Inspector'): updateWithXeditable(request, Inspector)
            if(reqClass == 'Property'):
                req = request.POST 
                if req.get('name') == 'propertyTypeId':
                    updateWithXeditable(request, Property, PropertyType, mode='select')
                elif req.get('name') == 'buildingTypeId':
                    updateWithXeditable(request, Property, BuildingType, mode='select')
                else:
                    updateWithXeditable(request, Property)

        else:
            return HttpResponse('<h1>Something is not right...</h1>')
        
    # render normal page if doesn't receive any request
    return render(request, 'inspection/inspector_start.html', {
        'allProperties' : allProperties,
        'inspectorForm' : inspectorForm,
        'propForm' : propForm,
        'propTypeList' : propTypeList,
        'buildTypeList' : buildTypeList
    })




## #/ (ROOMS)
def room(request, property_id):
    # get individual property
    property = get_object_or_404(Property, id = property_id)

    # AJAX call
    if request.method == 'POST':
        req = request.POST

        #-----add new room-----
        if req.get('roomType') and req.get('roomName'):
            room = Room()

            room.propertyId = property
            room.roomTypeId = get_object_or_404(RoomType, id = req.get('roomType'))
            room.roomName = req.get('roomName')

            room.save()

            return render(request, 'inspection/partial/room.partial.html', {
                'property' : property
            })

        #-----change room name-----
        if isXeditableCallRequest(request):
            updateWithXeditable(request, Room)

            # should return json or status rather than this... message
            return HttpResponse('<h3>{0}</h3>'.format('call ajax successfully'))
    else:
        roomType = get_list_or_404(RoomType)
        return render(request, 'inspection/room.html', {
            'property' : property,
            'roomType' : roomType
        })
## #/# (COMPONENTS)
def component(request, property_id, room_id):
    room = get_object_or_404(Room, id = room_id)

    return render(request, 'inspection/component.html', {
    'room' : room
    }) 
## #/delete (PROP) 
def deleteProp(request, property_id):
    # change the selected property to True
    if request.method == 'POST':
        selectedProp = get_object_or_404(Property, id=property_id)
        selectedProp.delete()
    allProperties = get_list_or_404(Property.objects.order_by('-id'))
    return render(request, 'inspection/partial/dashboard.partialreports.html', {
        'allProperties' : allProperties
    })
## #/#/delete (ROOM)
def deleteRoom(request, property_id, room_id):
    selectedRoom = get_object_or_404(Room, id=room_id).delete()

    property = get_object_or_404(Property, id=property_id)

    return render(request, 'inspection/partial/room.partial.html', {
        'property' : property
    })
### /REPORT PAGES ###



### FOOTER LINKS ###
## ABOUT 
def about(request):
    return render(request, 'inspection/about.html')
## CONTACT 
def contact(request):
    return render(request, 'inspection/contact.html')
## TECHNICAL_ARTICLES
def articles(request):
    return render(request, 'inspection/articles.html')
## TERMS_CONDITIONS
def terms(request):
    return render(request, 'inspection/terms.html')
### /FOOTER LINKS ###
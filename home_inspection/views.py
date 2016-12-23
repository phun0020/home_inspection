from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Inspector, Owner, Property, Room, RoomType, BuildingType, PropertyType
from .forms import PropertyForm, OwnerForm
from .service import isXeditableCallRequest, updateWithXeditable
import json

##### PROPERTY region ######
def index(request):
    # get all needed data: properties, buildingType, propType
    allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)

    # list of propType and BuildType for Xeditable's source
    propTypeList = [ob.as_json() for ob in PropertyType.objects.all()]
    buildTypeList = [ob.as_json() for ob in BuildingType.objects.all()]

    # form
    propForm = PropertyForm(prefix="propFrom")
    ownerForm = OwnerForm(prefix="ownerForm")

    # AJAX call
    
    if request.method == 'POST':
        #-----add new property-----
        ownerForm = OwnerForm(request.POST, prefix = 'ownerForm')
        propForm = PropertyForm(request.POST, prefix = 'propFrom')

        if ownerForm.is_valid() and propForm.is_valid():
            # don't commit yet
            # take owner that just created and add to new property
            prop = propForm.save(commit = False)
            prop.ownerId = ownerForm.save()

            # should be current user, instead of this
            prop.inspectorId = get_object_or_404(Inspector, id = 1)
            prop.save()

            # update the allProperties, can't use the one above
            allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)

            return render(request, 'inspection/partial/index.partial.html', {
                'allProperties' : allProperties
            })

            # or
            # redirect to the room page of created property
            # return HttpResponseRedirect('/inspection/'+ str(prop.id))
        
        #-----change property attributes-----
        if isXeditableCallRequest(request):
            reqClass = request.POST.get('class')
            # decision denpend on params class : Owner or Property
            # really need to refactor this xeditable after come back
            if(reqClass == 'Owner'): updateWithXeditable(request, Owner)
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
    return render(request, 'inspection/index.html', {
        'allProperties' : allProperties,
        'propForm' : propForm,
        'ownerForm' : ownerForm,
        'propTypeList' : propTypeList,
        'buildTypeList' : buildTypeList
    })

def deleteProp(request, property_id):
    # change the selected property to True
    
    selectedProp = get_object_or_404(Property, id=property_id)
    selectedProp.ownerId.delete()
    selectedProp.delete()

    allProperties = get_list_or_404(Property.objects.order_by('-id'), isDelete = False)

    return render(request, 'inspection/partial/index.partial.html', {
        'allProperties' : allProperties
    })

##### end of PROPERTY region ######


##### ROOM region ######
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

def deleteRoom(request, property_id, room_id):
    selectedRoom = get_object_or_404(Room, id=room_id).delete()

    property = get_object_or_404(Property, id=property_id)

    return render(request, 'inspection/partial/room.partial.html', {
        'property' : property
    })

##### end of ROOM region ######

##### COMPONENT region ######
def component(request, property_id, room_id):
    room = get_object_or_404(Room, id = room_id)

    return render(request, 'inspection/component.html', {
        'room' : room
    }) 

##### end of COMPONENT region ######

    
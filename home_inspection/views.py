from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Inspector, Owner, Property, Room, RoomType, BuildingType, PropertyType
from .forms import PropertyForm, OwnerForm


##### PROPERTY region ######
def index(request):
    # get all needed data: properties, buildingType, propType
    allProperties = get_list_or_404(Property, isDelete = False)

    # form
    propForm = PropertyForm(prefix="propFrom")
    ownerForm = OwnerForm(prefix="ownerForm")

    return render(request, 'inspection/index.html', {
        'allProperties' : allProperties,
        'propForm' : propForm,
        'ownerForm' : ownerForm,
    })

def post_property(request):
    if request.method == 'POST':
        ownerForm = OwnerForm(request.POST, prefix = 'ownerForm')
        propForm = PropertyForm(request.POST, prefix = 'propFrom')

        if ownerForm.is_valid() and propForm.is_valid():
            # don't commit yet
            # take owner that just created and add to new property
            prop = propForm.save(commit = False)
            prop.ownerId = ownerForm.save()
            # should be current user
            prop.inspectorId = get_object_or_404(Inspector, id = 1)
            prop.save()

    return HttpResponseRedirect('/inspection/'+ str(prop.id))


def deleteProp(request, property_id):
    # change the selected property to True
    allProperties = get_list_or_404(Property, isDelete=False)
    try:
        selectedProp = Property.objects.get(id=property_id)
    except Property.DoesNotExist:
        return render(request, 'inspection/index.html', {
            'allProperties' : allProperties
        })
    else:
        selectedProp.isDelete = True
        selectedProp.save()

        # missing: AJAX load
        return HttpResponseRedirect('/inspection/')

##### end of PROPERTY region ######


##### ROOM region ######
def room(request, property_id):
    # get individual property
    # all_room = Room.objects.filter(propertyId=property_id)
    property = get_object_or_404(Property, id = property_id)

    roomType = get_list_or_404(RoomType)

    return render(request, 'inspection/room.html', {
        'property' : property,
        'roomType' : roomType
    })

##### end of ROOM region ######

##### COMPONENT region ######
def component(request, property_id, room_id):
    room = get_object_or_404(Room, id = room_id)

    return render(request, 'inspection/component.html', {
        'room' : room
    }) 

##### end of COMPONENT region ######
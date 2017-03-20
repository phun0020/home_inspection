from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Inspector, Property, Room, RoomType, BuildingType, PropertyType #Inspector, Owner,
from .forms import PropertyForm, UserForm

def isXeditableCallRequest(request):
    if request.method == 'POST':
        req = request.POST
        if req.get('name') and req.get('value') and req.get('pk'):
            return True
        return False

def updateWithXeditable(request, objectClass, subObjectClass=None, mode='text'):
    if isXeditableCallRequest(request):
        req = request.POST
        obj = get_object_or_404(objectClass, id = req.get('pk'))
        if mode == 'text':
            setattr(obj, req.get('name'), req.get('value'))
            obj.save()
        if mode == 'select' and subObjectClass:
            subObj = get_object_or_404(subObjectClass, id = req.get('value'))
            setattr(obj, req.get('name'), subObj)
            obj.save()
    else:
        raise 'error when call xeditable update!'
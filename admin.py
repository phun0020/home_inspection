from django.contrib import admin
from .models import *
# Register your models here.

models = [Inspector, Payment, PropertyType, BuildingType, Property, RoomType, Room, Component]#Owner, Inspector,


for model in models:
    admin.site.register(model)

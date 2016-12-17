from django.contrib import admin
from .models import *
# Register your models here.

models = [Inspector, Owner, PropertyType, BuildingType, Property, RoomType, Room, Component]

for model in models:
    admin.site.register(model)

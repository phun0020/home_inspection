from django import forms
from .models import Property, Owner, PropertyType, BuildingType

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'propertyTypeId', 'propertySize', 'buildingTypeId']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control', 'value' : 'test Drive, Ottawa'}),
            'propertyTypeId': forms.Select(attrs={'class': 'form-control', 'value' : '1'}),
            'propertySize': forms.NumberInput(attrs={'class': 'form-control', 'value' : '123'}),
            'buildingTypeId': forms.Select(attrs={'class': 'form-control', 'value' : '1'})
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['firstname', 'lastname', 'email', 'phone']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'value' : 'test'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'value' : 'test'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'value' : 'test@gmail.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'value' : '613-265-2563'}),
        }


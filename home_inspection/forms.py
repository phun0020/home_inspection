from django import forms
from .models import Property, Owner, PropertyType, BuildingType

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'propertyTypeId', 'propertySize', 'buildingTypeId']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'propertyTypeId': forms.Select(attrs={'class': 'form-control'}),
            'propertySize': forms.NumberInput(attrs={'class': 'form-control'}),
            'buildingTypeId': forms.Select(attrs={'class': 'form-control'})
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['firstname', 'lastname', 'email', 'phone']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


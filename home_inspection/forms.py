from django import forms
from .models import Property, Owner, PropertyType, BuildingType

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['projectNum', 'client', 'address', 'propertyTypeId', 'propertySize']
        widgets = {
            'projectNum' : forms.TextInput(attrs={'class': 'form-control', 'value' : 'date-user'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'value' : 'Client Namespace'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'value' : 'test Drive, Ottawa'}),
            'propertyTypeId': forms.Select(attrs={'class': 'form-control', 'value' : '1'}),
            'propertySize': forms.NumberInput(attrs={'class': 'form-control', 'value' : '123'}),
            # create ref table
            # 'unitOfMeasure': forms.Select(attrs={'class': 'form-control', 'value' : '1'}),
        }     
            
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['username', 'company', 'email', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'value' : 'User Namespace'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'value' : 'Mycompany Inc.'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'value' : 'myname@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'value' : '613-265-2643'}),
        }

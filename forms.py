from django import forms
from .models import Property, Inspector, PropertyType, BuildingType, Property, RoomType, Room, Component, Payment

PAYMENT_OPTIONS = (
    ('MC', 'Mastercard'),
    ('VS', 'Visa'),
    ('PP', 'Paypal'),
    ('DT', 'Debit'),
)

MONTHS = (
    ('january', 'January'),
    ('february', 'February'),
    ('march', 'March'),
    ('april', 'April'),
    ('may', 'May'),
    ('june', 'June'),
    ('july', 'July'),
    ('august', 'August'),
    ('september', 'September'),
    ('october', 'October'),
    ('november', 'November'),
    ('december', 'December'),
    )

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
            # 'unitOfMeasure': forms.Select(attrs={'class': 'form-control', 'value' : '1'}),
        }     
     
class UserForm(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ['username', 'password', 'email', 'phone', 'company', 'description', 'subscriptionStatus', 'memberStatus']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'value' : 'User Namespace'}), 
            'password': forms.TextInput(attrs={'class': 'form-control', 'value' : '********'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'value' : 'myname@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'value' : '613-265-2643'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'value' : 'Mycompany Inc.'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'value' : 'A short company description.'}),
            'subscriptionStatus': forms.CheckboxInput(attrs={'class': 'form-control inline profileCheckbox', 'value' : False}),
            'memberStatus': forms.CheckboxInput(attrs={'class': 'form-control inline profileCheckbox', 'value' : False}),

        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['method', 'ccardHolder', 'ccardNumber1', 'ccardNumber2', 'ccardNumber3', 'ccardNumber4', 'ccardExpDateMth', 'ccardExpDateYr', 'ccardSecurity']
        widgets = {
            'method': forms.RadioSelect(attrs={'class': 'radioSelect form-control', 'required':'required'}, choices=PAYMENT_OPTIONS),
            'ccardHolder': forms.TextInput(attrs={'class': 'form-control', 'value' : 'User Namespace'}),
            'ccardNumber1': forms.NumberInput(attrs={'class': 'form-control quarter-form inline', 'value' : '0000'}),
            'ccardNumber2': forms.NumberInput(attrs={'class': 'form-control quarter-form inline', 'value' : '0000'}),
            'ccardNumber3': forms.NumberInput(attrs={'class': 'form-control quarter-form inline', 'value' : '0000'}),
            'ccardNumber4': forms.NumberInput(attrs={'class': 'form-control quarter-form inline', 'value' : '0000'}),
            'ccardExpDateMth': forms.SelectMultiple(attrs={'class': 'form-control'}, choices=MONTHS),
            'ccardExpDateYr': forms.NumberInput(attrs={'class': 'form-control', 'value' : '000'}),
            'ccardSecurity': forms.NumberInput(attrs={'class': 'form-control', 'value' : '0000'}),
            
        }   
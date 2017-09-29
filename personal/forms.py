from django import forms;
from django.forms import ModelForm;
from django.forms.formsets import formset_factory;

from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import PersonalInfo, PhoneInfo, AddressInfo;
"""
class PersonalInfoForm(forms.Form):

    GENDER_CHOICES = (
        ("M", ("Male")),
        ("F", ("Female")),
    );

    first_name  = forms.CharField(label='First Name', max_length=100)
    middle_name = forms.CharField(label='Middle Name', max_length=100)
    last_name   = forms.CharField(label='Last Name', max_length=100)
    dob         = forms.DateField(label='Date of Birth',widget = extras.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")));
    age         = forms.IntegerField(label='Age')
    gender      = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    emailid     = forms.CharField(label='Email Id', max_length=500)
"""


class PersonalInfoForm( ModelForm ):

    class Meta:
        model = PersonalInfo;
        fields=['first_name','middle_name','last_name','gender','age','emailid'];

class PersonPhoneInfoForm( ModelForm ):
    class Meta:
        model = PhoneInfo;
        fields=['phone_type','phone_nbr'];

class PersonAddressInfoForm( ModelForm ):
    class Meta:
        model = AddressInfo;
        fields=['address_type','door','street','pin','city','state','country'];

PhonesFormSet = inlineformset_factory(PersonalInfo, PhoneInfo, fields=('phone_type','phone_nbr'), can_delete=False, extra=3);

AddressFormSet= inlineformset_factory(PersonalInfo, AddressInfo, fields=('address_type','door','street','pin','city','state','country'),
                                     can_delete=False, extra=2);


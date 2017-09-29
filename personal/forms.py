from django import forms;
from django.forms import ModelForm;
from django.forms.formsets import formset_factory;

from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import PersonalInfo, PhoneInfo, AddressInfo, BankInfo;

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

class BankInfoForm(ModelForm):
    class Meta:
        model = BankInfo;
        fields=['name','bnk_abbr_name','branch','brn_abbr_name','address','phone_nbr'];


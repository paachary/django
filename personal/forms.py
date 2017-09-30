from django import forms;
from django.forms import ModelForm;
from django.forms.formsets import formset_factory;

from django.forms.models import inlineformset_factory
from django.forms.models import BaseInlineFormSet

from .models import PersonalInfo, PhoneInfo, AddressInfo, BankInfo, BankMembership;

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

PhonesFormSet = inlineformset_factory(PersonalInfo, PhoneInfo, fields=('phone_type','phone_nbr'), can_delete=True, extra=0);

AddressFormSet= inlineformset_factory(PersonalInfo, AddressInfo, fields=('address_type','door','street','pin','city','state','country'), can_delete=True, extra=0);

class BankInfoForm(ModelForm):
    class Meta:
        model = BankInfo;
        fields=['name','bnk_abbr_name','branch','brn_abbr_name','address','phone_nbr'];

class BankMembershipForm(ModelForm):
#    bank_name=forms.ModelChoiceField(queryset=BankInfo.objects.all().values_list('bnk_abbr_name','brn_abbr_name'));

    def __init__(self, *args, **kwargs):
        super(BankMembershipForm, self).__init__(*args, **kwargs)

        bank = BankInfo.objects.all();
        self.fields['bank'].choices =[(b.pk, b.bnk_abbr_name+"-"+b.brn_abbr_name)for b in bank]; 

    @staticmethod
#    def label_from_instance(obj):
#        return "My Field name %s" % obj.bnk_abbr_name;
    class Meta:
        model=BankMembership;
        fields=['person','bank','acct_type','acctnbr'];

BankMembershipFormSet = inlineformset_factory(parent_model=PersonalInfo, model=BankInfo.members.through,form=BankMembershipForm,fields=('person','bank','acct_type','acctnbr',), can_delete=True,extra=0);

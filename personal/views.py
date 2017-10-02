from django.shortcuts import render, redirect, get_object_or_404, render_to_response;
from . import person_view, bank_view;
from .models import BankMembership, PersonalInfo, BankInfo;
################################
"""
Start - Person specific functions
"""

def person_list( request, template_name='personal/person_list.html'):
    person = person_view.person();
    return (person.person_list(request=request, template_name=template_name));

def person_create(request, template_name='personal/person_form.html'):
    # create a form instance and populate it with data from the request:
    person = person_view.person();
    pk = None;
    return (person.person_upsert( request, template_name, pk ));

def person_update(request, pk, template_name='personal/person_form.html'):
    person = person_view.person();
    return (person.person_upsert( request=request, template_name=template_name, person_id=pk ));

def person_delete(request, pk, template_name='personal/person_delete.html'):
    person = person_view.person();
    return (person.person_delete(request, pk, template_name));

"""
End - Person specific functions
"""
################################

################################
"""
Start - Bank specific functions
"""

def bank_list( request, template_name='personal/bank_list.html'):
    bank = bank_view.bank();
    return (bank.bank_list(request=request, template_name=template_name));

def bank_create(request, template_name='personal/bank_form.html'):
    # create a form instance and populate it with data from the request:
    bank = bank_view.bank();
    pk = None;
    return (bank.bank_upsert( request, template_name, pk ));

def bank_update(request, pk, template_name='personal/bank_form.html'):
    bank = bank_view.bank();
    return (bank.bank_upsert( request=request, template_name=template_name, bank_id=pk ));

def bank_delete(request, pk, template_name='personal/bank_delete.html'):
    bank = bank_view.bank();
    return (bank.bank_delete(request=request, bank_id=pk, template_name=template_name));

def bank_details(request, pk, template_name='personal/bank_details_add.html'):
    bank = bank_view.bank();
    return (bank.bank_debit_dtls_upsert(request=request, membership_id=pk, template_name=template_name));

def bank_debit_details_list(request, pk, template_name='personal/bank_debit_details_list.html'):
    bank = bank_view.bank();
    return (bank.bank_debit_dtls_list(request=request, membership_id=pk, template_name=template_name));

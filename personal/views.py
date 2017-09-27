from django.shortcuts import render, redirect, get_object_or_404
from django_tables2 import RequestConfig

from django.http import Http404, HttpResponseRedirect, HttpResponse;

from django.forms.models import inlineformset_factory

from .forms import PersonalInfoForm, PersonPhoneInfoForm, PersonAddressInfoForm;

from .models import PersonalInfo, PhoneInfo, AddressInfo;

from .tables import PersonTable;



def person_list( request, template_name='personal/person_list.html'):
    """
    persons = PersonalInfo.objects.all();
    data = {};
    data['person_list'] = persons;
    return render(request, template_name, {'person': persons});
    """
    table = PersonTable(PersonalInfo.objects.all());
    RequestConfig(request).configure(table);
    return render(request, template_name, {'table':table});

def person_create(request, template_name='personal/person_form.html'):
    # create a form instance and populate it with data from the request:
    form = PersonalInfoForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        form.save();
        return redirect('personal:person_list');
    return render(request, template_name, {'form':form});

def person_update(request, pk, template_name='personal/person_form.html'):
    person = get_object_or_404(PersonalInfo, pk=pk)
    form = PersonalInfoForm(request.POST or None, instance=person);
    if form.is_valid():
        form.save();
        return redirect('personal:person_list');
    return render(request, template_name, {'form':form});

def person_delete(request, pk, template_name='personal/person_delete.html'):
    person = get_object_or_404(PersonalInfo, pk=pk)
    if (request.method == 'POST'):
        person.delete();
        return redirect('personal:person_list');
    return render(request, template_name, {'object':person});

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonalInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            first_name  = form.cleaned_data['first_name'];
            middle_name = form.cleaned_data['middle_name'];
            last_name   = form.cleaned_data['last_name'];
#            dob         = form.cleaned_data['dob'];
            emailid     = form.cleaned_data['emailid'];
            gender      = form.cleaned_data['gender'];
            age         = form.cleaned_data['age'];
            form.save();
            return HttpResponseRedirect('index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonalInfoForm()

    return render(request, 'personal/index.html', {'form': form})

def index(request):
    return(get_name(request));



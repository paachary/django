from django.shortcuts import render, redirect, get_object_or_404;

from django_tables2 import RequestConfig;

from django.http import HttpResponseRedirect;

from .forms import PersonalInfoForm, PersonPhoneInfoForm, PersonAddressInfoForm, PhonesFormSet, AddressFormSet ;

from .models import PersonalInfo, PhoneInfo, AddressInfo;

from .tables import PersonTable;

class person:

    def __init__(self):
        None;

    def __get_person_id ( self, personDetails, person_id ):
        return (get_object_or_404( personDetails, pk=person_id ));

    def __gen_person_form( self, request, template_name, person_id ):
        if ( person_id == None ):
            Person =  PersonalInfo();
        else:
            Person = person.__get_person_id(self, personDetails=PersonalInfo, person_id=person_id);

        if request.method == "POST":
            form = PersonalInfoForm(request.POST or None, instance=Person);
            phoneformset = PhonesFormSet(request.POST, request.FILES, instance=Person);

            addformset = AddressFormSet(request.POST, request.FILES, instance=Person);

            if (form.is_valid() 
              and phoneformset.is_valid() 
              and addformset.is_valid()
               ):
                form.save();
                phoneformset.save();
                addformset.save();
                return redirect('personal:person_list');
        else:
                form = PersonalInfoForm(instance=Person);
                phoneformset = PhonesFormSet(instance=Person);
                addformset = AddressFormSet(instance=Person);

        return render(request, template_name, {
           'form':form ,
            'phoneformset':phoneformset,
            'addformset':addformset
        });

    def person_list( self, request, template_name):
        table = PersonTable(PersonalInfo.objects.all());
        RequestConfig(request).configure(table);
        return render(request, template_name, {'table':table});

    def person_delete( self,request, pk, template_name):
        Person = person.__get_person_id(self,personDetails=PersonalInfo, person_id=pk);

        if (request.method == 'POST'):
            Person.delete();
            return redirect('personal:person_list');
        return render(request, template_name, {'object':Person});

    def person_upsert( self, request, template_name, person_id=None):
        # create a form instance and populate it with data from the request:
        return (person.__gen_person_form(self,request=request, template_name=template_name, person_id=person_id ));

#####################################################
"""
The follownig code is not being used.
"""
######################################################
    def index( self,request):
        return(get_name(request));

    def get_name( self,request):
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
#                dob         = form.cleaned_data['dob'];
                emailid     = form.cleaned_data['emailid'];
                gender      = form.cleaned_data['gender'];
                age         = form.cleaned_data['age'];
                form.save();
                return HttpResponseRedirect('index.html')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PersonalInfoForm()

        return render(request, 'personal/index.html', {'form': form})
###################################################################

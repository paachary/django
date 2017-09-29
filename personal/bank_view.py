from django.shortcuts import render, redirect, get_object_or_404;

from django_tables2 import RequestConfig;

from django.http import HttpResponseRedirect;

from .models import BankInfo;

from .tables import BankTable;

from .forms import BankInfoForm;

## An individual class specific for bank whose methods and invoked from the django view
class bank:

    def __init__(self):
        None;

    def __get_bank_id(self, bankDetails, bank_id):
        return (get_object_or_404(bankDetails, pk=bank_id));

    def __gen_bank_form( self, request, template_name, bank_id ):
        if ( bank_id == None ):
            Bank =  BankInfo();
        else:
            Bank = bank.__get_bank_id(self, bankDetails=BankInfo, bank_id=bank_id);

        if request.method == "POST":
            form = BankInfoForm(request.POST or None, instance=Bank);

            if (form.is_valid()
               ):
                form.save();
                return redirect('personal:bank_list');
        else:
                form = BankInfoForm(instance=Bank);

        return render(request, template_name, {
           'form':form ,
        });

    def bank_upsert(self, request, template_name, bank_id):
        return (bank.__gen_bank_form(self,request=request, template_name=template_name, bank_id=bank_id ));

    def bank_delete(self, request, template_name, bank_id):
        Bank = bank.__get_bank_id(self,bankDetails=BankInfo, bank_id=bank_id);
        if (request.method == 'POST'):
            Bank.delete();
            return redirect('personal:bank_list');
        return render(request, template_name, {'object':Bank});

    def bank_list(self, request, template_name):
        table = BankTable(BankInfo.objects.all());
        RequestConfig(request).configure(table);
        return render(request, template_name, {'table':table});

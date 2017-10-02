# tutorial/tables.py
import django_tables2 as tables;

from django_tables2.utils import A;

from .models import PersonalInfo, BankInfo, BankDebitDetails;

class PersonTable(tables.Table):
    edit_column = tables.LinkColumn('personal:person_edit', text="Link", args=[A('pk')]);
    delete_column = tables.LinkColumn('personal:person_delete', text="Link", args=[A('pk')]);

    def __init__(self, *args, _overriden_value="",**kwargs):
        super().__init__(*args, **kwargs);

        self.base_columns['edit_column'].verbose_name = "Edit";
        self.base_columns['delete_column'].verbose_name = "Delete";
        self.base_columns['emailid'].verbose_name = "Email Id";

    class Meta:
        fields = ['first_name','middle_name','last_name','emailid','edit_column','delete_column'];
        model = PersonalInfo;
        #exclude = ('id','dob', )
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class BankTable(tables.Table):
    edit_column = tables.LinkColumn('personal:bank_edit', text="Link", args=[A('pk')]);
    delete_column = tables.LinkColumn('personal:bank_delete', text="Link", args=[A('pk')]);

    def __init__(self, *args, _overriden_value="",**kwargs):
        super().__init__(*args, **kwargs);

        self.base_columns['edit_column'].verbose_name = "Edit";
        self.base_columns['delete_column'].verbose_name = "Delete";

    class Meta:
        fields=['name','branch'];
        model = BankInfo;
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}

class BankDebitDetailsTable(tables.Table):

    def __init__(self, *args, _overriden_value="",**kwargs):
        super().__init__(*args, **kwargs);

    debit_year_month = tables.Column(accessor='get_year_month', verbose_name='Year Month');
    class Meta:
        model = BankDebitDetails;
        fields=['debit_year_month','debit_type','debit_desc','amount','remarks'];
        attrs= {'class' : 'paleblue' }

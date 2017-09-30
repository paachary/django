from django.core.validators import RegexValidator;
from django.db import models;

# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=500, default=None, verbose_name="First Name");
    middle_name = models.CharField(max_length=500, default=None);
    last_name = models.CharField(max_length=500, default=None);
    gender = models.CharField(choices=(("M", ("Male")),
                                       ("F", ("Female"))), max_length=2);
    age = models.IntegerField(default = 0);
    dob = models.DateField(default=None, null=True , verbose_name="Date of Birth");
    emailid = models.CharField(max_length=500, default=None, verbose_name="Email ID");

    def __str__(self):
        return  (self.first_name+":"+
                 self.middle_name+":"+
                 self.last_name+":"+
                 self.gender+":"+
                 self.emailid);

    def custom_function(self):
        return "Link";

    class Meta:
        unique_together = ('first_name', 'middle_name', 'last_name');

class PhoneInfo(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    phone_type = models.CharField(choices=(("R",("Residence")),
                                           ("O",("Office")),
                                           ("M",("Mobile"))), max_length=1, default='R', verbose_name="Type");
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_nbr = models.CharField(validators=[phone_regex], max_length=15, blank=True, verbose_name="Phone Number");

    class Meta:
        unique_together = ('person', 'phone_type', 'phone_nbr');

class AddressInfo(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    address_type = models.CharField(choices=(("P", ("Permanent")),
                                             ("T", ("Temporary"))), max_length=1, default='P');
    door = models.IntegerField(default = 0, verbose_name="Door #");
    street = models.CharField(max_length=200, verbose_name="Street Name");
    pin = models.IntegerField(default = 0, verbose_name="Pin Code");
    city = models.CharField(max_length=50);
    state = models.CharField(max_length=50);
    country = models.CharField(max_length=50);

    class Meta:
        unique_together = ('person', 'address_type');

class BankInfo(models.Model):
    name = models.CharField(max_length=2000, verbose_name="Bank Name");
    bnk_abbr_name = models.CharField(max_length=200, verbose_name="Bank Short Name", null=True,default=None);
    branch = models.CharField(max_length=2000, verbose_name="Branch Name",null=True,default=None);
    brn_abbr_name = models.CharField(max_length=200, verbose_name="Branch Short Name", null=True, default=None);
    address = models.CharField(max_length=2000, verbose_name="Branch Address");
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_nbr = models.CharField(validators=[phone_regex], max_length=15, blank=True, verbose_name="Branch Phone Number");
    members = models.ManyToManyField(PersonalInfo, through='BankMembership', verbose_name="Membership between person and bank");

    class Meta:
        unique_together = ('name', 'branch');

    def __str__(self):
        return u'{0}'.format(self.bnk_abbr_name+"-"+brn_abbr_name);

class BankMembership(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    bank = models.ForeignKey(BankInfo, on_delete=models.CASCADE);
    acct_nbr_regex = RegexValidator(regex=r'^[1-9]\d*$', message="Phone number must be entered in a number format.")
    acctnbr = models.CharField(validators=[acct_nbr_regex], max_length=15, blank=True, verbose_name="Account Number");
    acct_type = models.CharField(choices=(("SB" ,("Savings Bank Account")),
                                          ("FD" ,("Fixed Deposit")),
                                          ("RD" ,("Recurring Deposit"))), max_length=2, default='SB', verbose_name="Account Type");

    class Meta:
        unique_together = ('person', 'bank', 'acct_type', 'acctnbr');


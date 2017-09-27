from django.db import models

# Create your models here.


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=500, default=None);
    middle_name = models.CharField(max_length=500, default=None);
    last_name = models.CharField(max_length=500, default=None);
    gender = models.CharField(choices=(("M", ("Male")),
                                       ("F", ("Female"))), max_length=2);
    age = models.IntegerField(default = 0);
    dob = models.DateField(default=None, null=True);
    emailid = models.CharField(max_length=500, default=None);

    def __str__(self):
        return  (self.first_name+":"+
                 self.middle_name+":"+
                 self.last_name+":"+
                 self.gender+":"+
                 self.emailid);

    def custom_function(self):
        return "Link";

class PhoneInfo(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    phone_type = models.CharField(max_length=1, default='R');
    phone_nbr = models.IntegerField(default = 0);

class AddressInfo(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    address_type = models.CharField(choices=(("P", ("Permanent")),
                                             ("T", ("Temporary"))), max_length=1, default='P');
    door = models.IntegerField(default = 0);
    street = models.CharField(max_length=200);
    pin = models.IntegerField(default = 0);
    city = models.CharField(max_length=50);
    state = models.CharField(max_length=50);
    country = models.CharField(max_length=50);

class BankInfo(models.Model):
    name = models.CharField(max_length=2000);
    branch = models.CharField(max_length=2000);
    address = models.CharField(max_length=2000);
    phone_nbr = models.IntegerField(default = 0);
    members = models.ManyToManyField(PersonalInfo, through='BankMembership');

class BankMembership(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE);
    bank = models.ForeignKey(BankInfo, on_delete=models.CASCADE);
    acctnbr = models.IntegerField(default = 0);
    acct_type = models.CharField(choices=(("SB" ,("Savings Bank Account")),
                                          ("FD" ,("Fixed Deposit")),
                                          ("RD" ,("Recurring Deposit"))), max_length=2, default='SB');


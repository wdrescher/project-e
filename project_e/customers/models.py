from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from hashid_field import HashidAutoField
#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(models.Model):
    cust_id = HashidAutoField(primary_key=True, allow_int_lookup=True)
    #salesman = models.ForeignKey(AbstractUser, blank=True, null=True, on_delete=models.CASCADE)
    #cont_name = models.CharField(_("Contractor Name"), blank=False, max_length=500)
    cust_email = models.CharField(_("Customer Email"), blank=False, max_length=500)
    address = models.CharField(_("Address"), blank=False, max_length=500)
    fname = models.CharField(_("First Name"), blank=False, max_length=30)
    lname = models.CharField(_("Last Name"), blank=False, max_length=30)
    phone = models.CharField(_("Phone Number"), blank=False, max_length=10)
    notes = models.CharField(_("Misc Notes"), blank=False, max_length=500)
    vin = models.CharField(_("VIN"), blank=False, max_length=50)
    car_make = models.CharField(_("Car Make"), blank=True, max_length=30)
    car_model = models.CharField(_("Car Model"), blank=True, max_length=30)
    #dealerid = ..dealers.models.???
    #salesman

    def get_absolute_url(self):
        return reverse("customers:detail", kwargs={"pk": self.cust_id.id})

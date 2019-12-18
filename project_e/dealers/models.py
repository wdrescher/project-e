from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Dealer(models.Model): 
    address = models.CharField(_("Address"), blank=False, max_length=500)
    name = models.CharField(_("Name"), blank=False, max_length=200)

    def get_absolute_url(self): 
        return reverse("dealers:detail", kwargs={"pk": self.id})
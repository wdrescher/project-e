from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

# settings.configure()

# Create your models here.
class Dealer(models.Model):
    #ref_id = models.AutoField(primary_key=True)
    address = models.CharField(_("Address"), blank=False, max_length=500)
    name = models.CharField(_("Name"), blank=False, max_length=200)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ref_id

    def get_absolute_url(self):
        return reverse("dealers:detail", kwargs={"pk": self.id})

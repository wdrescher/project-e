from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DealersConfig(AppConfig):
    name = 'project_e.dealers'
    verbose_name = _("Dealers")
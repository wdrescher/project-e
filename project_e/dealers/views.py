from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
#from django.views.generic.edit import AddCustView
from django.contrib.auth.mixins import LoginRequiredMixin
from project_e.dealers.forms import DealerCreationForm
#from project_e.dealers.forms import DealerAddCustForm
from project_e.customers.forms import DealerAddCustForm
from project_e.dealers.models import Dealer
from project_e.customers.models import Customer


class DealerCreationView(CreateView):
    model = Dealer
    fields = ["name", "address"]

class DealerDetailView(LoginRequiredMixin, DetailView):
    model = Dealer

class DealerAddCustView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ["cust_email", "cust_address", "fname", "lname", "phone", "vin"]

dealer_detail_view = DealerDetailView.as_view()
dealer_creation_view = DealerCreationView.as_view()
dealer_addcust_view = DealerAddCustView.as_view()

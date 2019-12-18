from django.shortcuts import render
from django.views.generic.edit import CreateView 
from django.views.generic import DetailView 
from project_e.dealers.forms import DealerCreationForm
from project_e.dealers.models import Dealer
from django.contrib.auth.mixins import LoginRequiredMixin

class DealerCreationView(CreateView): 
    model = Dealer
    fields = ["name", "address"]

class DealerDetailView(LoginRequiredMixin, DetailView): 
    model = Dealer

dealer_detail_view = DealerDetailView.as_view()
dealer_creation_view = DealerCreationView.as_view()

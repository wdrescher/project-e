from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from project_e.dealers.models import Dealer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()


class DealerCreationView(CreateView):
    model = Dealer
    fields = ["name", "address"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class DealerDetailView(LoginRequiredMixin, DetailView):
    model = Dealer

class DealerVerifyView(LoginRequiredMixin, ListView):
    queryset = User.objects.all()

    def get_queryset(self):
        dealer = self.request.user.dealership
        return User.objects.filter(dealership=dealer)
        
dealer_user_verify_view = DealerVerifyView.as_view()
dealer_detail_view = DealerDetailView.as_view()
dealer_creation_view = DealerCreationView.as_view()

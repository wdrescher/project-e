from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from project_e.dealers.models import Dealer

User = get_user_model()

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()

class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name", "dealership"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class UserAddDealerView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        dealer = Dealer.objects.get(ref_id=kwargs['ref_id'])
        self.request.user.dealership = dealer
        self.request.user.sales = True
        self.request.user.verified= False
        self.request.user.save(update_fields=['dealership', 'sales', 'verified'])
        return reverse("users:detail", kwargs={"username": self.request.user.username})

user_add_dealer_view = UserAddDealerView.as_view()

class UserVerifyView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(id=kwargs['user_id'])
        if user:
            user.verified = not user.verified
            user.save(update_fields=['verified'])
        return  reverse("dealers:verify")
user_verify_view = UserVerifyView.as_view()

class UserRemoveView(LoginRequiredMixin, RedirectView): 
    def get_redirect_url(self, *args, **kwargs): 
        user = User.objects.get(id=kwargs["user_id"])
        user.dealership = None
        user.verified = False
        user.sales = False
        user.save(update_fields=["dealership", "verified", "sales"])
        return reverse("dealers:verify")

user_remove_view = UserRemoveView.as_view()
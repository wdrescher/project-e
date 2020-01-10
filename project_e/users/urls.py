from django.urls import path

from project_e.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_add_dealer_view,
    user_add_contractor_view,
    user_add_customer_view
)

app_name = "users"
urlpatterns = [
    path("add-dealer/", view=user_add_dealer_view, name="add-dealer"),
    path("add-contractor/", view=user_add_contractor_view, name="add-contractor"),
    path("add-customer/", view=user_add_customer_view, name="add-customer"),
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail")
]

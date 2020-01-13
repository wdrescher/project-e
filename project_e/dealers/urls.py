from django.urls import path

from project_e.dealers.views import (
    dealer_creation_view, 
    dealer_detail_view, 
    dealer_user_verify_view
)

app_name = "dealers"
urlpatterns = [
    path("create/", view=dealer_creation_view, name="create"),
    path("<int:pk>/", view=dealer_detail_view, name="detail"),
    path("verify/", view=dealer_user_verify_view, name="verify")
]

from django.urls import path

from project_e.dealers.views import (
    dealer_creation_view,
    dealer_detail_view,
    dealer_addcust_view
)

# from project_e.customers.views import (
#     dealer_addcust_view
# )

app_name = "dealers"

urlpatterns = [
    path("create/", view=dealer_creation_view, name="create"),
    path("<int:pk>/", view=dealer_detail_view, name="detail"),
    path("<int:pk>/", view=dealer_addcust_view, name="addnewcust")
]

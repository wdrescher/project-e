from django.urls import path

from project_e.users.views import (
    user_redirect_view,
    user_update_view,
    user_detail_view,
    user_add_dealer_view
)

app_name = "users"
urlpatterns = [
    path("add-dealer/", view=user_add_dealer_view, name="add-dealer"),
    path("redirect/", view=user_redirect_view, name="redirect"),
    path("update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail")
]

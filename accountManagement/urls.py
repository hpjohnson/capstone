from django.urls import path
from .views import account_management_page_view

urlpatterns = [
    path("", account_management_page_view, name="account_management_page"),
]
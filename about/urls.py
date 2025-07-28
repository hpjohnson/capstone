from django.urls import path
from .views import about_page_view

urlpatterns = [
    path("about/", about_page_view, name="about"),
]
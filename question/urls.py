from django.urls import path
from .views import question_page_view

urlpatterns = [
    path("", question_page_view, name="question_page"),
]
from django.urls import path
from .views import manage_questions_page_view

urlpatterns = [
    path("", manage_questions_page_view, name="manage_questions_page"),
]
from django.urls import path
from .views import manage_questions_page_view, create_question_view

urlpatterns = [
    path("", manage_questions_page_view, name="manage_questions_page"),
    path("create_question/", create_question_view, name="create_question_view"),
]
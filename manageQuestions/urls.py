from django.urls import path
from .views import manage_questions_page_view, create_question_view, edit_question_view, delete_question_view

urlpatterns = [
    path("", manage_questions_page_view, name="manage_questions_page"),
    path("create_question/", create_question_view, name="create_question_view"),
    path("delete_question/<int:question_id>/", delete_question_view, name="delete_question_view"),
    path("edit_question/<int:question_id>/", edit_question_view, name="edit_question_view"),
]
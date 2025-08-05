from django.urls import path
from . import views as views


urlpatterns = [
    path("", views.manage_questions_page_view, name="manage_questions_page"),
    path("create_question/", views.create_question_view,
         name="create_question_view"),
    path("delete_question/<int:question_id>/",
         views.delete_question_view, name="delete_question_view"),
    path("edit_question/<int:question_id>/",
         views.edit_question_view, name="edit_question_view"),
]

from django.shortcuts import render
from .models import Question

# Create your views here.
def question_page_view(request):
    """
    render question page
    """

    #get all of the questions
    questions = Question.objects.all()

    return render(request, "question/question.html", {"questions": questions}, )
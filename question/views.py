from django.shortcuts import render

# Create your views here.
def question_page_view(request):
    """
    render question page
    """
    return render(request, "question/question.html", )
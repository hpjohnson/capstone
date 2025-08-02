from django.shortcuts import render

# Create your views here.
def manage_questions_page_view(request):

    return render(request, "manageQuestions/manageQuestions.html", )
from django.shortcuts import render
from question.models import Question

# Create your views here.
def manage_questions_page_view(request):

    # get the users uploaded questions
    questions = Question.objects.filter(userID=request.user)
    
    # testing stuff, delete this later
    # print(questions)
    # print(questions[0].questionID)

    return render(request, "manageQuestions/manageQuestions.html", {"questions": questions}, )
from django.shortcuts import render
from question.models import Question
from .forms import QuestionCreateForm

# Create your views here.
def manage_questions_page_view(request):

    # get the users uploaded questions
    questions = Question.objects.filter(userID=request.user)
    
    # testing stuff, delete this later
    # print(questions)
    # print(questions[0].questionID)

    #create or process the form
    if request.method == "POST":
        question_create_form = QuestionCreateForm(request.POST)
        if question_create_form.is_valid():
            question = question_create_form.save(commit=False)
            question.userID = request.user
            question.save()

    else:
        question_create_form = QuestionCreateForm()

    question_create_form = QuestionCreateForm()

    return render(request, "manageQuestions/manageQuestions.html", {"questions": questions, "question_create_form": question_create_form}, )
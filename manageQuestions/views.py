from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from question.models import Question
from .forms import QuestionCreateForm, QuestionEditForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def manage_questions_page_view(request):
    """
    view that loads the users own questions page
    """

    # get the users uploaded questions
    questions = Question.objects.filter(userID=request.user)

    # create the form for creating questions
    question_create_form = QuestionCreateForm()

    # create the form for editing questions (can use the same form model)
    question_edit_form = QuestionEditForm()

    return render(request, "manageQuestions/manageQuestions.html",
                  {"questions": questions,
                   "question_create_form": question_create_form,
                   "question_edit_form": question_edit_form}, )


@login_required
def create_question_view(request):
    """
    view that handles the creation of the users own questions
    """

    if request.method == "POST":
        question_create_form = QuestionCreateForm(request.POST)
        if question_create_form.is_valid():
            question = question_create_form.save(commit=False)
            question.userID = request.user
            question.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Question successfully uploaded.")
            return HttpResponseRedirect(reverse("manage_questions_page"))

        else:
            messages.add_message(request, messages.ERROR, "Form not valid.")
            return HttpResponseRedirect(reverse("manage_questions_page"))
    else:
        return HttpResponseRedirect(reverse("manage_questions_page"))


@login_required
def edit_question_view(request, question_id):
    """
    view that handles the editing of questions
    """

    # get the question
    question = get_object_or_404(Question, pk=question_id)

    # update the question
    if request.method == "POST":
        question_edit_form = QuestionEditForm(request.POST, instance=question)
        if question_edit_form.is_valid() and question.userID == request.user:
            question = question_edit_form.save(commit=False)
            question.updateCount = question.updateCount + 1
            question.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Question successfully edited.")
            return HttpResponseRedirect(reverse("manage_questions_page"))

        else:
            messages.add_message(request, messages.ERROR, "Form not valid.")
            return HttpResponseRedirect(reverse("manage_questions_page"))
        
    return HttpResponseRedirect(reverse("manage_questions_page"))


@login_required
def delete_question_view(request, question_id):
    """
    view to delete question
    """

    # get the question
    question = get_object_or_404(Question, pk=question_id)

    # delete
    if question.userID == request.user:
        question.delete()
        messages.add_message(request, messages.SUCCESS,
                             "Question successfully deleted.")
    else:
        messages.add_message(request, messages.ERROR,
                             "An unexpected error occured.")

    return HttpResponseRedirect(reverse("manage_questions_page"))

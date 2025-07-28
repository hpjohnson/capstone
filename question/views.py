from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def question_page_view(request):
    return HttpResponse("Question Page")
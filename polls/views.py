from ast import Try
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list
    }
    return render(request , 'polls/index.html' , context)

def detail(request , question_id):
    try:
        question = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        raise Http404("Question Doesn't Exist")
    return render(request , 'polls/detail.html' , { 'question':question})

def results(request , question_id):
    return HttpResponse("You'r looking at the results of question %s" %question_id)

def vote(request , question_id):
    return HttpResponse("You'r voting on question %s" %question_id)
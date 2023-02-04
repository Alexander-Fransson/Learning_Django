from django.shortcuts import HttpResponse, render, get_object_or_404
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    results = "You're looking at the results of question %s." 
    return HttpResponse(results % question_id)

def vote(request, question_id):
    results = "You are voteing on question %s."
    return HttpResponse(results % question_id)
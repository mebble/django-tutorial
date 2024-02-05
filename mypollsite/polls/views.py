from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question

def index(request: HttpRequest):
    questions = Question.objects.order_by("-pub_date")
    context = { "questions": questions }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", { "question": q })

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}".encode('ascii'))

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}".encode('ascii'))


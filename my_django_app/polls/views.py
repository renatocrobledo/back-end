# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Question, Layout
from django.http import Http404

def test(request, text):
  return HttpResponse(f'eeeaaa! {text}')

def index(request):
  template = Layout.objects.get()
  # get the last five questions order from newer to older
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  # return HttpResponse(template.render(context, request))
  return render(request, f'{template.template_name}/index.html', context)

def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
    #return HttpResponse("te la pelas no existe !!"
  return render(request, 'polls/detail.html', {'question': question or "notFound"})

def results(request, question_id):
  response = f'You\'re looking at the results of question {question_id}' 
  return HttpResponse(response)

def vote(request, quesiton_id):
  return HttpResponse(f'You \'re voting on question {question_id}')


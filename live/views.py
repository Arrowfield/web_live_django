from django.shortcuts import render

from django.http import HttpResponse

from .models import Question

from django.template import loader

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('live/index.html')
  context = {
    'latest_question_list':latest_question_list,
  }

  #output = ', '.join([q.question_text for q in latest_question_list])
  
  return HttpResponse(template.render(context,request))
  #return HttpResponse('Hello,world . you are at index view ')

def detail(request,question_id):
  return HttpResponse('you are looking at question %s' % question_id) 

def results(request,question_id):
  response = "you are looking at the result of question %s"
  return HttpResponse(response % question_id)

def vote(request,question_id):
  return HttpResponse('you are voting on question %s' %question_id)  
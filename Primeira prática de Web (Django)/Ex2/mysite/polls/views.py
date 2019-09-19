from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
#from django.http import HttpResponse
#from django.template import loader

from .models import Choice, Question

# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#template_name = loader.get_template('polls/index.html')
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context) 

def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise http404("Questão não existe")
	return render(request, 'polls/detail.html',{'question':question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(keyError, Choice.DoesNotExist):
		return render(request, 'polls/detal.html',{
			'question':question,
			'error_message':"você não selecionou uma opção",
			})
		else:
			selected_choice.votes += 1
			selected_choice.save()
			return HttpResponseRedirect(reverse('polls:results',
				args=(question_id,)))	
def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})
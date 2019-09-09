from django.shortcuts import render

from django.http import HttpResponse, Http404

# import models
from .models import Questions, Choice


# Create your views here.
#
def index(request):

    # here v order the questions in descending order based on publication date
    # and fetches 5 records. thud we get queryset of questions
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]

    # later v pass this queryset as a dictionary to the template.
    context = {'latest_question_list': latest_question_list}
    return render(request, 'pollsapp/index.html', context)
    # now we can access the data in index.html file


# need to display a specific question and its choices. for tat create a view named detail
def detail(request, question_id):
    pass

    # here v try to get the question from Questions and pass that question as dictionary to the
    # template v render and if no questions exist it raises an http404 error
    # here DoesNotExist is a class of model Questions
    try:
        q = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404('Question not exist')
    return render(request, 'pollsapp/results.html', {'question': q})






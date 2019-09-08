from django.shortcuts import render

from django.http import HttpResponse

# import models
from .models import Questions, Choice


# Create your views here.
#
def index(request):
    return render(request, 'pollsapp/index.html')

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):

    context = {}
    return render(request, 'master/index.html', context)
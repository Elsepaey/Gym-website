from django.shortcuts import render
from django.http import HttpResponse
from .models import machine


# Create your views here.
def index(request):
    context = {
        'machines': machine.objects.all()
    }
    return render(request, 'pages/index.html', context)


def about(request):

    return render(request, 'pages/about.html')

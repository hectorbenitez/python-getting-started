from django.shortcuts import render
from django.http import HttpResponse
from os import getenv

from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!' % getenv("COMMIT_HASH"))


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


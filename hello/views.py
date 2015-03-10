from django.shortcuts import render
from django.http import HttpResponse
from os import getenv

from .models import Greeting


# Create your views here.
def index(request):
	commit_hash = getenv('COMMIT_HASH', 'Not COMMIT_HASH')
	return HttpResponse('Hello from Python! ' % commit_hash)


def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})


from django.shortcuts import render
from django.http import HttpResponse
from os import getenv

from .models import Greeting


# Create your views here.
def index(request):
	commit_hash = getenv('COMMIT_HASH', 'Not COMMIT_HASH')
	heroku_slug = getenv('HEROKU_SLUG', 'Not HEROKU_SLUG')
	return HttpResponse('Hello from Python! {} {}'.format(commit_hash, heroku_slug))


def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, 'db.html', {'greetings': greetings})


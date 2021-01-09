from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	testing = "Profiled Playlist"
	return render(request, 'index.html', {
		'testing' : testing,
		})
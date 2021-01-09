from django.shortcuts import render
from django.http import HttpResponse
from spotify.views import IsAuthenticated
# Create your views here.



def home(request):
	testing = "Profiled Playlist"
	testing = IsAuthenticated.get(request, None)
	return render(request, 'index.html', {
		'testing' : testing,
		})
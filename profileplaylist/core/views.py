from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	testing = "Profiled Playlist"
	if request.method == 'POST':
		spotify = SpotifyAPI()
		spotify.get_user_tracks()
		spotify.get_user_top_tracks()
		spotify.get_user_top_artists()
		
	return render(request, 'index.html', {
		'testing' : testing,
		})

def about(request):
	testing = "Profiled Playlist"
	return render(request, 'about.html', {
		'testing' : testing,
		})

def comparison(request):
	testing = "Profiled Playlist"
	return render(request, 'comparison.html', {
		'testing' : testing,
		})
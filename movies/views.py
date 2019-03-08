from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    #Movie.objects.filter(release_year=1984)
    #output = ','.join([m.title for m in movies])
    return render(request, 'movies/index.html', {'movies': movies})

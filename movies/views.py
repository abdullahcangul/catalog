from django.shortcuts import get_object_or_404, render
from .models import Movie
from django.http.response import Http404
# Create your views here.



def liste(req):
    movies=Movie.objects.all()
    content={
    "movies":movies
    }
    return render(req,'movies/list.html',content)
def detail(req,movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    content={
    "movie":movie
    }
    return render(req,'movies/detail.html',content)
def search(req):
    return render(req,'movies/search.html')

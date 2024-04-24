from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "movies/index.html", {"title": "My Fav Movies", "movies": ["godfather", "once upon a time in the west", "young at heart"]})

def about(request):
    return render(request, "movies/about.html", {})
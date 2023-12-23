from django.shortcuts import render
from django.http import HttpResponse
from .models import BoardGame, Review, Rating, Comment, User



# Create your views here.
#homepage
def home(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews':reviews})


#specific board game review
def review(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'review.html', {'review':review.title})

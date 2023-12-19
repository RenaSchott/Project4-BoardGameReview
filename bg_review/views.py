from django.shortcuts import render
from django.http import HttpResponse
from .models import BoardGame, Review, Rating, Comment, User



# Create your views here.
#homepage
def home(request):
    return render(request, 'index.html')


#specific board game review
def boardgame(request, id):
    ls = Review.objects.get(id=id)
    bg_review = ls.review_set.all()
    bg_rating = ls.rating_set.all()
    bg_comment = ls.comment_set.all()
    return render(request, '' %(ls.name, review.title, rating.rating. comment.content))

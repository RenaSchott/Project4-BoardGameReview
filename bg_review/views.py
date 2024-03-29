from django.shortcuts import render
from .models import BoardGame, Review, Rating, CommentUser, CommentGuest



# Create your views here.
#homepage
def home(request):
    reviews = Review.objects.filter(status=1)
    return render(request, 'index.html', {'reviews':reviews})


#specific board game review
def single_review(request, id):
    review = Review.objects.get(id=id)
    rated = Rating.objects.filter(status=1)
    comments = Comment.object.filter(status=1)
    return render(request, 'review.html',   {
                "review": review,
                "comments": comments,
                "rated": rating,
            },)

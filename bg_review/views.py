from django.shortcuts import render
from django.views import generic
from .models import BoardGame, Review, Rating, CommentUser, CommentGuest



# Create your views here.
#homepage
class ReviewList(generic.ListView):
    """
    All reviews displayed in a list
    """
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = 'index.html'


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

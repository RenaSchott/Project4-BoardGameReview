from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import BoardGame, Review, Rating, Comment



# Create your views here.
#homepage
class ReviewList(generic.ListView):
    """
    All reviews displayed in a list
    """
    model = Review
    queryset = Review.objects.order_by('-created_on')
    print(queryset)
    template_name = "index.html"
    paginate_by = 6


#specific board game review
def single_review(request, slug):
    """
    All details for one review are displayed
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    rated = Rating.objects.filter(status=1)
    #comment = Comment.object.filter(status=1)
    return render(request, 'single_review.html',
                {"review": review},
            )

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import BoardGame, Review, Rating, Comment
from .forms import CommentForm



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
    comments = Review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.writer = request.user
            comment.review = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()
    
    return render(request, 'single_review.html',
                {
                    "review": review,
                    "comments": comments,
                    "comment_count": comment_count,
                    "comment_form": comment_form,            
            },)

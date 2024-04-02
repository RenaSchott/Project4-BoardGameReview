from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import BoardGame, Review, Rating, Comment
from .forms import CommentForm


class ReviewList(generic.ListView):
    """
    All reviews displayed in a list
    """
    model = Review
    queryset = Review.objects.order_by('-created_on')
    template_name = "index.html"
    paginate_by = 6


def single_review(request, slug):
    """
    All details for one review are displayed
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    rated = Rating.objects.filter(status=1)
    comments = review.comments.all().order_by("-created_on")
    comment_count = review.comments.filter(approved=True).count
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.writer = request.user
            # comment.content = review
            comment.comment = review
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


def comment_edit(request, slug, comment_id):
    """
    Edit comments
    """
    if request.method == "POST":

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.writer == request.user:
            comment = comment_form.save(commit=False)
            comment.comment = review
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('single_review', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete comments
    """
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.writer == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('single_review', args=[slug]))

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATE = ((0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))


# Model for board games
class BoardGame(models.Model):
    """
    Stores a single board game entry
    (related to :model:`auth.User`)
    """
    bg_name = models.CharField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="user")
    created_on = models.DateTimeField(auto_now_add=True)
    bg_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on", "approved"]

    def __str__(self):
        return self.bg_name


# Model for reviews
class Review(models.Model):
    """
    Stores a single review for a specific board game entry
    (related to :model:`auth.User`, :model: `bg_review.BoardGame`)
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="author")
    bg_name = models.ForeignKey(
        BoardGame, on_delete=models.CASCADE, related_name="bg")
    review_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    short = models.TextField(default="an_excerpt")

    class Meta:
        ordering = ["created_on", "approved"]

    def __str__(self):
        return self.title


# Model for rating
class Rating(models.Model):
    """
    Stores a single rating for a specific review entry
    (related to :model:`auth.User`, :model: `bg_review.Review`)
    """
    visitor = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="visitor")
    rating = models.IntegerField(choices=RATE, default=0)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="review")
    help_text = "Please rate the board game from  0 = horrible board\
        game to 10 = fantastic board game."
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.rating} as rating for {self.review} by {self.visitor}"


# Model for user comments
class Comment(models.Model):
    """
    Stores a single comment for a specific review entry 
    (related to :model:`auth.User`, :model: `bg_review.Review`)
    """
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="writer")
    comment = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments")
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["created_on", "approved"]

    def __str__(self):
        return f"Comment added by {self.writer}"

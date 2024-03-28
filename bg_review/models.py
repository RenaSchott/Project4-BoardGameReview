from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
#from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
RATE = ((0, "0"), (0.5, "0.5"), (1, "1"), (1.5, "1.5"), (2, "2"), (2.5, "2.5"), (3, "3"), (3.5, "3.5"), 
(4, "4"), (4.5, "4.5"), (5, "5"), (5.5, "5.5"), (6, "6"), (6.5, "6.5"), (7, "7"), (7.5, "7.5"), (8, "8"), 
(8.5, "8.5"), (9, "9"), (9.5, "9.5"), (10, "10"))

# Model for board games 
class BoardGame(models.Model):
    """ 
    Stores a single board game entry
    """
    bg_name = models.CharField(max_length=200, unique=True) 
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user")
    created_on = models.DateTimeField(auto_now_add=True)
    #bg_image = CloudinaryField('image', default='placeholder')


def __str__(self):
        return self.bg_name


# Model for reviews
class Review(models.Model):
    """ 
    Stores a single review for a specific board game entry
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=get_random_string(length=200))
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="author")
    bg_name = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="bg")
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


def __str__(self):
        return self.title


# Model for rating
class Rating(models.Model):
    """ 
    Stores a single rating for a specific review entry
    """
    visitor = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="visitor", default=get_random_string(length=200))
    rating = models.IntegerField(choices=RATE, default=0)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review")
    help_text = "Please rate the board game from  0 = horrible board game to 10 = fantastic board game."


def __str__(self):
        return f"{self.rating} as rating for {self.review} by {self.visitor}"


# Model for guest comments
class CommentGuest(models.Model):
    """ 
    Stores a single comment for a specific review entry
    """
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    guest = models.CharField(max_length=200, unique=True) 
    blog = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="blog")
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


def __str__(self):
    return f"Comment added to {self.review_id} by {self.guest}"


# Model for user comments
class CommentUser(models.Model):
    """ 
    Stores a single comment for a specific review entry
    """
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="writer")
    comment = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="comment")
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)


def __str__(self):
    return f"Comment added to {self.review_id} by {self.writer}"


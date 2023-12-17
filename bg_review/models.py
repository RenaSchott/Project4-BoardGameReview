from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Model for admin


# Model for board games 
class BoardGame(models.Model):
    """ 
    Stores a single board game entry
    """
    bg_name = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="bg-user")
    created_on = models.DateTimeFirls(auto_now_add=True)
    bg_image = CloudinaryField('image', default='placeholder')


def __str__(self):
        return self.bg_name


# Model for reviews
class Review(models.Model):
    """ 
    Stores a single review for a specific board game entry
    """
    title = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="review-user")
    bg_name = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="review-bg")
    created_on = models.DateTimeFirls(auto_now_add=True)
    content = models.TextField()
    rating = models.ForeignKey(Rating, on_delete=models.RESTRICT, related_name="review-rating")


def __str__(self):
        return self.title


# Model for comment
class Comment(models.Model):
    """ 
    Stores a single comment for a specific review entry
    """
    content = models.TextField()
    created_on = models.DateTimeFirls(auto_now_add=True)
    guest = models.CharField(max_length=200, unique=True) 
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="user-review")


 def __str__(self):
    return f"Comment added to {self.review_id}"


# Model for rating
class Rating(models.Model):
    """ 
    Stores a single rating for a specific review entry
    """
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user-rating")
    rating = [("0", "0"), ("0.5", "0.5"), ("1", "1"), ("1.5", "1.5"), ("2", "2"), ("2.5", "2.5"), ("3", "3"), ("3.5", "3.5"), ("4", "4"), ("4.5", "4.5"), ("5", "5"), ("5.5", "5.5"), ("6", "6"), ("6.5", "6.5"), ("7", "7"), ("7.5", "7.5"), ("8", "8"), ("8.5", "8.5"), ("9", "9"), ("9.5", "9.5"), ("10", "10")]
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="user-review")
    help_text = "Please rate the board game from  0 = horrible board game to 10 = fantastic board game."


def __str__(self):
        return self.rating


# Model for users
class User(models.Model):
    """
    Stores a single user of the site
    """
    user_name = models.CharField("person's user name", max_length=30)
    first_name = models.CharField("person's first name", max_length=30)
    last_name =  models.CharField("person's last name", max_length=30)
    email = = models.EmailField(max_length = 254)
    password =

from django.db import models
import???


# Model for admin


# Model for board games 
class BoardGame(models.Model):
    bg_id = 
    bg_name = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="bg-user")
    created_on = models.DateTimeFirls(auto_now_add=True)


def __str__(self):
        return self.bg_name


# Model for reviews
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="review-user")
    bg_name = models.ForeignKey(bg_name, on_delete=models.RESTRICT, related_name="review-bg")
    created_on = models.DateTimeFirls(auto_now_add=True)
    content = models.TextField()
    rating = models.ForeignKey(rating, on_delete=models.RESTRICT, related_name="review-rating")


def __str__(self):
        return self.title


# Model for comment
class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeFirls(auto_now_add=True)
    guest = models.CharField(max_length=200, unique=True) 
    review_id = models.ForeignKey


 def __str__(self):
        return f"Comment added to {self.review_id}"


# Model for rating
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user-rating")
    rating = [("0", "0"), ("0.5", "0.5"), ("1", "1"), ("1.5", "1.5"), ("2", "2"), ("2.5", "2.5"), ("3", "3"), ("3.5", "3.5"), ("4", "4"), ("4.5", "4.5"), ("5", "5"), ("5.5", "5.5"), ("6", "6"), ("6.5", "6.5"), ("7", "7"), ("7.5", "7.5"), ("8", "8"), ("8.5", "8.5"), ("9", "9"), ("9.5", "9.5"), ("10", "10")]
    review_id = models.ForeignKey


def __str__(self):
        return self.rating


# Model for users

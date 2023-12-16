from django.db import models
import???


# Model for admin


# Model for board games 
class BoardGame(models.Model):
    bg_id = 
    bg_name = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="bg-user")
    created_on = models.DateTimeFirls(auto_now_add=True)


# Model for reviews
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="review-user")
    bg_name = models.ForeignKey(bg_name, on_delete=models.RESTRICT, related_name="review-bg")
    created_on = models.DateTimeFirls(auto_now_add=True)
    content = models.TextField()
    rating = models.ForeignKey(rating, on_delete=models.RESTRICT, related_name="review-rating")


# Model for comment
class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeFirls(auto_now_add=True)
    guest = models.CharField(max_length=200, unique=True) 
    review_id = models.ForeignKey


# Model for rating
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="user-rating")
    rating = models.IntegerField(choices=1-10)
    review_id = models.ForeignKey

# Model for users

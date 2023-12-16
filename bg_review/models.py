from django.db import models
import???


# Model for admin


# Model for board games 
class board_game(models.Model):
    bg_id = 
    bg_name = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="")
    created_on = models.DateTimeFirls(auto_now_add=True)


# Model for reviews
class review(models.Model):
    title = models.CharField(max_length=200, unique=True) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="")
    bg_name = models.ForeignKey(bg_name, on_delete=models.CASCADE, related_name="")
    created_on = models.DateTimeFirls(auto_now_add=True)
    content = models.TextField()
    rating = models.ForeignKey(rating, on_delete=models.CASCADE, related_name="")


# Model for comment
class comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeFirls(auto_now_add=True)
    guest = models.CharField(max_length=200, unique=True) 
    review_id = models.ForeignKey


# Model for rating
class rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="")
    rating = models.IntegerField(choices=1-10)
    review_id = models.ForeignKey

# Model for users

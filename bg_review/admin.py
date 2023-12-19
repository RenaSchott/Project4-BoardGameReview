# Register your models here.
from django.contrib import admin
from .models import BoardGame, Review, Rating, Comment, User


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters(("', fields to prepopulate and rich-text editor'")).
    """
    list_display = ('bg_name', 'user', 'created_on', 'bg_image')
    list_filter = ('user', 'created_on', 'bg_name')
    search_fields = ['bg_name', 'user']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters(("', fields to prepopulate and rich-text editor'")).
    """
    list_display = ('title', 'author', 'bg_name', 'created_on', 'content')
    list_filter = ('author', 'created_on')
    search_fields = ['author', 'bg_name']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters(("', fields to prepopulate and rich-text editor'")).
    """
    list_display = ('user', 'rating', 'review', 'help_text')
    list_filter = ('user', 'review')
    search_fields = ['user', 'rating']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters(("', fields to prepopulate and rich-text editor'")).
    """
    list_display = ('content', 'created_on', 'guest', 'blog')
    list_filter = ('blog', 'created_on')
    search_fields = ['blog']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin(((, fields for search,
    field filters)))(("', fields to prepopulate and rich-text editor'")).
    """
    list_display = ('user_name', 'first_name', 'last_name', 'email')


# Register your models here.
#admin.site.register(BoardGame, BoardGameAdmin)
#admin.site.register(Review, ReviewAdmin)
#admin.site.register(Rating, RatingAdmin)
#admin.site.register(Comment, CommentAdmin)
#admin.site.register(User, UserAdmin)

# Register your models here.
from django.contrib import admin
from .models import BoardGame, Review, Rating, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters.
    """
    list_display = ('bg_name', 'user', 'created_on', 'bg_image')
    list_filter = ('user', 'created_on', 'bg_name')
    search_fields = ['bg_name', 'user']


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Used summernote for the better text editor needed in this case.
    """
    list_display = (
        'title', 'author', 'bg_name', 'created_on', 'content',
        'slug', 'status', 'approved', 'short')
    search_fields = ['title', 'author', 'bg_name']
    list_filter = ('status', 'author', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters.
    """
    list_display = ('visitor', 'rating', 'review', 'help_text')
    list_filter = ('visitor', 'review')
    search_fields = ['visitor', 'rating']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters.
    """
    list_display = (
        'content', 'created_on', 'writer', 'comment', 'updated_on', 'approved')
    list_filter = ('comment', 'created_on', 'approved')
    search_fields = ['comment']

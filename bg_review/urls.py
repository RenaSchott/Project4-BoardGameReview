from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('review/<str:id>', views.review, name='review'),
]
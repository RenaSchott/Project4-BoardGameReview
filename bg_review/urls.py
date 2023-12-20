from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>', views.review, name='review'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.single_review, name='single_review'),
]
from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<str:id>/', views.single_review, name='spec_review'),
]
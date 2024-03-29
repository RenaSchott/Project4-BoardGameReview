from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>/', views.single_review, name='spec_review'),
]
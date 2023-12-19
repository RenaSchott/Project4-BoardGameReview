from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.home, name='home'),
]
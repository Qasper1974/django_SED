from django.urls import path
from dictionary import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ),
    path('question1.html/', views.question1),
    path('question2.html/', views.question2),
    path('question3.html/', views.question3),
    path('question4.html/', views.question4),
    path('question5.html/', views.question5),
  


]

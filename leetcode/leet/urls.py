from django.urls import path
from . import views


urlpatterns = [
    path('', views.home ),
    path('question1/', views.question1),
    path('question2/', views.question2),
    path('question3/', views.question3),
    path('question4/', views.question4),
    path('question5/', views.question5),
  


]

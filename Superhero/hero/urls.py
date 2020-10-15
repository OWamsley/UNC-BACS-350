from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    path('<str:template>', PageView.as_view()),
    path('', HomePageView.as_view()),
    path('hero/<str:hero>/', HeroView.as_view()),
    path('home/', HomePageView.as_view()),
    path('detail/', DetailView.as_view()),
    path('addhero/', HeroEditView.as_view()),
]
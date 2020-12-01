from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from hero import views as core_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('<str:template>', PageView.as_view()),
    path('', HomePageView.as_view()),
    path('hero/<str:hero>/', HeroView.as_view()),
    path('home/', HomePageView.as_view()),
    path('detail/', DetailView.as_view()),
    path('addhero/', HeroEditView.as_view()),
    path('post/<int:pk>/delete', HeroDeleteView.as_view(), name="hero_delete"),
    
]
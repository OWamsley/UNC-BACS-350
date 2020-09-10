from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, HomeView, ProfileView

urlpatterns = [
    path('about/', AboutView.as_view()),
    path('home', HomeView.as_view()),
    path('', HomeView.as_view()),
    path('profile/', ProfileView.as_view()),
]
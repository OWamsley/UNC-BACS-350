from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, HomeView

urlpatterns = [
    path('about',TemplateView.as_view(template_name="about.html")),
    path('home', TemplateView.as_view(template_name="home.html")),
]
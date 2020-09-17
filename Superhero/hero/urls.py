from django.urls import path
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    #path('<str:template>', PageView.as_view()),
    path('', IndexView.as_view()),
    path('hero/<str:hero>', HeroView.as_view()),
    
]
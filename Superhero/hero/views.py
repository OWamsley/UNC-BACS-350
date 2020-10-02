from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Superhero

class PageView(TemplateView):
    def get_template_names(self):
        template_name = self.kwargs.get('template')
        return template_name

    
class IndexView(TemplateView):
    template_name = 'home.html'
    
    
class HeroView(TemplateView):
    def get_template_names(self):
        template_name = 'hero.html'
        return template_name
    
    def get_context_data(self, **kwargs):
        return{
            'hero': self.kwargs.get('hero')
        }
        

class HomePageView(ListView):
    model = Superhero
    template_name = 'home.html'
    context_object_name = "all_heros_list"

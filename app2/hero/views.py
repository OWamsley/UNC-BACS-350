from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'About Page',
            'body': 'about page',
        }
    
class HomeView(TemplateView):
    template_name="home.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Home',
            'info': 'Learn about superheroes!',
            
        }
    
class ProfileView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Title',
            'body': 'body',
        }

class HawkeyeView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Hawkeye',
            'info': 'Hawkeye is Clint Barton, and he is a master marksman. He is cooler in the comics than he is in the movies.',
            'otherHero': 'Rorschach',
            'otherHeroUrl': 'rorschach',
        }
class RorschachView(TemplateView):
    template_name="page.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Rorschach',
            'info': 'Rorschach is an anti-hero from Watchmen, a deconstruction of the idea of superheroes. Rorschach is a vigilante that believes in black and white good and evil.',
            'otherHero': 'Hawkeye',
            'otherHeroUrl': 'hawkeye',
        }
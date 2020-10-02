from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Superhero
from django.core.exceptions import *

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

class InspireView(TemplateView):
    template_name="base.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Inspire',
            'body' : 'What is the purpose of art? For many, its about expressing yourself and sharing that with others. This, Bob Ross does masterfully. Bob Ross is inspiring individual for many reasons.',
            'info' : "There are many figures on tb that try to showcase how important being nice to others is. Bob Ross' wholesome show is among the best. If it weren't for role models such as Bob Ross or Mr. Rogers, modern society wouldn't exist how it does today.",
        }
class AmuseView(TemplateView):
    template_name="base.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Amuse: FakeNameGenerator.com',
            'body' : 'This website will genenerate a name, based on gender, name set, and country of your choosing.',
            'info' : "It's fun to see different names that you may not have heard of, and the different data used in different countries that make up your identity. Try using this website to make you a fake identity when starting a career as a con man.",
        }
    
class EducateView(TemplateView):
    template_name="base.html"
    def get_context_data(self, **kwargs):
        return{
            'title': 'Educate',
            'body' : 'The monty hall problem is a classic brain teaser. You are a contestant in a game show with three doors, one being car, the other two being nothing. After picking a door once, the host opens a door with nothing behind it. You then have the option to stay, or switch.',
            'info' : "It's always better to switch the chosen door. One way to think about this is that the first time you pick a door, you have a 1/3 chance of picking the car. It stays 1/3 if you don't switch. If you do switch, you have a 1/2 chance of picking the car.",
        }
    
def search(request):
    if request.method== 'POST'
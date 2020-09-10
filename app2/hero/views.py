from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name="page.html"
    def get_contect_data(self, **kwargs):
        return{
            'title': 'About Page',
            'body': 'about page',
        }
    
class HomeView(TemplateView):
    template_name="page.html"
    def get_contect_data(self, **kwargs):
        return{
            'title': 'Home Page',
            'body': 'home page',
        }
    
class ProfileView(TemplateView):
    template_name="page.html"
    def get_contect_data(self, **kwargs):
        return{
            'title': 'Title',
            'body': 'body',
        }

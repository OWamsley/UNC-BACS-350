from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from django.views.generic.edit import CreateView
from .models import Superhero
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class PageView(TemplateView):
    def get_template_names(self):
        template_name = self.kwargs.get('template')
        return template_name

    
class IndexView(TemplateView):
    template_name = 'home.html'
    
    
class HeroView(ListView):
    def get_template_names(self):
        template_name = 'hero.html'
        return template_name
    def get_context_data(self, **kwargs):
        return{
            'hero': self.kwargs.get('hero')
        }
    model = Superhero
    context_object_name = "all_heros_list"

class HomePageView(ListView):
    model = Superhero
    template_name = 'home.html'
    context_object_name = "all_heros_list"

class DetailView(ListView):
    template_name = "detail.html"
    
    model = Superhero
    context_object_name = "all_heros_list"
    
class addHeroView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Superhero
    template_name = "create.html"
    context_object_name = "all_heros_list"
    fields = '__all__'
    
class HeroEditView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
    
    
class HeroDeleteView(LoginRequiredMixin, DetailView):
    model = Superhero
    template_name = "hero_delete.html"
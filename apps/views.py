from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView, UpdateView
from apps.models import Users
from apps.forms import UserForm
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'apps/index.html'


class AboutView(TemplateView):
    template_name = 'apps/about.html'


class BlogView(TemplateView):
    template_name = 'apps/blog.html'


class ContactView(TemplateView):
    template_name = 'apps/contact.html'


class ElementView(TemplateView):
    template_name = 'apps/elements.html'


class FacilityView(TemplateView):
    template_name = 'apps/facilites.html'


class MainView(TemplateView):
    template_name = 'apps/main.html'


class PropertyView(TemplateView):
    template_name = 'apps/property.html'


class SingleBlogView(TemplateView):
    template_name = 'apps/single-blog.html'


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('index')


class CustomLoginView(LoginView):
    next_page = 'index'
    redirect_authenticated_user = False
    template_name = 'apps/login.html'
    success_url = reverse_lazy('index')

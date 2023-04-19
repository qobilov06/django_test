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


def elements(request):
    return render(request, 'apps/elements.html')


def facilites(request):
    return render(request, 'apps/facilites.html')


def main(request):
    return render(request, 'apps/main.html')


def property(request):
    return render(request, 'apps/property.html')


def single_blog(request):
    return render(request, 'apps/single-blog.html')


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    template_name = 'apps/register.html'
    success_url = reverse_lazy('index')


class CustomLoginView(LoginView):
    next_page = 'index'
    redirect_authenticated_user = True
    template_name = 'apps/login.html'
    success_url = reverse_lazy('index')

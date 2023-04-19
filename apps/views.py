from django.shortcuts import render


def index(request):
    return render(request, 'apps/index.html')


def about(request):
    return render(request, 'apps/about.html')


def blog(request):
    return render(request, 'apps/blog.html')


def contact(request):
    return render(request, 'apps/contact.html')


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


def login(request):
    return render(request, 'apps/login.html')
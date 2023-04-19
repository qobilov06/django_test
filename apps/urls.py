from django.urls import path

from apps.views import *
from apps.views import CustomLoginView, RegisterView,IndexView

urlpatterns = [path('', IndexView, name='index'),
               path('about/', about, name='about'),
               path('blog/', blog, name='blog'),
               path('contact/', contact, name='contact'),
               path('elements/', elements, name='elements'),
               path('facilites/', facilites, name='facilites'),
               path('main/', main, name='main'),
               path('property/', property, name='property'),
               path('single_blog/', single_blog, name='single_blog'),
               path('login/', CustomLoginView.as_view(), name='login'),
               path('register/', RegisterView.as_view(), name='register'),
               ]

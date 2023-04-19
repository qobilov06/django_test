from django.urls import path

from apps.views import (CustomLoginView, RegisterView, IndexView, AboutView, BlogView, ContactView, ElementView,
                        FacilityView, MainView, PropertyView, SingleBlogView
                        )

urlpatterns = [path('', IndexView.as_view(), name='index'),
               path('about/', AboutView.as_view(), name='about'),
               path('blog/', BlogView.as_view(), name='blog'),
               path('contact/', ContactView.as_view(), name='contact'),
               path('elements/', ElementView.as_view(), name='elements'),
               path('facilites/', FacilityView.as_view(), name='facilites'),
               path('main/', MainView.as_view(), name='main'),
               path('property/', PropertyView.as_view(), name='property'),
               path('single_blog/', SingleBlogView.as_view(), name='single_blog'),
               path('login/', CustomLoginView.as_view(), name='login'),
               path('register/', RegisterView.as_view(), name='register'),
               ]

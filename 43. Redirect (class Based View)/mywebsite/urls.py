from django.contrib import admin
from django.urls import path, re_path

from django.views.generic.base import TemplateView, RedirectView

from .views import HomeView, HomeRedirectView, HomeUserView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home_view'),
    path('index', RedirectView.as_view(pattern_name='home'), name='index'),
    path('home', RedirectView.as_view(url='/'), name='home'),
    path('', 
        TemplateView.as_view(template_name='index.html'),
        name='index'),
    path('admin/', admin.site.urls),
    re_path('home/(?P<user>[\w]+)$', HomeRedirectView.as_view(), name='home_redirect'),
    re_path('(?P<user>[\w]+)$', HomeUserView.as_view(), name='user'),
]

from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from .views import IndexView , ContextView, ParameterView

urlpatterns = [
    # re_path('parameter/(?P<parameter1>[0-9]+)/(?P<parameter2>[0-9]+)', ParameterView.as_view()),
    path('parameter/<int:parameter1>/<int:parameter2>', ParameterView.as_view()),
    path('context/', ContextView.as_view()),
    path('default/', TemplateView.as_view(template_name='default.html')),
    path('', IndexView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
]


# 1. membuat class view di views.py tapi menggunakan templatenya
# di url
# 2. jika halaman kita itu status, tidak ada peruabahn apapun, 
# # maka kita lakukan TemplateView langsung di urls.py
# 3. membuat views dengan context saja, kita menggunakan class
# 4. kita memasukkan parameter kedalam template, dengan meggunakan regex

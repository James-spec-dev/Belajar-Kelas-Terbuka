from django.contrib import admin
from django.urls import path

from .views import index, IndexClassView

urlpatterns = [
    path('', index, name='home'),
    path('class/', IndexClassView.as_view(template_name='index.html'), name='home-class'),
    path('class2/', IndexClassView.as_view(template_name='index2.html'), name='home-class2'),
    path('admin/', admin.site.urls),
]

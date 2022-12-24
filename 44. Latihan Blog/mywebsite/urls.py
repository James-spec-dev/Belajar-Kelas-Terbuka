from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sosmed/', include(('sosmed.urls', 'sosmed'), namespace='sosmed')),
    path('admin/', admin.site.urls),
]
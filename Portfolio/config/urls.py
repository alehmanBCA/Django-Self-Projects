from django.contrib import admin
from django.urls import path
from Portfolio.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('projects', projects_screen, name='projects'),
]

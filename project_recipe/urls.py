from django.contrib import admin
from django.urls import path, include

from recipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe.urls')),
]
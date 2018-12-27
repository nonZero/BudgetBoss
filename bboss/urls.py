"""bboss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def home(request):
    n = 12
    return HttpResponse(f"You are {n} years old!")


def age(request, n):
    x = n + 1
    return HttpResponse(f"You are {x} years old!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('age/<int:n>/', age),
]

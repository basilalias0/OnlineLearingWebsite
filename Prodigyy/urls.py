"""Prodigyy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from courses.views import home, courses, video, mycourses
from courses.views import login_request, register_request,logout_request,checkout,verifypayment

urlpatterns = [
    path('', home, name='home'),
    path("login", login_request, name="login"),
    path("my_courses", mycourses, name="my_courrses"),
    path("register", register_request, name="register"),
    path("logout", logout_request, name= "logout"),
    path('prodigyy/course', courses, name='courses'),
    path('prodigyy/video/<str:slug>', video, name='videos'),
    path('prodigyy/checkout/<str:slug>', checkout, name='checkout'),
    path('verify_payment',verifypayment, name='verify_payment'),
    path('admin/', admin.site.urls),

]

"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tempfile import template

from django.contrib import admin
from django.urls import path
from task2.views import func_temp, class_temp
from task4.views import cart_temp, games_temp, platform_temp, menu
from task5.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_temp.as_view(), name='func_temp'),
    path('class/', class_temp.as_view(), name='class_view'),
    path('platform/', platform_temp.as_view()),
    path('platform/games/', games_temp.as_view()),
    path('platform/cart/', cart_temp.as_view()),
    path('', menu.as_view(template_name="fourth_task/menu.html")),
    path('registration/', sign_up_by_django),
]

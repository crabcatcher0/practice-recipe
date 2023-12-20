"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from vege.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, settings, static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),
    path('recepies/', receipes, name="recepies"),
    path('delete-receipe/<int:id>/', delete_receipe, name = "delete_receipe"),
    path('recepies/list/', list_recipe, name = "list_recipe"),
    path('recepies/list/<int:id>/', list_detail, name = "list_detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
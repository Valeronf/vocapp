"""swed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from words.views import main_page, word_list, delete_word, update_word, delete_theme, update_theme

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="main_page"),
    path('<int:theme_id>/', word_list, name='word_list'),
    path('delete_word/<int:word_id>/', delete_word, name="delete_word"),
    path('<int:theme_id>/update_word/<int:word_id>/', update_word, name='update_word'),
    path('delete_theme/<int:theme_id>/', delete_theme, name="delete_theme"),
    path('update_theme/<int:theme_id>/', update_theme, name='update_theme'),
]

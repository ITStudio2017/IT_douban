"""douban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from main import views as main_views
from users.views import ajax_val

urlpatterns = [
    # main 
    url(r'^write/',main_views.WriteArticl,name='WriteArticl'),
    url(r'^informationChange/',main_views.userInformation),
    url(r'^$',main_views.userPage),
    url(r'^index/',main_views.userPage),
    url(r'^userArticleList/',main_views.userArticle,name='userArticle'),

    # users
    url(r'^accounts/', include('users.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^ajax_val/', ajax_val, name='ajax_val'),

    # admin
    url(r'^admin/', admin.site.urls),

    
]

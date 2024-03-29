"""chandrayan URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rover import views
from . import main
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', main.mainfun, name='home'),
    url(r'^index/', views.index, name='index'),
    url(r'^harry/', main.testing, name='harry'),
    url(r'^admin/', admin.site.urls, name='adm'),
    url(r'^roverlink/', include('rover.urls')),
    url(r'^logout/$', views.user_logout,name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

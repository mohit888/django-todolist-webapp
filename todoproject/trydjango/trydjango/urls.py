"""trydjango URL Configuration

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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog1.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todo import views
 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^add', views.addTodo, name='add'),
    url(r'^complete/(\d+)/', views.completeTodo, name='complete'),
    url(r'^deletecomplete', views.deleteCompleted, name='deletecomplete'),
    url(r'^deleteall', views.deleteAll, name='deleteall')
    
]
 

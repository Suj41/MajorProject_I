"""
URL configuration for firstone project.

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
from django.contrib import admin
from django.urls import path
from firstone import views

urlpatterns = [
    path('homepage/',views.homepage),
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('login/',views.login),
    path('dashboard/', views.dashboard),
    path('product/', views.product),
    path('vendor/', views.vendor),
    path('warehouse/', views.warehouse),
    path('department/', views.department),
    path('customer/', views.customer),
    path('user/', views.user),
    path('order/', views.order),
    path('transaction/', views.transaction),
    
]

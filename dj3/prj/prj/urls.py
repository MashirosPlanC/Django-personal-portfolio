"""prj URL Configuration

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
from django.urls import path, include
from app import views as v1
from app2 import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app2/temp1', v2.temp1),
    path('app2/temp2', v2.temp2),   
    path('app/temp1', v1.temp1),    
    path('app/temp2', v1.temp1),  
    path('app/form', v1.form),
    path('app/main', v1.main),
    path('app/skills',v1.skills),
    path('app/experience',v1.experience),
    

]

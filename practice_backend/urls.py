"""
URL configuration for practice_backend project.

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
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls', namespace='main_page')),
    path('auth_student/', include('student.urls', namespace='student_page')),
    path('profile/', include('student.urls', namespace='student_profile')),
    path('auth_partners/', include('partners.urls', namespace='partners_page')),
    path('profile_part/', include('partners.urls', namespace='partners_profile')),
    path('auth_kafedra/', include('kafedra.urls', namespace='kafedra_page')),
    path('profile_kafedra/', include('kafedra.urls', namespace='profile_kafedra')),
]

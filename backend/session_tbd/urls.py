"""
URL configuration for session_tbd project.

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
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.contrib import admin

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#! Adjust to have api/v1/
# TODO adjust Pattern to meet project best practice
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('accounts_app.urls')),
    path('profile/', include('profile_app.urls')),
]

urlpatterns += [re_path(r'^.*',
                        TemplateView.as_view(template_name='index.html'))]
# catch all pattern that works react router /  will direct to the index.html page

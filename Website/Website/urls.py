"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import Caching.views as Views
from Caching.views import PreCache
PreCache()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cached/', Views.CachedAccess.as_view()),
    path('uncached/', Views.NonCachedAccess.as_view()),
    path('kmeanscached/', Views.kmeans_CachedAccess.as_view()),
    path('kmeansuncached/', Views.kmeans_NonCachedAccess.as_view()),
    path('dbscancached/', Views.dbscan_CachedAccess.as_view()),
    path('dbscanuncached/', Views.dbscan_NonCachedAccess.as_view()),
]

"""stagelite URL Configuration

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

# from topics.views import get_competition_overview
# from topics.viewsets import CompetitionViewSet
# import topics
# from topics import viewsets

urlpatterns = [
    path('', admin.site.urls),
    path('admin/', admin.site.urls),
    path('topics/', include('topics.urls'), name='topics'),
    # Add Topics URLs later
    # path('api/competitions', CompetitionViewSet),
    # path('api/get_competition_info', get_competition_overview, name='competition_info')
]

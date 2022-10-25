from django.urls import path, include

from topics.viewsets import CompetitionViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'competitions', CompetitionViewSet, 'competitions')

urlpatterns = [
    path('', include(router.urls)),
]

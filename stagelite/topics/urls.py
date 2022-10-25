from django.urls import path, include

from rest_framework.routers import DefaultRouter

from topics.viewsets import CompetitionViewSet,\
    TopicsViewSet

router = DefaultRouter()

router.register(r'competitions', CompetitionViewSet, 'competitions')
router.register(r'topics_list', TopicsViewSet, 'topics')

urlpatterns = [
    path('', include(router.urls)),

]

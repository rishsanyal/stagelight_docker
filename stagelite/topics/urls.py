from django.urls import path, include

from rest_framework.routers import DefaultRouter

from topics.viewsets import CompetitionViewSet,\
    TopicsViewSet, UserSubmissionViewSet

from topics.views import hello

router = DefaultRouter()

router.register(r'competitions', CompetitionViewSet, 'competitions')
router.register(r'topics_list', TopicsViewSet, 'topics')

urlpatterns = [
    path('hello/', hello),
    path('user_submission/', UserSubmissionViewSet.as_view()),
    path('', include(router.urls)),
]

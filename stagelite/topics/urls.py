from django.urls import path, include

from rest_framework.routers import DefaultRouter

from topics.viewsets import CompetitionViewSet,\
    TopicsViewSet, UserSubmissionViewSet

router = DefaultRouter()

router.register(r'competitions', CompetitionViewSet, 'competitions')
router.register(r'topics_list', TopicsViewSet, 'topics')

urlpatterns = [
    path('user_submission/', UserSubmissionViewSet.as_view()),
    path('', include(router.urls)),
]

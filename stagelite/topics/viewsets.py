
from datetime import date, timedelta

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from topics.models import Votes, Topic, Competitions, UserSubmission
from topics.serializers import VotesSerializer, CompetitionSerializer, UserSubmissionSerializer, TopicSerializer

import json
from django.http import JsonResponse

class BaseViewSet(viewsets.ModelViewSet):
    # queryset = BaseTopicModel.objects.all()
    # serializer_class = ModelNameSerializer

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class VotesViewSet(viewsets.ModelViewSet):
    queryset = Votes.objects.all()
    serializer_class = VotesSerializer


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class UserSubmissionViewSet(viewsets.ModelViewSet):
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer



class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionSerializer

    def list(self, request):
        pages = request.GET.get('page', 10)
        return_info = {}
        #TODO: Pagination here so we don't have to hardcode 10 here
        competition_objects = Competitions.objects.order_by('-start_time')
        paginator = Paginator(competition_objects, pages)

        for competition in competition_objects.iterator():
            return_info['competition_info'] = {}

            return_info['competition_info'][competition.theme] = {}
            return_info['competition_info'][competition.theme]['current_status'] = competition.is_open
            return_info['competition_info'][competition.theme]['upvotes'] = competition.votes.upvote
            return_info['competition_info'][competition.theme]['downvotes'] = competition.votes.downvote
            return_info['competition_info'][competition.theme]['id'] = competition.id
            return_info['competition_info'][competition.theme]['num_topics'] = competition.competition_topics.count()

        return(HttpResponse(json.dumps(return_info)))

class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1)))
    serializer_class = TopicSerializer

    def list(self, request):
        return_info = {}
        return_info = []
        competition_objects = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1))).order_by('-creation_time')
        for topic in competition_objects.iterator():
            temp_return_info = {}
            temp_return_info['title'] = topic.title
            temp_return_info['upvotes'] = topic.votes.upvote
            temp_return_info['downvotes'] = topic.votes.downvote
            temp_return_info['id'] = topic.id
            return_info.append(temp_return_info)

        return(JsonResponse(return_info, safe=False))
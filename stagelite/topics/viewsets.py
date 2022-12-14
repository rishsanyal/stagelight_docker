
from datetime import date, timedelta

from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from stage.models import StageUser

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


class UserSubmissionViewSet(APIView):
    permission_classes = [AllowAny]
    queryset = UserSubmission.objects.all()
    serializer_class = UserSubmissionSerializer

    def post(self, request):
        if request.user.is_authenticated:
            response = HttpResponse('blah')
            response.set_cookie('username', request.user.username)
        return_info = {}

        jsonBody = json.loads(request.body)
        textEntry = jsonBody['textEntry']
        topicId = int(jsonBody['id'])
        username = jsonBody['username']

        votes = Votes()
        votes.save()
        userEntry, creation_status = UserSubmission.objects.get_or_create(
            user=StageUser.objects.get(username=username),
            topic=Topic.objects.get(id=topicId),
            defaults={
                'votes': votes,
                'submission_entry': ''
            }
        )
        if not creation_status:
            userEntry.submission_entry = textEntry
            userEntry.save()


        return_info['success'] = True
        # else:
        #     return_info['success'] = False
        #     return_info['error'] = 'User already submitted an entry for this topic'

        return(JsonResponse(return_info, safe=False))

    def get(self, request):
        try:
            topicId = int(request.GET.get('topicId'))
            username = request.GET.get('username')

            return_info = {}
            userEntry = UserSubmission.objects.get(user=StageUser.objects.get(username=username), topic=Topic.objects.get(id=topicId))
            if userEntry:
                return_info['userEntry'] = userEntry.submission_entry
                return_info['success'] = True
            else:
                return_info['success'] = False
                return_info['userEntry'] = ''
                return_info['error'] = 'User has not submitted an entry for this topic'
        except UserSubmission.DoesNotExist:
            return_info['success'] = False
            return_info['userEntry'] = ''
            return_info['error'] = 'User has not submitted an entry for this topic'
        return JsonResponse(return_info, safe=False)



class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competitions.objects.all()
    serializer_class = CompetitionSerializer

    def list(self, request):
        if request.user.is_authenticated:
            response = HttpResponse('blah')
            response.set_cookie('username', request.user.username)
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
    permission_classes = [AllowAny]
    queryset = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1)))
    serializer_class = TopicSerializer

    def list(self, request):
        # if request.user.is_authenticated:
        #     response = HttpResponse('blah')
        #     response.set_cookie('username', request.user.username)
        return_info = {}
        return_info = []

        # jsonBody = json.loads(request.body)
        username = request.GET.get('username', 'test_user')

        competition_objects = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1))).order_by('-creation_time')
        for topic in competition_objects.iterator():
            temp_return_info = {}
            temp_return_info['title'] = topic.title
            temp_return_info['upvotes'] = topic.votes.upvote
            temp_return_info['downvotes'] = topic.votes.downvote
            temp_return_info['id'] = topic.id
            temp_return_info['userEntry'] = UserSubmission.objects.filter(user=StageUser.objects.get(username=username), topic=topic).exists()
            return_info.append(temp_return_info)

        return(JsonResponse(return_info, safe=False))

    def retrieve(self, request, pk=None):
        if request.user.is_authenticated:
            response = HttpResponse('blah')
            response.set_cookie('username', request.user.username)
        return_info = {}
        topic = get_object_or_404(Topic, pk=pk)
        return_info['title'] = topic.title
        return_info['upvotes'] = topic.votes.upvote
        return_info['downvotes'] = topic.votes.downvote
        return_info['id'] = topic.id

        return(JsonResponse(return_info, safe=False))

    def create(self, request):
        return_info = {}
        return_info['success'] = False
        return_info['error'] = 'Not Implemented'

        return(JsonResponse(return_info, safe=False))
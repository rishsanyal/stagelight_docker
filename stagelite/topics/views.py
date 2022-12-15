from datetime import date, timedelta
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from topics.models import Competitions, Topic

import json



def baseRequest(request):
    if request.user.is_authenticated:
        response = HttpResponseRedirect("http://localhost:3000/topics/")
        response.set_cookie('username', request.user.username)
        return response

def hello(request):
    if request.user.is_authenticated:
        response = HttpResponseRedirect("http://127.0.0.1:3000/topics/")
        response.set_cookie('username', request.user.username, 3600)
        return response

def vote(request):
    vote_type = request.GET.get('type')
    topic_id = int(request.GET.get('id'))

    topic = Topic.objects.get(id=topic_id)
    votes = topic.votes

    if vote_type == 'upvote':
        votes.upvote = topic.votes.upvote + 1
        votes.save()
    elif vote_type == 'downvote':
        votes.downvote = topic.votes.downvote + 1
        votes.save()

    print(vote_type == 'up')

    votes.save()
    topic.save()

    topic.votes.refresh_from_db()
    topic.refresh_from_db()

    return(HttpResponse(topic.votes.upvote))

def competition_info(request):
    baseRequest(request)
    if request.method == 'GET':
        return_info = {}

        for c in Competitions.objects.all():
            return_info[c.theme] = {}
            return_info[c.theme]['topics'] = []

            return_info[c.theme]['show'] = c.is_open

            for topic in c.competition_topics.iterator():
                return_info[c.theme]['topics'].append(topic.title)

        return(HttpResponse(json.dumps(return_info)))

def get_competition_overview(request):
    baseRequest(request)

    return_info = {}
    #TODO: Pagination here so we don't have to hardcode 10 here
    competition_objects = Competitions.objects.order_by('-start_time')[:10]

    for competition in competition_objects.iterator():
        return_info[competition.theme] = {}
        return_info[competition.theme]['current_status'] = competition.is_open
        return_info[competition.theme]['upvotes'] = competition.votes.upvote
        return_info[competition.theme]['downvotes'] = competition.votes.downvote
        return_info[competition.theme]['id'] = competition.id
        return_info[competition.theme]['num_topics'] = competition.competition_topics.count()

    return(HttpResponse(json.dumps(return_info)))

def get_competition_topics(request):
    baseRequest(request)

    if request.method == 'GET':
        return_info = {}
        return_info['topics'] = []
        return_info['userSubmittedAny'] = False

        topics_info = []
        competition_objects = Topic.objects.filter(creation_time__gte=(date.today() - timedelta(days=1))).order_by('-creation_time')[:3]
        for topic in competition_objects.iterator():
            temp_return_info = {}
            temp_return_info['title'] = topic.title
            temp_return_info['upvotes'] = topic.votes.upvote
            temp_return_info['downvotes'] = topic.votes.downvote
            temp_return_info['id'] = topic.id

            username = request.user.username
            temp_return_info['userSubmissionStatus'] = username in topic.usersubmission_set.values_list('user__username', flat=True)

            topics_info.append(temp_return_info)

            if temp_return_info['userSubmissionStatus']:
                return_info['userSubmittedAny'] = True

        return_info['topics'] = topics_info

        return(JsonResponse(return_info, safe=False))
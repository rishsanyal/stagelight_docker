from django.shortcuts import render
from django.http import HttpResponse

from topics.models import Competitions

import json

def competition_info(request):
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

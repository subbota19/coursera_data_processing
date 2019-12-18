from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Polls


def polls_list(request):
    # polls contain 20 Polls objects and return data with json-format
    MAX_OBJECTS = 20
    polls = Polls.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_data"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    # response data with json-format if server get valid pk
    poll = get_object_or_404(Polls, pk=pk)
    data = {
        "results": {"question": poll.question, "created_by__username": poll.created_by.username,
                    "pub_data": poll.pub_data}}
    return JsonResponse(data)

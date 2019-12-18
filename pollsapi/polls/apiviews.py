from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Polls, Vote, Choice
from .serializers import PollsSerializer, ChoiceSerializer, VoteSerializer


# ListCreateAPIView get list of objects or create them(use Post and Get)
class PollsList(generics.ListCreateAPIView):
    # def get(self, request):
    #     polls = Polls.objects.all()[:20]
    #     data = PollsSerializer(polls, many=True).data
    #     return Response(data)
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


# RetrieveDestroyAPIView retrieve object details (use Delete and Get)
class PollsDetail(generics.RetrieveDestroyAPIView):
    # def get(self, request, pk):
    #     poll = get_object_or_404(Polls, pk=pk)
    #     data = PollsSerializer(poll).data
    #     return Response(data)
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveDestroyAPIView):
    queryset = Polls.objects.all()
    serializer_class = PollsSerializer


# CreateAPIView create object(use Post)
class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

from django.urls import path
from .apiviews import PollsDetail, PollsList, ChoiceList, CreateVote

urlpatterns = [
    path("polls/", PollsList.as_view(), name=" polls_list"),
    path("polls/<int:pk>", PollsDetail.as_view(), name="polls_detail"),
    path("votes/", CreateVote.as_view(), name=" vote_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
]

from rest_framework import viewsets
from .serializers import PollSerializer, PollOptionSerializer, PollVoteSerializer, PollVoteCountSerializer
from .models import Poll, PollOption, PollVote


class PollView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollOptionView(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer


class PollVoteView(viewsets.ModelViewSet):
    queryset = PollVote.objects.all()
    serializer_class = PollVoteSerializer


class PollVoteCountView(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollVoteCountSerializer

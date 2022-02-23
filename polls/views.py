from rest_framework import viewsets, permissions
from .serializers import PollSerializer, PollOptionSerializer, PollVoteSerializer, PollVoteCountSerializer
from .models import Poll, PollOption, PollVote


class PollView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollOptionView(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollOptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollVoteView(viewsets.ModelViewSet):
    queryset = PollVote.objects.all()
    serializer_class = PollVoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollVoteCountView(viewsets.ModelViewSet):
    queryset = PollOption.objects.all()
    serializer_class = PollVoteCountSerializer
    permission_classes = [permissions.IsAuthenticated]

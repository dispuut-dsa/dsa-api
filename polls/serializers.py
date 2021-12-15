from rest_framework import serializers
from .models import Poll, PollVote, PollOption


class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = ('user', 'poll', 'option')


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ('id', 'poll', 'option')


class PollSerializer(serializers.ModelSerializer):
    options = PollOptionSerializer(read_only=True, many=True, required=False)
    votes = PollVoteSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Poll
        fields = ('id', 'author', 'name', 'description', 'options', 'votes')

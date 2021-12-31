from rest_framework import serializers
from .models import Poll, PollVote, PollOption


class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = ('user', 'poll', 'option')
        read_only_fields = ['poll']

    def create(self, validated_data):
        vote = PollVote(
            user=validated_data['user'],
            option=validated_data['option']
        )

        poll = vote.option.poll
        vote.poll = poll
        vote.save()
        return vote


class PollVoteCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, instance):
        print(type(instance))
        return instance.votes.count()

    class Meta:
        model = PollOption
        fields = ('option', 'count')


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ('id', 'poll', 'option')


class PollSerializer(serializers.ModelSerializer):
    # The following property is read-only since it's a count
    options = PollVoteCountSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Poll
        fields = ('id', 'author', 'name', 'description', 'options')

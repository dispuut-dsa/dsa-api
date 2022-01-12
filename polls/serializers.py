from rest_framework import serializers
from .models import Poll, PollVote, PollOption


class PollVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVote
        fields = ('user', 'poll', 'option')
        read_only_fields = ['poll', 'user']

    def create(self, validated_data):
        # Set the user to the currently logged in user
        request = self.context.get("request")
        user = None
        if request and hasattr(request, "user"):
            user = request.user

        if user is None or user.is_anonymous:
            raise ValueError("Expected logged in user. Anonymous voting is not allowed!")

        # Create our vote (without poll field)
        vote = PollVote(
            user=user,
            option=validated_data['option']
        )

        # Retrieve value for poll field from the chosen Option and set it on the PollVote
        poll = vote.option.poll
        vote.poll = poll
        vote.save()
        return vote


class PollVoteCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, instance):
        return instance.votes.count()

    class Meta:
        model = PollOption
        fields = ('id', 'option', 'count')


class PollOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollOption
        fields = ('id', 'poll', 'option')


class PollSerializer(serializers.ModelSerializer):
    # The following property is read-only since it's a count
    options = PollVoteCountSerializer(read_only=True, many=True, required=False)
    can_vote = serializers.SerializerMethodField()

    def get_can_vote(self, instance):
        # Get the current user
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            if user.is_anonymous:
                return False
            return not instance.votes.filter(user=user.id).exists()

    class Meta:
        model = Poll
        fields = ('id', 'author', 'name', 'description', 'options', 'can_vote')

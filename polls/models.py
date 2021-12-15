from django.db import models


class Poll(models.Model):
    """
        Models a single poll.
        This model does not contain votes, those are managed by the PollVote model below.
        This model also doesn't contain vote options. Those are provided by PollOption
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()


class PollOption(models.Model):
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll, related_name="options", on_delete=models.CASCADE)
    option = models.TextField()


class PollVote(models.Model):
    """
        Models a vote by a user on a poll
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name="votes", on_delete=models.CASCADE)
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "poll"], name="One vote per person constraint")
        ]

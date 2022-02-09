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

    def __repr__(self):
        return f"PollOption(id={self.id}, author={str(self.author)}, name={self.name})"

    def __str__(self):
        return self.__repr__()

class PollOption(models.Model):
    """
        Models an option for a poll
    """
    id = models.AutoField(primary_key=True)
    poll = models.ForeignKey(Poll, related_name="options", on_delete=models.CASCADE)
    option = models.TextField()

    def __repr__(self):
        return f"PollOption(id={self.id}, poll={str(self.poll)}, option={self.option})"

    def __str__(self):
        return self.__repr__()


class PollVote(models.Model):
    """
        Models a vote by a user on a poll.
        The poll field is supposed to be set by the backend, not by any API call
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, related_name="votes", on_delete=models.CASCADE)
    option = models.ForeignKey(PollOption, related_name="votes", on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "poll"], name="One vote per person constraint")
        ]

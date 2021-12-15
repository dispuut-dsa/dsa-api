from django.db import models


class WikiPage(models.Model):
    author = models.ForeignKey('auth.User', related_name='wiki', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
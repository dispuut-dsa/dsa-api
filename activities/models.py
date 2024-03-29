from django.db import models


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', related_name='activities', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    costs = models.DecimalField(max_digits=5, decimal_places=2)

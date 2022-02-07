from rest_framework import serializers
from .models import WikiPage


class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = WikiPage
        fields = ('id', 'author', 'title', 'content')
from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'author', 'name', 'description', 'start_time', 'end_time', 'location', 'costs')
from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

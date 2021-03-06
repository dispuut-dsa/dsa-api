from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer


class ActivityView(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

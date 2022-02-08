from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view

from .models import Activity
from .serializers import ActivitySerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
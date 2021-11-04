from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer
import authentication.views

class ActivityView(authentication.views.AuthenticatedReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

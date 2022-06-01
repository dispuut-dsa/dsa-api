from rest_framework import viewsets
from .models import WikiPage
from .serializers import WikiSerializer


class WikiView(viewsets.ModelViewSet):
    queryset = WikiPage.objects.all()
    serializer_class = WikiSerializer
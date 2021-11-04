from rest_framework import viewsets
from rest_framework.response import Response
import inspect

def authenticated(func):
    def authenticate(*args, **kwargs):
        request = args[0]
        if request.body == "I'm authenticated":
            return func(*args, **kwargs)
        else:
            return Response("Sorry, not authenticated")
    return authenticate

class AuthenticatedReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):

    @authenticated
    def list(self, request):
        super().list(request)

    @authenticated
    def retrieve(self, request, pk=None):
        super().retrieve(request, pk)

class AuthenticatedViewSet(viewsets.ViewSet):

    @authenticated
    def list(self, request):
        super().list(request)

    @authenticated
    def create(self, request):
        super().create(request)

    @authenticated
    def retrieve(self, request, pk=None):
        super().retrieve(request, pk)

    @authenticated
    def update(self, request, pk=None):
        super().update(request, pk)

    @authenticated
    def partial_update(self, request, pk=None):
        super().partial_update(request, pk)

    @authenticated
    def destroy(self, request, pk=None):
        super().destroy(request, pk)
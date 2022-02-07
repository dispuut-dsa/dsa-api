from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view

from .models import Activity
from .serializers import ActivitySerializer


class ActivityView(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]
#     @api_view(['GET'])
#     def resolveQueryset(self, context, request):
#         if request.user:
#             return self.queryset
# #
#
# authenticate(fun, args):
#     if args[context].token is valid:
#         args.context.is_admin =
#         return fun(args)
#     return
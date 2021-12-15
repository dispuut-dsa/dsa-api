from rest_framework import viewsets
from .models import Activity
from .serializers import ActivitySerializer


class ActivityView(viewsets.ReadOnlyModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# @authenticate
# def resolveQueryset(context, request):
#     if context.is_admin:
#         return queryset
#
#
# authenticate(fun, args):
#     if args[context].token is valid:
#         args.context.is_admin =
#         return fun(args)
#     return
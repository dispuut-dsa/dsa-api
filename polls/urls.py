from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('polls', views.PollView)
router.register('pollOption', views.PollOptionView)
router.register('pollVote', views.PollVoteView)
router.register('pollVoteCount', views.PollVoteCountView)


urlpatterns = [
    path('', include(router.urls))
]
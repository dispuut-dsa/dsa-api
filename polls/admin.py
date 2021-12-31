from django.contrib import admin

from .models import Poll, PollOption, PollVote


class PollAdmin(admin.ModelAdmin):
    list_display = ('author', 'name')


class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option')


class PollVoteAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option', 'user')


admin.site.register(Poll, PollAdmin)
admin.site.register(PollOption, PollOptionAdmin)
admin.site.register(PollVote, PollVoteAdmin)

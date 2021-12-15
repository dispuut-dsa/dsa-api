from django.contrib import admin

from .models import Poll


class PollAdmin(admin.ModelAdmin):
    list_display = ('author', 'name')


class PollOptionAdmin(admin.ModelAdmin):
    list_display = ('poll', 'option')


admin.site.register(Poll, PollAdmin)

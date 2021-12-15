from django.contrib import admin

from .models import WikiPage


class WikiAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(WikiPage, WikiAdmin)


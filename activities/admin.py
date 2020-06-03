from django.contrib import admin

from .models import Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time')


admin.site.register(Activity, ActivityAdmin)

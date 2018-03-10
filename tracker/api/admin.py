from django.contrib import admin

from tracker.api.models import UserLocation


class UserLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'lat', 'lng', 'created_at')
admin.site.register(UserLocation, UserLocationAdmin)

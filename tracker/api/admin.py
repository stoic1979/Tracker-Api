from django.contrib import admin

from tracker.api.models import ChildLocation, Child


class ChildLocationAdmin(admin.ModelAdmin):
    list_display = ('child', 'lat', 'lng', 'created_at')
admin.site.register(ChildLocation, ChildLocationAdmin)


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at')
admin.site.register(Child, ChildAdmin)

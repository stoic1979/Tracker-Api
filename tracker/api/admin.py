from django.contrib import admin

from tracker.api.models import Child, ChildLocation, ChildDevice

@admin.register(ChildLocation)
class ChildLocationAdmin(admin.ModelAdmin):
    list_display = ('child', 'lat', 'lng', 'created_at')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at')


@admin.register(ChildDevice)
class ChildDeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'os', 'created_at')

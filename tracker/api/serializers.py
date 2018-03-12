from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tracker.api.models import Child, ChildLocation, ChildDevice
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'name', 'created_at')

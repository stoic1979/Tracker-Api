from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tracker.api.models import Child, ChildLocation, ChildDevice
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'url', 'username', 'email', 'groups')
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=6, max_length=100,
            write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ( 'username', 'email', 'password')        

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ChildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'name', 'created_at')

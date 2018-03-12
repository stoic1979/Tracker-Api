from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.http import HttpResponse
from rest_framework import viewsets

from tracker.api.models import Child, ChildLocation, ChildDevice
from tracker.api.serializers import UserSerializer,GroupSerializer, ChildSerializer

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    resp = {'success': True}
    if user:
        token, status = Token.objects.get_or_create(user=user)
        resp['token'] = token.key
        resp['msg'] = 'Login successful'
    else:
        resp['success'] = False
        resp['msg'] = 'Invalid userame or password'
    return HttpResponse(json.dumps(resp), content_type="application/json")


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    @csrf_exempt
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows children to be viewed or edited.
    """
    queryset = Child.objects.all().order_by('-created_at')
    serializer_class = ChildSerializer


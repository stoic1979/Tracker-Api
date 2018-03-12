from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from tracker.api.models import Child, ChildLocation, ChildDevice
from tracker.api.serializers import ChildSerializer

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.renderers import JSONRenderer


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


@csrf_exempt
def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = User(username=username, password=password, email=email)
    user.save()
    resp = {'success': True}
    if user:
        token, status = Token.objects.get_or_create(user=user)
        resp['token'] = token.key
        resp['msg'] = 'Registration successful'
    else:
        resp['success'] = False
        resp['msg'] = 'Registration failed'
    return HttpResponse(json.dumps(resp), content_type="application/json")


class ChildViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows children to be viewed or edited.
    """
    queryset = Child.objects.all().order_by('-created_at')
    serializer_class = ChildSerializer

    def create(self, request):
        resp = {'success': True}
        name = request.POST['name']
        child = Child(parent=request.user, name=name)
        child.save()
        if child:
            resp['msg'] = 'Child added successfully'
            resp['child_id'] = child.id
        else:
            resp['success'] = False
            resp['msg'] = 'Failed to create child'
        return HttpResponse(json.dumps(resp), content_type="application/json")

    def list(self, request):
        # only get childer for given parent
        # i.e. authenticated/logged-in user
        children = Child.objects.filter(parent=request.user)
        serializer = ChildSerializer(children, many=True)
        return JsonResponse(serializer.data, safe=False)

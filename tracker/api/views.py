from django.shortcuts import render

from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets

from tracker.api.models import Child, ChildLocation, ChildDevice
from tracker.api.serializers import ChildSerializer, ChildLocationSerializer

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json

from rest_framework import serializers
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
    resp = {'success': True}
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=make_password(password), email=email)
        user.save()
        if user:
            token, status = Token.objects.get_or_create(user=user)
            resp['token'] = token.key
            resp['msg'] = 'Registration successful'
        else:
            resp['success'] = False
            resp['msg'] = 'Registration failed'
    except Exception as exp:
        resp['success'] = False
        resp['msg'] = 'Registration failed, exception: %s' % exp

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


class ChildLocationViewSet(viewsets.ModelViewSet):
    queryset = ChildLocation.objects.all().order_by('created_at')
    serializer_class = ChildLocationSerializer

    def retrieve(self, request, pk=None):
        resp = {'success': True}
        try:
            child = Child.objects.get(pk=pk)

            # NOTE
            # we will provide child location to his/her parent only
            if child.parent == request.user:
                child_locations = ChildLocation.objects.filter(child=child)
                serializer = ChildLocationSerializer(child_locations, many=True)
                resp["locations"] = serializer.data
                return JsonResponse(resp, safe=False)
            else:
                resp["success"] = False
                resp["msg"] = "Invalid parent"
                return HttpResponse(json.dumps(resp), content_type="application/json")
        except Child.DoesNotExist as exp:
            resp["success"] = False
            resp["msg"] = "Child not found"
            return HttpResponse(json.dumps(resp), content_type="application/json")

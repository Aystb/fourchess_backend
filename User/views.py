from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json

from Serializers.UserSerializer import UserSerializer
from User.models import User


# Create your views here.
def login(request):
    postBody = request.body
    json_result = json.loads(postBody)
    name = json_result['name']
    password = json_result['password']
    try:
        user = User.objects.get(name=name, password=password);
        userSerializer = UserSerializer(user)
        return JsonResponse(userSerializer.data, safe=False, status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=401)


def register(request):
    postBody = request.body
    json_result = json.loads(postBody)
    name = json_result['name']
    password = json_result['password']

    isUserExist = User.objects.filter(name=name)
    if (isUserExist.exists()):
        wrongUser = {
            "id": -1,
            "name": isUserExist[0].name,
            "password": isUserExist[0].password
        }
        userSerializer = UserSerializer(wrongUser)
        return JsonResponse(userSerializer.data, safe=False, status=400)
    else:
        User.objects.create(name=name, password=password)
        user = User.objects.get(name=name, password=password);
        userSerializer = UserSerializer(user)
        return JsonResponse(userSerializer.data, safe=False, status=200)

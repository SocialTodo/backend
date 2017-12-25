import json
from http import HTTPStatus

from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render


# Create your views here.

@csrf_exempt
def i_am_a_teapot_test(request):
    return JsonResponse({"message": "ERROR 418: I'm sorry sir, but a poor little teapot like me is no use to you"}, status= 418)

@csrf_exempt
def log_in_user(request):
    print(request.POST)
    return HttpResponse(status=HTTPStatus.OK)
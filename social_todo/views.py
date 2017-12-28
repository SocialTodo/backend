import json
import requests
import os
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
    result = json.loads(request.body)
    print(os.environ["SOCIAL_TODO_APP_ID"])
    print(os.environ["SOCIAL_TODO_APP_SECRET"])
    facebook_graph_response = requests.get("https://graph.facebook.com/debug_token", \
                                           data = {"input_token": result["Token"], \
                                                   "access_token": os.environ["SOCIAL_TODO_APP_ID"] \
                                                                   + "|" \
                                                                   + os.environ["SOCIAL_TODO_APP_SECRET"]})
    print(facebook_graph_response)
    print(result)
    print(len(result["Token"]))
    print(len(result["UserID"]))
    return HttpResponse(status=HTTPStatus.OK)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from facebook_users.models import *
import json
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


@csrf_exempt
def authenticate_facebook_token(request):
    user = authenticate(request, token=json.loads(request.body)["Token"])
    import pdb
    pdb.set_trace()  # breakpoint 1ff73cd2 //
    return HttpResponse(status=200)

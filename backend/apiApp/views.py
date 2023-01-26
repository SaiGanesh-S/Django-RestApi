from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def apiHome(request,*args, **kwargs):
    return JsonResponse({"message":"Messahe from api Home"})

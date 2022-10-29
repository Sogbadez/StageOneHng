from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from .models import Me
from .serializer import MeSerializer


def name(response):
    return HttpResponse('Hello Zainab Sogbade')

def me_intro(request):
    people=Me.objects.all()
    serializer=MeSerializer(people,many=True)
    return JsonResponse(serializer.data,safe=False)

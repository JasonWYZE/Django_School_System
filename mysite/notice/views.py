from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addNotice(request):
    return HttpResponse("Add Notice here")
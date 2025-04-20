from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    s1 = '<H1>Welcome to the team Kromation !!!</H1>'
    return HttpResponse(s1)
# Create your views here.

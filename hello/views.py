from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = HttpResponse()
    response.write("hello everyone")
    return response
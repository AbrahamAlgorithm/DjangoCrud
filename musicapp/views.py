from django.shortcuts import render

# Create your views here.


def index(request):
    return Httpresponse('wow welcome to our site')
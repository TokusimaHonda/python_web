from django.shortcuts import render
from django.http import HttpResponse

def helloworldappview(request):
    returnobject = HttpResponse('<h1>乃木坂</h1>')
    return returnobject

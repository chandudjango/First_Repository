from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='<h1>welcome first django application!!!</h1>'
    return HttpResponse(s)

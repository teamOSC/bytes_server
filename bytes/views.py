from django.shortcuts import render, HttpResponse, render_to_response

# Create your views here.


def mainPage(request):
    return HttpResponse("Shubham")


def getOutlets(request):
    pass
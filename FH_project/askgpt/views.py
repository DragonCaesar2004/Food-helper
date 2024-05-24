from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('The home page')


def error_handler(request):
    return HttpResponse('404 page')



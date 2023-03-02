from django.http import HttpResponse
from django.shortcuts import render, redirect


DEFAULT_REDIRECT_VIEW = 'homepage'


def default_redirect_view(request):
    return redirect(DEFAULT_REDIRECT_VIEW)


def index(request):
    return HttpResponse('Hi')

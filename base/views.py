from django.shortcuts import render
from django.http import HttpResponse


def task_list(request):
    return HttpResponse('Hello guys!')
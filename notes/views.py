from django.shortcuts import render
from django.http import HttpResponse

def notes_index(request):
    return HttpResponse('notes')

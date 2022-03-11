from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница1')

def group_posts(request,slug):    
    return HttpResponse(f'group_posts-- {slug}')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json, requests
from pathlib import Path

# Create your views here.
with open('portfolio.config.json', 'r') as fp:
	config = json.load(fp)

def blog(request):
	return HttpResponse("Coming soon.")
	

def foremanbportfolio(request):
    projects = Project.objects.all().order_by('-id')
        
    return render(request, 'pages/foremanbportfolio.html', {
        'projects': projects,
    })
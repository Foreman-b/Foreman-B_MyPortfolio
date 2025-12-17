from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import json, requests
from pathlib import Path

# Create your views here.
with open('portfolio.config.json', 'r') as fp:
	config = json.load(fp)

def foremanbportfolio(request):
	projects = Projects.objects.all()
	config_path = Path(__file__).resolve().parent.parent / "portfolio.config.json"
	with open(config_path) as f:
		data = json.load(f)

	jobs = Jobs.objects.all()
	ctx = {'config': config['Config'],'projects': projects if projects else None,"jobs": jobs if jobs else None}
	if request.method == "POST":
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = request.POST.get('message')
		data = {
		"content" : f"**EMAIL**: {email}\n**NAME:** {name}\n**MESSAGE:** {message}"
		}
		result = requests.post(config['Config']["contact"]["webhook_url"], json=data)
		
	return render(request, 'pages/foremanbportfolio.html')

def blog(request):
	return HttpResponse("Coming soon.")
	
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from pages.models import *
from .serializer import *

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    It automatically handles GET, POST, PUT, and DELETE.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class JobViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing project instances.
    It automatically handles GET, POST, PUT, and DELETE.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

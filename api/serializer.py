from rest_framework import serializers
from pages.models import Project, Job

## serializers here:
class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
	class Meta:
		model = Job
		fields = '__all__'
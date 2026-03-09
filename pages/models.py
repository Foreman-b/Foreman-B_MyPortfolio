from django.db import models
from django.core.exceptions import ValidationError

def validate_only_one_instance(obj):
	model = obj.__class__
	if (model.objects.count() > 0 and
			obj.id != model.objects.get().id):
		raise ValidationError("ERROR: You can only create 1 config instance.")

# Create your models here.
class Project(models.Model):
	banner = models.ImageField(upload_to='pages/photos',verbose_name='Project Image', null=True, blank=True)
	title = models.CharField(max_length=50000,verbose_name="Project Name", null=True, blank=True)
	tech_stack = models.CharField(max_length=50000,verbose_name="Project Stack", null=True, blank=True)
	description = models.TextField(max_length=500, verbose_name="Project Description", null=True, blank=True)
	key_features = models.TextField(max_length=500, verbose_name="Key Features", null=True, blank=True)
	lesson_learned= models.TextField(max_length=500, verbose_name="What I Learned", null=True, blank=True)
	github = models.CharField(max_length=50000,verbose_name="View on Github", null=True, blank=True)
	url = models.CharField(max_length=50000,verbose_name="Project Url", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created", null=True, blank=True)

	class Meta:
		ordering = ['-date_created']
	
	def __str__(self):
		return self.title

	def get_features_list(self):
		lines = self.key_features.strip().split('\n')
		parsed_features = []
        
		for line in lines:
			clean_line = line.strip('* ').strip()
			if ':' in clean_line:
				title, desc = clean_line.split(':', 1)
				parsed_features.append({
                    'title': title.strip(),
                    'desc': desc.strip()
                })
		return parsed_features

class Job(models.Model):
	name = models.CharField(max_length=100,verbose_name="Job name")
	description = models.CharField(max_length=200, verbose_name="Job rank")
	banner = models.ImageField(upload_to='pages/photos',verbose_name='Job banner')
	redirect = models.URLField(verbose_name='Job redirect link')
	def __str__(self):
		return self.name

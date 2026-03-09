from django.contrib import admin
from .models import *
# Register your models here.
## Config
admin.site.site_title = 'Portfolio Administration'
admin.site.index_title = 'Dashboard'
admin.site.site_header = 'Portfolio Admin Panel'
## Models
admin.site.register(Project)
admin.site.register(Job)

@property
def banner_url(self):
    if self.banner and hasattr(self.banner, 'url'):
        return self.banner.url
    return "/static/images/default-banner.jpg"

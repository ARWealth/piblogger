from django.contrib import admin

# Register models for piblogger.
from .models import Title, BlogPost

admin.site.register(Title)
admin.site.register(BlogPost)

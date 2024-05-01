from django.contrib import admin

# Register your models here.
# portfolio/admin.py
from .models import Project

admin.site.register(Project)

from django.contrib import admin
from .models import Job, Category, JobOrder

admin.site.register(Job)
admin.site.register(Category)

admin.site.register(JobOrder)
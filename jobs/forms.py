from django import forms
from .models import JobOrder, Job, Category

class JobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = ['job_title', 'job_type', 'job_salary', 'job_vacancy', 'job_category', 'job_description', 'job_location', 'job_image']


class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = '__all__'


class JobOrderForm(forms.ModelForm):
  class Meta:
    model = JobOrder
    fields = ['cv', 'website_link', 'cover_letter']
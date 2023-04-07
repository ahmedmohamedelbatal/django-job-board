from django.db import models
from accounts.models import Profile

class Job(models.Model):
  job_type = {
    ('Part-time', 'Part-time'),
    ('Full-time', 'Full-time')
  }
  job_title = models.CharField(max_length=100)
  job_type = models.CharField(max_length=100, choices=job_type)
  job_salary = models.DecimalField(max_digits=6, decimal_places=2)
  job_vacancy = models.IntegerField()
  job_category = models.ForeignKey("Category", on_delete=models.CASCADE)
  job_description = models.TextField(max_length=300)
  job_location = models.CharField(max_length=100)
  job_image = models.ImageField(upload_to='jobs/')
  created_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.job_title


class Category(models.Model):
  category_name = models.CharField(max_length=100)
  
  class Meta:
    verbose_name = ("Category")
    verbose_name_plural = ("Categories")
  
  def __str__(self):
    return self.category_name


class JobOrder(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
  job = models.ForeignKey("Job", on_delete=models.CASCADE)
  cv = models.FileField(upload_to='cv/')
  website_link = models.URLField()
  cover_letter = models.TextField(max_length=300)
  created_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
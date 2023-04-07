from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
  gender = {
    ('male','male'),
    ('female','female'),
  }
  user = models.OneToOneField(User, on_delete=models.CASCADE, default='not found')
  job = models.CharField(max_length=100, default='not found')
  address = models.CharField(max_length=100, default='not found')
  phone_number = models.CharField(max_length=12, default='not found')
  gender = models.CharField(max_length=100, choices=gender, default='not found')
  image = models.ImageField(upload_to='profiles/')
  
  def __str__(self):
    return str(self.user)
  
  @receiver(post_save, sender = User)
  def create_user_profile(sender, instance, created, **kwargs):
    if created: 
      Profile.objects.create(user = instance)
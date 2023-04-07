from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2', 'is_superuser']


class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['job', 'address', 'phone_number', 'gender', 'image']
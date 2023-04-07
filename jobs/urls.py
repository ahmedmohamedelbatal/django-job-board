from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
  path('', views.jobs, name='jobs'),
  path('<int:id>/', views.job, name='job'),
  path('add-job/', views.add_job, name='add_job'),
  path('add-category/', views.add_category, name='add_category'),
  path('job-orders/', views.job_orders, name='job_orders'),
  path('delete/<int:id>/', views.delete_job, name='delete_job'),
]
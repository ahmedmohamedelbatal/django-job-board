from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import JobForm, CategoryForm, JobOrderForm
from accounts.models import Profile
from .models import Job, JobOrder

@login_required(login_url='login')
def jobs(request):
  jobs = Job.objects.all()
  jobs_count = Job.objects.all().count()
  
  paginator = Paginator(jobs, 3)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  context = {'jobs': page_obj, 'jobs_count': jobs_count}
  return render(request, 'jobs/jobs.html', context)


@login_required(login_url='login')
def job(request, id):
  job = Job.objects.get(id = id)
  profile = Profile.objects.get(user = request.user)
  if request.method == 'POST':
    form = JobOrderForm(request.POST, request.FILES)
    if form.is_valid():
      myform = form.save(commit=False)
      myform.job = job
      myform.profile = profile
      myform.save()
  else:
    form = JobOrderForm()
  return render(request, 'jobs/job.html', {'job': job, 'form': form})


@login_required(login_url='login')
def add_job(request):
  if request.method == 'POST':
    form = JobForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = JobForm()
  return render(request, 'jobs/add_job.html', {'form': form})


def delete_job(request, id):
  delete_category = Job.objects.get(id = id)
  delete_category.delete()
  return redirect('/')


@login_required(login_url='login')
def add_category(request):
  if request.method == 'POST':
    form = CategoryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = CategoryForm()
  return render(request, 'jobs/add_category.html', {'form': form})


@login_required(login_url='login')
def job_orders(request):
  job_orders = JobOrder.objects.all()
  return render(request, 'jobs/job_orders.html', {'job_orders': job_orders})
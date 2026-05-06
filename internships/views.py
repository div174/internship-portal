from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Application
from .forms import ApplicationForm
from .decorators import superuser_required
from .utils import get_chart_data
import json

# =======================
# PUBLIC VIEWS
# =======================

def index(request):
    return render(request, 'index.html')

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Application submitted successfully!'})
            messages.success(request, 'Your application has been submitted successfully!')
            return render(request, 'apply.html', {'success': True})
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ApplicationForm()
    
    return render(request, 'apply.html', {'form': form})

# =======================
# AUTHENTICATION
# =======================

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Access denied. You must be an administrator.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
        
    return render(request, 'dashboard/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

# =======================
# DASHBOARD VIEWS
# =======================

@superuser_required
def dashboard(request):
    applications = Application.objects.all()
    
    # Stats
    total = applications.count()
    pending = applications.filter(status='Pending').count()
    selected = applications.filter(status='Selected').count()
    rejected = applications.filter(status='Rejected').count()
    
    recent_apps = applications.order_by('-created_at')[:5]
    
    # Chart data
    chart_data = get_chart_data(applications)

    context = {
        'total': total,
        'pending': pending,
        'selected': selected,
        'rejected': rejected,
        'recent_apps': recent_apps,
        'chart_data': chart_data,
    }
    return render(request, 'dashboard/dashboard.html', context)

@superuser_required
def applicants_list(request):
    query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    applications = Application.objects.all().order_by('-created_at')

    if query:
        applications = applications.filter(
            Q(full_name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(skills__icontains=query) |
            Q(college_name__icontains=query)
        )
    
    if status_filter:
        applications = applications.filter(status=status_filter)

    # Pagination
    paginator = Paginator(applications, 10) # 10 apps per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'status_filter': status_filter
    }
    return render(request, 'dashboard/applicants.html', context)

@superuser_required
def applicant_detail(request, pk):
    app = get_object_or_404(Application, pk=pk)
    return render(request, 'dashboard/applicant_detail.html', {'app': app})

@superuser_required
def update_status(request, pk, status):
    app = get_object_or_404(Application, pk=pk)
    valid_statuses = [choice[0] for choice in Application.STATUS_CHOICES]
    if status in valid_statuses:
        app.status = status
        app.save()
        messages.success(request, f'Status updated to {status} for {app.full_name}')
    else:
        messages.error(request, 'Invalid status.')
    
    # redirect back to referer or detail page
    return redirect(request.META.get('HTTP_REFERER', 'applicants'))

@superuser_required
@require_POST
def delete_applicant(request, pk):
    app = get_object_or_404(Application, pk=pk)
    app.delete()
    messages.success(request, 'Applicant deleted successfully.')
    return redirect('applicants')

@superuser_required
def dashboard_settings(request):
    # Dummy view for settings page
    return render(request, 'dashboard/settings.html')

# =======================
# ERROR VIEWS
# =======================

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)

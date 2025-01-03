# This is a template file. For the complete implementation, please contact the repository owner.
# The actual views.py contains sensitive implementation details and is available upon request.

import requests
from django.conf import settings
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)

def home(request):
    """Render the homepage"""
    return render(request, 'home.html')

# Template for other views
# For security reasons, the actual implementation is not public
# Please contact: Himanshusingh-18 (https://github.com/Himanshusingh-18)
# or create an issue in the repository for access to the complete implementation

"""
Available Views:
- live_matches(): Get live cricket matches
- recent_matches(): Get recent match results
- upcoming_matches(): Get upcoming match schedule
- commentary(): Get ball-by-ball commentary
- scorecard(): Get detailed match scorecard
- match_info(): Get match information
- schedule(): Get match schedules
- news(): Get cricket news
- players(): Get player information
- teams(): Get team information
- series(): Get series information
"""
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})



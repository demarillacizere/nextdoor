from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Neighborhood, Profile, Business, Alert, Hospital
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, NewBusinessForm, ProfileUpdateForm, NewAlertForm
from django.contrib.auth.models import User

def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'index.html',{'hoods':hoods})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username)
            profile=Profile.objects.create(user=user,email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'registration/registration_form.html')

def home(request):
    hoods = Neighborhood.objects.all()
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    hood = Neighborhood.objects.get(pk=profile.neighborhood.id)
    businesses = Business.objects.filter(neighborhood=hood).all()
    alerts = Alert.objects.filter(hood=hood).all()
    if request.method == 'POST':
        user=request.user
        form = NewAlertForm(request.POST)
        if form.is_valid():
            neighborhood = hood
            alert=form.save()
            alert.save()

    else:
        form=NewAlertForm
    return render(request, 'home.html',{'hood':hood,'hoods':hoods,'alerts':alerts,'businesses':businesses,'form':form})

def my_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form=ProfileUpdateForm(instance=profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    context={
        'form':form,
        'profile':profile,
    }
    return render(request,"my_profile.html",context=context)

from django.shortcuts import render ,redirect , get_object_or_404

# from django.http import HttpRequest
from django.views import generic
from django.contrib.auth.forms import UserCreationForm  , UserChangeForm
from accounts.forms import ProfileForm , SignupForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from  . models import Blacklist, Profile
from . forms import SignupForm , ProfileForm , EditProfileForm
from . import views
# Create your views here.




def signup(request):
    form = SignupForm()

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile/edit/')

    

    
    context = {'form' : form}
    return render (request , 'registration/signup.html' , context)


def loginPage(request ):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request , user)
            messages.success(request , 'Login Successfully For '  +user)
            return redirect('/products')
        else:
            messages.info(request , 'User Or Password Incorrect')
    context= {}
    return render(request , 'registration/login.html' , context)


def logoutUser(request):
    auth.logout(request)
    messages.info(request , 'logout done,')

    return redirect('/')




@login_required
def profile(request):
    profile = Profile.objects.get(user = request.user )
    context = {'profile' : profile}
    return render (request, 'accounts/profile.html' , context  ) 



@login_required
def profile_edit(request):
    post_data =request.POST or None
    file_data=request.FILES or None

    profile_edit=EditProfileForm( post_data, instance=request.user)
    profile_form = ProfileForm(post_data , file_data ,instance=request.user.profile)

    if profile_edit.is_valid() and profile_form.is_valid():
        profile_edit.save()
        profile_form.save()
        messages.success(request , 'Your profile was successefully updated')
        return redirect('/accounts/profile')



    return render (request , 'accounts/profile_edit.html' , {'profile_edit':profile_edit , 'profile_form':profile_form})




@login_required
def Black_list(request):
    list = Blacklist.objects.all()
    context = {'list':list}
    return render(request , 'Blacklist/bls.html' , context)
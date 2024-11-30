from django.shortcuts import redirect, render
from django.views import View
from .models import Donor,Volunteer,Donation,DonationArea,Gallery
from .forms import UserForm,DonorSignupForm,VolunteerSignupForm,LoginForm,MyPasswordChangeForm,DonateNowForm,DonationAreaForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from datetime import date

# Create your views here.
def index(request):
    return render(request, "index.html")



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


class login_admin(View):
    def get(self, request):
        form = LoginForm()
        # print("get")

        return render(request, "login-admin.html", locals())

    def post(self, request):
        form = LoginForm(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                # donor_user = Donor.objects.filter(user_id=user.id)
                if user.is_staff:
                    login(request, user)
                    # messages.success(request,'Login Successfully')
                    return redirect('/index-admin')
                else:
                    messages.warning(request, 'Invalid Admin User')
            else:
                messages.warning(request, 'invalid username and password')

        except:
            messages.warning(request, 'Login Failed')
        return render(request, 'login-admin.html', locals())


class login_donor(View):
    def get(self, request):
        form = LoginForm()
        print("get")
        return render(request, "login-donor.html", locals())

    def post(self, request):
        form = LoginForm(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                donor_user = Donor.objects.filter(user_id=user.id)
                if donor_user:
                    login(request, user)
                    # messages.success(request,'Login Successfully')
                    return redirect('/index-donor')
                else:
                    messages.warning(request, 'Invalid Donor User')
            else:
                messages.warning(request, 'invalid username and password')

        except:
            messages.warning(request, 'Login Failed')
        return render(request, 'login-donor.html', locals())


class login_volunteer(View):
    def get(self, request):
        form = LoginForm()
        # print("get")

        return render(request, "login-volunteer.html", locals())

    def post(self, request):
        form = LoginForm(request.POST)
        us = request.POST['username']
        pwd = request.POST['password']
        try:
            user = authenticate(username=us, password=pwd)
            if user:
                vol_user = Volunteer.objects.filter(user_id=user.id)
                if vol_user:
                    login(request, user)
                    # messages.success(request,'Login Successfully')
                    return redirect('/index-volunteer')
                else:
                    messages.warning(request, 'Invalid Volunteer User')
            else:
                messages.warning(request, 'invalid username and password')

        except:
            messages.warning(request, 'Login Failed')
        return render(request, 'login-volunteer.html', locals())


class signup_donor(View):
    def get(self, request):
        form1 = UserForm()
        form2 = DonorSignupForm()
        return render(request, "signup_donor.html", locals())
        # def get(self,request):
        return render(request, "signup_donor.html")

    def post(self, request):
        form1 = UserForm(request.POST)
        form2 = DonorSignupForm(request.POST)
        if form1.is_valid() & form2.is_valid():
            fn = request.POST["first_name"]
            ln = request.POST["last_name"]
            em = request.POST["email"]
            us = request.POST["username"]
            pwd = request.POST["password1"]
            contact = request.POST["contact"]
            userpic = request.FILES["userpic"]
            address = request.POST["address"]

            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, username=us, email=em, password=pwd)
                Donor.objects.create(user=user, contact=contact, userpic=userpic, address=address)
                messages.success(request, 'Congratulations!!Donor Profile Created Successfully')
            except:
                messages.warning(request, 'Profile Not Created')

        return render(request, "signup_donor.html", locals())


class signup_volunteer(View):
    def get(self, request):
        form1 = UserForm()
        form2 = VolunteerSignupForm()
        return render(request, "signup_volunteer.html", locals())

    def post(self, request):
        form1 = UserForm(request.POST)
        form2 = VolunteerSignupForm(request.POST)
        if form1.is_valid() & form2.is_valid():
            fn = request.POST['first_name']
            ln = request.POST['last_name']
            em = request.POST['email']
            us = request.POST['username']
            contact = request.POST['contact']
            pwd = request.POST['password1']
            userpic = request.FILES['userpic']
            idpic = request.FILES['idpic']
            address = request.POST['address']
            aboutme = request.POST['aboutme']

            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, username=us, email=em, password=pwd)
                Volunteer.objects.create(user=user, contact=contact, userpic=userpic, idpic=idpic, address=address,
                                         aboutme=aboutme, status='pending')
                messages.success(request, 'Congratulations!! voulunteer profile created successfully')
            except:
                messages.warning(request, 'Profile Not Created')

            return render(request, "signup_volunteer.html", locals())



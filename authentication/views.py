
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from datetime import datetime
from authentication.models import Contactus



def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(username=username,password=password1)
        if user is None:
            messages.error(request, 'Invalid credential')
            return redirect('/Signin')
        else:
            login(request, user)
            return redirect('/Account')
    else:
        
        return render(request, 'Signin.html')



def Signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Name validation in character 
        if not first_name.isalpha():
            messages.error(request, 'Firstname Should Be Alphabets')
            return redirect('/Signup')
        elif not last_name.isalpha():
            messages.error(request, 'Lastname Should Be Alphabets')
            return redirect('/Signup')
        else:
            pass

        # length Validation
        if len(first_name)>20:
            messages.error(request, 'Firstname Should be less than 20 characters')
            return redirect('/Signup')
        elif len(last_name)>20:
            messages.error(request, 'Firstname Should be less than 20 characters')
            return redirect('/Signup')
        elif len(username)>10:
            messages.error(request, 'username must be under 10 characters')
            return redirect('/Signup')
        elif len(password1)<6:
            messages.error(request, 'Password Must be greater than 6 character')
            return redirect('/Signup')
        elif len(password1)>15:
            messages.error(request, 'Password Should not be greater than 15 character')
            return redirect('/Signup')
        else:
            pass
        
        #User creating validation
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('/Signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Exists')
                return redirect('/Signup')
            else:
                myuser = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                myuser.firstname='first_name'
                myuser.lastname='last_name'
                myuser.save()
                messages.success(request,'user created')
                return redirect('/Signin')
        else:
            messages.error(request, 'Password does not match')
            return redirect('/Signup')
    else:
        return render(request, 'Signup.html')

def Signout(request):
    logout(request)
    return redirect('/')

def Documentation(request):
    return render(request, 'Documentation.html')

def Services(request):
    return render(request, 'Service.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name']
        Email = request.POST['Email']
        Comment = request.POST['Comment']
        
        if not Name.isalpha():
            messages.error(request, 'Name Should be in Alphabets')
            return redirect('/contact')
        elif len(Comment)>300:
             messages.error(request, 'Comment Should be Less than 300 characters')
             return redirect('/contact')
        else:
            contact = Contactus(Name=Name, Email=Email, Comment=Comment, Date=datetime.today())
            contact.save()
            messages.success(request, 'your request was submitted successfully')
            return redirect('/contact')
    else:
        return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def Account(request):
    return render(request, 'Account.html')

def Dashboard(request):
    return render(request, 'Account.html')


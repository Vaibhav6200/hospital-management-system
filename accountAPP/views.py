from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import RegisteredUser


def register(request):
    if request.method == "POST":
        fn = request.POST['fname']
        ln = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password1']
        number = request.POST['number']
        address = request.POST['address']
        date_of_birth = request.POST['dob']
        Gender = request.POST.get('radio',False)
        if password1 == password2:
            if RegisteredUser.objects.filter(phone_number=number).first():
                messages.info(request, "number already Exist")
                return redirect('register')
            if RegisteredUser.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('register')

            else:
                reguser = RegisteredUser.objects.create(first_name=fn, last_name=ln,  email=email, 
                                      phone_number=number, address=address, DOB=date_of_birth, gender=Gender
                                      )
                user = User.objects.create_user(first_name=fn,last_name=ln,username=email,password=password1)
                user.save()
                print("data saved")
                return redirect('login')
        else:
            messages.info(request, "Password not Match")
            return redirect('register')

        return redirect('/')

    return render(request, 'Register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
                auth.login(request, user)
                return redirect('userlog')
        messages.info(request, "invalid credentials")
        return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

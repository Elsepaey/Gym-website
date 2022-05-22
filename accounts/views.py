from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
import re
# Create your views here.
def signin (request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.error(request, 'username or password  invalid')

        return redirect('signin')
    else:

        return render(request, 'accounts/signin.html')
def logout (request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('index')
def signup (request):
    if request.method == 'POST':
        fname = 'none'
        lname = 'none'
        username = 'none'
        password = 'none'
        email = 'none'

        # "############"
        if 'fname' in request.POST:fname=request.POST['fname']
        else:messages.error(request,'error in first name')
        if 'lname' in request.POST: lname = request.POST['lname']
        else:messages.error(request,'error in last name')
        if 'name' in request.POST: username = request.POST['name']
        else:messages.error(request,'error in username')
        if 'pass' in request.POST: password = request.POST['pass']
        else:messages.error(request,'error in password')
        if 'email' in request.POST: email = request.POST['email']
        else:messages.error(request,'error in email')

        # '########'
        if fname and lname and username and password and email :
            if User.objects.filter(username=username).exists():
                messages.error(request,'try another username')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
                user.save()
                messages.success(request,'your account is succefully created')
        else:
             messages.error(request, 'check empty field')





        return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')
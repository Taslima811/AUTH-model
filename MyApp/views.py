from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 

def home(request): 
    return render(request,'home.html') 

def register(request): 
    if request.method=="POST":
         username=request.POST['username'] 
         email=request.POST['email'] 
         password1=request.POST['password1'] 
         password2=request.POST['password2'] 
         if password1!=password2:
             messages.error(request,"Password not matched") 
             
             return redirect('register') 
         
         if User.objects.filter(username=username).exists(): 
            messages.error(request,"Username already exists") 
            
            return redirect('register') 
         User.objects.create_user( 
             username=username, 
             email=email, 
             password=password1 
             ) 
         messages.success(request,"Registration Successful") 
         
         return redirect('login') 
    return render(request, 'register.html')

def loginPage(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username = username,
            password = password
        )

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")
    
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')

from email import message
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from database import settings
from django.contrib import auth

def home(request):
	return render(request,"index.html")



def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'signup.html',{'error':'Username is already taken'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,"signup.html",{'error':'password doesnt matched'})
    else:
        return render(request,"signup.html")
      
            		

def login(request):
	if request .method =='POST': 
		username = request.POST['username']
		password1 = request.POST['password1']
		user = authenticate(username=username, password=password1)
		if user is not None:
			auth.login(request, user)
			return render (request, "movie/movie_list.html" )
		else:
			return redirect(request, "login.html",{'error': 'username or password is incorrect'})

	return render(request,"login.html")


	
 
	


from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url="Login")
def Homepage(request):
    return render(request,"home.html")

def Loginpage(request):
    if request.method == "POST":
        username=request.POST.get("username")
        pass1=request.POST.get("pass")
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect("Home")
        else:
            return HttpResponse("wrong login")    
        print(username,pass1)
    
    return render(request,"login.html")

def Signuppage(request):
    if request.method == "POST" :
        uname=request.POST.get("username")
        email=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        if (pass1 != pass2):
            return HttpResponse("Password Not Match")
        else:    

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect ("Login")
        print(uname,email,pass1,pass2)
    return render(request,"signup.html")



def Logoutpage(request):
    logout(request)
    return redirect("Login")
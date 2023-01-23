
from django.shortcuts import render,redirect
from .forms import CustomerUserForm
from . models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    return render(request,'shopApp/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1==password2:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request,'Registration success,you can login now..')
            return redirect('login')
        else:
            messages.warning(request, "Passwords mismatching")
            return redirect('/register')
            
    else:
        form = CustomerUserForm()
        return render(request,'shopApp/register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"logged in successfully")
                return redirect('/')
            else:
                messages.warning(request,"Invalid username or password")
                return redirect('/login')
        return render(request,'shopApp/login.html')

def logout_page(request):
    if request.user.is_authenticated:#inbuilt func to check if user is logged in 
        logout(request)
        messages.success(request,"loggout in successfully")
        return redirect('/')



def collections(request):
    category = Category.objects.filter(status=0) # status in catagory admin
    return render(request,'shopApp/collections.html',{"category" : category})
    
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products = Products.objects.filter(category__name=name)
        return render(request,'shopApp/products/index.html',{"products":products,"category_name":name})
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            products = Products.objects.filter(name=pname,status=0).first()
            return render(request,'shopApp/products/product_details.html',{"products":products})
        else:
            messages.warning(request,"Product Not Found")
            return redirect('collections')
    else:
        messages.warning(request,"No such Category")
        return redirect('collections')
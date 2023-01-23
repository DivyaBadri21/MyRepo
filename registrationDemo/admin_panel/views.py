from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm # creates form with uname nd pw
from .forms import CreateUserForm # for email in form
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "admin_panel/home.html")

def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1==password2:
            user = User.objects.create_user(username=name,first_name=first_name,last_name=last_name,email=email,password=password1)
            # In admin to login and edit the details for the users added through UI
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request,"You account has been created")
            return redirect("Login")
        else:
            messages.warning(request,'password mismatching!')
            return redirect("Register")

    else:
        form = CreateUserForm()
        return render(request, "admin_panel/register.html", {'form':form})


@login_required
def profile(request):
    return render(request,"admin_panel/profile.html")
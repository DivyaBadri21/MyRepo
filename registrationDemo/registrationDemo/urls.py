"""registrationDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admin_panel import views
from django.contrib.auth import views as auth_views # to display default username and pw form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="Home"),
    #path('login/', views.login,name="Login"),
    path('login/',auth_views.LoginView.as_view(template_name='admin_panel/login.html'),name="Login"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='admin_panel/login.html'),name="Login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='admin_panel/logout.html'),name="Logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),  
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('register/', views.register,name="Register"),
    path('profile/', views.profile,name="Profile"),
    

]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name='home'),
    path('register',views.register, name='register'),
    path('login',views.login_page, name='login'),
    path('accounts/login/',views.login_page, name='login'),
    path('logout/',views.logout_page,name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset_confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),  
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    path('collections',views.collections, name='collections'),
    path('collections/<str:name>',views.collectionsview, name='collections'),
    path('collections/<str:cname>/<str:pname>',views.product_details, name='product_details'),
]
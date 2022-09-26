from django.urls import path
from django.contrib.auth import views as auth_views
from .views import myaccount, profile_update, activate_user,  dashbord, UserRegistrationView, LoginPageView, LogoutView

urlpatterns = [
    path(
        "register/", UserRegistrationView.as_view(),
        name="user_registration"
    ),

    path(
        "login/", LoginPageView.as_view(),
        name="user_login"
    ),
    path(
        "activate-user/<uidb64>/<token>", activate_user, name="activate"
    ),
    
    #path(
    #    "login/", UserLoginView.as_view(),
    #    name="user_login"
    #),

    path(
        "logout/", LogoutView.as_view(),
        name="user_logout"
    ),
    
    path('dashbord/', dashbord, name='dashbord'),
    path('myaccount/', myaccount, name='myaccount'),
    path('myaccount/profile_update/',profile_update, name='profile_update'), 



    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             subject_template_name='accounts/password_reset_subject.txt',
             email_template_name='accounts/password_reset_email.html',
             #success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    

]

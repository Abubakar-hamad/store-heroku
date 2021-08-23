from django.urls import path , include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
# from users import views as user_views

from django.views.generic import TemplateView



from . import views

app_name = 'accounts'


urlpatterns = [
    path('signup/' , views.signup , name= 'signup'),
    path('login/' , views.loginPage , name= 'login'),
    
     path(
        'change_password/',
        auth_views.PasswordChangeView.as_view(
            template_name='registration/password_change.html',
            # success_url = '/'
        ),
        name='change_password'
    ),
    path('blist/' , views.views.Black_list , name = 'blist'),


    # path('password_reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='registration/password-reset/password_reset_form.html'
    #      ),
    #      name='password_reset'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='registration/password-reset/password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='registration/password-reset/password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='registration/password-reset/password_reset_complete.html'
    #      ),
    #      name='password_reset_complete'),




    path('profile/' , views.profile , name ='profile'),
    path('profile/edit/' , views.profile_edit , name ='edit'),
    # path('<slug:slug>' , views.profile , name= 'profile'),
    path('logout/' , views.logoutUser , name= 'logout'),
   



    
    
]

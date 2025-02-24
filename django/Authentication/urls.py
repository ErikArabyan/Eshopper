from django.urls import path
from .views import *
from django.contrib.auth import views
from django.urls import reverse_lazy

app_name = 'AuthenticationUrls'

urlpatterns = [
    path('login_or_register/', LoginRegisterView.as_view(), name='login'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('logout/', Logout, name = 'logout'),

    path('password_reset/',
         views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        success_url = reverse_lazy("AuthenticationUrls:password_reset_done")
        ),
        name='password_reset'),

    path('password_reset_done/', views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', 
     views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('AuthenticationUrls:password_reset_complete')
     ), 
     name='password_reset_confirm'),
     
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_complete.html"), name='password_reset_complete'),
]

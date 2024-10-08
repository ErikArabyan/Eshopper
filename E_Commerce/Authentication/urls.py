from django.urls import path
from .views import *

app_name = 'AuthenticationUrls'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login')
]

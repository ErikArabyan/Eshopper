from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('cart/',CartListView.as_view(),name='cart'),
]
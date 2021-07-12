from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('all_customers',views.all_customers,name='all_customers'),
    path('transfer',views.transfer,name='transfer'),
]
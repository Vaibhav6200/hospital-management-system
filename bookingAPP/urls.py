from . import views
from django.urls import path




urlpatterns = [
   path('', views.booking, name="booking"),
   path('<str:fname>/receipt/', views.receipt, name="receipt"),
]
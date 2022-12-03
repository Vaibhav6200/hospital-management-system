from django.urls import path


from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.aboutUs, name="about"),
    path('<int:d_slug>/', views.departmentView, name="depview"),
    path('userlog/',views.dashboard, name="userlog"),

]


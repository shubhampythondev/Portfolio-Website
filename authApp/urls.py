from django.urls import path
from authApp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.HandleLogin, name='Handle_login'),
    path('logout/', views.HandleLogout, name='Handle_logout'),
]

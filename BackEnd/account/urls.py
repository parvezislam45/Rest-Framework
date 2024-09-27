from django.urls import path
from .import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('admin/',views.admin_dashboard,name='admin'),
    path('logout/', views.user_logout, name='logout'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import ExtendedAuthenicationForm

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='cringe_app/login.html', 
            authentication_form=ExtendedAuthenicationForm), name='login'),
    path('thread/<int:thread_id>/', views.thread, name='thread'),
    path('new_thread/', views.new_thread, name='new_thread'),
]

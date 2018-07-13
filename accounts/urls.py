from django.urls import path
from . import views


urlpatterns = [
    # ex: accounts/signup/
    path('signup/', views.signup, name='signup'),
    # ex: accounts/login/
    path('login/', views.login, name='login'),
    # ex: accounts/logout/
    path('logout/', views.logout, name='logout'),
]

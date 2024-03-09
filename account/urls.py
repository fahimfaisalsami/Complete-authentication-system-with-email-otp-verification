from django.urls import path
from .views import *

urlpatterns = [
    path('', login_user, name='login_user'),
    path('registration_user', registration_user, name='registration_user'),
    path('logout_user', logout_user, name='logout_user'),
    path('verify_acc', verify_acc, name='verify_acc'),
]
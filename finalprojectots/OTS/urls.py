from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signup),
    path('save-user/',saveUser),
    path('login/',login),
    path('login-validation/',loginValidation),
    #path('upload/',upload),
    
    
    
]
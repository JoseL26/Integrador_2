from django.urls import path

from login.views import *

urlpatterns = [
    path('', LoginFormWiew.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutFormWiew.as_view(), name='logout'),

]
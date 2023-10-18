from django.urls import path
from .views import *


urlpatterns = [

    path('',base,name='base'),
    path('ThreadView',ThreadView,name='ThreadView'),
    path('inbox',home,name='inbox'),

]
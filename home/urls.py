from django.urls import path
from .views import *

urlpatterns = [
  path('',Home1,name='home1'),
  path('feedback/',HomePage.as_view(),name='home'),
  path('order/<int:pk>',Delete,name='delete'),
]
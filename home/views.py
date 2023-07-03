from django.shortcuts import render,redirect
from rest_framework.generics import ListCreateAPIView
from .serializers import *

# Create your views here.

class HomePage(ListCreateAPIView):
  queryset = HomeModel.objects.all()
  serializer_class = FeedbackSerializer

def Home1(request):
  order = HomeModel.objects.all()
  return render(request,'index.html',{'order':order})

def Delete(request,pk):
  context = HomeModel.objects.get(id=pk)
  context.delete()
  return redirect('home1')
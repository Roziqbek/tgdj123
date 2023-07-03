from .models import *
from rest_framework.serializers import ModelSerializer

class FeedbackSerializer(ModelSerializer):
  class Meta:
    model = HomeModel
    fields = ('user_id',"tel","location","food","many",'check1',"food2","many2",'check2',"food3","many3",'check3',"food4","many4",'check4',"food5","many5")
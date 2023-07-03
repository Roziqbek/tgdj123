from django.db import models

# Create your models here.

class HomeModel(models.Model):
  user_id = models.CharField(max_length=123)
  tel = models.CharField(max_length=123)
  location = models.CharField(max_length=123)
  food = models.CharField(max_length=123)
  many = models.CharField(max_length=123)
  check1 = models.CharField(max_length=123)
  food2 = models.CharField(max_length=123,null=True,blank=True)
  many2 = models.CharField(max_length=123,null=True,blank=True)
  check2 = models.CharField(max_length=123,null=True,blank=True)
  food3 = models.CharField(max_length=123,null=True,blank=True)
  many3 = models.CharField(max_length=123,null=True,blank=True)
  check3 = models.CharField(max_length=123,null=True,blank=True)
  food4 = models.CharField(max_length=123,null=True,blank=True)
  many4 = models.CharField(max_length=123,null=True,blank=True)
  check4 = models.CharField(max_length=123,null=True,blank=True)
  food5 = models.CharField(max_length=123,null=True,blank=True)
  many5 = models.CharField(max_length=123,null=True,blank=True)

  def __str__(self):
    return self.user_id
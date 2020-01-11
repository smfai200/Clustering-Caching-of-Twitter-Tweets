from django.db import models
from random import seed
from random import random

seed(1)
def random_value():
    return str(random())

def Random_Initializer():
    all = Data.objects.all()
    count = 0
    for single in all:
        print("Count: ",count)
        single.popularity = random()
        single.save()
        count += 1

# Create your models here.
class Data(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    text = models.TextField(max_length=1000)
    timeStamp = models.CharField(max_length=100)
    user_id = models.FloatField()
    mb_cluster = models.FloatField()
    db_cluster = models.FloatField()
    cluster = models.FloatField()
    popularity = models.IntegerField(default=0)


from rest_framework import serializers
class Data_Serializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    text = serializers.CharField()
    timeStamp = serializers.CharField()
    user_id = serializers.FloatField()
    mb_cluster = serializers.FloatField()
    db_cluster = serializers.FloatField()
    cluster = serializers.FloatField()
    popularity = serializers.IntegerField()


